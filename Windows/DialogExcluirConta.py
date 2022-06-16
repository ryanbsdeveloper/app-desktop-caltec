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
        ExcluirConta.resize(792, 554)
        icon = QIcon()
        icon.addFile(u":/icons/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        ExcluirConta.setWindowIcon(icon)
        ExcluirConta.setStyleSheet(u"background-color: rgba(0, 0, 0, 130);")
        ExcluirConta.setModal(True)
        self.verticalLayout = QVBoxLayout(ExcluirConta)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(ExcluirConta)
        self.frame.setObjectName(u"frame")
        font = QFont()
        font.setFamily(u"Segoe UI")
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"background-color: rgba(0, 0, 0, 130);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_13 = QFrame(self.frame)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(388, 264))
        self.frame_13.setFont(font)
        self.frame_13.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.frame_13)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 0, 391, 50))
        self.frame_3.setMinimumSize(QSize(0, 50))
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setFont(font)
        self.frame_3.setStyleSheet(u"background-color: rgb(43, 43, 43);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(127, 17, 144, 18))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(341, 16, 20, 20))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"border:0")
        icon1 = QIcon()
        icon1.addFile(u":/icons/xmark-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(16, 20))
        self.frame_2 = QFrame(self.frame_13)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(-2, 180, 391, 75))
        self.frame_2.setMinimumSize(QSize(0, 64))
        self.frame_2.setMaximumSize(QSize(16777215, 139))
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(9)
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setContentsMargins(7, 0, 7, 0)
        self.sim = QPushButton(self.frame_2)
        self.sim.setObjectName(u"sim")
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(9)
        self.sim.setFont(font2)
        self.sim.setCursor(QCursor(Qt.PointingHandCursor))
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
        self.nao.setFont(font2)
        self.nao.setCursor(QCursor(Qt.PointingHandCursor))
        self.nao.setStyleSheet(u"QPushButton{border:1px solid red;\n"
"background:rgb(250, 250, 250);\n"
"padding:5px}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 170, 170);\n"
"}")

        self.gridLayout_2.addWidget(self.nao, 4, 0, 1, 1)

        self.text_info = QLabel(self.frame_2)
        self.text_info.setObjectName(u"text_info")
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        self.text_info.setFont(font3)
        self.text_info.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_2.addWidget(self.text_info, 1, 0, 1, 2, Qt.AlignHCenter)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 50))
        self.label.setFont(font3)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 2)

        self.label_3 = QLabel(self.frame_13)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 50, 388, 65))
        self.label_3.setMinimumSize(QSize(197, 65))
        self.label_3.setMaximumSize(QSize(16777215, 65))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_3.setFont(font4)
        self.label_3.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 170, 170);\n"
"border:1px solid red;\n"
"padding:10px")
        self.label_3.setWordWrap(True)
        self.lineEdit = QLineEdit(self.frame_13)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(50, 140, 291, 33))
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setMaximumSize(QSize(16777215, 35))
        self.lineEdit.setFont(font3)
        self.lineEdit.setStyleSheet(u"QLineEdit{padding:3px}\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")

        self.horizontalLayout_4.addWidget(self.frame_13)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(ExcluirConta)

        QMetaObject.connectSlotsByName(ExcluirConta)
    # setupUi

    def retranslateUi(self, ExcluirConta):
        ExcluirConta.setWindowTitle(QCoreApplication.translate("ExcluirConta", u"Excluir conta", None))
        self.label_2.setText(QCoreApplication.translate("ExcluirConta", u"Remo\u00e7\u00e3o da conta", None))
        self.pushButton.setText("")
        self.sim.setText(QCoreApplication.translate("ExcluirConta", u"SIM", None))
        self.nao.setText(QCoreApplication.translate("ExcluirConta", u"N\u00c3O", None))
        self.text_info.setText(QCoreApplication.translate("ExcluirConta", u"Senha n\u00e3o \u00e9 val\u00edda.", None))
        self.label.setText(QCoreApplication.translate("ExcluirConta", u"Tem certeza que deseja excuir sua conta?", None))
        self.label_3.setText(QCoreApplication.translate("ExcluirConta", u"Ao remover sua conta voc\u00ea ser\u00e1 deconectada dela imediatamente, e n\u00e3o poder\u00e1 mais entrar.", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("ExcluirConta", u"SENHA ATUAL", None))
    # retranslateUi

