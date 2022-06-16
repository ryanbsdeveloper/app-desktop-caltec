# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'excluir_conta.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_ExcluirConta(object):
    def setupUi(self, ExcluirConta):
        if not ExcluirConta.objectName():
            ExcluirConta.setObjectName(u"ExcluirConta")
        ExcluirConta.resize(702, 554)
        icon = QIcon()
        icon.addFile(u":/icons/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        ExcluirConta.setWindowIcon(icon)
        ExcluirConta.setModal(True)
        self.verticalLayout = QVBoxLayout(ExcluirConta)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(ExcluirConta)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(0, 0, 0, 130);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_13 = QFrame(self.frame)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(350, 257))
        self.frame_13.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_13)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 7)
        self.input_senha_atual = QLineEdit(self.frame_13)
        self.input_senha_atual.setObjectName(u"input_senha_atual")
        self.input_senha_atual.setMinimumSize(QSize(1, 0))
        self.input_senha_atual.setStyleSheet(u"QLineEdit{padding:3px}\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")
        self.input_senha_atual.setEchoMode(QLineEdit.Password)

        self.verticalLayout_11.addWidget(self.input_senha_atual)

        self.frame_3 = QFrame(self.frame_13)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 50))
        self.frame_3.setStyleSheet(u"background-color: rgb(43, 43, 43);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 16, 144, 18))
        font = QFont()
        font.setFamily(u"Century Gothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(314, 15, 20, 20))
        self.pushButton.setStyleSheet(u"border:0")
        icon1 = QIcon()
        icon1.addFile(u":/icons/xmark-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(16, 20))

        self.verticalLayout_11.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_13)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 74))
        self.frame_4.setMaximumSize(QSize(16777215, 100))
        font1 = QFont()
        font1.setFamily(u"Mudir MT")
        font1.setPointSize(9)
        self.frame_4.setFont(font1)
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(197, 65))
        font2 = QFont()
        font2.setFamily(u"Century Gothic")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 170, 170);\n"
"border:1px solid red;\n"
"padding:10px")
        self.label_3.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        font3 = QFont()
        font3.setFamily(u"Century Gothic")
        font3.setPointSize(10)
        self.label_4.setFont(font3)

        self.verticalLayout_2.addWidget(self.label_4)

        self.lineEdit_2 = QLineEdit(self.frame_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_2.addWidget(self.lineEdit_2)


        self.verticalLayout_11.addWidget(self.frame_4)

        self.frame_2 = QFrame(self.frame_13)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(9)
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setContentsMargins(7, 0, 7, 0)
        self.sim = QPushButton(self.frame_2)
        self.sim.setObjectName(u"sim")
        font4 = QFont()
        font4.setFamily(u"Century Gothic")
        font4.setPointSize(9)
        self.sim.setFont(font4)
        self.sim.setStyleSheet(u"QPushButton{border:1px solid;\n"
"background:rgb(250, 250, 250);\n"
"padding:5px}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(204, 204, 204);\n"
"}")

        self.gridLayout_2.addWidget(self.sim, 4, 1, 1, 1)

        self.nao = QPushButton(self.frame_2)
        self.nao.setObjectName(u"nao")
        self.nao.setFont(font4)
        self.nao.setStyleSheet(u"QPushButton{border:1px solid red;\n"
"background:rgb(250, 250, 250);\n"
"padding:5px}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 170, 170);\n"
"}")

        self.gridLayout_2.addWidget(self.nao, 4, 0, 1, 1)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 50))
        self.label.setFont(font3)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 2)

        self.text_info = QLabel(self.frame_2)
        self.text_info.setObjectName(u"text_info")
        font5 = QFont()
        font5.setPointSize(10)
        self.text_info.setFont(font5)
        self.text_info.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_2.addWidget(self.text_info, 1, 0, 1, 2, Qt.AlignHCenter)


        self.verticalLayout_11.addWidget(self.frame_2)


        self.horizontalLayout_4.addWidget(self.frame_13)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(ExcluirConta)

        QMetaObject.connectSlotsByName(ExcluirConta)
    # setupUi

    def retranslateUi(self, ExcluirConta):
        ExcluirConta.setWindowTitle(QCoreApplication.translate("ExcluirConta", u"Excluir conta", None))
        self.label_2.setText(QCoreApplication.translate("ExcluirConta", u"Remo\u00e7\u00e3o da conta", None))
        self.pushButton.setText("")
        self.label_3.setText(QCoreApplication.translate("ExcluirConta", u"Ao remover sua conta voc\u00ea ser\u00e1 deconectada dela imediatamente, e n\u00e3o poder\u00e1 mais entrar.", None))
        self.label_4.setText(QCoreApplication.translate("ExcluirConta", u"   SENHA", None))
        self.sim.setText(QCoreApplication.translate("ExcluirConta", u"SIM", None))
        self.nao.setText(QCoreApplication.translate("ExcluirConta", u"N\u00c3O", None))
        self.label.setText(QCoreApplication.translate("ExcluirConta", u"Tem certeza que deseja excuir sua conta?", None))
        self.text_info.setText(QCoreApplication.translate("ExcluirConta", u"Senha n\u00e3o \u00e9 val\u00edda.", None))
    # retranslateUi

