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
        AtualizarTelefone.resize(400, 174)
        icon = QIcon()
        icon.addFile(u":/icons/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        AtualizarTelefone.setWindowIcon(icon)
        AtualizarTelefone.setModal(True)
        self.verticalLayout = QVBoxLayout(AtualizarTelefone)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(AtualizarTelefone)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 50))
        self.frame_4.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamily(u"Mudir MT")
        font.setPointSize(9)
        self.frame_4.setFont(font)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"Century Gothic")
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignHCenter)

        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamily(u"Century Gothic")
        font2.setPointSize(9)
        self.label_2.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.frame_4, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame = QFrame(AtualizarTelefone)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setFamily(u"Century Gothic")
        font3.setPointSize(10)
        self.label_3.setFont(font3)

        self.verticalLayout_3.addWidget(self.label_3)

        self.input_novo_telefone = QLineEdit(self.frame)
        self.input_novo_telefone.setObjectName(u"input_novo_telefone")
        self.input_novo_telefone.setStyleSheet(u"QLineEdit{padding:3px}\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")
        self.input_novo_telefone.setEchoMode(QLineEdit.Password)

        self.verticalLayout_3.addWidget(self.input_novo_telefone)


        self.verticalLayout.addWidget(self.frame)

        self.text_info = QLabel(AtualizarTelefone)
        self.text_info.setObjectName(u"text_info")
        font4 = QFont()
        font4.setPointSize(10)
        self.text_info.setFont(font4)
        self.text_info.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.verticalLayout.addWidget(self.text_info, 0, Qt.AlignHCenter)

        self.frame_2 = QFrame(AtualizarTelefone)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.bt_cancelar = QPushButton(self.frame_2)
        self.bt_cancelar.setObjectName(u"bt_cancelar")
        self.bt_cancelar.setFont(font3)
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

        self.horizontalLayout_2.addWidget(self.btn_alterar)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(AtualizarTelefone)

        QMetaObject.connectSlotsByName(AtualizarTelefone)
    # setupUi

    def retranslateUi(self, AtualizarTelefone):
        AtualizarTelefone.setWindowTitle(QCoreApplication.translate("AtualizarTelefone", u"Alterar telefone", None))
        self.label.setText(QCoreApplication.translate("AtualizarTelefone", u"Alterar telefone", None))
        self.label_2.setText(QCoreApplication.translate("AtualizarTelefone", u"Insira seu novo telefone", None))
        self.label_3.setText(QCoreApplication.translate("AtualizarTelefone", u"NOVO TELEFONE", None))
        self.text_info.setText(QCoreApplication.translate("AtualizarTelefone", u"Telefone n\u00e3o \u00e9 val\u00eddo.", None))
        self.bt_cancelar.setText(QCoreApplication.translate("AtualizarTelefone", u"Cancelar", None))
        self.btn_alterar.setText(QCoreApplication.translate("AtualizarTelefone", u"Alterar", None))
    # retranslateUi

