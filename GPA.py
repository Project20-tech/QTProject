# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GPA.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GPA(object):
    def setupUi(self, GPA):
        GPA.setObjectName("GPA")
        GPA.resize(442, 447)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 96, 178))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        GPA.setPalette(palette)
        GPA.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        GPA.setDocumentMode(False)
        GPA.setTabShape(QtWidgets.QTabWidget.Rounded)
        GPA.setDockNestingEnabled(False)
        GPA.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(GPA)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 80, 221, 111))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(130, 10, 51, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setGeometry(QtCore.QRect(130, 40, 51, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(70, 80, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 91, 16))
        self.label_2.setObjectName("label_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(240, 80, 191, 261))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 161, 16))
        self.label_5.setObjectName("label_5")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 210, 221, 131))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(30, 20, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 121, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(80, 20, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 50, 61, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(10, 90, 91, 16))
        self.label_6.setObjectName("label_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 360, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 360, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(310, 360, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.lblTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblTitle.setGeometry(QtCore.QRect(110, 10, 191, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTitle.sizePolicy().hasHeightForWidth())
        self.lblTitle.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lblTitle.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitle.setFont(font)
        self.lblTitle.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblTitle.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lblTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitle.setObjectName("lblTitle")
        self.lblTitle_2 = QtWidgets.QLabel(self.centralwidget)
        self.lblTitle_2.setGeometry(QtCore.QRect(80, 40, 251, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTitle_2.sizePolicy().hasHeightForWidth())
        self.lblTitle_2.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lblTitle_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitle_2.setFont(font)
        self.lblTitle_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblTitle_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lblTitle_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitle_2.setObjectName("lblTitle_2")
        GPA.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GPA)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 442, 21))
        self.menubar.setObjectName("menubar")
        self.menuGPA = QtWidgets.QMenu(self.menubar)
        self.menuGPA.setObjectName("menuGPA")
        self.menuCGPA = QtWidgets.QMenu(self.menubar)
        self.menuCGPA.setObjectName("menuCGPA")
        self.menuHELP = QtWidgets.QMenu(self.menubar)
        self.menuHELP.setObjectName("menuHELP")
        self.menuABOUT = QtWidgets.QMenu(self.menubar)
        self.menuABOUT.setObjectName("menuABOUT")
        GPA.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(GPA)
        self.statusbar.setObjectName("statusbar")
        GPA.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuGPA.menuAction())
        self.menubar.addAction(self.menuCGPA.menuAction())
        self.menubar.addAction(self.menuHELP.menuAction())
        self.menubar.addAction(self.menuABOUT.menuAction())

        self.retranslateUi(GPA)
        QtCore.QMetaObject.connectSlotsByName(GPA)

    def retranslateUi(self, GPA):
        _translate = QtCore.QCoreApplication.translate
        GPA.setWindowTitle(_translate("GPA", "MainWindow"))
        self.pushButton.setText(_translate("GPA", "ADD"))
        self.label.setText(_translate("GPA", "GRADE"))
        self.label_2.setText(_translate("GPA", "CREDIT HOUR (S)"))
        self.label_5.setText(_translate("GPA", "GPA ADDED PREVIEW"))
        self.label_3.setText(_translate("GPA", "GPA:"))
        self.label_4.setText(_translate("GPA", "TOTAL CREDIT HOURS"))
        self.label_6.setText(_translate("GPA", "CLASS ATTAINED"))
        self.pushButton_2.setText(_translate("GPA", "NEW"))
        self.pushButton_3.setText(_translate("GPA", "PushButton"))
        self.pushButton_4.setText(_translate("GPA", "SCREENSHOT"))
        self.lblTitle.setText(_translate("GPA", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:400;\">GPA</span></p></body></html>"))
        self.lblTitle_2.setText(_translate("GPA", "<html><head/><body><p>CALCULATOR</p></body></html>"))
        self.menuGPA.setTitle(_translate("GPA", "GPA"))
        self.menuCGPA.setTitle(_translate("GPA", "CGPA"))
        self.menuHELP.setTitle(_translate("GPA", "HELP"))
        self.menuABOUT.setTitle(_translate("GPA", "ABOUT"))

