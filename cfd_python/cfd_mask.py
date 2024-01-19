from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class CFDMaskWindow(QMainWindow):

    def __init__(self):
        super(CFDMaskWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("CFD Mask")
        self.initUI()

    def initUI(self):
        pass

    
def window():
    app = QApplication(sys.argv)
    win = CFDMaskWindow()
    win.show()
    sys.exit(app.exec_())


window()