# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sair_conta.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_SairConta(object):
    def setupUi(self, SairConta):
        if not SairConta.objectName():
            SairConta.setObjectName(u"SairConta")
        SairConta.resize(770, 421)
        icon = QIcon()
        icon.addFile(u":/icons/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        SairConta.setWindowIcon(icon)
        SairConta.setStyleSheet(u"background-color: rgba(0, 0, 0, 130);")
        SairConta.setSizeGripEnabled(False)
        SairConta.setModal(True)
        self.horizontalLayout = QHBoxLayout(SairConta)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(SairConta)
        self.frame_2.setObjectName(u"frame_2")
        font = QFont()
        font.setFamily(u"Segoe UI")
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(331, 171))
        self.frame_5.setFont(font)
        self.frame_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border:0")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_5)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 50))
        self.frame_6.setMaximumSize(QSize(16777215, 50))
        self.frame_6.setFont(font)
        self.frame_6.setStyleSheet(u"background-color: rgb(43, 43, 43);")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(129, 16, 90, 20))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(self.frame_6)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(290, 16, 20, 20))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/xmark-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(16, 20))

        self.verticalLayout.addWidget(self.frame_6)

        self.frame_3 = QFrame(self.frame_5)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFont(font)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 50))
        self.frame_4.setMaximumSize(QSize(16777215, 50))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(9)
        self.frame_4.setFont(font2)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 21))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        self.label_3.setFont(font3)

        self.verticalLayout_2.addWidget(self.label_3, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFont(font)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(9)
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.sim = QPushButton(self.frame)
        self.sim.setObjectName(u"sim")
        self.sim.setFont(font2)
        self.sim.setCursor(QCursor(Qt.PointingHandCursor))
        self.sim.setStyleSheet(u"QPushButton{border:1px solid;\n"
"background:rgb(250, 250, 250);\n"
"padding:5px}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(204, 204, 204);\n"
"}")

        self.gridLayout_2.addWidget(self.sim, 2, 1, 1, 1)

        self.nao = QPushButton(self.frame)
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

        self.gridLayout_2.addWidget(self.nao, 2, 0, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setFont(font3)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)


        self.verticalLayout_3.addWidget(self.frame)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout_2.addWidget(self.frame_5)


        self.horizontalLayout.addWidget(self.frame_2)


        self.retranslateUi(SairConta)

        QMetaObject.connectSlotsByName(SairConta)
    # setupUi

    def retranslateUi(self, SairConta):
        SairConta.setWindowTitle(QCoreApplication.translate("SairConta", u"Sair", None))
        self.label_2.setText(QCoreApplication.translate("SairConta", u"Sair da conta", None))
        self.pushButton.setText("")
        self.label_3.setText(QCoreApplication.translate("SairConta", u"Voc\u00ea sera redirecionado para a tela de login", None))
        self.sim.setText(QCoreApplication.translate("SairConta", u"SIM", None))
        self.nao.setText(QCoreApplication.translate("SairConta", u"N\u00c3O", None))
        self.label.setText(QCoreApplication.translate("SairConta", u"Tem certeza que deseja sair da sua conta?", None))
    # retranslateUi

