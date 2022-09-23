# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Splash_Screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.7


from PyQt5 import QtCore, QtGui, QtWidgets

# from distutils.cmd import Command

from Main_Window import Ui_MainWindow_main
import manage
import time


class Ui_MainWindow_intro(object):
    def mainWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_main()
        self.ui.setupUi(self.window)
        self.window.show()
        manage.response("")
        #manage.command()
    def setupUi(self, MainWindow_intro):
        MainWindow_intro.setObjectName("MainWindow_intro")
        MainWindow_intro.resize(580, 390)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow_intro.setWindowIcon(icon)
        MainWindow_intro.setStyleSheet("background-color: rgb(223, 223, 223);")
        MainWindow_intro.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.centralwidget = QtWidgets.QWidget(MainWindow_intro)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(39, 19, 501, 331))
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(3)
        self.frame.setMidLineWidth(1)
        self.frame.setObjectName("frame")
        self.label_Intro = QtWidgets.QLabel(self.frame)
        self.label_Intro.setEnabled(True)
        self.label_Intro.setGeometry(QtCore.QRect(80, 20, 330, 41))
        self.label_Intro.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.label_Intro.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_Intro.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_Intro.setLineWidth(3)
        self.label_Intro.setMidLineWidth(1)
        self.label_Intro.setScaledContents(True)
        self.label_Intro.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Intro.setWordWrap(True)
        self.label_Intro.setIndent(1)
        self.label_Intro.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_Intro.setObjectName("label_Intro")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 91, 410, 151))
        self.label.setBaseSize(QtCore.QSize(2, 2))
        self.label.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.label.setToolTipDuration(1)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("font: 12pt \"Verdana\";\n"
"color: rgb(0, 0, 0);")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setLineWidth(3)
        self.label.setMidLineWidth(1)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setIndent(10)
        self.label.setOpenExternalLinks(False)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        
        MainWindow_intro.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_intro)
        self.statusbar.setObjectName("statusbar")
        MainWindow_intro.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_intro)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_intro)

    def retranslateUi(self, MainWindow_intro):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_intro.setWindowTitle(_translate("MainWindow_intro", "AOS - Introduction"))
        self.label_Intro.setToolTip(_translate("MainWindow_intro", "Introduction"))
        self.label_Intro.setText(_translate("MainWindow_intro", "INTRODUCTION"))
        self.label.setToolTip(_translate("MainWindow_intro", "Introduction"))
        self.label.setText(_translate("MainWindow_intro", "AOS 1.0 is a virtual assistant. It\'s set up to do simple things like play music, surf the web, and view YouTube videos.\n"
"\n"
"\n"
"\n"
"In order to make it more accessible, it has been designed to function some of the time offline."))
        self.label.text()
        
        
    def respd(self):
        self.str_cont = ui.label.text()
        manage.response(self.str_cont)


    n = 100
    def com_wait(self, n):
        completed = 0
        for i in range(n):
                time.sleep(0.01)
                completed += 1
                if completed == 99:
                        self.mainWindow()

import image_assets


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_intro = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_intro()
    ui.setupUi(MainWindow_intro)
    MainWindow_intro.show()
    manage.response("")
    ui.respd()
    ui.com_wait(100)
    MainWindow_intro.close()
    sys.exit(app.exec_())
