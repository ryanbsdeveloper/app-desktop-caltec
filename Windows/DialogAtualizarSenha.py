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
        AtualizarSenha.resize(400, 340)
        icon = QIcon()
        icon.addFile(u":/icons/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        AtualizarSenha.setWindowIcon(icon)
        AtualizarSenha.setModal(True)
        self.verticalLayout = QVBoxLayout(AtualizarSenha)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(AtualizarSenha)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 50))
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamily(u"Mudir MT")
        font.setPointSize(9)
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"Century Gothic")
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)

        self.verticalLayout_3.addWidget(self.label, 0, Qt.AlignHCenter)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamily(u"Century Gothic")
        font2.setPointSize(9)
        self.label_2.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignHCenter)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setFamily(u"Century Gothic")
        font3.setPointSize(10)
        self.label_3.setFont(font3)

        self.verticalLayout_4.addWidget(self.label_3)

        self.input_senha_atual = QLineEdit(self.frame_3)
        self.input_senha_atual.setObjectName(u"input_senha_atual")
        self.input_senha_atual.setStyleSheet(u"QLineEdit{padding:3px}\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")
        self.input_senha_atual.setEchoMode(QLineEdit.Password)

        self.verticalLayout_4.addWidget(self.input_senha_atual)

        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)

        self.verticalLayout_4.addWidget(self.label_4)

        self.input_senha_nova_1 = QLineEdit(self.frame_3)
        self.input_senha_nova_1.setObjectName(u"input_senha_nova_1")
        self.input_senha_nova_1.setStyleSheet(u"QLineEdit{padding:3px}\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")
        self.input_senha_nova_1.setEchoMode(QLineEdit.Password)

        self.verticalLayout_4.addWidget(self.input_senha_nova_1)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)

        self.verticalLayout_4.addWidget(self.label_5)

        self.input_senha_nova_2 = QLineEdit(self.frame_3)
        self.input_senha_nova_2.setObjectName(u"input_senha_nova_2")
        self.input_senha_nova_2.setStyleSheet(u"QLineEdit{padding:3px}\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")
        self.input_senha_nova_2.setEchoMode(QLineEdit.Password)

        self.verticalLayout_4.addWidget(self.input_senha_nova_2)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.text_info = QLabel(self.frame)
        self.text_info.setObjectName(u"text_info")
        font4 = QFont()
        font4.setPointSize(10)
        self.text_info.setFont(font4)
        self.text_info.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.verticalLayout_2.addWidget(self.text_info, 0, Qt.AlignHCenter)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_cancelar = QPushButton(self.frame_4)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setFont(font3)
        self.btn_cancelar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cancelar.setStyleSheet(u"\n"
"QPushButton{border:1px solid;\n"
"padding:3px;\n"
"background-color: rgb(250, 250, 250);}\n"
"QPushButton:hover{\n"
"	background-color: rgb(204, 204, 204);\n"
"}")

        self.horizontalLayout.addWidget(self.btn_cancelar)

        self.btn_alterar = QPushButton(self.frame_4)
        self.btn_alterar.setObjectName(u"btn_alterar")
        self.btn_alterar.setFont(font3)
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

        self.horizontalLayout.addWidget(self.btn_alterar)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(AtualizarSenha)

        QMetaObject.connectSlotsByName(AtualizarSenha)
    # setupUi

    def retranslateUi(self, AtualizarSenha):
        AtualizarSenha.setWindowTitle(QCoreApplication.translate("AtualizarSenha", u"Alterar senha", None))
        self.label.setText(QCoreApplication.translate("AtualizarSenha", u"Alterar senha", None))
        self.label_2.setText(QCoreApplication.translate("AtualizarSenha", u"Insira sua senha atual e uma nova senha", None))
        self.label_3.setText(QCoreApplication.translate("AtualizarSenha", u"SENHA ATUAL", None))
        self.label_4.setText(QCoreApplication.translate("AtualizarSenha", u"NOVA SENHA", None))
        self.label_5.setText(QCoreApplication.translate("AtualizarSenha", u"CONFIRMAR NOVA SENHA", None))
        self.text_info.setText("")
        self.btn_cancelar.setText(QCoreApplication.translate("AtualizarSenha", u"Cancelar", None))
        self.btn_alterar.setText(QCoreApplication.translate("AtualizarSenha", u"Alterar", None))
    # retranslateUi

