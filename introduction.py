# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Splash_Screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.7


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_Intro(object):
    def setupUi(self, MainWindow_Intro):
        MainWindow_Intro.setObjectName("MainWindow_Intro")
        MainWindow_Intro.resize(580, 390)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/images/RGU_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow_Intro.setWindowIcon(icon)
        MainWindow_Intro.setStyleSheet("background-color: rgb(223, 223, 223);")
        MainWindow_Intro.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.centralwidget = QtWidgets.QWidget(MainWindow_Intro)
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
        self.pushButton_Skip = QtWidgets.QPushButton(self.frame)
        self.pushButton_Skip.setGeometry(QtCore.QRect(210, 280, 70, 30))
        self.pushButton_Skip.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Skip.setToolTipDuration(1)
        self.pushButton_Skip.setStyleSheet("font: 9pt \"Verdana\";")
        self.pushButton_Skip.setAutoDefault(True)
        self.pushButton_Skip.setFlat(False)
        self.pushButton_Skip.setObjectName("pushButton_Skip")
        self.pushButton_Nxt = QtWidgets.QPushButton(self.frame)
        self.pushButton_Nxt.setGeometry(QtCore.QRect(360, 280, 70, 30))
        self.pushButton_Nxt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Nxt.setToolTipDuration(1)
        self.pushButton_Nxt.setStyleSheet("font: 9pt \"Verdana\";")
        self.pushButton_Nxt.setAutoDefault(True)
        self.pushButton_Nxt.setObjectName("pushButton_Nxt")
        MainWindow_Intro.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_Intro)
        self.statusbar.setObjectName("statusbar")
        MainWindow_Intro.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_Intro)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_Intro)

    def retranslateUi(self, MainWindow_Intro):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_Intro.setWindowTitle(_translate("MainWindow_Intro", "Sofi - Introduction"))
        self.label_Intro.setToolTip(_translate("MainWindow_Intro", "Introduction"))
        self.label_Intro.setText(_translate("MainWindow_Intro", "INTRODUCTION"))
        self.label.setToolTip(_translate("MainWindow_Intro", "Introduction"))
        self.label.setText(_translate("MainWindow_Intro", "AOS 1.0 is a virtual assistant. It\'s set up to do simple things like play music, surf the web, and view YouTube videos.\n"
"\n"
"\n"
"\n"
"In order to make it more accessible, it has been designed to function some of the time offline."))
        self.pushButton_Skip.setToolTip(_translate("MainWindow_Intro", "<html><head/><body><p align=\"center\">skip</p></body></html>"))
        self.pushButton_Skip.setText(_translate("MainWindow_Intro", "Skip"))
        self.pushButton_Nxt.setToolTip(_translate("MainWindow_Intro", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">Next Button</span></p></body></html>"))
        self.pushButton_Nxt.setText(_translate("MainWindow_Intro", "Next"))
import image_assets


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_Intro = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_Intro()
    ui.setupUi(MainWindow_Intro)
    MainWindow_Intro.show()
    sys.exit(app.exec_())
