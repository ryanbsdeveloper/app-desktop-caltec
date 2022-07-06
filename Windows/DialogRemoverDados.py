# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'remover_dados.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_RemoverDados(object):
    def setupUi(self, RemoverDados):
        if not RemoverDados.objectName():
            RemoverDados.setObjectName(u"RemoverDados")
        RemoverDados.resize(816, 534)
        RemoverDados.setMaximumSize(QSize(5000000, 5000000))
        RemoverDados.setStyleSheet(u"background-color: rgba(0, 0, 0, 130);")
        RemoverDados.setSizeGripEnabled(False)
        RemoverDados.setModal(True)
        self.verticalLayout = QVBoxLayout(RemoverDados)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(RemoverDados)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgba(0, 0, 0, 130);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_5)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(480, 0))
        self.frame.setMaximumSize(QSize(480, 275))
        self.frame.setStyleSheet(u"background-color:rgb(43,43,43)")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 45))
        self.frame_4.setStyleSheet(u"background-color:rgb(15,15,15)")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: bold 13pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_4, 0, Qt.AlignVCenter)

        self.close_window = QPushButton(self.frame_4)
        self.close_window.setObjectName(u"close_window")
        self.close_window.setMaximumSize(QSize(50, 16777215))
        self.close_window.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_window.setStyleSheet(u"border:0")
        icon = QIcon()
        icon.addFile(u":/icons/xmark-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window.setIcon(icon)
        self.close_window.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.close_window, 0, Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(80, 50))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"font: bold 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label_2)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"font:  12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setScaledContents(False)
        self.label.setWordWrap(True)

        self.horizontalLayout.addWidget(self.label, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignHCenter)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"font:  bold 12pt \"Segoe UI\";\n"
"color: rgb(115, 114, 114);")

        self.verticalLayout_3.addWidget(self.label_3)

        self.input_delete = QLineEdit(self.frame_3)
        self.input_delete.setObjectName(u"input_delete")
        self.input_delete.setMinimumSize(QSize(0, 36))
        self.input_delete.setStyleSheet(u"QLineEdit{\n"
"	border:1px solid gray;\n"
"	font: 12pt \"Segoe UI\";\n"
"	color:white;\n"
"}")

        self.verticalLayout_3.addWidget(self.input_delete)

        self.btn_remove = QPushButton(self.frame_3)
        self.btn_remove.setObjectName(u"btn_remove")
        self.btn_remove.setMinimumSize(QSize(0, 37))
        self.btn_remove.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_remove.setStyleSheet(u"QPushButton{\n"
"border:1px solid  rgb(237, 51, 59);\n"
"font:  bold 12pt \"Segoe UI\";\n"
"color: rgb(237, 51, 59)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:white;\n"
"	background-color: rgb(237, 51, 59)\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_remove)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_4.addWidget(self.frame, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.frame_5)


        self.retranslateUi(RemoverDados)

        QMetaObject.connectSlotsByName(RemoverDados)
    # setupUi

    def retranslateUi(self, RemoverDados):
        RemoverDados.setWindowTitle(QCoreApplication.translate("RemoverDados", u"Dialog", None))
        self.label_4.setText(QCoreApplication.translate("RemoverDados", u"          Remover dados", None))
        self.close_window.setText("")
        self.label_2.setText(QCoreApplication.translate("RemoverDados", u"Aten\u00e7\u00e3o:", None))
        self.label.setText(QCoreApplication.translate("RemoverDados", u"Para continuar a remo\u00e7\u00e3o dos dados selecionados, prossiga abaixo", None))
        self.label_3.setText(QCoreApplication.translate("RemoverDados", u"Digite \"DELETE\" para continuar", None))
        self.input_delete.setPlaceholderText(QCoreApplication.translate("RemoverDados", u"DELETE", None))
        self.btn_remove.setText(QCoreApplication.translate("RemoverDados", u"Remover", None))
    # retranslateUi

