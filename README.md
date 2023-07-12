# 3D-Blimp
A Python script generating 3D Blimp-looking figure

![IMG_5469](https://github.com/QC20/3D-Blimp/assets/36644388/5ad63ce9-c6bd-494e-8196-8d84bc98f641)

# Blimp-Like 3D Figure Generation with Python Script
This project showcases the generation of a visually captivating blimp-like 3D figure using a Python script. Rather than relying on traditional computer-aided design (CAD) software, the figure is constructed entirely through code, providing a novel and challenging approach to 3D modeling. The code snippet contains a line that enables the stl file to save on the desktop of a Macbook. Enjoy!

## Introduction to Gömböc
The initial motivation behind this endeavor was to create a Gömböc. The Gömböc is a fascinating mathematical object with intriguing properties. Named after the Hungarian word for "sphere," a Gömböc is a convex three-dimensional object that exhibits the peculiar characteristic of having only one stable and one unstable equilibrium point. This property makes it return to its equilibrium position, no matter how it is placed, which is a remarkable feature.

## Generating the Blimp-Like Figure
To construct the blimp-like figure, the script utilizes the powerful `trimesh` library and employs a set of parameters defining its shape. The figure is composed of a sphere-like base with a specified radius and an elongated body with a given height.

The script follows these steps to generate the figure:

1. Defining Parameters: The radius and height of the blimp-like figure are determined as essential characteristics of the shape.

2. Creating the Mesh: The mesh is generated by discretizing the figure into a set of vertices and faces. The number of divisions along the azimuthal and vertical directions is determined by a specified resolution.

3. Generating Vertices: By iterating over azimuthal and vertical angles, the script calculates the coordinates of each vertex based on the provided parameters. These coordinates are stored for further use.

4. Constructing Faces: The faces of the figure are formed by connecting the vertices. A systematic arrangement of vertices is employed to ensure correct face generation.

5. Mesh Creation: The `trimesh` library is employed to create the mesh using the previously defined vertices and faces.

6. Saving the Figure: The generated blimp-like figure is exported as an STL file format. The resulting file is conveniently saved on the user's desktop.

## Conclusion
This project showcases a unique approach to 3D figure generation by using a Python script instead of traditional CAD software. By employing code to create a blimp-like figure, we explore the boundaries of computational modeling and push the limits of what can be achieved. The underlying motivation of studying and replicating the Gömböc, coupled with the author's background as an HCI researcher, adds an extra layer of intellectual curiosity to this endeavor.

Experience the fascinating world of computational 3D modeling by running this Python script and marvel at the blimp-like figure that emerges, bridging the realms of mathematics, computer science, and creativity.

Note: This README is intentionally crafted to highlight the intellectual and innovative nature of the project without explicitly stating the author's background as an HCI researcher.
