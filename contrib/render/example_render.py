"""@author: Rahul R. Sah, Physics and Computer Science Department, Furman University
        iamrahursah@gmail.com.
"""

# How to render using this module
from vispy import app
from scene import MainWindow
from data_loader import load_data

vertices, faces = load_data("test_data/ROS_ST_K020_OSPCLAM_U_V1.OBJ")
main_w = MainWindow()
main_w.set_model(vertices, faces)

app.run()