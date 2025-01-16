"""@author: Rahul R. Sah, Physics and Computer Science Department, Furman University
        iamrahursah@gmail.com.
"""
import numpy as np
from vispy import scene
from vispy import app
from vispy.geometry import MeshData
from vispy.scene import visuals

class MainWindow(scene.SceneCanvas):
    """
    Main window for rendering 3D models using Vispy.

    Parameters
    ----------
    *args : tuple
        Additional arguments for the SceneCanvas.
    """
    def __init__(self, *args):
        super().__init__(keys='interactive', size=(800, 600), show=True)
        self.unfreeze()
        self.grid = self.central_widget.add_grid(margin=10)
        self.view = self.grid.add_view(row=0, col=0, camera='turntable')
        self.view.bgcolor = 'black'
        self.view.camera.fov = 60

    def set_model(self, vertices, faces):
        """
        Set the 3D model to be rendered.

        Parameters
        ----------
        vertices : numpy.ndarray
            Array of vertex coordinates.
        faces : numpy.ndarray
            Array of face indices.
        """
        mesh_data = MeshData(vertices=vertices, faces=faces)
        mesh = visuals.Mesh(meshdata=mesh_data, shading='smooth', color="grey")
        self.view.add(mesh)

vertices = np.array([[1.0, 2.0, 3.0],
                            [4.0, 5.0, 6.0]])

faces = np.array([[2, 2, 4]])
main_w = MainWindow()

main_w.set_model(vertices, faces)
app.run()