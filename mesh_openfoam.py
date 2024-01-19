# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mesh_openfoam.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import numpy as np
import pyqtgraph.opengl as gl
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from stl import mesh
from stl.mesh import Mesh

from cfd_python.surf2stl import surf2stl


def pol2cart(r, theta):
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return (x, y)


class Ui_MeshOpenFoam(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MeshOpenFoam, self).__init__()

    def AddData(self):

        self.radius_le = QtWidgets.QLineEdit(self.centralwidget)
        self.radius_le.setGeometry(QtCore.QRect(130, 110, 113, 22))
        self.radius_le.setObjectName("radius_le")
        self.radius_lb = QtWidgets.QLabel(self.centralwidget)
        self.radius_lb.setGeometry(QtCore.QRect(50, 110, 60, 16))
        self.radius_lb.setObjectName("radius_lb")

        # Connect the returnPressed signal to the check_float method
        self.radius_le.returnPressed.connect(lambda: self.check_float("radius"))

        self.height_lb = QtWidgets.QLabel(self.centralwidget)
        self.height_lb.setGeometry(QtCore.QRect(48, 140, 60, 16))
        self.height_lb.setObjectName("height_lb")
        self.height_le = QtWidgets.QLineEdit(self.centralwidget)
        self.height_le.setGeometry(QtCore.QRect(130, 140, 111, 22))
        self.height_le.setObjectName("height_le")

        # Connect the returnPressed signal to the check_float method
        self.radius_le.returnPressed.connect(lambda: self.check_float("height"))

        self.number_lb = QtWidgets.QLabel(self.centralwidget)
        self.number_lb.setGeometry(QtCore.QRect(50, 170, 60, 16))
        self.number_lb.setObjectName("number_lb")
        self.number_z_le = QtWidgets.QLineEdit(self.centralwidget)
        self.number_z_le.setGeometry(QtCore.QRect(130, 170, 113, 22))
        self.number_z_le.setObjectName("number_z_le")

        # Connect the returnPressed signal to the check_float method
        self.radius_le.returnPressed.connect(lambda: self.check_float("number"))

        self.nodes_lb = QtWidgets.QLabel(self.centralwidget)
        self.nodes_lb.setGeometry(QtCore.QRect(50, 200, 60, 16))
        self.nodes_lb.setObjectName("nodes_lb")
        self.nodes_le = QtWidgets.QLineEdit(self.centralwidget)
        self.nodes_le.setGeometry(QtCore.QRect(130, 200, 113, 22))
        self.nodes_le.setObjectName("nodes_le")

        # Connect the returnPressed signal to the check_float method
        self.radius_le.returnPressed.connect(lambda: self.check_float("nodes"))

    def check_float(self, check_item):
        input_text = self.radius_le.text()

        try:
            # Try converting the input to an integer
            int_value = float(input_text)
            # If successful, reset the line edit's background color
            self.radius_le.setStyleSheet("")

        except ValueError:
            # If the conversion fails, set the line edit's background color to red
            self.radius_le.setStyleSheet("background-color: red;")

            # Show a warning message box with the error message
            QtWidgets.QMessageBox.warning(self, "Invalid Input", f"Please enter a valid float for the {check_item}")

    def setupUi(self, MeshOpenFoam):
        MeshOpenFoam.setObjectName("MeshOpenFoam")
        MeshOpenFoam.resize(697, 450)
        self.centralwidget = QtWidgets.QWidget(MeshOpenFoam)
        self.centralwidget.setObjectName("centralwidget")

        self.AddData()

        self.create_stl = QtWidgets.QPushButton(self.centralwidget)
        self.create_stl.setGeometry(QtCore.QRect(100, 240, 111, 26))
        self.create_stl.setObjectName("create_stl")
        self.run_openfoam = QtWidgets.QPushButton(self.centralwidget)
        self.run_openfoam.setGeometry(QtCore.QRect(100, 280, 111, 31))
        self.run_openfoam.setObjectName("run_openfoam")
        MeshOpenFoam.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MeshOpenFoam)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 697, 21))
        self.menubar.setObjectName("menubar")
        MeshOpenFoam.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MeshOpenFoam)
        self.statusbar.setObjectName("statusbar")
        MeshOpenFoam.setStatusBar(self.statusbar)

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(280, 20, 401, 381))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.retranslateUi(MeshOpenFoam)
        QtCore.QMetaObject.connectSlotsByName(MeshOpenFoam)
        self.create_stl.clicked.connect(self.write_stl)

    def retranslateUi(self, MeshOpenFoam):
        _translate = QtCore.QCoreApplication.translate
        MeshOpenFoam.setWindowTitle(_translate("MeshOpenFoam", "MainWindow"))
        self.radius_lb.setText(_translate("MeshOpenFoam", "Radius"))
        self.height_lb.setText(_translate("MeshOpenFoam", "Height"))
        self.number_lb.setText(_translate("MeshOpenFoam", "Number z"))
        self.nodes_lb.setText(_translate("MeshOpenFoam", "Nodes"))
        self.create_stl.setText(_translate("MeshOpenFoam", "Create stl file"))
        self.run_openfoam.setText(_translate("MeshOpenFoam", "OPENFOAM run"))

    def plot_stl(self):
        try:
            # Load the STL file
            mesh_data = mesh.Mesh.from_file(self.stl_filename)

            # Extract vertices from the mesh
            vertices = mesh_data.vectors

            # Create a 3D mesh item
            mesh_item = gl.GLMeshItem(vertexes=vertices, color=(0.0, 0.0, 1.0, 1.0))  # Blue color
            self.view.addItem(mesh_item)

            # Add global axes
            axis_item = gl.GLAxisItem()
            self.view.addItem(axis_item)

            # Add a white background
            bg_color = (1.0, 1.0, 1.0, 1.0)
            self.view.setBackgroundColor(bg_color)

        except Exception as e:
            print(f"Error loading STL file: {e}")

    def write_stl(self):
        radius = float(self.radius_le.text())
        height = float(self.height_le.text())
        number_z = int(self.number_z_le.text())
        nodes = int(self.nodes_le.text())

        r = radius * np.ones(nodes)
        th = np.linspace(0, 2 * np.pi, nodes)
        z = np.linspace(0, height, number_z)

        x, y = pol2cart(r, th)

        X = np.tile(x, (number_z, 1))
        Y = np.tile(y, (number_z, 1))
        Z = np.tile(z, (nodes, 1)).T

        x_c = np.zeros(nodes)
        y_c = np.zeros(nodes)
        z_c = np.tile(height, nodes)

        X = np.vstack([X, x_c])
        Y = np.vstack([Y, y_c])
        Z = np.vstack([Z, z_c])

        surf2stl('cylinder.stl', X, Y, Z, 'ascii')
        msg = QMessageBox()
        msg.setWindowTitle('INFO')
        msg.setText(".stl File created!")
        msg.exec()

        self.stl_filename = 'cylinder.stl'
        mesh = Mesh.from_file(self.stl_filename)
        plot_layout = self.horizontalLayout

        self.view = gl.GLViewWidget()
        plot_layout.addWidget(self.view)
        self.plot_stl()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MeshOpenFoam = QtWidgets.QMainWindow()
    ui = Ui_MeshOpenFoam()
    ui.setupUi(MeshOpenFoam)
    MeshOpenFoam.show()
    sys.exit(app.exec_())
