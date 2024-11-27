Here's the revised README file that incorporates the presence of a Python GUI for executing the simulation:

---

# OpenFOAM Chimney Simulation with Python GUI

This repository contains a simulation case for analyzing chimney airflow using **OpenFOAM**, integrated with a **Python-based GUI** to streamline the execution of setup, simulation, and post-processing tasks.

The Python GUI simplifies interaction with the OpenFOAM workflow, making it more accessible for users who prefer a graphical interface over command-line operations.

## Features

- **Python GUI**: A user-friendly interface to configure, run, and visualize chimney simulations.
- **Mesh setup**: Automates the creation of a chimney geometry using OpenFOAM's `blockMesh` utility.
- **Simulation control**: Allows users to select solvers and adjust simulation parameters directly through the GUI.
- **Post-processing**: Integrated options to launch `Paraview` for result visualization.

## Repository Structure

```
OpenFOAM-Chimney/
├── constant/           # Physical properties and boundary condition settings
├── system/             # Simulation control settings (e.g., timesteps, solvers)
├── 0/                  # Initial and boundary condition files for the simulation
├── scripts/            # Utility scripts for pre- and post-processing
├── gui.py              # Python GUI application for managing the simulation
├── README.md           # Project documentation (this file)
└── LICENSE             # Licensing information
```

## Requirements

- **OpenFOAM**: Compatible with OpenFOAM version X.X (ensure your version matches the configurations).
- **Python 3.9 or earlier**: Required for running the GUI application.
- **PyQt5**: For the GUI interface.
- **Paraview**: For visualizing simulation results.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/iammix/OpenFOAM-Chimney.git
   cd OpenFOAM-Chimney
   ```

2. Install required Python packages:

   ```bash
   pip install PyQt5
   ```

3. Source your OpenFOAM environment:

   ```bash
   source /opt/openfoamX.X/etc/bashrc  # Update with your OpenFOAM version path
   ```

## Running the GUI Application

1. Launch the Python GUI:

   ```bash
   python gui.py
   ```

2. Use the GUI to:
   - Configure the simulation settings.
   - Execute `blockMesh` for mesh generation.
   - Run the selected solver (e.g., `simpleFoam` or `pimpleFoam`).
   - Open results directly in Paraview for visualization.

## Customization

- Update the Python GUI to include additional OpenFOAM utilities or customize its layout.
- Modify boundary conditions in the `0/` folder or solver settings in the `constant/` and `system/` directories as needed.
- Extend the `gui.py` functionality to handle complex cases, such as multi-region or multi-phase simulations.

## Contributions

Contributions are welcome! Feel free to fork the repository, add features, and submit pull requests. Ensure changes are well-documented and tested.

---
