import math
import numpy as np


def calculate_beta(F, R):
    """Calculates the tilt angle (beta) of a ring."""
    return math.atan(F / R) / 2 + math.pi / 2


def calculate_width(d, beta):
    """Calculates the width (L) of a ring."""
    return d * math.sin(2 * beta - math.pi / 2) / math.cos(beta)


def create_ring_mesh(inner_radius, outer_radius, height, segments=32):
    """Creates the mesh data for a single truncated conical ring."""
    vertices = []
    faces = []

    for i in range(segments):
        theta1 = 2 * math.pi * i / segments
        theta2 = 2 * math.pi * (i + 1) / segments

        x1_inner = inner_radius * math.cos(theta1)
        y1_inner = inner_radius * math.sin(theta1)
        z1_inner = 0

        x2_inner = inner_radius * math.cos(theta2)
        y2_inner = inner_radius * math.sin(theta2)
        z2_inner = 0

        x1_outer = outer_radius * math.cos(theta1)
        y1_outer = outer_radius * math.sin(theta1)
        z1_outer = height

        x2_outer = outer_radius * math.cos(theta2)
        y2_outer = outer_radius * math.sin(theta2)
        z2_outer = height

        vertex_indices = len(vertices)
        vertices.extend([(x1_inner, y1_inner, z1_inner),
                         (x2_inner, y2_inner, z2_inner),
                         (x2_outer, y2_outer, z2_outer),
                         (x1_outer, y1_outer, z1_outer)])

        faces.append([vertex_indices + 0, vertex_indices + 2,
                     vertex_indices + 1])  # First Triangle
        faces.append([vertex_indices + 0, vertex_indices + 3,
                     vertex_indices + 2])  # Second Triangle

    return np.array(vertices, dtype=np.float32), np.array(faces, dtype=np.int32)


def generate_wahaj_concentrator_rings(focal_diameter, total_radius, num_rings, focal_height):
    """Generates the geometry for all Wahaj concentrator rings."""
    rings = []
    d = focal_diameter  # diameter of the concentrated beam at focus

    # Initialize first ring with starting parameters
    # first ring is offset a bit so its not centered at the focus
    current_R = 0.1 * total_radius
    current_F = focal_height  # all rings focus to same vertical position

    for i in range(num_rings):
        beta = calculate_beta(current_F, current_R)
        L = calculate_width(d, beta)  # ring width
        inner_radius = current_R
        outer_radius = inner_radius + L * math.cos(beta)
        ring_height = L * math.sin(beta)

        vertices, faces = create_ring_mesh(
            inner_radius, outer_radius, ring_height, 64)
        rings.append((vertices, faces))

        # Update for the next ring: The R value is updated based on the position
        # of the previous ring
        current_R = outer_radius

    return rings


def write_stl_file(filename, vertices_list, faces_list):
    """Writes the mesh data to an STL file."""

    with open(filename, 'w') as f:
        f.write("solid wahaj_concentrator\n")
        for vertices, faces in zip(vertices_list, faces_list):
            for face in faces:
                normal = np.cross(
                    vertices[face[1]] - vertices[face[0]], vertices[face[2]] - vertices[face[0]])
                normal /= np.linalg.norm(normal)
                f.write("  facet normal {:.6f} {:.6f} {:.6f}\n".format(
                    normal[0], normal[1], normal[2]))
                f.write("    outer loop\n")
                for vertex_index in face:
                    vertex = vertices[vertex_index]
                    f.write("      vertex {:.6f} {:.6f} {:.6f}\n".format(
                        vertex[0], vertex[1], vertex[2]))
                f.write("    endloop\n")
                f.write("  endfacet\n")
        f.write("endsolid wahaj_concentrator\n")


if __name__ == "__main__":
    # Example Usage
    focal_diameter = 0.2  # diameter of concentrated beams
    total_radius = 2.0    # Total Radius of the concentrator
    num_rings = 15        # Number of concentric rings
    focal_height = 3.0  # Vertical distance from focal point to the base of the concentrator

    rings = generate_wahaj_concentrator_rings(
        focal_diameter, total_radius, num_rings, focal_height)

    vertices_list = [r[0] for r in rings]
    faces_list = [r[1] for r in rings]
    write_stl_file("wahaj_generator.stl", vertices_list, faces_list)
    print("Wahaj concentrator STL file generated: wahaj_generator.stl")