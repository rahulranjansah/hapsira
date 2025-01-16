# Hapsira 3D Asteroid and Comet Visualization

## Overview
This enhancement adds a **3D visualization feature** to **Hapsira**, rendering precise models of asteroids and comets using **SPICE Digital Shape Kernel (DSK) files**. The visualization leverages the **Vispy** library for rendering, offering interactive exploration of shape and topography data. Additionally, a **bash script** automates the conversion of `.bds` files into `.obj` files using `dskexp` on Linux systems.

---

## Key Features

### 1. 3D Visualization with Vispy
- **Interactive 3D Rendering**: Displays 3D models of asteroids and comets.
- **Camera Controls**: Allows zooming, rotating, and panning for full exploration.
- **Lighting and Shading**: Enhances topographical detail.

### 2. DSK Export Automation
- **Bash Script**: Automates conversion of `.bds` files to `.obj` files.
- **Batch Processing**: Converts multiple files efficiently.
- **Linux Compatibility**: Uses `dskexp` from the SPICE toolkit.

---

## Installation

If your file downloaded from **NAIF kernel** dsk is .bds format, you might have to convert the file into text format that is .obj. The dsk could be found here within files [NAIF Kernels](https://naif.jpl.nasa.gov/pub/naif/generic_kernels/)

### Bash Script for BDS to OBJ Conversion
```bash
source setup_dskexp.sh
```
```bash
dskexp -dsk filename.bds -text filename.obj -format obj -prec 10
```

### Prerequisite
1. **Python 3.7+**
2. **Vispy**: Install with `pip install requirements`

---

## Usage

How to use this file to reproduce results or render your own:
[example_render.py](/example_render.py)
```python
from vispy import app
from scene import MainWindow
from data_loader import load_data

vertices, faces = load_data("test_data/ROS_ST_K020_OSPCLAM_U_V1.OBJ")
main_w = MainWindow()
main_w.set_model(vertices, faces)

app.run()
```
---

## Future Developments

- **Projectile Simulation of Flybys**: Visualize spacecraft trajectories, including entry, flyby, and exit paths around asteroids and comets.
- **Landing and Movement Tracking**: Display historical landing points and movement trails.
- **Saving Options**: Enable users to save visualized models and trajectories in standard formats.
- **GIF Export**: Add functionality to export animations of rotating objects or flybys as GIFs for presentations and reports.

---

## About Me
I am **Rahul R. Sah**, an undergraduate student at **Furman University**, SC. I am passionate about **Astronomy** and **Machine Learning**. This is one of my first contributions to the **open-source community**. If there are any requirements I missed or improvements needed, please let me know!

**Email**: [iamrahulrsah@gmail.com](mailto:iamrahulrsah@gmail.com)