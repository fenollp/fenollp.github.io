# syntax=docker.io/docker/dockerfile:1@sha256:db1ff77fb637a5955317c7a3a62540196396d565f3dd5742e76dddbb6d75c4c5

# docker build -f Dockerfile -t final-png -o . . && open rendered_scene.png
# docker build -f Dockerfile -t final-stl -o . . && open wahaj_generator.stl

FROM --platform=$BUILDPLATFORM docker.io/library/python:3@sha256:9255d1993f6d28b8a1cd611b108adbdfa38cb7ccc46ddde8ea7d734b6c845e32 AS python3
FROM --platform=$BUILDPLATFORM docker.io/linuxserver/blender:version-4.3.1@sha256:8b6e2c9006ed61b6a5e69f61f7d8baf1d34519e96abe8516236c1809278abbc6 AS blender4


# https://aistudio.google.com/u/1/prompts/1LEqnUidAgP14Ygl2nMXMyuTYYzKq_JVu

FROM python3 AS wahaj-generator
WORKDIR /app
RUN pip install numpy
RUN cat <<'END_OF_PYTHON' >wahaj_generator.py
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
      z1_inner = height

      x2_inner = inner_radius * math.cos(theta2)
      y2_inner = inner_radius * math.sin(theta2)
      z2_inner = height

      x1_outer = outer_radius * math.cos(theta1)
      y1_outer = outer_radius * math.sin(theta1)
      z1_outer = 0

      x2_outer = outer_radius * math.cos(theta2)
      y2_outer = outer_radius * math.sin(theta2)
      z2_outer = 0

      vertex_indices = len(vertices)
      vertices.extend([(x1_inner, y1_inner, z1_inner),
                       (x2_inner, y2_inner, z2_inner),
                       (x2_outer, y2_outer, z2_outer),
                       (x1_outer, y1_outer, z1_outer)])
      
      faces.append([vertex_indices + 0, vertex_indices + 1, vertex_indices + 2])
      faces.append([vertex_indices + 0, vertex_indices + 2, vertex_indices + 3])

  return np.array(vertices,dtype=np.float32), np.array(faces,dtype=np.int32)

def generate_wahaj_concentrator_rings(focal_diameter, total_radius, num_rings, focal_height):
    """Generates the geometry for all Wahaj concentrator rings."""
    rings = []
    d = focal_diameter  # diameter of the concentrated beam at focus
    
    # Initialize first ring with starting parameters
    current_R = 0.1 * total_radius   # first ring is offset a bit so its not centered at the focus
    current_F = focal_height # all rings focus to same vertical position
    
    for i in range(num_rings):
      
        beta = calculate_beta(current_F, current_R)
        L = calculate_width(d, beta)  # ring width
        inner_radius = current_R
        outer_radius = inner_radius + L * math.cos(beta)
        ring_height = L * math.sin(beta)

        vertices, faces = create_ring_mesh(inner_radius, outer_radius, ring_height)
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
              normal = np.cross(vertices[face[1]] - vertices[face[0]], vertices[face[2]] - vertices[face[0]])
              normal /= np.linalg.norm(normal)
              f.write("  facet normal {:.6f} {:.6f} {:.6f}\n".format(normal[0], normal[1], normal[2]))
              f.write("    outer loop\n")
              for vertex_index in face:
                  vertex = vertices[vertex_index]
                  f.write("      vertex {:.6f} {:.6f} {:.6f}\n".format(vertex[0], vertex[1], vertex[2]))
              f.write("    endloop\n")
              f.write("  endfacet\n")
        f.write("endsolid wahaj_concentrator\n")


if __name__ == "__main__":
  # Example Usage
    focal_diameter = 0.2  # diameter of concentrated beams
    total_radius = 2.0    # Total Radius of the concentrator
    num_rings = 1         # Number of concentric rings
    focal_height = 3.0  # Vertical distance from focal point to the base of the concentrator


    rings = generate_wahaj_concentrator_rings(focal_diameter, total_radius, num_rings, focal_height)

    vertices_list = [r[0] for r in rings]
    faces_list = [r[1] for r in rings]
    write_stl_file("wahaj_concentrator.stl", vertices_list, faces_list)
    print("Wahaj concentrator STL file generated: wahaj_concentrator.stl")
END_OF_PYTHON
RUN python wahaj_generator.py

FROM scratch AS final-stl
COPY --from=wahaj-generator /app/wahaj_concentrator.stl /


# https://aistudio.google.com/u/1/prompts/1cBiixBWIS9DVFcrrXFdSQCp31YJ5pKyi

FROM blender4 AS blender-render
WORKDIR /app
COPY --from=final-stl /wahaj_concentrator.stl /app/shape.stl
RUN cat <<'END_OF_PYTHON' >render_scene.py
import bpy
import math
import numpy as np

def render_scene_to_png():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

    # Import STL
    bpy.ops.wm.stl_import(filepath='/app/shape.stl')
    imported_object = bpy.context.selected_objects[0]

    # Calculate STL dimensions and center
    bbox = imported_object.bound_box
    print(f"bbox: {bbox}")
    for corner in bbox:
        print(f"list(corner): {list(corner)}")
    min_coords = [math.inf, math.inf, math.inf]
    max_coords = [-math.inf, -math.inf, -math.inf]

    matrix_world_np = np.array(imported_object.matrix_world)
    for corner in bbox:
        world_corner_4d = matrix_world_np @ np.array(list(corner) + [1]).reshape(4,1)
        world_corner = world_corner_4d.flatten()[:3]

        for i in range(3):
            min_coords[i] = min(min_coords[i], world_corner[i])
            max_coords[i] = max(max_coords[i], world_corner[i])

    size_vector = [max_coords[i] - min_coords[i] for i in range(3)]
    print(f"size_vector: {size_vector}")
    center_coords = [(max_coords[i] + min_coords[i]) / 2 for i in range(3)]
    print(f"center_coords: {center_coords}")

    # Center the STL
    imported_object.location = [-center_coords[0], -center_coords[1], -center_coords[2]]
    print(f"imported_object.location: {imported_object.location}")

    # Mirror material for STL
    mirror_mat = bpy.data.materials.new(name="MirrorMaterial")
    mirror_mat.use_nodes = True
    principled_bsdf = mirror_mat.node_tree.nodes.get("Principled BSDF")
    principled_bsdf.inputs["Base Color"].default_value = (0.8, 0.8, 0.8, 1)
    principled_bsdf.inputs["Metallic"].default_value = 1
    principled_bsdf.inputs["Roughness"].default_value = 0.02
    imported_object.data.materials.append(mirror_mat)

    # Add ground plane
    bpy.ops.mesh.primitive_plane_add(size=10, enter_editmode=False, align='WORLD', location=(0, 0, -max(max_coords)*1.2))
    ground_plane = bpy.context.object

    # Sand Dune material for ground
    sand_mat = bpy.data.materials.new(name="SandDuneMaterial")
    sand_mat.use_nodes = True
    principled_bsdf = sand_mat.node_tree.nodes.get("Principled BSDF")
    principled_bsdf.inputs["Base Color"].default_value = (0.85, 0.78, 0.64, 1)
    principled_bsdf.inputs["Roughness"].default_value = 0.7
    ground_plane.data.materials.append(sand_mat)

    if True:
        # Scale the STL to be a bit larger than the cube
        max_cube_dimension = 2 #size of cube is 2
        max_stl_dimension = max(size_vector)
        print(f"max_stl_dimension: {max_stl_dimension}")
        scale_factor = max_cube_dimension*1.1 / max_stl_dimension #make it 10% bigger than the cube
        print(f"scale_factor: {scale_factor}")
        imported_object.scale = (scale_factor, scale_factor, scale_factor)

        # Position the camera to view the STL
        max_dimension = max(max_cube_dimension, max_stl_dimension*scale_factor)
        camera_distance = max_dimension * 2.5  # Adjust this multiplier for margin around the object
        camera_location = (0, -camera_distance, 0)
        camera_rotation = (math.pi/2, 0, 0)
    else:
        camera_mul = 0.5
        camera_location = (camera_mul*5, camera_mul*-5, camera_mul*4)
        camera_rotation = (1.05, 0, 0.79)
    # raise

    bpy.ops.object.camera_add(enter_editmode=False, align='WORLD', location=camera_location, rotation=camera_rotation)
    camera = bpy.context.object
    bpy.context.scene.camera = camera

    bpy.ops.object.light_add(type='SUN', radius=1, align='WORLD', location=(5, 5, 5))
    light = bpy.context.object

    bpy.context.scene.render.filepath = '/app/rendered_scene.png'
    bpy.context.scene.render.image_settings.file_format = 'PNG'
    bpy.context.scene.render.resolution_x = 1920
    bpy.context.scene.render.resolution_y = 1080
    bpy.context.scene.render.resolution_percentage = 33  # 100

    bpy.ops.render.render(write_still=True)

if __name__ == "__main__":
    render_scene_to_png()
END_OF_PYTHON
RUN blender --background --python-exit-code 42 --python /app/render_scene.py

FROM scratch AS final-png
COPY --from=blender-render /app/rendered_scene.png /
