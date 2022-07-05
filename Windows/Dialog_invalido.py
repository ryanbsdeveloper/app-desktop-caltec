# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled_login_invalido.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_AcessoNegado(object):
    def setupUi(self, AcessoNegado):
        if not AcessoNegado.objectName():
            AcessoNegado.setObjectName(u"AcessoNegado")
        AcessoNegado.setWindowModality(Qt.WindowModal)
        AcessoNegado.setEnabled(True)
        AcessoNegado.resize(341, 120)
        AcessoNegado.setMinimumSize(QSize(175, 120))
        AcessoNegado.setMaximumSize(QSize(341, 120))
        AcessoNegado.setCursor(QCursor(Qt.ArrowCursor))
        icon = QIcon()
        icon.addFile(u":/icons/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        AcessoNegado.setWindowIcon(icon)
        AcessoNegado.setSizeGripEnabled(False)
        AcessoNegado.setModal(True)
        self.verticalLayout = QVBoxLayout(AcessoNegado)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(AcessoNegado)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        font1 = QFont()
        font1.setFamily(u"Century Gothic")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setWeight(50)
        self.pushButton.setFont(font1)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton{border:1px solid;\n"
"background:rgb(250, 250, 250);\n"
"padding:5px}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(204, 204, 204);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/person-walking-arrow-loop-left-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(25, 25))
        self.pushButton.setFlat(True)

        self.verticalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(AcessoNegado)

        QMetaObject.connectSlotsByName(AcessoNegado)
    # setupUi

    def retranslateUi(self, AcessoNegado):
        AcessoNegado.setWindowTitle(QCoreApplication.translate("AcessoNegado", u"Acesso Negado", None))
        self.label.setText(QCoreApplication.translate("AcessoNegado", u"Email ou Senha n\u00e3o s\u00e3o v\u00e1lidos.", None))
        self.pushButton.setText(QCoreApplication.translate("AcessoNegado", u"Tentar novamente", None))
    # retranslateUi

