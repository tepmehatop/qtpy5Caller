# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *





class Ui_mainTest(object):
    def setupUi(self, mainTest):
        if not mainTest.objectName():
            mainTest.setObjectName(u"mainTest")
        # основное окно
        mainTest.showFullScreen()
        # Кнопка открыть замок
        self.openDoorButton = QPushButton(mainTest)
        self.openDoorButton.setObjectName(u"openDoorButton")
        self.openDoorButton.setGeometry(QRect(100, 220, 271, 91))
        self.openDoorButton.show()

        # Кнопка камера 1
        self.camButton1 = QPushButton(mainTest)
        self.camButton1.setObjectName(u"camButton1")
        self.camButton1.setGeometry(QRect(102, 70, 271, 91))
        self.camButton1.show()

        # Кнопка конфиг
        self.configButton = QPushButton(mainTest)
        self.configButton.setObjectName(u"configButton")
        self.configButton.setGeometry(QRect(400, 220, 271, 91))
        self.configButton.show()

        # Кнопка камера 2
        self.camButton2 = QPushButton(mainTest)
        self.camButton2.setObjectName(u"camButton2")
        self.camButton2.setGeometry(QRect(400, 70, 271, 91))
        self.camButton2.show()

        # Кнопка камера 2
        self.closeAppButton = QPushButton(mainTest)
        self.closeAppButton.setObjectName(u"closeAppButton")
        self.closeAppButton.setGeometry(QRect(700, 20, 91, 51))
        self.closeAppButton.show()

        self.retranslateUi(mainTest)

        QMetaObject.connectSlotsByName(mainTest)
    # setupUi

    def retranslateUi(self, mainTest):
        mainTest.setWindowTitle(QCoreApplication.translate("mainTest", u"mainTest", None))
        self.openDoorButton.setText(QCoreApplication.translate("mainTest", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0437\u0430\u043c\u043e\u043a", None))
        self.camButton1.setText(QCoreApplication.translate("mainTest", u"\u041a\u0430\u043c\u0435\u0440\u0430 1", None))
        self.configButton.setText(QCoreApplication.translate("mainTest", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.camButton2.setText(QCoreApplication.translate("mainTest", u"\u041a\u0430\u043c\u0435\u0440\u0430 2", None))
        self.closeAppButton.setText(QCoreApplication.translate("mainTest", u"Закрыть", None))
    # retranslateUi


    def click_button(self):
        print("hello world")