"""
This module demonstrates how to render a 3D model using Vispy.

The module includes the following steps:
1. Load the 3D model data from a file.
2. Create a MainWindow instance.
3. Set the 3D model in the MainWindow.
4. Run the Vispy application.

Usage:
    python example_render.py

"""

# How to render using this module
from vispy import app
from render.scene import MainWindow
from render.data_loader import load_data

def main():
    """
    Main function to render the 3D model.

    This function performs the following steps:
    1. Load the 3D model data from a file.
    2. Create a MainWindow instance.
    3. Set the 3D model in the MainWindow.
    4. Run the Vispy application.
    """

    vertices, faces = load_data("test_data/ROS_ST_K020_OSPCLAM_U_V1.OBJ")
    main_w = MainWindow()
    main_w.set_model(vertices, faces)
    app.run()

if __name__ == "__main__":
    main()