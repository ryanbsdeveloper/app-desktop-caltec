# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'atualizar_senha.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_AtualizarSenha(object):
    def setupUi(self, AtualizarSenha):
        if not AtualizarSenha.objectName():
            AtualizarSenha.setObjectName(u"AtualizarSenha")
        AtualizarSenha.setWindowModality(Qt.WindowModal)
        AtualizarSenha.resize(865, 544)
        font = QFont()
        font.setFamily(u"Ebrima")
        AtualizarSenha.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        AtualizarSenha.setWindowIcon(icon)
        AtualizarSenha.setStyleSheet(u"background-color: rgba(0, 0, 0, 130);")
        AtualizarSenha.setModal(True)
        self.verticalLayout = QVBoxLayout(AtualizarSenha)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(AtualizarSenha)
        self.frame.setObjectName(u"frame")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        self.frame.setFont(font1)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(390, 343))
        self.frame_2.setMaximumSize(QSize(448, 315))
        self.frame_2.setFont(font1)
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border:0\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 50))
        self.frame_7.setFont(font1)
        self.frame_7.setStyleSheet(u"background-color: rgb(15, 15, 15);border:0")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_7)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 17, 120, 16))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setWeight(75)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(self.frame_7)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(350, 15, 51, 23))
        self.pushButton.setFont(font1)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"border:0")
        icon1 = QIcon()
        icon1.addFile(u":/icons/xmark-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(16, 22))

        self.verticalLayout_2.addWidget(self.frame_7)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFont(font1)
        self.frame_6.setStyleSheet(u"background-color:rgb(43,43,43)")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.frame_3 = QFrame(self.frame_6)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 30))
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(9)
        self.frame_3.setFont(font3)
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"color:white")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)


        self.verticalLayout_5.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_6)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFont(font1)
        self.frame_4.setStyleSheet(u"color:white")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setWeight(50)
        self.label_3.setFont(font5)
        self.label_3.setStyleSheet(u"color:white")

        self.verticalLayout_4.addWidget(self.label_3)

        self.input_senha_atual = QLineEdit(self.frame_4)
        self.input_senha_atual.setObjectName(u"input_senha_atual")
        self.input_senha_atual.setMinimumSize(QSize(0, 32))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(11)
        self.input_senha_atual.setFont(font6)
        self.input_senha_atual.setStyleSheet(u"QLineEdit{padding:3px;\n"
"border:1px solid;\n"
"color:white}\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")
        self.input_senha_atual.setEchoMode(QLineEdit.Password)

        self.verticalLayout_4.addWidget(self.input_senha_atual)

        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font5)
        self.label_4.setStyleSheet(u"color:white")

        self.verticalLayout_4.addWidget(self.label_4)

        self.input_senha_nova_1 = QLineEdit(self.frame_4)
        self.input_senha_nova_1.setObjectName(u"input_senha_nova_1")
        self.input_senha_nova_1.setMinimumSize(QSize(0, 32))
        self.input_senha_nova_1.setFont(font6)
        self.input_senha_nova_1.setStyleSheet(u"QLineEdit{padding:3px;\n"
"border:1px solid;\n"
"color:white}\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")
        self.input_senha_nova_1.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_4.addWidget(self.input_senha_nova_1)

        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font5)
        self.label_5.setStyleSheet(u"color:white")

        self.verticalLayout_4.addWidget(self.label_5)

        self.input_senha_nova_2 = QLineEdit(self.frame_4)
        self.input_senha_nova_2.setObjectName(u"input_senha_nova_2")
        self.input_senha_nova_2.setMinimumSize(QSize(0, 32))
        self.input_senha_nova_2.setFont(font6)
        self.input_senha_nova_2.setStyleSheet(u"QLineEdit{padding:3px;\n"
"border:1px solid;\n"
"color:white}\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")
        self.input_senha_nova_2.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_4.addWidget(self.input_senha_nova_2)

        self.text_info = QLabel(self.frame_4)
        self.text_info.setObjectName(u"text_info")
        self.text_info.setFont(font2)
        self.text_info.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.text_info.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.text_info)


        self.verticalLayout_5.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_6)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFont(font1)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_cancelar = QPushButton(self.frame_5)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(12)
        self.btn_cancelar.setFont(font7)
        self.btn_cancelar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cancelar.setStyleSheet(u"\n"
"QPushButton{border:1px solid;\n"
"padding:3px;\n"
"background-color: rgb(15, 15, 15);\n"
"color:white}\n"
"QPushButton:hover{\n"
"	background-color: rgb(80, 80, 80);\n"
"}")

        self.horizontalLayout.addWidget(self.btn_cancelar)

        self.btn_alterar = QPushButton(self.frame_5)
        self.btn_alterar.setObjectName(u"btn_alterar")
        self.btn_alterar.setFont(font7)
        self.btn_alterar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar.setStyleSheet(u"\n"
"\n"
"QPushButton{border:1px solid rgb(67, 202, 0);\n"
"padding:3px;\n"
"background-color: rgb(15, 15, 15);\n"
"color:white;}\n"
"\n"
"QPushButton:hover{\n"
"	color:black;\n"
"	background-color: rgb(151, 255, 151);\n"
"}")

        self.horizontalLayout.addWidget(self.btn_alterar)


        self.verticalLayout_5.addWidget(self.frame_5)


        self.verticalLayout_2.addWidget(self.frame_6)


        self.verticalLayout_6.addWidget(self.frame_2, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(AtualizarSenha)

        QMetaObject.connectSlotsByName(AtualizarSenha)
    # setupUi

    def retranslateUi(self, AtualizarSenha):
        AtualizarSenha.setWindowTitle(QCoreApplication.translate("AtualizarSenha", u"Alterar senha", None))
        self.label.setText(QCoreApplication.translate("AtualizarSenha", u"Alterar senha", None))
        self.pushButton.setText("")
        self.label_2.setText(QCoreApplication.translate("AtualizarSenha", u"Insira sua senha atual e uma nova senha", None))
        self.label_3.setText(QCoreApplication.translate("AtualizarSenha", u"SENHA ATUAL", None))
        self.label_4.setText(QCoreApplication.translate("AtualizarSenha", u"NOVA SENHA", None))
        self.label_5.setText(QCoreApplication.translate("AtualizarSenha", u"CONFIRMAR NOVA SENHA", None))
        self.text_info.setText(QCoreApplication.translate("AtualizarSenha", u"Erro", None))
        self.btn_cancelar.setText(QCoreApplication.translate("AtualizarSenha", u"Cancelar", None))
        self.btn_alterar.setText(QCoreApplication.translate("AtualizarSenha", u"Alterar", None))
    # retranslateUi

