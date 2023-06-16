import os
import numpy as np
import trimesh

def create_gomboc():
    # Define the parameters of the Gömböc shape
    radius = 2.0  # Radius of the Gömböc
    height = 8.0  # Height of the Gömböc

    # Create the Gömböc mesh
    resolution = 15  # Number of divisions along the azimuthal and vertical directions
    azim_steps = resolution * 2
    vert_steps = resolution
    azimuths = np.linspace(0, 2 * np.pi, azim_steps)
    verticals = np.linspace(-np.pi / 2, np.pi / 2, vert_steps)
    vertices = []

    # Generate the vertices of the Gömböc
    for v in verticals:
        for a in azimuths:
            x = radius * np.cos(a) * np.cos(v)
            y = radius * np.sin(a) * np.cos(v)
            z = height * np.sin(v)
            vertices.append([x, y, z])

    # Create the faces of the Gömböc
    faces = []
    for i in range(vert_steps - 1):
        for j in range(azim_steps - 1):
            v1 = i * azim_steps + j
            v2 = i * azim_steps + (j + 1)
            v3 = (i + 1) * azim_steps + (j + 1)
            v4 = (i + 1) * azim_steps + j
            face1 = [v1, v2, v3]
            face2 = [v1, v3, v4]
            faces.append(face1)
            faces.append(face2)

    # Create the mesh using trimesh
    gomboc_mesh = trimesh.Trimesh(vertices=vertices, faces=faces)

    # Get the path to the desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    # Save the Gömböc mesh as an STL file on the desktop
    save_path = os.path.join(desktop_path, "gomboc.stl")
    gomboc_mesh.export(save_path, file_type='stl')

# Call the function to create and save the Gömböc on the desktop
create_gomboc()
