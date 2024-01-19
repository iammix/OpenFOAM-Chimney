# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mesh_openfoam.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MeshOpenFoam(object):
    def setupUi(self, MeshOpenFoam):
        MeshOpenFoam.setObjectName("MeshOpenFoam")
        MeshOpenFoam.resize(697, 450)
        self.centralwidget = QtWidgets.QWidget(MeshOpenFoam)
        self.centralwidget.setObjectName("centralwidget")
        self.radius_le = QtWidgets.QLineEdit(self.centralwidget)
        self.radius_le.setGeometry(QtCore.QRect(130, 110, 113, 22))
        self.radius_le.setObjectName("radius_le")
        self.radius_lb = QtWidgets.QLabel(self.centralwidget)
        self.radius_lb.setGeometry(QtCore.QRect(50, 110, 60, 16))
        self.radius_lb.setObjectName("radius_lb")
        self.height_lb = QtWidgets.QLabel(self.centralwidget)
        self.height_lb.setGeometry(QtCore.QRect(48, 140, 60, 16))
        self.height_lb.setObjectName("height_lb")
        self.height_le = QtWidgets.QLineEdit(self.centralwidget)
        self.height_le.setGeometry(QtCore.QRect(130, 140, 111, 22))
        self.height_le.setObjectName("height_le")
        self.number_lb = QtWidgets.QLabel(self.centralwidget)
        self.number_lb.setGeometry(QtCore.QRect(50, 170, 60, 16))
        self.number_lb.setObjectName("number_lb")
        self.number_z_le = QtWidgets.QLineEdit(self.centralwidget)
        self.number_z_le.setGeometry(QtCore.QRect(130, 170, 113, 22))
        self.number_z_le.setObjectName("number_z_le")
        self.nodes_lb = QtWidgets.QLabel(self.centralwidget)
        self.nodes_lb.setGeometry(QtCore.QRect(50, 200, 60, 16))
        self.nodes_lb.setObjectName("nodes_lb")
        self.nodes_le = QtWidgets.QLineEdit(self.centralwidget)
        self.nodes_le.setGeometry(QtCore.QRect(130, 200, 113, 22))
        self.nodes_le.setObjectName("nodes_le")
        self.create_stl = QtWidgets.QPushButton(self.centralwidget)
        self.create_stl.setGeometry(QtCore.QRect(100, 240, 111, 26))
        self.create_stl.setObjectName("create_stl")
        self.run_openfoam = QtWidgets.QPushButton(self.centralwidget)
        self.run_openfoam.setGeometry(QtCore.QRect(100, 280, 111, 31))
        self.run_openfoam.setObjectName("run_openfoam")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(280, 20, 401, 381))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        MeshOpenFoam.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MeshOpenFoam)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 697, 21))
        self.menubar.setObjectName("menubar")
        MeshOpenFoam.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MeshOpenFoam)
        self.statusbar.setObjectName("statusbar")
        MeshOpenFoam.setStatusBar(self.statusbar)

        self.retranslateUi(MeshOpenFoam)
        QtCore.QMetaObject.connectSlotsByName(MeshOpenFoam)

    def retranslateUi(self, MeshOpenFoam):
        _translate = QtCore.QCoreApplication.translate
        MeshOpenFoam.setWindowTitle(_translate("MeshOpenFoam", "MainWindow"))
        self.radius_lb.setText(_translate("MeshOpenFoam", "Radius"))
        self.height_lb.setText(_translate("MeshOpenFoam", "Height"))
        self.number_lb.setText(_translate("MeshOpenFoam", "Number z"))
        self.nodes_lb.setText(_translate("MeshOpenFoam", "Nodes"))
        self.create_stl.setText(_translate("MeshOpenFoam", "Create stl file"))
        self.run_openfoam.setText(_translate("MeshOpenFoam", "OPENFOAM run"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MeshOpenFoam = QtWidgets.QMainWindow()
    ui = Ui_MeshOpenFoam()
    ui.setupUi(MeshOpenFoam)
    MeshOpenFoam.show()
    sys.exit(app.exec_())

