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
        SairConta.resize(341, 148)
        icon = QIcon()
        icon.addFile(u":/icons/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        SairConta.setWindowIcon(icon)
        SairConta.setStyleSheet(u"")
        SairConta.setSizeGripEnabled(False)
        SairConta.setModal(True)
        self.verticalLayout = QVBoxLayout(SairConta)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(SairConta)
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
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamily(u"Century Gothic")
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 21))
        font2 = QFont()
        font2.setFamily(u"Century Gothic")
        font2.setPointSize(9)
        self.label_3.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_3, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.frame_4, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame = QFrame(SairConta)
        self.frame.setObjectName(u"frame")
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
        font3 = QFont()
        font3.setFamily(u"Century Gothic")
        font3.setPointSize(10)
        self.label.setFont(font3)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(SairConta)

        QMetaObject.connectSlotsByName(SairConta)
    # setupUi

    def retranslateUi(self, SairConta):
        SairConta.setWindowTitle(QCoreApplication.translate("SairConta", u"Sair", None))
        self.label_2.setText(QCoreApplication.translate("SairConta", u"Sair da conta", None))
        self.label_3.setText(QCoreApplication.translate("SairConta", u"Voc\u00ea sera redirecionado para a tela de login", None))
        self.sim.setText(QCoreApplication.translate("SairConta", u"SIM", None))
        self.nao.setText(QCoreApplication.translate("SairConta", u"N\u00c3O", None))
        self.label.setText(QCoreApplication.translate("SairConta", u"Tem certeza que deseja sair da sua conta?", None))
    # retranslateUi

