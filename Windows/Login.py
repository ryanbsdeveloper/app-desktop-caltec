# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled_login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc
import resources_rc

class Ui_Login_Widget(object):
    def setupUi(self, Login_Widget):
        if not Login_Widget.objectName():
            Login_Widget.setObjectName(u"Login_Widget")
        Login_Widget.setWindowModality(Qt.ApplicationModal)
        Login_Widget.setEnabled(True)
        Login_Widget.resize(700, 434)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Login_Widget.sizePolicy().hasHeightForWidth())
        Login_Widget.setSizePolicy(sizePolicy)
        Login_Widget.setMinimumSize(QSize(700, 400))
        Login_Widget.setMaximumSize(QSize(700, 457))
        Login_Widget.setMouseTracking(False)
        Login_Widget.setTabletTracking(False)
        Login_Widget.setAcceptDrops(False)
        icon = QIcon()
        icon.addFile(u":/icons/icon (2).png", QSize(), QIcon.Normal, QIcon.Off)
        Login_Widget.setWindowIcon(icon)
        Login_Widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(Login_Widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Login_Widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        font = QFont()
        font.setPointSize(8)
        self.frame_3.setFont(font)
        self.frame_3.setLayoutDirection(Qt.RightToLeft)
        self.frame_3.setStyleSheet(u"border:1px solid black;\n"
"background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(378, 194, 47, 13))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"border:0")
        self.email_input = QLineEdit(self.frame_3)
        self.email_input.setObjectName(u"email_input")
        self.email_input.setGeometry(QRect(370, 214, 270, 40))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setWeight(50)
        self.email_input.setFont(font2)
        self.email_input.setStyleSheet(u"\n"
"QLineEdit:focus\n"
"{\n"
"    border: 2px solid rgb(65, 229, 62);\n"
"}\n"
"QLineEdit{\n"
"	border-radius:5px;\n"
"	border:1px solid;\n"
"	padding:7px;\n"
"}")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(379, 264, 47, 13))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"border:0")
        self.entrar_button = QPushButton(self.frame_3)
        self.entrar_button.setObjectName(u"entrar_button")
        self.entrar_button.setGeometry(QRect(440, 334, 131, 38))
        self.entrar_button.setFont(font1)
        self.entrar_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.entrar_button.setLayoutDirection(Qt.LeftToRight)
        self.entrar_button.setStyleSheet(u"QPushButton{\n"
"		border-radius:10px;\n"
"		outline:0px\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(91, 240, 91);\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/arrow-right-to-bracket-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.entrar_button.setIcon(icon1)
        self._senha_input = QLineEdit(self.frame_3)
        self._senha_input.setObjectName(u"_senha_input")
        self._senha_input.setGeometry(QRect(370, 284, 270, 40))
        font3 = QFont()
        font3.setFamily(u"Century Gothic")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setWeight(50)
        self._senha_input.setFont(font3)
        self._senha_input.setStyleSheet(u"\n"
"QLineEdit:focus\n"
"{\n"
"    border: 2px solid rgb(65, 229, 62);\n"
"}\n"
"QLineEdit{\n"
"	border-radius:5px;\n"
"	border:1px solid;\n"
"	padding:7px;\n"
"}")
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(514, 411, 60, 16))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(9)
        font4.setBold(False)
        font4.setWeight(50)
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"border:0")
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(600, 410, 90, 16))
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"border:0")
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(55, 88, 131, 58))
        font5 = QFont()
        font5.setFamily(u"Segoe UI Light")
        font5.setPointSize(40)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setUnderline(False)
        font5.setWeight(50)
        self.label_6.setFont(font5)
        self.label_6.setStyleSheet(u"border:0")
        self.esqueceu_senha_button = QPushButton(self.frame_3)
        self.esqueceu_senha_button.setObjectName(u"esqueceu_senha_button")
        self.esqueceu_senha_button.setGeometry(QRect(194, 391, 80, 23))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(11)
        font6.setBold(True)
        font6.setWeight(75)
        self.esqueceu_senha_button.setFont(font6)
        self.esqueceu_senha_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.esqueceu_senha_button.setStyleSheet(u"border:0;\n"
"color: rgb(0, 213, 0);\n"
"outline:0")
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(63, 394, 130, 17))
        self.label_7.setFont(font6)
        self.label_7.setStyleSheet(u"border:0")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 52, 251, 131))
        self.label.setStyleSheet(u"border:0")
        self.label.setPixmap(QPixmap(u":/icons/ori.png"))
        self.label.setScaledContents(True)
        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(578, 409, 20, 20))
        self.label_8.setMinimumSize(QSize(20, 20))
        self.label_8.setMaximumSize(QSize(20, 20))
        self.label_8.setStyleSheet(u"border:0")
        self.label_8.setPixmap(QPixmap(u":/icons/github-brands.svg"))
        self.label_8.setScaledContents(True)
        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(55, 196, 260, 141))
        self.label_9.setFont(font6)
        self.label_9.setStyleSheet(u"border:0")
        self.label_9.setScaledContents(False)
        self.label_9.setWordWrap(True)
        self.mais_servicos_button = QPushButton(self.frame_3)
        self.mais_servicos_button.setObjectName(u"mais_servicos_button")
        self.mais_servicos_button.setGeometry(QRect(101, 278, 100, 18))
        self.mais_servicos_button.setFont(font6)
        self.mais_servicos_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.mais_servicos_button.setStyleSheet(u"border:0;\n"
"color: rgb(0, 213, 0);\n"
"outline:0")
        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(-1, 1, 711, 35))
        self.frame_2.setStyleSheet(u"background-color: rgb(15, 15, 15);\n"
"border:0")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(40, 20, 47, 21))
        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(261, 3, 200, 30))
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(11)
        self.label_11.setFont(font7)
        self.label_11.setStyleSheet(u"color:white")
        self.btn_close_windows = QPushButton(self.frame_2)
        self.btn_close_windows.setObjectName(u"btn_close_windows")
        self.btn_close_windows.setGeometry(QRect(649, 1, 50, 32))
        self.btn_close_windows.setMinimumSize(QSize(50, 32))
        self.btn_close_windows.setMaximumSize(QSize(50, 32))
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        self.btn_close_windows.setFont(font8)
        self.btn_close_windows.setStyleSheet(u"QPushButton:hover{\n"
"\n"
"background-color: rgb(218, 14, 14)}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/xmark-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close_windows.setIcon(icon2)
        self.btn_close_windows.setIconSize(QSize(21, 21))
        self.label_30 = QLabel(self.frame_2)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(13, 7, 25, 20))
        self.label_30.setMaximumSize(QSize(25, 20))
        self.label_30.setFont(font8)
        self.label_30.setPixmap(QPixmap(u":/icons/icon (2).png"))
        self.label_30.setScaledContents(True)
        self.btn_minimize_window = QPushButton(self.frame_2)
        self.btn_minimize_window.setObjectName(u"btn_minimize_window")
        self.btn_minimize_window.setGeometry(QRect(594, 1, 50, 32))
        self.btn_minimize_window.setMinimumSize(QSize(50, 32))
        self.btn_minimize_window.setMaximumSize(QSize(50, 32))
        self.btn_minimize_window.setFont(font8)
        self.btn_minimize_window.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgb(43, 43, 43);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/minus-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize_window.setIcon(icon3)
        self.btn_minimize_window.setIconSize(QSize(21, 21))
        self.erro = QLabel(self.frame_3)
        self.erro.setObjectName(u"erro")
        self.erro.setGeometry(QRect(400, 376, 221, 21))
        self.erro.setFont(font6)
        self.erro.setStyleSheet(u"color: rgb(255, 0, 0);border:0")
        self.erro.setAlignment(Qt.AlignCenter)
        self.email_input.raise_()
        self.entrar_button.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.esqueceu_senha_button.raise_()
        self.label_7.raise_()
        self.label.raise_()
        self.label_6.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.mais_servicos_button.raise_()
        self._senha_input.raise_()
        self.frame_2.raise_()
        self.erro.raise_()

        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)

        QWidget.setTabOrder(self.email_input, self._senha_input)
        QWidget.setTabOrder(self._senha_input, self.entrar_button)
        QWidget.setTabOrder(self.entrar_button, self.mais_servicos_button)
        QWidget.setTabOrder(self.mais_servicos_button, self.esqueceu_senha_button)

        self.retranslateUi(Login_Widget)

        QMetaObject.connectSlotsByName(Login_Widget)
    # setupUi

    def retranslateUi(self, Login_Widget):
        Login_Widget.setWindowTitle(QCoreApplication.translate("Login_Widget", u"Caltec - Software de pesagem", None))
        self.label_2.setText(QCoreApplication.translate("Login_Widget", u"E-mail:", None))
        self.label_3.setText(QCoreApplication.translate("Login_Widget", u"Senha:", None))
        self.entrar_button.setText(QCoreApplication.translate("Login_Widget", u"Entrar na conta", None))
        self.label_4.setText(QCoreApplication.translate("Login_Widget", u"Created by:", None))
        self.label_5.setText(QCoreApplication.translate("Login_Widget", u"ryanbsdeveloper", None))
        self.label_6.setText(QCoreApplication.translate("Login_Widget", u"Entrar", None))
        self.esqueceu_senha_button.setText(QCoreApplication.translate("Login_Widget", u"Clique aqui.", None))
        self.label_7.setText(QCoreApplication.translate("Login_Widget", u"Esqueceu a senha?", None))
        self.label.setText("")
        self.label_8.setText("")
        self.label_9.setText(QCoreApplication.translate("Login_Widget", u"O melhor e mais completo aplicativo de pesagem. Acesse mais servi\u00e7os da Caltec ", None))
        self.mais_servicos_button.setText(QCoreApplication.translate("Login_Widget", u"Clicando aqui.", None))
        self.label_10.setText("")
        self.label_11.setText(QCoreApplication.translate("Login_Widget", u"Caltec - Software de pesagem", None))
        self.btn_close_windows.setText("")
        self.label_30.setText("")
        self.btn_minimize_window.setText("")
        self.erro.setText(QCoreApplication.translate("Login_Widget", u"E-mail ou senha inval\u00edda.", None))
    # retranslateUi

