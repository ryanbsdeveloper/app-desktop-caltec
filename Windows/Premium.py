# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'premium.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.ApplicationModal)
        Dialog.resize(990, 661)
        Dialog.setMaximumSize(QSize(555555, 5555555))
        Dialog.setStyleSheet(u"background-color: rgba(0, 0, 0, 130);")
        Dialog.setModal(True)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(Dialog)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"background-color: rgba(0, 0, 0, 130);")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_13)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_13)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(450, 500))
        self.frame_5.setMaximumSize(QSize(450, 491))
        self.frame_5.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 100))
        self.frame_8.setMaximumSize(QSize(16777215, 100))
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.label_20 = QLabel(self.frame_8)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(0, -80, 451, 181))
        self.label_20.setPixmap(QPixmap(u":/icons/sobre.jpg"))
        self.label_20.setScaledContents(True)
        self.label_20.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)
        self.label_20.setWordWrap(False)
        self.label_20.setIndent(25)
        self.btn_close_window = QPushButton(self.frame_8)
        self.btn_close_window.setObjectName(u"btn_close_window")
        self.btn_close_window.setGeometry(QRect(415, 8, 26, 22))
        self.btn_close_window.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_close_window.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);border:0")
        icon = QIcon()
        icon.addFile(u":/icons/xmark-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close_window.setIcon(icon)
        self.btn_close_window.setIconSize(QSize(25, 25))

        self.verticalLayout_5.addWidget(self.frame_8)

        self.stackedWidget = QStackedWidget(self.frame_5)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMaximumSize(QSize(16777215, 20000))
        self.stackedWidget.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.page_inicial = QWidget()
        self.page_inicial.setObjectName(u"page_inicial")
        self.verticalLayout_2 = QVBoxLayout(self.page_inicial)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.page_inicial)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(16777215, 39))
        self.frame.setStyleSheet(u"background-color: rgb(25, 25, 25);\n"
"color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 71, 21))
        font = QFont()
        font.setFamily(u"Dubai")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"border:0;color:white")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(91, 10, 21, 21))
        font1 = QFont()
        font1.setFamily(u"Papyrus")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"border:0;;color:white")
        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(106, 10, 45, 21))
        font2 = QFont()
        font2.setFamily(u"Dubai")
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setWeight(50)
        self.label_14.setFont(font2)
        self.label_14.setStyleSheet(u"border:0;color:white")
        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(153, 10, 21, 21))
        self.label_15.setFont(font1)
        self.label_15.setStyleSheet(u"border:0;;color:white")
        self.label_19 = QLabel(self.frame)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(169, 10, 121, 21))
        self.label_19.setFont(font2)
        self.label_19.setStyleSheet(u"border:0;;color:white")

        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.page_inicial)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        font3 = QFont()
        font3.setFamily(u"MS Shell Dlg 2")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setWeight(75)
        self.frame_2.setFont(font3)
        self.frame_2.setStyleSheet(u"border:0;\n"
"background-color: rgb(43, 43, 43);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(100, 120, 241, 20))
        font4 = QFont()
        font4.setFamily(u"Dubai")
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setItalic(False)
        font4.setUnderline(False)
        font4.setWeight(75)
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"color: rgb(6, 180, 20);border:0")
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(100, 56, 231, 20))
        font5 = QFont()
        font5.setFamily(u"Dubai")
        font5.setPointSize(13)
        font5.setBold(True)
        font5.setItalic(False)
        font5.setUnderline(False)
        font5.setWeight(75)
        font5.setStrikeOut(False)
        font5.setStyleStrategy(QFont.PreferDefault)
        self.label_7.setFont(font5)
        self.label_7.setAcceptDrops(False)
        self.label_7.setStyleSheet(u"color: rgb(6, 180, 20);border:0")
        self.label_7.setScaledContents(False)
        self.label_7.setOpenExternalLinks(False)
        self.label_7.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(100, 251, 261, 20))
        font6 = QFont()
        font6.setFamily(u"Dubai")
        font6.setPointSize(13)
        font6.setBold(True)
        font6.setItalic(False)
        font6.setUnderline(False)
        font6.setWeight(75)
        self.label_11.setFont(font6)
        self.label_11.setStyleSheet(u"color: rgb(6, 180, 20);border:0")
        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(100, 174, 281, 70))
        self.label_12.setFont(font6)
        self.label_12.setStyleSheet(u"color: rgb(6, 180, 20);border:0")
        self.label_12.setWordWrap(True)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 80, 201, 20))
        font7 = QFont()
        font7.setFamily(u"Dubai")
        font7.setPointSize(10)
        self.label_2.setFont(font7)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);border:0")
        self.label_2.setWordWrap(True)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(120, 140, 211, 31))
        self.label_3.setFont(font7)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);border:0")
        self.label_3.setWordWrap(True)
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(130, 20, 221, 21))
        font8 = QFont()
        font8.setFamily(u"Dubai")
        font8.setPointSize(14)
        font8.setBold(True)
        font8.setWeight(75)
        self.label_6.setFont(font8)
        self.label_6.setStyleSheet(u"color:white")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_16 = QLabel(self.frame_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(83, 4, 51, 41))
        self.label_16.setStyleSheet(u"border:0")
        self.label_16.setPixmap(QPixmap(u":/icons/crown-solid (2).svg"))
        self.label_16.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.page_inicial)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 70))
        self.frame_3.setMaximumSize(QSize(16777215, 70))
        self.frame_3.setStyleSheet(u"background-color: rgb(25, 25, 25);\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.btn_comprar = QPushButton(self.frame_3)
        self.btn_comprar.setObjectName(u"btn_comprar")
        self.btn_comprar.setGeometry(QRect(268, 15, 133, 40))
        self.btn_comprar.setMinimumSize(QSize(133, 40))
        self.btn_comprar.setMaximumSize(QSize(50, 40))
        self.btn_comprar.setFont(font4)
        self.btn_comprar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_comprar.setStyleSheet(u"QPushButton{\n"
"border:0;\n"
"	background-color: qlineargradient(spread:reflect, x1:0.203955, y1:0, x2:1, y2:0, stop:0 rgba(97, 187, 104, 255), stop:0.613636 rgba(6, 180, 20, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:reflect, x1:0.573, y1:0, x2:1, y2:0, stop:0.272727 rgba(97, 187, 104, 255), stop:0.613636 rgba(6, 180, 20, 255));\n"
"}")
        self.btn_pular = QPushButton(self.frame_3)
        self.btn_pular.setObjectName(u"btn_pular")
        self.btn_pular.setGeometry(QRect(200, 49, 50, 16))
        font9 = QFont()
        font9.setFamily(u"Dubai")
        font9.setPointSize(12)
        font9.setBold(True)
        font9.setItalic(False)
        font9.setUnderline(True)
        font9.setWeight(75)
        self.btn_pular.setFont(font9)
        self.btn_pular.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pular.setStyleSheet(u"color: rgb(91, 91, 91);\n"
"border:0\n"
"")
        self.btn_licenca = QPushButton(self.frame_3)
        self.btn_licenca.setObjectName(u"btn_licenca")
        self.btn_licenca.setGeometry(QRect(41, 27, 138, 16))
        self.btn_licenca.setMinimumSize(QSize(50, 0))
        self.btn_licenca.setMaximumSize(QSize(16777215, 40))
        self.btn_licenca.setFont(font4)
        self.btn_licenca.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_licenca.setStyleSheet(u"QPushButton{\n"
"border:0;\n"
"\n"
"	color: rgb(85, 85, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/key-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_licenca.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.page_inicial)
        self.page_plano = QWidget()
        self.page_plano.setObjectName(u"page_plano")
        self.verticalLayout_3 = QVBoxLayout(self.page_plano)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.page_plano)
        self.frame_4.setObjectName(u"frame_4")
        font10 = QFont()
        font10.setFamily(u"MS Shell Dlg 2")
        font10.setPointSize(10)
        font10.setBold(False)
        font10.setItalic(False)
        font10.setWeight(50)
        self.frame_4.setFont(font10)
        self.frame_4.setStyleSheet(u"background-color: rgb(43, 43, 43);border:0")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 60, 110, 25))
        font11 = QFont()
        font11.setFamily(u"Dubai")
        font11.setPointSize(13)
        font11.setBold(True)
        font11.setItalic(False)
        font11.setWeight(75)
        self.label_8.setFont(font11)
        self.label_8.setStyleSheet(u"color: rgb(15, 202, 2);")
        self.radioButton_anual = QRadioButton(self.frame_4)
        self.radioButton_anual.setObjectName(u"radioButton_anual")
        self.radioButton_anual.setGeometry(QRect(30, 101, 381, 31))
        font12 = QFont()
        font12.setFamily(u"Dubai")
        font12.setPointSize(14)
        font12.setBold(False)
        font12.setWeight(50)
        self.radioButton_anual.setFont(font12)
        self.radioButton_anual.setStyleSheet(u"QRadioButton {\n"
"    color:                  white;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:                  22px;\n"
"    height:                 22px;\n"
"    border-radius:          11px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"	image: url(:/icons/check-solid.svg);\n"
"	background-color: rgb(6, 180, 20);\n"
"    border:                 1px solid rgb(88, 88, 88);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    border:                 1px solid rgb(88, 88, 88);\n"
"}")
        self.radioButton_6m = QRadioButton(self.frame_4)
        self.radioButton_6m.setObjectName(u"radioButton_6m")
        self.radioButton_6m.setGeometry(QRect(30, 150, 381, 30))
        self.radioButton_6m.setFont(font12)
        self.radioButton_6m.setStyleSheet(u"QRadioButton {\n"
"    color:                  white;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:                  22px;\n"
"    height:                 22px;\n"
"    border-radius:          11px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"	image: url(:/icons/check-solid.svg);\n"
"	background-color: rgb(6, 180, 20);\n"
"    border:                 1px solid rgb(88, 88, 88);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    border:                 1px solid rgb(88, 88, 88);\n"
"}")
        self.radioButton_6m.setIconSize(QSize(29, 29))
        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(120, 107, 111, 21))
        font13 = QFont()
        font13.setFamily(u"Dubai")
        font13.setPointSize(10)
        font13.setBold(True)
        font13.setWeight(75)
        self.label_9.setFont(font13)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(15, 202, 2);\n"
"border-radius:5px")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_10 = QLabel(self.frame_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(320, 110, 91, 21))
        self.label_10.setFont(font12)
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_13 = QLabel(self.frame_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(330, 150, 81, 30))
        self.label_13.setFont(font12)
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(-20, 0, 491, 39))
        self.frame_9.setMinimumSize(QSize(0, 0))
        self.frame_9.setMaximumSize(QSize(16777215, 39))
        self.frame_9.setStyleSheet(u"background-color: rgb(25, 25, 25);\n"
"color: rgb(0, 0, 0);\n"
"margin: 0px 15px")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.label_21 = QLabel(self.frame_9)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(40, 10, 71, 21))
        self.label_21.setFont(font2)
        self.label_21.setStyleSheet(u"border:0;color:white;margin:0")
        self.label_22 = QLabel(self.frame_9)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(111, 10, 21, 21))
        self.label_22.setFont(font1)
        self.label_22.setStyleSheet(u"border:0;;color:white;margin:0")
        self.label_23 = QLabel(self.frame_9)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(126, 10, 45, 21))
        self.label_23.setFont(font)
        self.label_23.setStyleSheet(u"border:0;color:white;margin:0")
        self.label_24 = QLabel(self.frame_9)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(173, 10, 21, 21))
        self.label_24.setFont(font1)
        self.label_24.setStyleSheet(u"border:0;;color:white;margin:0")
        self.label_25 = QLabel(self.frame_9)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(187, 10, 121, 21))
        self.label_25.setFont(font2)
        self.label_25.setStyleSheet(u"border:0;;color:white;margin:0")
        self.frame_10 = QFrame(self.frame_4)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(0, 328, 448, 70))
        self.frame_10.setMinimumSize(QSize(0, 70))
        self.frame_10.setMaximumSize(QSize(16777215, 70))
        self.frame_10.setStyleSheet(u"background-color: rgb(43, 43, 43);\n"
"margin: 0px 15px")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_2.setSpacing(87)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(40, -1, 40, -1)
        self.btn_voltar = QPushButton(self.frame_10)
        self.btn_voltar.setObjectName(u"btn_voltar")
        self.btn_voltar.setFont(font9)
        self.btn_voltar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_voltar.setStyleSheet(u"color: rgb(91, 91, 91);\n"
"border:0\n"
"")

        self.horizontalLayout_2.addWidget(self.btn_voltar)

        self.btn_continuar = QPushButton(self.frame_10)
        self.btn_continuar.setObjectName(u"btn_continuar")
        self.btn_continuar.setMinimumSize(QSize(50, 0))
        self.btn_continuar.setMaximumSize(QSize(16777215, 40))
        self.btn_continuar.setFont(font4)
        self.btn_continuar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_continuar.setStyleSheet(u"QPushButton{\n"
"border:0;\n"
"	background-color: qlineargradient(spread:reflect, x1:0.203955, y1:0, x2:1, y2:0, stop:0 rgba(97, 187, 104, 255), stop:0.613636 rgba(6, 180, 20, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"margin:0\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:reflect, x1:0.573, y1:0, x2:1, y2:0, stop:0.272727 rgba(97, 187, 104, 255), stop:0.613636 rgba(6, 180, 20, 255));\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_continuar)

        self.frame_11 = QFrame(self.frame_4)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(10, 204, 420, 101))
        self.frame_11.setStyleSheet(u"border-top:1px solid rgb(88, 88, 88)")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.label_26 = QLabel(self.frame_11)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(50, 70, 26, 25))
        self.label_26.setStyleSheet(u"border:0")
        self.label_26.setPixmap(QPixmap(u":/icons/circle-info-solid.svg"))
        self.label_26.setScaledContents(True)
        self.label_27 = QLabel(self.frame_11)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(40, 16, 50, 25))
        font14 = QFont()
        font14.setFamily(u"Dubai")
        font14.setPointSize(15)
        font14.setBold(True)
        font14.setItalic(False)
        font14.setWeight(75)
        self.label_27.setFont(font14)
        self.label_27.setStyleSheet(u"color: rgb(255, 255, 255);border:0")
        self.label_28 = QLabel(self.frame_11)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(82, 60, 290, 41))
        font15 = QFont()
        font15.setFamily(u"Dubai")
        font15.setPointSize(10)
        font15.setBold(False)
        font15.setWeight(50)
        self.label_28.setFont(font15)
        self.label_28.setStyleSheet(u"border:0;\n"
"color: rgb(255, 255, 255);")
        self.label_28.setWordWrap(True)
        self.text_valor_total = QLabel(self.frame_11)
        self.text_valor_total.setObjectName(u"text_valor_total")
        self.text_valor_total.setGeometry(QRect(290, 7, 94, 39))
        font16 = QFont()
        font16.setFamily(u"Dubai")
        font16.setPointSize(16)
        font16.setBold(True)
        font16.setWeight(75)
        self.text_valor_total.setFont(font16)
        self.text_valor_total.setStyleSheet(u"color: rgb(255, 255, 255);border:0")

        self.verticalLayout_3.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.page_plano)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setMinimumSize(QSize(0, 0))
        self.page.setMaximumSize(QSize(16777215, 265))
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 398))
        self.frame_6.setFont(font10)
        self.frame_6.setStyleSheet(u"background-color: rgb(43, 43, 43);border:0")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_17 = QLabel(self.frame_6)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(100, 44, 241, 25))
        self.label_17.setFont(font11)
        self.label_17.setStyleSheet(u"color: rgb(85, 85, 255);")
        self.label_17.setAlignment(Qt.AlignCenter)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(20, 190, 411, 70))
        self.frame_7.setMinimumSize(QSize(0, 70))
        self.frame_7.setMaximumSize(QSize(16777215, 70))
        self.frame_7.setStyleSheet(u"border-top:1px solid rgb(88, 88, 88);\n"
"background-color: rgb(43, 43, 43);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.btn_ativar_licenca = QPushButton(self.frame_7)
        self.btn_ativar_licenca.setObjectName(u"btn_ativar_licenca")
        self.btn_ativar_licenca.setGeometry(QRect(140, 14, 141, 41))
        self.btn_ativar_licenca.setFont(font6)
        self.btn_ativar_licenca.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ativar_licenca.setStyleSheet(u"QPushButton{\n"
"border:0;\n"
"	background-color: rgb(85, 85, 255);\n"
"border-radius:15px;\n"
"color:white\n"
"}\n"
"\n"
"")
        self.lineEdit = QLineEdit(self.frame_6)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(63, 100, 301, 31))
        font17 = QFont()
        font17.setFamily(u"Dubai")
        font17.setPointSize(12)
        font17.setBold(True)
        font17.setWeight(75)
        self.lineEdit.setFont(font17)
        self.lineEdit.setStyleSheet(u"padding:7px;border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);")
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.label_18 = QLabel(self.frame_6)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(70, 138, 291, 50))
        font18 = QFont()
        font18.setFamily(u"Dubai")
        font18.setPointSize(12)
        self.label_18.setFont(font18)
        self.label_18.setStyleSheet(u"border:0;\n"
"color: rgb(255, 255, 255);")
        self.label_18.setWordWrap(True)
        self.pushButton_2 = QPushButton(self.frame_6)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(107, 166, 95, 20))
        self.pushButton_2.setFont(font18)
        self.pushButton_2.setStyleSheet(u"border:0;\n"
"color: rgb(85, 85, 255);")
        self.text_info_licenca = QLabel(self.frame_6)
        self.text_info_licenca.setObjectName(u"text_info_licenca")
        self.text_info_licenca.setGeometry(QRect(80, 76, 291, 20))
        font19 = QFont()
        font19.setFamily(u"Century Gothic")
        font19.setPointSize(10)
        self.text_info_licenca.setFont(font19)
        self.text_info_licenca.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.text_info_licenca.setAlignment(Qt.AlignCenter)
        self.frame_12 = QFrame(self.frame_6)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(-20, 0, 491, 39))
        self.frame_12.setMinimumSize(QSize(0, 0))
        self.frame_12.setMaximumSize(QSize(16777215, 39))
        self.frame_12.setStyleSheet(u"background-color: rgb(25, 25, 25);\n"
"color: rgb(0, 0, 0);\n"
";margin: 0px 15px")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.label_30 = QLabel(self.frame_12)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(40, 10, 91, 21))
        self.label_30.setFont(font)
        self.label_30.setStyleSheet(u"border:0;color:white;margin:0")

        self.verticalLayout_4.addWidget(self.frame_6)

        self.stackedWidget.addWidget(self.page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame_13)


        self.retranslateUi(Dialog)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_20.setText("")
        self.btn_close_window.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"Benef\u00edcios", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u">", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"Planos", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u">", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", u"Redirecionamento", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u25cf  Utiliza\u00e7\u00e3o completa do software", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u25cf  Sem limita\u00e7\u00f5es de pesagem", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"\u25cf  Atualiza\u00e7\u00f5es e suporte t\u00e9cnico", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"\u25cf  Exclusividade em outros servi\u00e7os da empresa", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"30 pesagens dispon\u00edveis para n\u00e3o VIP", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"N\u00e3o-vip ter\u00e1 algumas telas bloqueadas", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Benef\u00edcios para PREMIUM", None))
        self.label_16.setText("")
        self.btn_comprar.setText(QCoreApplication.translate("Dialog", u"Comprar Agora", None))
        self.btn_pular.setText(QCoreApplication.translate("Dialog", u"Pular", None))
        self.btn_licenca.setText(QCoreApplication.translate("Dialog", u"Digite sua licen\u00e7a", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Escolha um:", None))
        self.radioButton_anual.setText(QCoreApplication.translate("Dialog", u"Anual", None))
        self.radioButton_6m.setText(QCoreApplication.translate("Dialog", u"6 Meses", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Economize 25%", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"R$  119,99 ", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"R$  79,99", None))
        self.label_21.setText(QCoreApplication.translate("Dialog", u"Benef\u00edcios", None))
        self.label_22.setText(QCoreApplication.translate("Dialog", u">", None))
        self.label_23.setText(QCoreApplication.translate("Dialog", u"Planos", None))
        self.label_24.setText(QCoreApplication.translate("Dialog", u">", None))
        self.label_25.setText(QCoreApplication.translate("Dialog", u"Redirecionamento", None))
        self.btn_voltar.setText(QCoreApplication.translate("Dialog", u"Voltar", None))
        self.btn_continuar.setText(QCoreApplication.translate("Dialog", u"Continuar", None))
        self.label_26.setText("")
        self.label_27.setText(QCoreApplication.translate("Dialog", u"Total:", None))
        self.label_28.setText(QCoreApplication.translate("Dialog", u"O pre\u00e7o final ser\u00e1 cobrado apenas essa vez. Ao expirar ser\u00e1 poss\u00edvel assinar novamente.", None))
        self.text_valor_total.setText("")
        self.label_17.setText(QCoreApplication.translate("Dialog", u"Digite sua licen\u00e7a", None))
        self.btn_ativar_licenca.setText(QCoreApplication.translate("Dialog", u"Ativar", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"XXXX-XXXX-XXXX-XXXX", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"Se ainda estiver sem uma licen\u00e7a, compre agora", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"clicando aqui", None))
        self.text_info_licenca.setText("")
        self.label_30.setText(QCoreApplication.translate("Dialog", u"Ativar licen\u00e7a", None))
    # retranslateUi

