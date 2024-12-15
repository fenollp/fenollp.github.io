#!/usr/bin/env python3
"""
This script generates an STL file of the rings of a Wahaj concentrator and includes a hemisphere at the focal area.
It also prints out geometric details of each ring (inner radius, outer radius, area) for analysis.

Variable meanings:
- F1: The vertical distance between the center of the single focal area and the center of the reflective surface of the first ring.
  In other words, if the focal point is at z=0, and the ring is above or below it, F1 sets that vertical offset.
- R1: The horizontal distance between the center of the focal area and the center of the reflective surface of the first ring.
  This places the ring radially outward from the center line.
- d1: The diameter of the concentrated sunbeams reflected off the first ring at the focal area.
  This sets the size of the focal spot where the beams converge.
- deltaF: The increment in vertical distance for each subsequent ring. Each ring is placed further along the vertical axis.
- deltaR: The increment in horizontal distance for each subsequent ring. Each ring is placed further out radially.
- β1: The tilt angle of the first ring's reflective surface. Derived from the geometry, ensuring incoming rays reflect to the focal point.
- L1: The width of the first ring element. Computed so that all sunbeams from that ring surface form a spot of diameter d1 at the focal area.

In practice, these values would be determined from the design specifications in the referenced works.
For instance, large-scale concentrators described in the papers might have R1 on the order of several meters,
F1 on the order of a few meters, and d1 might be a few centimeters to decimeters depending on the desired focal spot size.
deltaF and deltaR would depend on how many rings are needed and how they are arranged.
"""

import math
import numpy as np
from stl import mesh

##################################
# Parameter Setup (example values)
##################################
F1 = 5.0   # Vertical offset of first ring from focal area
R1 = 1.0   # Horizontal offset of first ring from focal area
d1 = 1.0   # Focal spot diameter from the first ring
ring_count = 16
deltaF = 0.9
deltaR = 0.9

revolve_steps = 64
hemisphere_steps = 32
radius_hem = d1   # Radius of the hemisphere at the focal point (z=0)


###############################
# Geometric Computation Functions
###############################
def compute_beta(F, R):
    # β = arctan(F/R)/2 + π/2
    return math.atan(F/R)/2 + math.pi/2


def compute_L(d, beta):
    # L = d * sin(2β−π/2)/cos(β)
    angle_for_L = 2*beta - math.pi/2
    return d * math.sin(angle_for_L) / math.cos(beta)


# Pre-compute β1 and L1 for reference
β1 = compute_beta(F1, R1)
L1 = compute_L(d1, β1)

##################################
# Functions to generate ring geometry
##################################


def ring_geometry(F_i, R_i, d_i):
    beta_i = compute_beta(F_i, R_i)
    L_i = compute_L(d_i, beta_i)
    dx = math.sin(beta_i)
    dz = math.cos(beta_i)
    E1 = np.array([R_i + (L_i/2)*dx, 0, F_i + (L_i/2)*dz])
    E2 = np.array([R_i - (L_i/2)*dx, 0, F_i - (L_i/2)*dz])
    angles = np.linspace(0, 2*math.pi, revolve_steps, endpoint=False)
    top_curve = np.array(
        [[E1[0]*math.cos(a), E1[0]*math.sin(a), E1[2]] for a in angles])
    bottom_curve = np.array(
        [[E2[0]*math.cos(a), E2[0]*math.sin(a), E2[2]] for a in angles])
    return top_curve, bottom_curve, E1, E2


##################################
# Generate rings
##################################
vertices_list = []
faces_list = []
vertex_count = 0

for i in range(ring_count):
    F_i = F1 + i*deltaF
    R_i = R1 + i*deltaR
    d_i = d1
    top_curve, bottom_curve, E1, E2 = ring_geometry(F_i, R_i, d_i)
    n = len(top_curve)
    ring_verts = np.vstack((top_curve, bottom_curve))
    start_index = vertex_count
    vertices_list.append(ring_verts)

    # Create faces
    for k in range(n):
        k_next = (k+1) % n
        top0 = start_index + k
        top1 = start_index + k_next
        bot0 = start_index + n + k
        bot1 = start_index + n + k_next
        faces_list.append([top0, bot0, top1])
        faces_list.append([bot0, bot1, top1])
    vertex_count += ring_verts.shape[0]

    # Compute inner and outer radii and area of this ring
    # The ring is formed by revolving a line segment. Its endpoints are E1 and E2.
    # Radii at the endpoints (since Y=0 for endpoints): R_top = E1[0], R_bottom = E2[0]
    R_top = abs(E1[0])
    R_bottom = abs(E2[0])
    R_inner = min(R_top, R_bottom)
    R_outer = max(R_top, R_bottom)
    # The slant length is L_i (distance between E1 and E2)
    L_i = np.linalg.norm(E1 - E2)
    # Area of frustum surface: π * (R_inner + R_outer) * L_i
    ring_area = math.pi*(R_inner + R_outer)*L_i

    print(f"Ring {i+1}:")
    print(f"  Inner radius: {R_inner:.4f} m")
    print(f"  Outer radius: {R_outer:.4f} m")
    print(f"  Surface area: {ring_area:.4f} m²")

##################################
# Add a hemisphere at the focal point
##################################
# We'll parametrize the hemisphere using spherical coordinates:
# φ (phi) from 0 (top) to π/2 (equator) and θ (theta) from 0 to 2π.
phi_values = np.linspace(0, math.pi/2, hemisphere_steps)
theta_values = np.linspace(0, 2*math.pi, revolve_steps, endpoint=False)

hemisphere_vertices = []
for phi in phi_values:
    # A "ring" of vertices at this phi
    ring_line = []
    for theta in theta_values:
        x = radius_hem * math.sin(phi) * math.cos(theta)
        y = radius_hem * math.sin(phi) * math.sin(theta)
        z = radius_hem * math.cos(phi)
        ring_line.append([x, y, z])
    hemisphere_vertices.append(ring_line)

# Add the top vertex (phi=0) separately
# Actually phi=0 line is a single point at top: (0,0,radius_hem)
# We'll handle that in faces construction.

# Flatten hemisphere vertices
# hemisphere_vertices is a 2D array [phi_index][theta_index]
# Add them to vertices_list
hemisphere_start = vertex_count
for ring_line in hemisphere_vertices:
    vblock = np.array(ring_line)
    vertices_list.append(vblock)
    vertex_count += vblock.shape[0]

# Add top vertex
top_vertex_index = vertex_count
vertices_list.append(np.array([[0, 0, radius_hem]]))
vertex_count += 1

# Create hemisphere faces
# For each phi ring (except top), connect it to next.
# The top ring is actually a single point, the bottom ring is the largest circle.
# phi=0 line is the top vertex. Actually, we started at phi=0 in hemisphere_vertices,
# that gives a circle of radius 0 (just one ring?), If sin(phi=0)=0 => ring is all at the same point
# Let's handle that carefully:
#
# Actually, with phi_values starting at 0, we got a circle that is all zeros except the top point?
# sin(0)=0 => all x,y=0, just z=radius => all points coincide at top.
# That top ring_line is actually all the same point repeated revolve_steps times.
# We can ignore duplicates and just use the single top vertex added at the end.
#
# So effectively, hemisphere_vertices[0][*] is all the same point. Let's not form faces with it.
# We'll form faces between top_vertex_index and hemisphere_vertices[1], and so forth.

# We have hemisphere_steps phi values, starting at 0 to π/2.
# hemisphere_vertices[0] = top circle (all same point)
# hemisphere_vertices[-1] = bottom circle (largest)
#
# Actually, let's shift indexing:
# Let top vertex = top_vertex_index
# hemisphere rings from 1 to hemisphere_steps-1 connect upwards to top vertex
# and from 1 to hemisphere_steps-1 connect down to next ring.

hemisphere_vertices_count = sum(len(ring) for ring in hemisphere_vertices)
base_index = hemisphere_start
for i_phi in range(1, hemisphere_steps):
    # ring_i and ring_{i+1}
    ring_i = base_index + (i_phi-1)*revolve_steps
    ring_next = base_index + i_phi*revolve_steps if i_phi < hemisphere_steps else None

    # Connect ring_i to top_vertex_index if i_phi=1
    if i_phi == 1:
        # all faces connect each vertex in ring 1 to the top vertex
        for k in range(revolve_steps):
            k_next = (k+1) % revolve_steps
            faces_list.append([top_vertex_index, ring_i + k, ring_i + k_next])
    else:
        # connect ring_i to ring_{i-1} and ring_{i} to ring_{i+1} if exists
        # Actually we handle that when we go downwards.
        # We formed rings in order: hemisphere_vertices[i_phi]
        # We should connect ring_i to ring_{i-1}, forming a band of quads.
        ring_prev = ring_i - revolve_steps
        for k in range(revolve_steps):
            k_next = (k+1) % revolve_steps
            top0 = ring_prev + k
            top1 = ring_prev + k_next
            bot0 = ring_i + k
            bot1 = ring_i + k_next
            faces_list.append([top0, bot0, top1])
            faces_list.append([bot0, bot1, top1])

# Now we have a hemisphere formed from top_vertex and rings of latitude.
# Actually, the last ring at φ=π/2 is the "equator", we do not close anything below that, as it's a hemisphere.

##################################
# Create final mesh and save
##################################
all_vertices = np.vstack(vertices_list)
all_faces = np.array(faces_list)

concentrator_mesh = mesh.Mesh(
    np.zeros(all_faces.shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(all_faces):
    for j in range(3):
        concentrator_mesh.vectors[i][j] = all_vertices[f[j], :]

print("\nVariables meaning and suggested context from referenced works:")
print("F1: vertical offset of first ring from focal point. In large systems, could be a few meters.")
print("R1: horizontal offset of first ring from focal point. For a large concentrator, could be several meters.")
print("d1: diameter of focal spot. Typically a few centimeters to decimeters, depending on desired concentration.")
print("deltaF: vertical increment between rings. Might be on order of tens of cm to meters, depending on ring spacing.")
print("deltaR: horizontal increment between rings. Could be meters, depending on ring arrangement.")
print("β1: tilt angle of first ring. Determined by geometry, typically >90° since π/2 is added.")
print("L1: width of the first ring, ensuring correct beam concentration. Could be a few cm to tens of cm.")


# #!/usr/bin/env python3
# """
# Generate an STL file of the rings of a Wahaj concentrator described in the referenced patent and documents.
# Each ring is a reflective, conical, non-imaging concentrator element arranged to focus solar radiation to a single focal area.
# This code uses given relationships to compute ring angles and widths, then generates a 3D model of several nested rings.
# """
# import math
# import numpy as np
# from stl import mesh


# def compute_beta(F, R):
#     # β = arctan(F/R)/2 + π/2
#     return math.atan(F/R)/2 + math.pi/2


# def compute_L(d, beta):
#     # L = d * sin(2β−π/2)/cos(β)
#     angle_for_L = 2*beta - math.pi/2
#     return d * math.sin(angle_for_L) / math.cos(beta)


# # Given parameters for first ring (example values):
# F1 = 50.0  # vertical distance from focal area
# R1 = 2.0   # horizontal distance from focal area
# d1 = 0.5   # diameter of concentrated beam

# # Compute tilt angle β1:
# β1 = compute_beta(F1, R1)

# # Compute width L1:
# L1 = compute_L(d1, β1)


# # We will generate multiple rings by varying F, R similarly.
# # For ring i, define:
# # Fi = F1 + (i)*deltaF, Ri = R1 + (i)*deltaR
# # Keep d_i = d1 for simplicity.
# # Then compute β_i and L_i similarly.
# # This is a simplified demonstration.

# ring_count = 16
# deltaF = 1.0
# deltaR = 2.0

# # For meshing: we revolve each ring line segment around z-axis.
# # We choose a number of angular segments for revolve.
# revolve_steps = 64

# # Each ring is formed by revolving a line segment tilted at β_i.
# # The line segment length is L_i. Its center is at (R_i, 0, F_i).
# # The direction of the line segment is along a vector forming angle β_i from vertical.
# # Direction vector (in xz-plane): dx = sin(β_i), dz = cos(β_i)
# # Endpoints:
# # E1 = (R_i + (L_i/2)*dx, 0, F_i + (L_i/2)*dz)
# # E2 = (R_i - (L_i/2)*dx, 0, F_i - (L_i/2)*dz)
# # Revolve E1 and E2 around z to form top and bottom curves of ring.


# def ring_geometry(F_i, R_i, d_i):
#     beta_i = compute_beta(F_i, R_i)
#     L_i = compute_L(d_i, beta_i)
#     dx = math.sin(beta_i)
#     dz = math.cos(beta_i)
#     E1 = np.array([R_i + (L_i/2)*dx, 0, F_i + (L_i/2)*dz])
#     E2 = np.array([R_i - (L_i/2)*dx, 0, F_i - (L_i/2)*dz])
#     # Revolve around z-axis
#     angles = np.linspace(0, 2*math.pi, revolve_steps, endpoint=False)
#     top_curve = np.array(
#         [[E1[0]*math.cos(a), E1[0]*math.sin(a), E1[2]] for a in angles])
#     bottom_curve = np.array(
#         [[E2[0]*math.cos(a), E2[0]*math.sin(a), E2[2]] for a in angles])
#     return top_curve, bottom_curve


# # Create all rings and combine into a single mesh.
# vertices_list = []
# faces_list = []
# vertex_count = 0

# for i in range(ring_count):
#     F_i = F1 + i*deltaF
#     R_i = R1 + i*deltaR
#     d_i = d1  # constant in this example
#     top_curve, bottom_curve = ring_geometry(F_i, R_i, d_i)

#     # Each ring is formed by connecting top_curve and bottom_curve.
#     # top_curve[k], top_curve[k+1], bottom_curve[k], bottom_curve[k+1]
#     # Create quad faces, split into triangles.
#     n = len(top_curve)
#     ring_verts = np.vstack((top_curve, bottom_curve))
#     start_index = vertex_count
#     vertices_list.append(ring_verts)
#     for k in range(n):
#         k_next = (k+1) % n
#         top0 = start_index + k
#         top1 = start_index + k_next
#         bot0 = start_index + n + k
#         bot1 = start_index + n + k_next
#         # Two triangles: (top0, bot0, top1), (bot0, bot1, top1)
#         faces_list.append([top0, bot0, top1])
#         faces_list.append([bot0, bot1, top1])
#     vertex_count += ring_verts.shape[0]

# # Combine all vertices and faces
# all_vertices = np.vstack(vertices_list)
# all_faces = np.array(faces_list)

# # Create mesh
# concentrator_mesh = mesh.Mesh(
#     np.zeros(all_faces.shape[0], dtype=mesh.Mesh.dtype))
# for i, f in enumerate(all_faces):
#     for j in range(3):
#         concentrator_mesh.vectors[i][j] = all_vertices[f[j], :]

# Save to STL
concentrator_mesh.save("my.stl")

# ---

# https://chatgpt.com/c/6758c951-9098-8008-ad1a-4938ed1e2958

# Give me the Python code to generate an STL file of the rings of a Wahaj concentrator described described in FIG. 2B of US10436182B2 and in the following publicly-accessible documents:
# * (2022) Design & demonstration of a 10-meter metallic reflector-based Fresnel lens, with lower focal point fixed to the ground
# * (2022) Dispatchable power supply from beam down solar point concentrator coupled to thermal energy storage and a Stirling engine
# * US10436182B2 "System for collecting radiant energy with a non-imaging solar concentrator"

# And note that the rings describe
# a non-imaging solar concentrator comprising:
# a plurality of nested, concentric, conical ring-like reflective elements that are arranged to evenly concentrate incoming solar radiation to a single focal area, each ring-like reflective element has a tilt angle, a width, and includes a reflective surface on an interior side thereof;
# wherein, while a top side of the solar concentrator is positioned perpendicular to the sun, each ring-like reflective element is positioned to not shade the reflective surface of a ring-like reflective element positioned adjacent thereto, to not block sunbeams reflected by the adjacent ring-like reflective element, and to leave no gap therebetween through which any incoming sunbeams may pass without being reflected;
# wherein the tilt angle of each ring-like reflective element is set so that incoming sunbeams striking a center of the reflective surface thereof are reflected to a center of the single focal area; and
# wherein the width of each ring-like reflective element causes incoming sunbeams striking the reflective surface thereof to form a circle of concentrated sunbeams having a diameter, the plurality of ring-like reflective elements form overlapping circles of concentrated sunbeams having the same diameter.

# The width of a first ring-like reflective element satisfies the following relationship,
# L1 = d1 * sin(2*β1−π/2)/Cos(β1), wherein:
# L1=width of the first ring-like reflective element;
# β1=tilt angle of the reflective surface of the first ring-like reflective element; and
# d1=diameter of the concentrated sunbeams reflected off the reflective surface of the first reflective element at the focal area of the solar concentrator;

# wherein the tilt angle of the first reflective element satisfies the following relationship,
# β1=arctan(F1/R1)/2+π/2, wherein:
# F1=vertical distance between the center of the single focal area and the center of the reflective surface of the first ring-like reflective element;
# R1=horizontal distance between the center of the single focal area and the center of the reflective surface of the first ring-like reflective element; and
# wherein a diameter of the single focal area is equal to the diameter d1 of the concentrated sunbeams reflected off of the first ring-like reflective element.

# Make sure to embed the Python script in a Dockerfile based on python:3.
# Have the python script directly included in the Dockerfile using heredoc syntax.
# Make it so that a docker build installs the required deps in a first stage, runs the code in a second stage then moves the generated STL file in a final scratch stage.
# Make sure to only output the Dockerfile, no additional instructions.
# Keep your Python code tidy and with the right amount of comments.

# And start the dockerfile with the following line:
# # syntax=docker.io/docker/dockerfile:1@sha256:db1ff77fb637a5955317c7a3a62540196396d565f3dd5742e76dddbb6d75c4c5
