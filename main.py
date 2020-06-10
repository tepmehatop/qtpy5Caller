# This Python file uses the following encoding: utf-8
import sys
import os


from PyQt5.QtWidgets import QApplication, QWidget
# from PyQt5.QtCore import QFile
# from PyQt5.QtUiTools import QUiLoader
from configWindow import Ui_Dialog
from form import Ui_mainTest



app = QApplication([])

mainTest = QWidget()
ui = Ui_mainTest()
ui.setupUi(mainTest)
mainTest.showFullScreen()

Dialog = QWidget()
confUI = Ui_Dialog()

def runConfWin():
    confUI.setupUi(Dialog)
    Dialog.showFullScreen()

def test():
    mainTest.hide()
    runConfWin()
    confUI.returnButton.clicked.connect(test3)

def test3():
    mainTest.showFullScreen()
    Dialog.hide()



ui.configButton.clicked.connect(test)
ui.closeAppButton.clicked.connect(mainTest.close)

sys.exit(app.exec_())