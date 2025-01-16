"""@author: Rahul R. Sah, Physics and Computer Science Department, Furman University
        iamrahursah@gmail.com.
"""

import pandas as pd

def load_data(file_path):
    """
    Load 3D model data from a file.

    Parameters
    ----------
    file_path : str
        Path to the file containing the 3D model data.

    Returns
    -------
    vertices : numpy.ndarray
        Array of vertex coordinates.
    faces : numpy.ndarray
        Array of face indices.
    """
    comet = pd.read_csv(file_path, delim_whitespace=True, names=["TYPE", "X1", "X2", "X3"])
    vertices = comet.loc[comet["TYPE"] == "v"][["X1", "X2", "X3"]].values
    faces = comet.loc[comet["TYPE"] == "f"][["X1", "X2", "X3"]].values
    faces = faces - 1
    faces = faces.astype(int)
    return vertices, faces

