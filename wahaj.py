#!/usr/bin/env python3
"""
Generate an STL file of the rings of a Wahaj concentrator described in the referenced patent and documents.
Each ring is a reflective, conical, non-imaging concentrator element arranged to focus solar radiation to a single focal area.
This code uses given relationships to compute ring angles and widths, then generates a 3D model of several nested rings.
"""
import math
import numpy as np
from stl import mesh


def compute_beta(F, R):
    # β = arctan(F/R)/2 + π/2
    return math.atan(F/R)/2 + math.pi/2


def compute_L(d, beta):
    # L = d * sin(2β−π/2)/cos(β)
    angle_for_L = 2*beta - math.pi/2
    return d * math.sin(angle_for_L) / math.cos(beta)


# Given parameters for first ring (example values):
F1 = 5.0   # vertical distance from focal area
R1 = 2.0   # horizontal distance from focal area
d1 = 0.5   # diameter of concentrated beam

# Compute tilt angle β1:
β1 = compute_beta(F1, R1)

# Compute width L1:
L1 = compute_L(d1, β1)


# We will generate multiple rings by varying F, R similarly.
# For ring i, define:
# Fi = F1 + (i)*deltaF, Ri = R1 + (i)*deltaR
# Keep d_i = d1 for simplicity.
# Then compute β_i and L_i similarly.
# This is a simplified demonstration.

ring_count = 32
deltaF = 1.0
deltaR = 2.0

# For meshing: we revolve each ring line segment around z-axis.
# We choose a number of angular segments for revolve.
revolve_steps = 64

# Each ring is formed by revolving a line segment tilted at β_i.
# The line segment length is L_i. Its center is at (R_i, 0, F_i).
# The direction of the line segment is along a vector forming angle β_i from vertical.
# Direction vector (in xz-plane): dx = sin(β_i), dz = cos(β_i)
# Endpoints:
# E1 = (R_i + (L_i/2)*dx, 0, F_i + (L_i/2)*dz)
# E2 = (R_i - (L_i/2)*dx, 0, F_i - (L_i/2)*dz)
# Revolve E1 and E2 around z to form top and bottom curves of ring.


def ring_geometry(F_i, R_i, d_i):
    beta_i = compute_beta(F_i, R_i)
    L_i = compute_L(d_i, beta_i)
    dx = math.sin(beta_i)
    dz = math.cos(beta_i)
    E1 = np.array([R_i + (L_i/2)*dx, 0, F_i + (L_i/2)*dz])
    E2 = np.array([R_i - (L_i/2)*dx, 0, F_i - (L_i/2)*dz])
    # Revolve around z-axis
    angles = np.linspace(0, 2*math.pi, revolve_steps, endpoint=False)
    top_curve = np.array(
        [[E1[0]*math.cos(a), E1[0]*math.sin(a), E1[2]] for a in angles])
    bottom_curve = np.array(
        [[E2[0]*math.cos(a), E2[0]*math.sin(a), E2[2]] for a in angles])
    return top_curve, bottom_curve


# Create all rings and combine into a single mesh.
vertices_list = []
faces_list = []
vertex_count = 0

for i in range(ring_count):
    F_i = F1 + i*deltaF
    R_i = R1 + i*deltaR
    d_i = d1  # constant in this example
    top_curve, bottom_curve = ring_geometry(F_i, R_i, d_i)

    # Each ring is formed by connecting top_curve and bottom_curve.
    # top_curve[k], top_curve[k+1], bottom_curve[k], bottom_curve[k+1]
    # Create quad faces, split into triangles.
    n = len(top_curve)
    ring_verts = np.vstack((top_curve, bottom_curve))
    start_index = vertex_count
    vertices_list.append(ring_verts)
    for k in range(n):
        k_next = (k+1) % n
        top0 = start_index + k
        top1 = start_index + k_next
        bot0 = start_index + n + k
        bot1 = start_index + n + k_next
        # Two triangles: (top0, bot0, top1), (bot0, bot1, top1)
        faces_list.append([top0, bot0, top1])
        faces_list.append([bot0, bot1, top1])
    vertex_count += ring_verts.shape[0]

# Combine all vertices and faces
all_vertices = np.vstack(vertices_list)
all_faces = np.array(faces_list)

# Create mesh
concentrator_mesh = mesh.Mesh(
    np.zeros(all_faces.shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(all_faces):
    for j in range(3):
        concentrator_mesh.vectors[i][j] = all_vertices[f[j], :]

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
