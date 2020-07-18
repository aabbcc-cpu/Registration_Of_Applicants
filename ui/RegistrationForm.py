# -- coding: utf-8 --

# Form implementation generated from reading ui file
# 'C:\Users\dmitr\Documents\PyCharm Projects\Practice\ui\RegistrationOfApplicants.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import sys
import sqlite3
from PyQt5.Qt import QLineEdit
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    insert_error = False

    CSS_line_edit = '''QLineEdit {
                    border-radius: 7px;
                    font-family: JetBrains Mono;
                    font-size: 12px;
                    border: 1px solid black;
    }
    '''

    CSS_label = '''QLabel{
                    color: #404040;
                    font-family: JetBrains Mono Medium;
                    font-size: 12px;
    }
    '''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        MainWindow.setFixedSize(1024, 768)
        MainWindow.setWindowIcon(QtGui.QIcon("img\\shield.svg"))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Персональные данные
        self.surname_label = QtWidgets.QLabel(self.centralwidget)
        self.surname_label.setGeometry(QtCore.QRect(300, 60, 65, 16))
        self.surname_label.setObjectName("surname_label")
        self.surname_label.setStyleSheet(self.CSS_label)

        self.surname_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.surname_line_edit.setGeometry(QtCore.QRect(300, 80, 113, 20))
        self.surname_line_edit.setObjectName("surname_line_edit")
        self.surname_line_edit.setStyleSheet(self.CSS_line_edit)

        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(440, 60, 61, 16))
        self.name_label.setObjectName("name_label")
        self.name_label.setStyleSheet(self.CSS_label)

        self.name_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.name_line_edit.setGeometry(QtCore.QRect(440, 80, 113, 20))
        self.name_line_edit.setObjectName("name_line_edit")
        self.name_line_edit.setStyleSheet(self.CSS_line_edit)

        self.patronymic_label = QtWidgets.QLabel(self.centralwidget)
        self.patronymic_label.setGeometry(QtCore.QRect(580, 60, 61, 16))
        self.patronymic_label.setObjectName("patronymic_label")
        self.patronymic_label.setStyleSheet(self.CSS_label)

        self.patronymic_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.patronymic_line_edit.setGeometry(QtCore.QRect(580, 80, 113, 20))
        self.patronymic_line_edit.setObjectName("patronymic_line_edit")
        self.patronymic_line_edit.setStyleSheet(self.CSS_line_edit)

        self.sex_label = QtWidgets.QLabel(self.centralwidget)
        self.sex_label.setGeometry(QtCore.QRect(300, 100, 61, 16))
        self.sex_label.setObjectName("sex_label")
        self.sex_label.setStyleSheet(self.CSS_label)

        self.male_cb = QtWidgets.QCheckBox(self.centralwidget)
        self.male_cb.setGeometry(QtCore.QRect(300, 120, 70, 17))
        self.male_cb.setObjectName("male_cb")
        self.male_cb.clicked.connect(self.check_mcb)
        self.male_cb.setStyleSheet("color: #404040;"
                                   "font-family: JetBrains Mono;"
                                   "font-size: 12px;")

        self.female_cb = QtWidgets.QCheckBox(self.centralwidget)
        self.female_cb.setGeometry(QtCore.QRect(370, 120, 70, 17))
        self.female_cb.setObjectName("female_cb")
        self.female_cb.clicked.connect(self.check_fcb)
        self.female_cb.setStyleSheet("color: #404040;"
                                     "font-family: JetBrains Mono;"
                                     "font-size: 12px;")

        self.birthday_label = QtWidgets.QLabel(self.centralwidget)
        self.birthday_label.setGeometry(QtCore.QRect(440, 100, 91, 16))
        self.birthday_label.setObjectName("birthday_label")
        self.birthday_label.setStyleSheet(self.CSS_label)

        self.birthday_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.birthday_line_edit.setGeometry(QtCore.QRect(440, 120, 113, 20))
        self.birthday_line_edit.setObjectName("birthday_line_edit")
        self.birthday_line_edit.setStyleSheet(self.CSS_line_edit)

        self.nationality_label = QtWidgets.QLabel(self.centralwidget)
        self.nationality_label.setGeometry(QtCore.QRect(580, 100, 81, 16))
        self.nationality_label.setObjectName("nationality_label")
        self.nationality_label.setStyleSheet(self.CSS_label)

        self.nationality_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.nationality_line_edit.setGeometry(QtCore.QRect(580, 120, 113, 20))
        self.nationality_line_edit.setObjectName("nationality_line_edit")
        self.nationality_line_edit.setStyleSheet(self.CSS_line_edit)

        self.birthplace_label = QtWidgets.QLabel(self.centralwidget)
        self.birthplace_label.setGeometry(QtCore.QRect(300, 140, 101, 16))
        self.birthplace_label.setObjectName("birthplace_label")
        self.birthplace_label.setStyleSheet(self.CSS_label)

        self.birthplace_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.birthplace_line_edit.setGeometry(QtCore.QRect(300, 160, 391, 20))
        self.birthplace_line_edit.setObjectName("birthplace_line_edit")
        self.birthplace_line_edit.setStyleSheet(self.CSS_line_edit)

        # Документ, удостоверяющий личность
        self.document_label = QtWidgets.QLabel(self.centralwidget)
        self.document_label.setGeometry(QtCore.QRect(300, 180, 250, 21))
        self.document_label.setObjectName("document_label")
        self.document_label.setStyleSheet(self.CSS_label)

        self.document_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.document_line_edit.setGeometry(QtCore.QRect(300, 200, 391, 20))
        self.document_line_edit.setObjectName("document_line_edit")
        self.document_line_edit.setStyleSheet(self.CSS_line_edit)

        self.identity_series_label = QtWidgets.QLabel(self.centralwidget)
        self.identity_series_label.setGeometry(QtCore.QRect(300, 220, 41, 16))
        self.identity_series_label.setObjectName("identity_series_label")
        self.identity_series_label.setStyleSheet(self.CSS_label)

        self.identity_series_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.identity_series_line_edit.setGeometry(QtCore.QRect(300, 240, 111, 20))
        self.identity_series_line_edit.setObjectName("identity_series_line_edit")
        self.identity_series_line_edit.setStyleSheet(self.CSS_line_edit)

        self.identity_number_label = QtWidgets.QLabel(self.centralwidget)
        self.identity_number_label.setGeometry(QtCore.QRect(440, 220, 51, 16))
        self.identity_number_label.setObjectName("identity_number_label")
        self.identity_number_label.setStyleSheet(self.CSS_label)

        self.identity_number_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.identity_number_line_edit.setGeometry(QtCore.QRect(440, 240, 111, 20))
        self.identity_number_line_edit.setObjectName("identity_number_line_edit")
        self.identity_number_line_edit.setStyleSheet(self.CSS_line_edit)

        self.identity_issue_date_label = QtWidgets.QLabel(self.centralwidget)
        self.identity_issue_date_label.setGeometry(QtCore.QRect(580, 220, 71, 16))
        self.identity_issue_date_label.setObjectName("identity_issue_date_label")
        self.identity_issue_date_label.setStyleSheet(self.CSS_label)

        self.identity_issue_date_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.identity_issue_date_line_edit.setGeometry(QtCore.QRect(580, 240, 111, 20))
        self.identity_issue_date_line_edit.setObjectName("identity_issue_date_line_edit")
        self.identity_issue_date_line_edit.setStyleSheet(self.CSS_line_edit)

        self.identity_issue_org_label = QtWidgets.QLabel(self.centralwidget)
        self.identity_issue_org_label.setGeometry(QtCore.QRect(300, 260, 71, 16))
        self.identity_issue_org_label.setObjectName("identity_issue_org_label")
        self.identity_issue_org_label.setStyleSheet(self.CSS_label)

        self.identity_issue_org_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.identity_issue_org_line_edit.setGeometry(QtCore.QRect(300, 280, 391, 20))
        self.identity_issue_org_line_edit.setObjectName("identity_issue_org_line_edit")
        self.identity_issue_org_line_edit.setStyleSheet(self.CSS_line_edit)

        # Контактная информация
        self.email_label = QtWidgets.QLabel(self.centralwidget)
        self.email_label.setGeometry(QtCore.QRect(300, 310, 41, 16))
        self.email_label.setObjectName("email_label")
        self.email_label.setStyleSheet(self.CSS_label)

        self.email_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.email_line_edit.setGeometry(QtCore.QRect(300, 330, 111, 20))
        self.email_line_edit.setObjectName("email_line_edit")
        self.email_line_edit.setStyleSheet(self.CSS_line_edit)

        self.phone_number_label = QtWidgets.QLabel(self.centralwidget)
        self.phone_number_label.setGeometry(QtCore.QRect(440, 310, 91, 16))
        self.phone_number_label.setObjectName("phone_number_label")
        self.phone_number_label.setStyleSheet(self.CSS_label)

        self.phone_number_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.phone_number_line_edit.setGeometry(QtCore.QRect(440, 330, 111, 20))
        self.phone_number_line_edit.setObjectName("phone_number_line_edit")
        self.phone_number_line_edit.setStyleSheet(self.CSS_line_edit)

        self.home_phone_number_label = QtWidgets.QLabel(self.centralwidget)
        self.home_phone_number_label.setGeometry(QtCore.QRect(580, 310, 151, 16))
        self.home_phone_number_label.setObjectName("home_phone_number_line_edit")
        self.home_phone_number_label.setStyleSheet(self.CSS_label)

        self.home_phone_number_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.home_phone_number_line_edit.setGeometry(QtCore.QRect(580, 330, 111, 20))
        self.home_phone_number_line_edit.setObjectName("home_phone_number_line_edit")
        self.home_phone_number_line_edit.setStyleSheet(self.CSS_line_edit)

        # Образование
        self.name_ei_label = QtWidgets.QLabel(self.centralwidget)
        self.name_ei_label.setGeometry(QtCore.QRect(300, 350, 220, 15))
        self.name_ei_label.setObjectName("name_ei_label")
        self.name_ei_label.setStyleSheet(self.CSS_label)

        self.name_ei_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.name_ei_line_edit.setGeometry(QtCore.QRect(300, 370, 391, 20))
        self.name_ei_line_edit.setObjectName("name_ei_line_edit")
        self.name_ei_line_edit.setStyleSheet(self.CSS_line_edit)

        self.issue_year_ei_label = QtWidgets.QLabel(self.centralwidget)
        self.issue_year_ei_label.setGeometry(QtCore.QRect(300, 390, 100, 15))
        self.issue_year_ei_label.setObjectName("issue_year_ei_label")
        self.issue_year_ei_label.setStyleSheet(self.CSS_label)

        self.issue_year_ei_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.issue_year_ei_line_edit.setGeometry(QtCore.QRect(300, 410, 111, 20))
        self.issue_year_ei_line_edit.setObjectName("issue_year_ei_line_edit")
        self.issue_year_ei_line_edit.setStyleSheet(self.CSS_line_edit)

        self.education_label = QtWidgets.QLabel(self.centralwidget)
        self.education_label.setGeometry(QtCore.QRect(440, 390, 131, 16))
        self.education_label.setObjectName("education_label")
        self.education_label.setStyleSheet(self.CSS_label)

        self.education_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.education_line_edit.setGeometry(QtCore.QRect(440, 410, 111, 20))
        self.education_line_edit.setObjectName("education_line_edit")
        self.education_line_edit.setStyleSheet(self.CSS_line_edit)

        self.education_document_label = QtWidgets.QLabel(self.centralwidget)
        self.education_document_label.setGeometry(QtCore.QRect(580, 390, 81, 16))
        self.education_document_label.setObjectName("education_document_label")
        self.education_document_label.setStyleSheet(self.CSS_label)

        self.education_document_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.education_document_line_edit.setGeometry(QtCore.QRect(580, 410, 111, 20))
        self.education_document_line_edit.setObjectName("education_document_line_edit")
        self.education_document_line_edit.setStyleSheet(self.CSS_line_edit)

        self.education_series_label = QtWidgets.QLabel(self.centralwidget)
        self.education_series_label.setGeometry(QtCore.QRect(300, 430, 131, 16))
        self.education_series_label.setObjectName("education_series_label")
        self.education_series_label.setStyleSheet(self.CSS_label)

        self.education_series_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.education_series_line_edit.setGeometry(QtCore.QRect(300, 450, 111, 20))
        self.education_series_line_edit.setObjectName("education_series_line_edit")
        self.education_series_line_edit.setStyleSheet(self.CSS_line_edit)

        self.education_number_label = QtWidgets.QLabel(self.centralwidget)
        self.education_number_label.setGeometry(QtCore.QRect(440, 430, 81, 16))
        self.education_number_label.setObjectName("education_number_label")
        self.education_number_label.setStyleSheet(self.CSS_label)

        self.education_number_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.education_number_line_edit.setGeometry(QtCore.QRect(440, 450, 111, 20))
        self.education_number_line_edit.setObjectName("education_number_line_edit")
        self.education_number_line_edit.setStyleSheet(self.CSS_line_edit)

        self.education_issue_date_label = QtWidgets.QLabel(self.centralwidget)
        self.education_issue_date_label.setGeometry(QtCore.QRect(580, 430, 131, 16))
        self.education_issue_date_label.setObjectName("education_issue_date_line_edit")
        self.education_issue_date_label.setStyleSheet(self.CSS_label)

        self.education_issue_date_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.education_issue_date_line_edit.setGeometry(QtCore.QRect(580, 450, 111, 20))
        self.education_issue_date_line_edit.setObjectName("education_issue_date_line_edit")
        self.education_issue_date_line_edit.setStyleSheet(self.CSS_line_edit)

        # Экзамены
        self.discipline_label = QtWidgets.QLabel(self.centralwidget)
        self.discipline_label.setGeometry(QtCore.QRect(300, 520, 91, 16))
        self.discipline_label.setObjectName("discipline_label")
        self.discipline_label.setStyleSheet(self.CSS_label)

        self.discipline1_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.discipline1_line_edit.setGeometry(QtCore.QRect(300, 540, 190, 20))
        self.discipline1_line_edit.setObjectName("discipline1_line_edit")
        self.discipline1_line_edit.setStyleSheet(self.CSS_line_edit)

        self.discipline2_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.discipline2_line_edit.setGeometry(QtCore.QRect(300, 570, 190, 20))
        self.discipline2_line_edit.setObjectName("discipline2_line_edit")
        self.discipline2_line_edit.setStyleSheet(self.CSS_line_edit)

        self.discipline3_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.discipline3_line_edit.setGeometry(QtCore.QRect(300, 600, 190, 20))
        self.discipline3_line_edit.setObjectName("discipline3_line_edit")
        self.discipline3_line_edit.setStyleSheet(self.CSS_line_edit)

        self.discipline4_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.discipline4_line_edit.setGeometry(QtCore.QRect(300, 630, 190, 20))
        self.discipline4_line_edit.setObjectName("discipline4_line_edit")
        self.discipline4_line_edit.setStyleSheet(self.CSS_line_edit)

        self.point_label = QtWidgets.QLabel(self.centralwidget)
        self.point_label.setGeometry(QtCore.QRect(500, 520, 91, 16))
        self.point_label.setObjectName("point_label")
        self.point_label.setStyleSheet(self.CSS_label)

        self.point1_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.point1_line_edit.setGeometry(QtCore.QRect(500, 540, 91, 20))
        self.point1_line_edit.setObjectName("point1_line_edit")
        self.point1_line_edit.setStyleSheet(self.CSS_line_edit)

        self.point2_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.point2_line_edit.setGeometry(QtCore.QRect(500, 570, 91, 20))
        self.point2_line_edit.setObjectName("point2_line_edit")
        self.point2_line_edit.setStyleSheet(self.CSS_line_edit)

        self.point3_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.point3_line_edit.setGeometry(QtCore.QRect(500, 600, 91, 20))
        self.point3_line_edit.setObjectName("point3_line_edit")
        self.point3_line_edit.setStyleSheet(self.CSS_line_edit)

        self.point4_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.point4_line_edit.setGeometry(QtCore.QRect(500, 630, 91, 20))
        self.point4_line_edit.setObjectName("point4_line_edit")
        self.point4_line_edit.setStyleSheet(self.CSS_line_edit)

        self.year_delivery_label = QtWidgets.QLabel(self.centralwidget)
        self.year_delivery_label.setGeometry(QtCore.QRect(600, 520, 91, 16))
        self.year_delivery_label.setObjectName("year_delivery_label")
        self.year_delivery_label.setStyleSheet(self.CSS_label)

        self.year_delivery1_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.year_delivery1_line_edit.setGeometry(QtCore.QRect(600, 540, 91, 20))
        self.year_delivery1_line_edit.setObjectName("year_delivery1_line_edit")
        self.year_delivery1_line_edit.setStyleSheet(self.CSS_line_edit)

        self.year_delivery2_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.year_delivery2_line_edit.setGeometry(QtCore.QRect(600, 570, 91, 20))
        self.year_delivery2_line_edit.setObjectName("year_delivery2_line_edit")
        self.year_delivery2_line_edit.setStyleSheet(self.CSS_line_edit)

        self.year_delivery3_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.year_delivery3_line_edit.setGeometry(QtCore.QRect(600, 600, 91, 20))
        self.year_delivery3_line_edit.setObjectName("year_delivery3_line_edit")
        self.year_delivery3_line_edit.setStyleSheet(self.CSS_line_edit)

        self.year_delivery4_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.year_delivery4_line_edit.setGeometry(QtCore.QRect(600, 630, 91, 20))
        self.year_delivery4_line_edit.setObjectName("year_delivery4_line_edit")
        self.year_delivery4_line_edit.setStyleSheet(self.CSS_line_edit)

        self.hostel_cb = QtWidgets.QCheckBox(self.centralwidget)
        self.hostel_cb.setGeometry(QtCore.QRect(540, 660, 151, 17))
        self.hostel_cb.setObjectName("hostel_cb")
        self.hostel_cb.setStyleSheet("color: #404040;"
                                     "font-family: JetBrains Mono;"
                                     "font-size: 12px;")

        self.push_button = QtWidgets.QPushButton(self.centralwidget)
        self.push_button.setGeometry(480, 690, 110, 30)
        self.push_button.setObjectName("push_button")
        self.push_button.clicked.connect(self.registration)
        self.push_button.setStyleSheet("QPushButton {"
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

        self.export_db_button = QtWidgets.QPushButton(self.centralwidget)
        self.export_db_button.setGeometry(600, 690, 110, 30)
        self.export_db_button.setObjectName("export_db_button")
        self.export_db_button.clicked.connect(self.export_db)
        self.export_db_button.setStyleSheet("QPushButton {"
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

        # ЗАМЕТКА
        self.note = QtWidgets.QLabel(self.centralwidget)
        self.note.setGeometry(QtCore.QRect(300, 675, 200, 50))
        self.note.setWordWrap(True)
        self.note.setObjectName("note")
        self.note.setStyleSheet(self.CSS_label)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def check_mcb(self):
        self.female_cb.setChecked(False)
        if self.male_cb.isChecked():
            self.female_cb.setChecked(False)

    def check_fcb(self):
        self.male_cb.setChecked(False)
        if self.female_cb.isChecked():
            self.male_cb.setChecked(False)

    def registration(self):
        # Подключение к базе данных
        conn = sqlite3.connect("database\\database.s3db")
        cursor = conn.cursor()

        # ПЕРСОНАЛЬНЫЕ ДАННЫЕ
        surname = self.surname_line_edit.text()  # получение фамилии
        name = self.name_line_edit.text()  # получение имени
        patronymic = "\'" + self.patronymic_line_edit.text() + "\'"  # получение отчества

        if patronymic == "\'\'":
            patronymic = "NULL"

        sex = ""
        if self.male_cb.isChecked():
            sex = "мужской"
        if self.female_cb.isChecked():
            sex = "женский"

        birthday = self.birthday_line_edit.text()  # получение дата рождения
        nationality = self.nationality_line_edit.text()  # получение гражданства
        birthplace = self.birthplace_line_edit.text()  # получение место рождения

        hostel = ""
        if self.hostel_cb.isChecked():
            hostel = "требуется"
        elif not self.hostel_cb.isChecked():
            hostel = "не требуется"

        # ДОКУМЕНТ, УДОСТОВЕРЯЮЩИЙ ЛИЧНОСТЬ
        identity_document = self.document_line_edit.text()  # получение документа, документ удостоверяющий личность
        identity_series = self.identity_series_line_edit.text()  # получение серии
        identity_number = self.identity_number_line_edit.text()  # получение номера
        identity_issue_date = self.identity_issue_date_line_edit.text()  # получение даты выдачи
        identity_issue_org = self.identity_issue_org_line_edit.text()  # получение кем выдан

        # КОНТАКТНАЯ ИНФОРМАЦИЯ
        email = self.email_line_edit.text()  # получение email
        phone_number = self.phone_number_line_edit.text()  # получение номера телефона
        home_phone_number = "\'" + self.home_phone_number_line_edit.text() + "\'"  # получение номера дом. телефона

        if home_phone_number == "\'\'":
            home_phone_number = "NULL"

        # ОБРАЗОВАНИЕ
        name_ei = self.name_ei_line_edit.text()  # получение наименования учебного заведения
        issue_year_ei = self.issue_year_ei_line_edit.text()  # получение год окончания
        education = self.education_line_edit.text()  # получение имеющеего образования
        education_document = self.education_document_line_edit.text()  # получение документа
        education_series = self.education_series_line_edit.text()  # получение серии
        education_number = self.education_number_line_edit.text()  # получение номера
        education_issue_date = self.education_issue_date_line_edit.text()  # получение дата выдачи

        # ЭКЗАМЕНЫ
        discipline1 = self.discipline1_line_edit.text()  # получение дисциплины 1
        discipline2 = self.discipline2_line_edit.text()  # получение дисциплины 2
        discipline3 = self.discipline3_line_edit.text()  # получение дисциплины 3
        discipline4 = "\'" + self.discipline4_line_edit.text() + "\'"  # получение дисциплины 4
        if discipline4 == "\'\'":
            discipline4 = "NULL"

        point1 = self.point1_line_edit.text()  # получение балл 1
        point2 = self.point2_line_edit.text()  # получение балл 2
        point3 = self.point3_line_edit.text()  # получение балл 3
        point4 = "\'" + self.point4_line_edit.text() + "\'"  # получение балл 4
        if point4 == "\'\'":
            point4 = "NULL"

        passing_year1 = self.year_delivery1_line_edit.text()  # получение год сдачи 1
        passing_year2 = self.year_delivery2_line_edit.text()  # получение год сдачи 2
        passing_year3 = self.year_delivery3_line_edit.text()  # получение год сдачи 3
        passing_year4 = "\'" + self.year_delivery4_line_edit.text() + "\'"  # получение год сдачи 4
        if passing_year4 == "\'\'":
            passing_year4 = "NULL"

        # СОЗДАНИЕ ТАБЛИЦЫ
        cursor.execute("""CREATE TABLE IF NOT EXISTS applicants (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                                    surname TEXT NOT NULL,
                                                    name TEXT NOT NULL,
                                                    patronymic TEXT DEFAULT NULL,
                                                    sex TEXT NOT NULL,
                                                    birthday TEXT NOT NULL,
                                                    nationality TEXT NOT NULL,
                                                    birthplace TEXT NOT NULL,
                                                    hostel TEXT NOT NULL,
                                                    identity_document TEXT NOT NULL,
                                                    identity_series INTEGER NOT NULL,
                                                    identity_number INTEGER NOT NULL,
                                                    identity_issue_date TEXT NOT NULL,
                                                    identity_issue_org TEXT NOT NULL,
                                                    email TEXT NOT NULL,                   
                                                    phone_number INTEGER NOT NULL,
                                                    home_phone_number INTEGER DEFAULT NULL,
                                                    name_ei TEXT NOT NULL,
                                                    issue_year_ei INTEGER NOT NULL,
                                                    education TEXT NOT NULL,
                                                    education_document TEXT NOT NULL,
                                                    education_series INTEGER NOT NULL,
                                                    education_number INTEGER NOT NULL,
                                                    education_issue_date TEXT NOT NULL,
                                                    discipline1 TEXT NOT NULL,
                                                    point1 INTEGER NOT NULL,
                                                    passing_year1 TEXT NOT NULL,
                                                    discipline2 TEXT NOT NULL,
                                                    point2 INTEGER NOT NULL,
                                                    passing_year2 TEXT NOT NULL,
                                                    discipline3 TEXT NOT NULL,
                                                    point3 INTEGER NOT NULL,
                                                    passing_year3 TEXT NOT NULL,
                                                    discipline4 TEXT DEFAULT NULL,
                                                    point4 INTEGER DEFAULT NULL,
                                                    passing_year4 TEXT DEFAULT NULL)
        """)

        # ЗАПИСЬ ДАННЫХ В ТАБЛИЦУ
        self.insert_error = False

        try:
            cursor.execute("INSERT INTO applicants ('surname', 'name', 'patronymic', 'sex', 'birthday', 'nationality', "
                           "'birthplace', 'hostel', 'identity_document', 'identity_series', 'identity_number', "
                           "'identity_issue_date', 'identity_issue_org', 'email', 'phone_number', 'home_phone_number', "
                           "'name_ei', 'issue_year_ei', 'education', 'education_document', 'education_series', "
                           "'education_number', 'education_issue_date', 'discipline1', 'point1', 'passing_year1', "
                           "'discipline2', 'point2', 'passing_year2', 'discipline3', 'point3', 'passing_year3', "
                           "'discipline4', 'point4', 'passing_year4')"
                           " VALUES ('{0}', '{1}', {2}, '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', {9},"
                           "{10}, '{11}', '{12}', '{13}', {14}, {15}, '{16}', {17}, '{18}', '{19}',"
                           "{20}, {21}, '{22}', '{23}', {24}, '{25}', '{26}', {27}, '{28}', '{29}',"
                           "{30}, '{31}', {32}, {33}, {34})".format(surname,
                                                                    name,
                                                                    patronymic,
                                                                    sex,
                                                                    birthday,
                                                                    nationality,
                                                                    birthplace,
                                                                    hostel,
                                                                    identity_document,
                                                                    identity_series,
                                                                    identity_number,
                                                                    identity_issue_date,
                                                                    identity_issue_org,
                                                                    email,
                                                                    phone_number,
                                                                    home_phone_number,
                                                                    name_ei,
                                                                    issue_year_ei,
                                                                    education,
                                                                    education_document,
                                                                    education_series,
                                                                    education_number,
                                                                    education_issue_date,
                                                                    discipline1,
                                                                    point1,
                                                                    passing_year1,
                                                                    discipline2,
                                                                    point2,
                                                                    passing_year2,
                                                                    discipline3,
                                                                    point3,
                                                                    passing_year3,
                                                                    discipline4,
                                                                    point4,
                                                                    passing_year4,
                                                                    ))

            print("INSERT INTO applicants ('surname', 'name', 'patronymic', 'sex', 'birthday', 'nationality', "
                  "'birthplace', 'hostel', 'identity_document', 'identity_series', 'identity_number', "
                  "'identity_issue_date', 'identity_issue_org', 'email', 'phone_number', 'home_phone_number', "
                  "'name_ei', 'issue_year_ei', 'education', 'education_document', 'education_series', "
                  "'education_number', 'education_issue_date', 'discipline1', 'point1', 'passing_year1', "
                  "'discipline2', 'point2', 'passing_year2', 'discipline3', 'point3', 'passing_year3', "
                  "'discipline4', 'point4', 'passing_year4')"
                  " VALUES ('{0}', '{1}', {2}, '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', {9},"
                  "{10}, '{11}', '{12}', '{13}', {14}, {15}, '{16}', {17}, '{18}', '{19}',"
                  "{20}, {21}, '{22}', '{23}', {24}, '{25}', '{26}', {27}, '{28}', '{29}',"
                  "{30}, '{31}', {32}, {33}, {34})".format(surname,
                                                           name,
                                                           patronymic,
                                                           sex,
                                                           birthday,
                                                           nationality,
                                                           birthplace,
                                                           hostel,
                                                           identity_document,
                                                           identity_series,
                                                           identity_number,
                                                           identity_issue_date,
                                                           identity_issue_org,
                                                           email,
                                                           phone_number,
                                                           home_phone_number,
                                                           name_ei,
                                                           issue_year_ei,
                                                           education,
                                                           education_document,
                                                           education_series,
                                                           education_number,
                                                           education_issue_date,
                                                           discipline1,
                                                           point1,
                                                           passing_year1,
                                                           discipline2,
                                                           point2,
                                                           passing_year2,
                                                           discipline3,
                                                           point3,
                                                           passing_year3,
                                                           discipline4,
                                                           point4,
                                                           passing_year4,
                                                           ))

            print("Success")
        except Exception:
            self.insert_error = True
            print("Failed to fill the table.")

        if self.insert_error:
            msg_error = QtWidgets.QMessageBox()
            msg_error.setIcon(QtWidgets.QMessageBox.Critical)
            msg_error.setWindowTitle("Insert Error")
            msg_error.setWindowIcon(QtGui.QIcon("img\\error.svg"))
            msg_error.setText("Ошибка записи")
            msg_error.setInformativeText("Не удалось выполнить запись в таблицу, проверьте чтобы "
                                   "обязательные поля были заполнены и повторите попытку снова.")
            msg_error.setStyleSheet("font-family: JetBrains Mono;"
                              "font-size: 12px;")
            ok_button = msg_error.addButton('OK', QtWidgets.QMessageBox.AcceptRole)
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
            msg_error.exec_()

        if not self.insert_error:
            msg_complete = QtWidgets.QMessageBox()
            msg_complete.setIcon(QtWidgets.QMessageBox.Information)
            msg_complete.setWindowIcon(QtGui.QIcon("img\\insert.svg"))
            msg_complete.setText("Запись данных в базу прошла успешно :)")
            msg_complete.setWindowTitle("Complete")
            ok = msg_complete.addButton('OK', QtWidgets.QMessageBox.AcceptRole)
            ok.setFixedSize(100, 25)
            ok.setStyleSheet("QPushButton {"
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

            msg_complete.exec_()
            self.default_()

        conn.commit()
        conn.close()

    def default_(self):
        # ОБНУЛЕНИЕ ПРЕЗИДЕНТСКИХ СРОКОВ
        self.surname_line_edit.setText("")
        self.name_line_edit.setText("")
        self.patronymic_line_edit.setText("")
        self.male_cb.setChecked(False)
        self.female_cb.setChecked(False)
        self.birthday_line_edit.setText("")
        self.nationality_line_edit.setText("")
        self.birthplace_line_edit.setText("")
        self.hostel_cb.setChecked(False)
        self.document_line_edit.setText("")
        self.identity_series_line_edit.setText("")
        self.identity_number_line_edit.setText("")
        self.identity_issue_date_line_edit.setText("")
        self.identity_issue_org_line_edit.setText("")
        self.email_line_edit.setText("")
        self.phone_number_line_edit.setText("")
        self.home_phone_number_line_edit.setText("")
        self.name_ei_line_edit.setText("")
        self.issue_year_ei_line_edit.setText("")
        self.education_line_edit.setText("")
        self.education_document_line_edit.setText("")
        self.education_series_line_edit.setText("")
        self.education_number_line_edit.setText("")
        self.education_issue_date_line_edit.setText("")
        self.discipline1_line_edit.setText("")
        self.discipline2_line_edit.setText("")
        self.discipline3_line_edit.setText("")
        self.discipline4_line_edit.setText("")
        self.point1_line_edit.setText("")
        self.point2_line_edit.setText("")
        self.point3_line_edit.setText("")
        self.point4_line_edit.setText("")
        self.year_delivery1_line_edit.setText("")
        self.year_delivery2_line_edit.setText("")
        self.year_delivery3_line_edit.setText("")
        self.year_delivery4_line_edit.setText("")

    def export_db(self):
        conn = sqlite3.connect("database\\database.s3db")
        with open('dump.sql', 'w') as f:
            for line in conn.iterdump():
                f.write('%s\n' % line)
        conn.close()

        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowIcon(QtGui.QIcon("img\\export.svg"))
        msg.setText("База данных была успешно экспортирована.")
        msg.setWindowTitle("Export")
        ok = msg.addButton('OK', QtWidgets.QMessageBox.AcceptRole)
        ok.setFixedSize(100, 25)
        ok.setStyleSheet("QPushButton {"
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Регистрация абитуриентов"))
        self.identity_issue_org_label.setText(_translate("MainWindow", "Кем выдан"))
        self.identity_number_label.setText(_translate("MainWindow", "Номер"))
        self.document_label.setText(_translate("MainWindow", "Документ удостоверяющий личность"))
        self.identity_issue_date_label.setText(_translate("MainWindow", "Дата выдачи"))
        self.identity_series_label.setText(_translate("MainWindow", "Серия"))
        self.nationality_label.setText(_translate("MainWindow", "Гражданство "))
        self.name_label.setText(_translate("MainWindow", "Имя "))
        self.sex_label.setText(_translate("MainWindow", "Пол"))
        self.male_cb.setText(_translate("MainWindow", "Мужской"))
        self.surname_label.setText(_translate("MainWindow", "Фамилия "))
        self.birthday_label.setText(_translate("MainWindow", "Дата рождения "))
        self.female_cb.setText(_translate("MainWindow", "Женский"))
        self.patronymic_label.setText(_translate("MainWindow", "Отчество"))
        self.birthplace_label.setText(_translate("MainWindow", "Место рождения "))
        self.home_phone_number_label.setText(_translate("MainWindow", "Номер дом. телефона"))
        self.phone_number_label.setText(_translate("MainWindow", "Номер телефона"))
        self.email_label.setText(_translate("MainWindow", "Email"))
        self.name_ei_label.setText(_translate("MainWindow", "Наименование учебного заведения"))
        self.education_label.setText(_translate("MainWindow", "Образование"))
        self.issue_year_ei_label.setText(_translate("MainWindow", "Год окончания"))
        self.education_document_label.setText(_translate("MainWindow", "Документ"))
        self.education_series_label.setText(_translate("MainWindow", "Серия"))
        self.education_issue_date_label.setText(_translate("MainWindow", "Дата выдачи"))
        self.education_number_label.setText(_translate("MainWindow", "Номер"))
        self.discipline_label.setText(_translate("MainWindow", "Дисциплина"))
        self.point_label.setText(_translate("MainWindow", "Балл"))
        self.year_delivery_label.setText(_translate("MainWindow", "Год сдачи"))
        self.hostel_cb.setText(_translate("MainWindow", "нуждаюсь в общежитии"))
        self.push_button.setText(_translate("MainWindow", "Регистрация"))
        self.note.setText(_translate("MainWindow", "Отчество, номер домашнего телефона и "
                                                   "экзамен №4 не обязательны к заполнению"))
        self.export_db_button.setText(_translate("MainWindow", "Export SQL"))
