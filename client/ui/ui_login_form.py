
from PyQt6 import QtCore, QtGui, QtWidgets

import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 305)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 60, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.line_login = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.line_login.setGeometry(QtCore.QRect(150, 100, 113, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_login.setFont(font)
        self.line_login.setReadOnly(False)
        self.line_login.setObjectName("line_login")
        self.line_password = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.line_password.setGeometry(QtCore.QRect(150, 140, 113, 21))
        self.line_password.setObjectName("line_password")
        self.Button_entrer = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Button_entrer.setGeometry(QtCore.QRect(150, 180, 111, 24))
        self.Button_entrer.setObjectName("Button_entrer")
        self.Button_cancel = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Button_cancel.setGeometry(QtCore.QRect(150, 220, 111, 24))
        self.Button_cancel.setObjectName("Button_cancel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "форма входа"))
        self.label.setText(_translate("MainWindow", "Добро пожаловать в МУЗЕЙ"))
        self.line_login.setPlaceholderText(_translate("MainWindow", "логин"))
        self.line_password.setPlaceholderText(_translate("MainWindow", "пароль"))
        self.Button_entrer.setText(_translate("MainWindow", "Войти"))
        self.Button_cancel.setText(_translate("MainWindow", "Отмена"))



