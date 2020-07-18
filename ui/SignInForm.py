# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file
# 'C:\Users\dmitr\Documents\PyCharm Projects\Practice\ui\SignInForm.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from ui.RegistrationForm import *


class QPasswordEdit(QLineEdit):
    def __init__(self, parent):
        super().__init__(parent)

        self.eye_visible = QtGui.QIcon("img\\eye_visible.svg")
        self.eye_hidden = QtGui.QIcon("img\\eye_hidden.svg")

        self.setEchoMode(QLineEdit.Password)
        self.toggle_password_visibility = self.addAction(self.eye_visible, QLineEdit.TrailingPosition)
        self.toggle_password_visibility.triggered.connect(self.on_toggle_password_Action)
        self.password_visibility = False

    def on_toggle_password_Action(self):
        if not self.password_visibility:
            self.setEchoMode(QLineEdit.Normal)
            self.password_visibility = True
            self.toggle_password_visibility.setIcon(self.eye_hidden)
        else:
            self.setEchoMode(QLineEdit.Password)
            self.password_visibility = False
            self.toggle_password_visibility.setIcon(self.eye_visible)


class Ui_SignIn(object):
    link = ""

    def setupUi(self, SignInForm):
        self.link = SignInForm
        SignInForm.setObjectName("SignInForm")
        SignInForm.resize(480, 240)
        SignInForm.setFixedSize(480, 240)
        SignInForm.setWindowIcon(QtGui.QIcon("img\\shield.svg"))

        self.centralwidget = QtWidgets.QWidget(SignInForm)
        self.centralwidget.setObjectName("centralwidget")

        self.login_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.login_line_edit.setGeometry(QtCore.QRect(140, 60, 200, 30))
        self.login_line_edit.setPlaceholderText("Login")
        self.login_line_edit.setObjectName("login_line_edit")
        self.login_line_edit.setStyleSheet("border-radius: 7px;"
                                           "font-family: JetBrains Mono;"
                                           "font-size: 12px;")

        self.password_line_edit = QPasswordEdit(self.centralwidget)
        self.password_line_edit.setGeometry(QtCore.QRect(140, 100, 200, 30))
        self.password_line_edit.setPlaceholderText("Password")
        self.password_line_edit.setObjectName("password_line_edit")
        self.password_line_edit.setStyleSheet("border-radius: 7px;"
                                              "font-family: JetBrains Mono;"
                                              "font-size: 12px;")

        self.signinbutton = QtWidgets.QPushButton(self.centralwidget)
        self.signinbutton.setGeometry(QtCore.QRect(165, 144, 150, 30))
        self.signinbutton.setObjectName("signinbutton")
        self.signinbutton.setStyleSheet("QPushButton {"
                                        "background-color: #02A3D6;"
                                        "border-radius: 15px;"
                                        "color: white;"
                                        "text-align: center;"
                                        "text-decoration: none;"
                                        "display: inline-block;"
                                        "font-family: JetBrains Mono ExtraBold;"
                                        "font-size: 14px;"
                                        "}"
                                        "QPushButton:hover {"
                                        "background-color: #00C1FF;"
                                        "}")
        self.signinbutton.clicked.connect(self.button_clicked)

        SignInForm.setCentralWidget(self.centralwidget)

        self.retranslateUi(SignInForm)
        QtCore.QMetaObject.connectSlotsByName(SignInForm)

    def open_main(self):
        self.win = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.win)
        self.win.show()
        self.link.close()

    def button_clicked(self):
        login_value = self.login_line_edit.text()
        password_value = self.password_line_edit.text()

        if login_value == "admin" and password_value == "admin":
            self.open_main()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setWindowIcon(QtGui.QIcon("img\\error.svg"))
            msg.setText("Ошибка входа")
            msg.setInformativeText("Логин или пароль введены неверно!"
                                   "Пожалуйства, попробуйте еще раз (убедитесь, что ваш caps lock выключен)")
            msg.setStyleSheet("font-family: JetBrains Mono;"
                              "font-size: 12px;")
            ok_button = msg.addButton('OK', QtWidgets.QMessageBox.AcceptRole)
            ok_button.setFixedSize(150, 25)
            ok_button.setStyleSheet("QPushButton {"
                                    "background-color: #02A3D6;"
                                    "border-radius: 10px;"
                                    "color: white;"
                                    "text-align: center;"
                                    "text-decoration: none;"
                                    "display: inline-block;"
                                    "font-family: JetBrains Mono ExtraBold;"
                                    "font-size: 14px;"
                                    "}"
                                    "QPushButton:hover {"
                                    "background-color: #00C1FF;"
                                    "}")
            msg.exec_()

    def retranslateUi(self, SignInForm):
        _translate = QtCore.QCoreApplication.translate
        SignInForm.setWindowTitle(_translate("SignInForm", "Вход в систему"))
        self.signinbutton.setText(_translate("SignInForm", "ВОЙТИ"))
