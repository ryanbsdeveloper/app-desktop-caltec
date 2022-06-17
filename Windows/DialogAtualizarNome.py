# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'atualizar_nome.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_AtualizarNome(object):
    def setupUi(self, AtualizarNome):
        if not AtualizarNome.objectName():
            AtualizarNome.setObjectName(u"AtualizarNome")
        AtualizarNome.resize(925, 536)
        icon = QIcon()
        icon.addFile(u":/icons/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        AtualizarNome.setWindowIcon(icon)
        AtualizarNome.setStyleSheet(u"background-color: rgba(0, 0, 0, 130);")
        AtualizarNome.setModal(True)
        self.verticalLayout_4 = QVBoxLayout(AtualizarNome)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_31 = QFrame(AtualizarNome)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_31)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.frame_31)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(409, 216))
        font = QFont()
        font.setPointSize(5)
        self.frame_13.setFont(font)
        self.frame_13.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_13)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_30 = QFrame(self.frame_13)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(400, 0))
        self.frame_30.setMaximumSize(QSize(415, 428))
        self.frame_30.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.frame_30.setFrameShape(QFrame.NoFrame)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_30)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_30)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 37))
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setStyleSheet(u"background-color: rgb(43, 43, 43);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(360, 14, 20, 21))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"border:0")
        icon1 = QIcon()
        icon1.addFile(u":/icons/xmark-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(16, 21))
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(68, 15, 248, 20))
        self.label.setMinimumSize(QSize(0, 19))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_12.addWidget(self.frame)

        self.frame_6 = QFrame(self.frame_30)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, 0, -1, -1)
        self.frame_3 = QFrame(self.frame_6)
        self.frame_3.setObjectName(u"frame_3")
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.frame_3.setFont(font2)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 19))
        self.frame_4.setMaximumSize(QSize(16777215, 33))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(11)
        self.frame_4.setFont(font3)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)

        self.verticalLayout_2.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.frame_4, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_13.addWidget(self.frame_3)

        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_3.setFont(font4)

        self.verticalLayout_13.addWidget(self.label_3)

        self.input_novo_nome = QLineEdit(self.frame_6)
        self.input_novo_nome.setObjectName(u"input_novo_nome")
        self.input_novo_nome.setFont(font2)
        self.input_novo_nome.setStyleSheet(u"QLineEdit{padding:3px}\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")
        self.input_novo_nome.setEchoMode(QLineEdit.Password)

        self.verticalLayout_13.addWidget(self.input_novo_nome)

        self.text_info = QLabel(self.frame_6)
        self.text_info.setObjectName(u"text_info")
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(10)
        self.text_info.setFont(font5)
        self.text_info.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.text_info.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.text_info)

        self.frame_32 = QFrame(self.frame_6)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.bt_cancelar = QPushButton(self.frame_32)
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

        self.horizontalLayout_6.addWidget(self.bt_cancelar)

        self.btn_alterar = QPushButton(self.frame_32)
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

        self.horizontalLayout_6.addWidget(self.btn_alterar)


        self.verticalLayout_13.addWidget(self.frame_32)


        self.verticalLayout_12.addWidget(self.frame_6)


        self.verticalLayout.addWidget(self.frame_30)


        self.verticalLayout_14.addWidget(self.frame_13, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addWidget(self.frame_31)


        self.retranslateUi(AtualizarNome)

        QMetaObject.connectSlotsByName(AtualizarNome)
    # setupUi

    def retranslateUi(self, AtualizarNome):
        AtualizarNome.setWindowTitle(QCoreApplication.translate("AtualizarNome", u"Alterar nome", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("AtualizarNome", u"Alterar Nome da empresa / Pessoal", None))
        self.label_2.setText(QCoreApplication.translate("AtualizarNome", u"Insira o seu novo nome", None))
        self.label_3.setText(QCoreApplication.translate("AtualizarNome", u"NOVO NOME DA EMPRESA / PESSOAL", None))
        self.text_info.setText(QCoreApplication.translate("AtualizarNome", u"Nome muito curto.", None))
        self.bt_cancelar.setText(QCoreApplication.translate("AtualizarNome", u"Cancelar", None))
        self.btn_alterar.setText(QCoreApplication.translate("AtualizarNome", u"Alterar", None))
    # retranslateUi

