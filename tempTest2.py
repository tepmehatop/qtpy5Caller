from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

from tempTest import Ui_Main

class Main(QMainWindow, Ui_Main):
       def __init__(self, parent=None):
           super(Main, self).__init__(parent)
           self.setupUi(self)

           self.configButton.clicked.connect(self.OpenWindow1)
           self.returnButton.clicked.connect(self.OpenWindow2)
           # self.openDoorButton.clicked.connect(self.OpenWindow2)

       def OpenWindow1(self):
           self.QtStack.setCurrentIndex(1)

       def OpenWindow2(self):
           self.QtStack.setCurrentIndex(0)

if __name__ == '__main__':
       app = QApplication(sys.argv)
       showMain = Main()
       sys.exit(app.exec_())