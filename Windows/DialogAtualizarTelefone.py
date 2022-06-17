# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'atualizar_telefone.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_AtualizarTelefone(object):
    def setupUi(self, AtualizarTelefone):
        if not AtualizarTelefone.objectName():
            AtualizarTelefone.setObjectName(u"AtualizarTelefone")
        AtualizarTelefone.resize(810, 614)
        icon = QIcon()
        icon.addFile(u":/icons/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        AtualizarTelefone.setWindowIcon(icon)
        AtualizarTelefone.setStyleSheet(u"background-color: rgba(0, 0, 0, 130);")
        AtualizarTelefone.setModal(True)
        self.verticalLayout = QVBoxLayout(AtualizarTelefone)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(AtualizarTelefone)
        self.frame_8.setObjectName(u"frame_8")
        font = QFont()
        font.setFamily(u"Segoe UI")
        self.frame_8.setFont(font)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_5 = QFrame(self.frame_8)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(392, 0))
        self.frame_5.setMaximumSize(QSize(392, 208))
        self.frame_5.setFont(font)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(1, 1, 390, 50))
        self.frame_7.setMinimumSize(QSize(0, 50))
        self.frame_7.setMaximumSize(QSize(390, 50))
        self.frame_7.setFont(font)
        self.frame_7.setStyleSheet(u"background-color: rgb(43, 43, 43);")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(141, 17, 121, 16))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(self.frame_7)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(330, 15, 51, 23))
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"border:0")
        icon1 = QIcon()
        icon1.addFile(u":/icons/xmark-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(16, 22))
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(1, 51, 390, 155))
        self.frame_6.setMinimumSize(QSize(390, 155))
        self.frame_6.setMaximumSize(QSize(390, 231))
        self.frame_6.setFont(font)
        self.frame_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_3 = QFrame(self.frame_6)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 30))
        self.frame_3.setFont(font)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setMaximumSize(QSize(16777215, 32))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        self.frame_4.setFont(font2)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 13))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(11)
        self.label_2.setFont(font3)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.frame_4)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame = QFrame(self.frame_6)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 80))
        self.frame.setFont(font)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 30))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_3.setFont(font4)

        self.verticalLayout_4.addWidget(self.label_3)

        self.input_novo_telefone = QLineEdit(self.frame)
        self.input_novo_telefone.setObjectName(u"input_novo_telefone")
        self.input_novo_telefone.setFont(font)
        self.input_novo_telefone.setStyleSheet(u"QLineEdit{padding:3px}\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")
        self.input_novo_telefone.setEchoMode(QLineEdit.Password)

        self.verticalLayout_4.addWidget(self.input_novo_telefone)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignBottom)

        self.text_info = QLabel(self.frame_6)
        self.text_info.setObjectName(u"text_info")
        self.text_info.setMaximumSize(QSize(16777215, 30))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(10)
        self.text_info.setFont(font5)
        self.text_info.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.text_info.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.text_info)

        self.frame_2 = QFrame(self.frame_6)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 30))
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.bt_cancelar = QPushButton(self.frame_2)
        self.bt_cancelar.setObjectName(u"bt_cancelar")
        self.bt_cancelar.setFont(font5)
        self.bt_cancelar.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_cancelar.setStyleSheet(u"\n"
"QPushButton{border:1px solid;\n"
"padding:3px;\n"
"background-color: rgb(250, 250, 250);}\n"
"QPushButton:hover{\n"
"	background-color: rgb(204, 204, 204);\n"
"}")

        self.horizontalLayout_2.addWidget(self.bt_cancelar)

        self.btn_alterar = QPushButton(self.frame_2)
        self.btn_alterar.setObjectName(u"btn_alterar")
        self.btn_alterar.setFont(font5)
        self.btn_alterar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar.setStyleSheet(u"\n"
"\n"
"QPushButton{border:1px solid rgb(67, 202, 0);\n"
"padding:3px;\n"
"background-color: rgb(250, 250, 250);}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(151, 255, 151);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_alterar)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout_3.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame_8)


        self.retranslateUi(AtualizarTelefone)

        QMetaObject.connectSlotsByName(AtualizarTelefone)
    # setupUi

    def retranslateUi(self, AtualizarTelefone):
        AtualizarTelefone.setWindowTitle(QCoreApplication.translate("AtualizarTelefone", u"Alterar telefone", None))
        self.label_4.setText(QCoreApplication.translate("AtualizarTelefone", u"Alterar Telefone", None))
        self.pushButton.setText("")
        self.label_2.setText(QCoreApplication.translate("AtualizarTelefone", u"Insira seu novo telefone", None))
        self.label_3.setText(QCoreApplication.translate("AtualizarTelefone", u"NOVO TELEFONE", None))
        self.text_info.setText(QCoreApplication.translate("AtualizarTelefone", u"Telefone n\u00e3o \u00e9 val\u00eddo.", None))
        self.bt_cancelar.setText(QCoreApplication.translate("AtualizarTelefone", u"Cancelar", None))
        self.btn_alterar.setText(QCoreApplication.translate("AtualizarTelefone", u"Alterar", None))
    # retranslateUi

