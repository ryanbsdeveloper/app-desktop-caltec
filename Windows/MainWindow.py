# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.ApplicationModal)
        MainWindow.resize(1102, 728)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Ebrima")
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/icon (2).png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.adicionar_balanca = QAction(MainWindow)
        self.adicionar_balanca.setObjectName(u"adicionar_balanca")
        self.fechar_aplicativo = QAction(MainWindow)
        self.fechar_aplicativo.setObjectName(u"fechar_aplicativo")
        self.actionAvan_adas = QAction(MainWindow)
        self.actionAvan_adas.setObjectName(u"actionAvan_adas")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"		outline:0px\n"
"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.menu_frame = QFrame(self.centralwidget)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setMaximumSize(QSize(200, 999999))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(11)
        self.menu_frame.setFont(font1)
        self.menu_frame.setStyleSheet(u"background-color: rgb(231, 231, 231);\n"
"")
        self.menu_frame.setFrameShape(QFrame.NoFrame)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.menu_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(8, 0, 8, 0)
        self.menuTop_frame = QFrame(self.menu_frame)
        self.menuTop_frame.setObjectName(u"menuTop_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.menuTop_frame.sizePolicy().hasHeightForWidth())
        self.menuTop_frame.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.menuTop_frame.setFont(font2)
        self.menuTop_frame.setFrameShape(QFrame.NoFrame)
        self.menuTop_frame.setFrameShadow(QFrame.Plain)
        self.menuTop_frame.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.menuTop_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.frame_3 = QFrame(self.menuTop_frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
        self.frame_3.setFont(font2)
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_3)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.aba_pesagem_button = QPushButton(self.frame_3)
        self.aba_pesagem_button.setObjectName(u"aba_pesagem_button")
        self.aba_pesagem_button.setMinimumSize(QSize(160, 40))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setWeight(75)
        self.aba_pesagem_button.setFont(font3)
        self.aba_pesagem_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.aba_pesagem_button.setFocusPolicy(Qt.ClickFocus)
        self.aba_pesagem_button.setLayoutDirection(Qt.LeftToRight)
        self.aba_pesagem_button.setAutoFillBackground(False)
        self.aba_pesagem_button.setStyleSheet(u"QPushButton{\n"
"	border:0;\n"
"	color:white;\n"
"	padding-left:10px;\n"
"	background-color: rgb(43, 43, 43);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(70, 70, 70);\n"
"	\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/weight-scale-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.aba_pesagem_button.setIcon(icon1)
        self.aba_pesagem_button.setIconSize(QSize(23, 22))
        self.aba_pesagem_button.setAutoExclusive(False)
        self.aba_pesagem_button.setAutoDefault(False)
        self.aba_pesagem_button.setFlat(False)

        self.verticalLayout_9.addWidget(self.aba_pesagem_button)

        self.menu_pesagem_frame = QFrame(self.frame_3)
        self.menu_pesagem_frame.setObjectName(u"menu_pesagem_frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.menu_pesagem_frame.sizePolicy().hasHeightForWidth())
        self.menu_pesagem_frame.setSizePolicy(sizePolicy3)
        self.menu_pesagem_frame.setMaximumSize(QSize(16777215, 79))
        self.menu_pesagem_frame.setFont(font2)
        self.menu_pesagem_frame.setFrameShape(QFrame.NoFrame)
        self.menu_pesagem_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.menu_pesagem_frame)
        self.verticalLayout_8.setSpacing(2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.button_avulsas_pesagens = QPushButton(self.menu_pesagem_frame)
        self.button_avulsas_pesagens.setObjectName(u"button_avulsas_pesagens")
        self.button_avulsas_pesagens.setMinimumSize(QSize(0, 25))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setWeight(50)
        self.button_avulsas_pesagens.setFont(font4)
        self.button_avulsas_pesagens.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_avulsas_pesagens.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(250, 250, 250);\n"
"	border:1px solid\n"
"}\n"
"QPushButton:hover{\n"
"font: bold 10pt \"Segoe UI\";\n"
"	background-color: rgb(43, 43, 43);\n"
"color:white;\n"
"}\n"
"")

        self.verticalLayout_8.addWidget(self.button_avulsas_pesagens)

        self.button_entsaid_pesagens = QPushButton(self.menu_pesagem_frame)
        self.button_entsaid_pesagens.setObjectName(u"button_entsaid_pesagens")
        self.button_entsaid_pesagens.setMinimumSize(QSize(130, 25))
        self.button_entsaid_pesagens.setFont(font4)
        self.button_entsaid_pesagens.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_entsaid_pesagens.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(250, 250, 250);\n"
"	border:1px solid\n"
"}\n"
"QPushButton:hover{\n"
"font: bold 10pt \"Segoe UI\";\n"
"	background-color: rgb(43, 43, 43);\n"
"color:white;\n"
"}\n"
"")

        self.verticalLayout_8.addWidget(self.button_entsaid_pesagens)

        self.btn_alterar_saida = QPushButton(self.menu_pesagem_frame)
        self.btn_alterar_saida.setObjectName(u"btn_alterar_saida")
        self.btn_alterar_saida.setMinimumSize(QSize(130, 25))
        self.btn_alterar_saida.setFont(font4)
        self.btn_alterar_saida.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_saida.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(250, 250, 250);\n"
"	border:1px solid\n"
"}\n"
"QPushButton:hover{\n"
"font: bold 10pt \"Segoe UI\";\n"
"	background-color: rgb(43, 43, 43);\n"
"color:white;\n"
"}\n"
"")

        self.verticalLayout_8.addWidget(self.btn_alterar_saida)


        self.verticalLayout_9.addWidget(self.menu_pesagem_frame, 0, Qt.AlignRight)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.menuTop_frame)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy2.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy2)
        self.frame_4.setFont(font2)
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_4)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.aba_grupo_button = QPushButton(self.frame_4)
        self.aba_grupo_button.setObjectName(u"aba_grupo_button")
        self.aba_grupo_button.setMinimumSize(QSize(160, 40))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(11)
        font5.setBold(True)
        font5.setWeight(75)
        self.aba_grupo_button.setFont(font5)
        self.aba_grupo_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.aba_grupo_button.setStyleSheet(u"QPushButton{\n"
"	border:0;\n"
"	color:white;\n"
"	padding-left:10px;\n"
"	background-color: rgb(43, 43, 43);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(70, 70, 70);\n"
"	\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/layer-group-solid .svg", QSize(), QIcon.Normal, QIcon.Off)
        self.aba_grupo_button.setIcon(icon2)
        self.aba_grupo_button.setIconSize(QSize(22, 22))
        self.aba_grupo_button.setFlat(False)

        self.verticalLayout_10.addWidget(self.aba_grupo_button)

        self.menu_grupos_frame = QFrame(self.frame_4)
        self.menu_grupos_frame.setObjectName(u"menu_grupos_frame")
        sizePolicy3.setHeightForWidth(self.menu_grupos_frame.sizePolicy().hasHeightForWidth())
        self.menu_grupos_frame.setSizePolicy(sizePolicy3)
        self.menu_grupos_frame.setFont(font2)
        self.menu_grupos_frame.setFrameShape(QFrame.NoFrame)
        self.menu_grupos_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.menu_grupos_frame)
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.button_clientes_grupos = QPushButton(self.menu_grupos_frame)
        self.button_clientes_grupos.setObjectName(u"button_clientes_grupos")
        self.button_clientes_grupos.setMinimumSize(QSize(130, 25))
        self.button_clientes_grupos.setMaximumSize(QSize(100, 16777215))
        self.button_clientes_grupos.setFont(font4)
        self.button_clientes_grupos.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_clientes_grupos.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(250, 250, 250);\n"
"	border:1px solid\n"
"}\n"
"QPushButton:hover{\n"
"font: bold 10pt \"Segoe UI\";\n"
"	background-color: rgb(43, 43, 43);\n"
"color:white;\n"
"}\n"
"")

        self.verticalLayout_7.addWidget(self.button_clientes_grupos)

        self.button_produtos_grupos = QPushButton(self.menu_grupos_frame)
        self.button_produtos_grupos.setObjectName(u"button_produtos_grupos")
        self.button_produtos_grupos.setMinimumSize(QSize(0, 25))
        self.button_produtos_grupos.setFont(font4)
        self.button_produtos_grupos.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_produtos_grupos.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(250, 250, 250);\n"
"	border:1px solid\n"
"}\n"
"QPushButton:hover{\n"
"font: bold 10pt \"Segoe UI\";\n"
"	background-color: rgb(43, 43, 43);\n"
"color:white;\n"
"}\n"
"")

        self.verticalLayout_7.addWidget(self.button_produtos_grupos)

        self.button_veiculos_grupos = QPushButton(self.menu_grupos_frame)
        self.button_veiculos_grupos.setObjectName(u"button_veiculos_grupos")
        self.button_veiculos_grupos.setMinimumSize(QSize(130, 25))
        self.button_veiculos_grupos.setMaximumSize(QSize(100, 16777215))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(10)
        font6.setBold(False)
        font6.setWeight(50)
        font6.setKerning(False)
        self.button_veiculos_grupos.setFont(font6)
        self.button_veiculos_grupos.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_veiculos_grupos.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(250, 250, 250);\n"
"	border:1px solid\n"
"}\n"
"QPushButton:hover{\n"
"font: bold 10pt \"Segoe UI\";\n"
"	background-color: rgb(43, 43, 43);\n"
"color:white;\n"
"}\n"
"")

        self.verticalLayout_7.addWidget(self.button_veiculos_grupos)


        self.verticalLayout_10.addWidget(self.menu_grupos_frame, 0, Qt.AlignRight)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.aba_relatorio_button = QPushButton(self.menuTop_frame)
        self.aba_relatorio_button.setObjectName(u"aba_relatorio_button")
        self.aba_relatorio_button.setMinimumSize(QSize(160, 40))
        self.aba_relatorio_button.setMaximumSize(QSize(5555, 40))
        self.aba_relatorio_button.setBaseSize(QSize(555, 2))
        self.aba_relatorio_button.setFont(font5)
        self.aba_relatorio_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.aba_relatorio_button.setLayoutDirection(Qt.LeftToRight)
        self.aba_relatorio_button.setStyleSheet(u"QPushButton{\n"
"	border:0;\n"
"	color:white;\n"
"	padding-left:10px;\n"
"	background-color: rgb(43, 43, 43);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(70, 70, 70);\n"
"	\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/notepad-with-text-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.aba_relatorio_button.setIcon(icon3)
        self.aba_relatorio_button.setIconSize(QSize(24, 23))
        self.aba_relatorio_button.setFlat(False)

        self.verticalLayout_3.addWidget(self.aba_relatorio_button)

        self.menu_relatorio_frame = QFrame(self.menuTop_frame)
        self.menu_relatorio_frame.setObjectName(u"menu_relatorio_frame")
        sizePolicy3.setHeightForWidth(self.menu_relatorio_frame.sizePolicy().hasHeightForWidth())
        self.menu_relatorio_frame.setSizePolicy(sizePolicy3)
        self.menu_relatorio_frame.setMaximumSize(QSize(16777215, 79))
        self.menu_relatorio_frame.setFont(font2)
        self.menu_relatorio_frame.setFrameShape(QFrame.NoFrame)
        self.menu_relatorio_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_93 = QVBoxLayout(self.menu_relatorio_frame)
        self.verticalLayout_93.setSpacing(2)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.verticalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.button_avulsas_relatorio = QPushButton(self.menu_relatorio_frame)
        self.button_avulsas_relatorio.setObjectName(u"button_avulsas_relatorio")
        self.button_avulsas_relatorio.setMinimumSize(QSize(0, 25))
        self.button_avulsas_relatorio.setFont(font4)
        self.button_avulsas_relatorio.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_avulsas_relatorio.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(250, 250, 250);\n"
"	border:1px solid\n"
"}\n"
"QPushButton:hover{\n"
"font: bold 10pt \"Segoe UI\";\n"
"	background-color: rgb(43, 43, 43);\n"
"color:white;\n"
"}\n"
"")

        self.verticalLayout_93.addWidget(self.button_avulsas_relatorio)

        self.button_entsaid_relatorio = QPushButton(self.menu_relatorio_frame)
        self.button_entsaid_relatorio.setObjectName(u"button_entsaid_relatorio")
        self.button_entsaid_relatorio.setMinimumSize(QSize(130, 25))
        self.button_entsaid_relatorio.setFont(font4)
        self.button_entsaid_relatorio.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_entsaid_relatorio.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(250, 250, 250);\n"
"	border:1px solid\n"
"}\n"
"QPushButton:hover{\n"
"font: bold 10pt \"Segoe UI\";\n"
"	background-color: rgb(43, 43, 43);\n"
"color:white;\n"
"}\n"
"")

        self.verticalLayout_93.addWidget(self.button_entsaid_relatorio)


        self.verticalLayout_3.addWidget(self.menu_relatorio_frame, 0, Qt.AlignRight)

        self.aba_conta_button = QPushButton(self.menuTop_frame)
        self.aba_conta_button.setObjectName(u"aba_conta_button")
        self.aba_conta_button.setMinimumSize(QSize(160, 40))
        self.aba_conta_button.setFont(font5)
        self.aba_conta_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.aba_conta_button.setStyleSheet(u"QPushButton{\n"
"	border:0;\n"
"	color:white;\n"
"	padding-left:10px;\n"
"	background-color: rgb(43, 43, 43);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(70, 70, 70);\n"
"	\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/circle-user-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.aba_conta_button.setIcon(icon4)
        self.aba_conta_button.setIconSize(QSize(24, 22))
        self.aba_conta_button.setAutoExclusive(True)
        self.aba_conta_button.setFlat(False)

        self.verticalLayout_3.addWidget(self.aba_conta_button)


        self.verticalLayout_2.addWidget(self.menuTop_frame, 0, Qt.AlignVCenter)

        self.info_menu_pro_frame = QFrame(self.menu_frame)
        self.info_menu_pro_frame.setObjectName(u"info_menu_pro_frame")
        self.info_menu_pro_frame.setMaximumSize(QSize(16777215, 115))
        self.info_menu_pro_frame.setFont(font2)
        self.info_menu_pro_frame.setStyleSheet(u"border:0;\n"
"")
        self.info_menu_pro_frame.setFrameShape(QFrame.StyledPanel)
        self.info_menu_pro_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.info_menu_pro_frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.info_pro_frame = QFrame(self.info_menu_pro_frame)
        self.info_pro_frame.setObjectName(u"info_pro_frame")
        self.info_pro_frame.setMinimumSize(QSize(0, 22))
        self.info_pro_frame.setMaximumSize(QSize(16777215, 30))
        self.info_pro_frame.setFont(font2)
        self.info_pro_frame.setFrameShape(QFrame.NoFrame)
        self.info_pro_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.info_pro_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.info_pro_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(20, 20))
        self.label_4.setFont(font2)
        self.label_4.setTextFormat(Qt.AutoText)
        self.label_4.setPixmap(QPixmap(u":/icons/circle-info-solid.svg"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.restantes_label = QLabel(self.info_pro_frame)
        self.restantes_label.setObjectName(u"restantes_label")
        self.restantes_label.setMinimumSize(QSize(0, 23))
        self.restantes_label.setMaximumSize(QSize(150, 160))
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(10)
        font7.setBold(True)
        font7.setWeight(75)
        self.restantes_label.setFont(font7)
        self.restantes_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.restantes_label, 0, Qt.AlignVCenter)


        self.verticalLayout_5.addWidget(self.info_pro_frame)

        self.info_pro_label = QLabel(self.info_menu_pro_frame)
        self.info_pro_label.setObjectName(u"info_pro_label")
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(10)
        self.info_pro_label.setFont(font8)
        self.info_pro_label.setLineWidth(0)
        self.info_pro_label.setAlignment(Qt.AlignCenter)
        self.info_pro_label.setWordWrap(True)
        self.info_pro_label.setMargin(1)

        self.verticalLayout_5.addWidget(self.info_pro_label)


        self.verticalLayout_2.addWidget(self.info_menu_pro_frame, 0, Qt.AlignBottom)

        self.menuEnd_frame = QFrame(self.menu_frame)
        self.menuEnd_frame.setObjectName(u"menuEnd_frame")
        self.menuEnd_frame.setFont(font2)
        self.menuEnd_frame.setFrameShape(QFrame.NoFrame)
        self.menuEnd_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.menuEnd_frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 9)
        self.aba_sair_button = QPushButton(self.menuEnd_frame)
        self.aba_sair_button.setObjectName(u"aba_sair_button")
        self.aba_sair_button.setMinimumSize(QSize(60, 40))
        self.aba_sair_button.setFont(font5)
        self.aba_sair_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.aba_sair_button.setStyleSheet(u"QPushButton{\n"
"	border:0;\n"
"	color:white;\n"
"	\n"
"	background-color: rgb(43, 43, 43);\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: rgb(70, 70, 70);\n"
"	\n"
"}\n"
"")
        self.aba_sair_button.setIconSize(QSize(25, 25))
        self.aba_sair_button.setFlat(False)

        self.verticalLayout_4.addWidget(self.aba_sair_button, 0, Qt.AlignBottom)


        self.verticalLayout_2.addWidget(self.menuEnd_frame, 0, Qt.AlignBottom)

        self.menuEnd_frame.raise_()
        self.menuTop_frame.raise_()
        self.info_menu_pro_frame.raise_()

        self.gridLayout.addWidget(self.menu_frame, 2, 0, 1, 1)

        self.frame_29 = QFrame(self.centralwidget)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(0, 35))
        self.frame_29.setFont(font2)
        self.frame_29.setStyleSheet(u"background-color: rgb(15, 15, 15);\n"
"")
        self.frame_29.setFrameShape(QFrame.NoFrame)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(10, 0, 0, 0)
        self.frame_44 = QFrame(self.frame_29)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setMinimumSize(QSize(147, 0))
        self.frame_44.setFont(font2)
        self.frame_44.setFrameShape(QFrame.NoFrame)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_16.setSpacing(16)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_30 = QLabel(self.frame_44)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMaximumSize(QSize(25, 21))
        self.label_30.setFont(font2)
        self.label_30.setPixmap(QPixmap(u":/icons/icon (2).png"))
        self.label_30.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.label_30)

        self.pushButton = QPushButton(self.frame_44)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 32))
        font9 = QFont()
        font9.setFamily(u"Segoe UI")
        font9.setPointSize(11)
        font9.setBold(False)
        font9.setWeight(50)
        self.pushButton.setFont(font9)
        self.pushButton.setCursor(QCursor(Qt.ForbiddenCursor))
        self.pushButton.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"border:0\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(43, 43, 43);\n"
"}")

        self.horizontalLayout_16.addWidget(self.pushButton)


        self.horizontalLayout_10.addWidget(self.frame_44, 0, Qt.AlignLeft)

        self.nome_pc = QLabel(self.frame_29)
        self.nome_pc.setObjectName(u"nome_pc")
        self.nome_pc.setFont(font9)
        self.nome_pc.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.nome_pc.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.nome_pc, 0, Qt.AlignHCenter)

        self.frame_30 = QFrame(self.frame_29)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMaximumSize(QSize(16777215, 32))
        self.frame_30.setFont(font2)
        self.frame_30.setStyleSheet(u"border:0")
        self.frame_30.setFrameShape(QFrame.NoFrame)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_9.setSpacing(3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 1, 1, 0)
        self.btn_minimize_window = QPushButton(self.frame_30)
        self.btn_minimize_window.setObjectName(u"btn_minimize_window")
        self.btn_minimize_window.setMinimumSize(QSize(50, 32))
        self.btn_minimize_window.setMaximumSize(QSize(50, 32))
        self.btn_minimize_window.setFont(font2)
        self.btn_minimize_window.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgb(43, 43, 43);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/minus-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize_window.setIcon(icon5)
        self.btn_minimize_window.setIconSize(QSize(21, 21))

        self.horizontalLayout_9.addWidget(self.btn_minimize_window)

        self.btn_close_windows = QPushButton(self.frame_30)
        self.btn_close_windows.setObjectName(u"btn_close_windows")
        self.btn_close_windows.setMinimumSize(QSize(50, 32))
        self.btn_close_windows.setMaximumSize(QSize(50, 32))
        self.btn_close_windows.setFont(font2)
        self.btn_close_windows.setStyleSheet(u"QPushButton:hover{\n"
"\n"
"background-color: rgb(218, 14, 14)}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/xmark-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close_windows.setIcon(icon6)
        self.btn_close_windows.setIconSize(QSize(21, 21))

        self.horizontalLayout_9.addWidget(self.btn_close_windows)


        self.horizontalLayout_10.addWidget(self.frame_30, 0, Qt.AlignRight)


        self.gridLayout.addWidget(self.frame_29, 0, 0, 1, 2)

        self.top_frame = QFrame(self.centralwidget)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setMinimumSize(QSize(0, 110))
        self.top_frame.setMaximumSize(QSize(16777215, 110))
        self.top_frame.setFont(font2)
        self.top_frame.setStyleSheet(u"background-color: rgb(43, 43, 43);")
        self.top_frame.setFrameShape(QFrame.NoFrame)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.top_frame.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.top_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 0, 0)
        self.frame = QFrame(self.top_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFont(font2)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(167, 0))
        self.label.setMaximumSize(QSize(183, 96))
        self.label.setFont(font2)
        self.label.setStyleSheet(u"border:0")
        self.label.setPixmap(QPixmap(u":/icons/ori.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(True)

        self.horizontalLayout_2.addWidget(self.label)


        self.horizontalLayout.addWidget(self.frame, 0, Qt.AlignLeft)

        self.frame_59 = QFrame(self.top_frame)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setFrameShape(QFrame.NoFrame)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.label_2 = QLabel(self.frame_59)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 56))
        self.label_2.setFont(font5)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border:0")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_48.addWidget(self.label_2)

        self.conexao_label = QPushButton(self.frame_59)
        self.conexao_label.setObjectName(u"conexao_label")
        self.conexao_label.setEnabled(False)
        self.conexao_label.setMinimumSize(QSize(0, 34))
        self.conexao_label.setMaximumSize(QSize(150, 16777215))
        self.conexao_label.setFont(font7)
        self.conexao_label.setCursor(QCursor(Qt.ArrowCursor))
        self.conexao_label.setMouseTracking(False)
        self.conexao_label.setFocusPolicy(Qt.NoFocus)
        self.conexao_label.setAcceptDrops(False)
        self.conexao_label.setLayoutDirection(Qt.LeftToRight)
        self.conexao_label.setStyleSheet(u"QPushButton{\n"
"border:0;\n"
"	color: rgb(255, 80, 80);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/plug-circle-exclamation-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon7.addFile(u":/icons/plug-circle-exclamation-solid.svg", QSize(), QIcon.Disabled, QIcon.Off)
        icon7.addFile(u":/icons/plug-circle-exclamation-solid.svg", QSize(), QIcon.Disabled, QIcon.On)
        icon7.addFile(u":/icons/plug-solid (1).svg", QSize(), QIcon.Active, QIcon.Off)
        icon7.addFile(u":/icons/plug-solid (1).svg", QSize(), QIcon.Active, QIcon.On)
        self.conexao_label.setIcon(icon7)
        self.conexao_label.setCheckable(False)
        self.conexao_label.setFlat(False)

        self.horizontalLayout_48.addWidget(self.conexao_label)


        self.horizontalLayout.addWidget(self.frame_59, 0, Qt.AlignLeft)

        self.conteudo_top_frame = QFrame(self.top_frame)
        self.conteudo_top_frame.setObjectName(u"conteudo_top_frame")
        self.conteudo_top_frame.setMinimumSize(QSize(600, 70))
        self.conteudo_top_frame.setFont(font2)
        self.conteudo_top_frame.setCursor(QCursor(Qt.ArrowCursor))
        self.conteudo_top_frame.setFrameShape(QFrame.NoFrame)
        self.conteudo_top_frame.setFrameShadow(QFrame.Plain)
        self.conteudo_top_frame.setLineWidth(0)
        self.gridLayout_2 = QGridLayout(self.conteudo_top_frame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(0, 0, 20, 0)
        self.btn_virepro_button = QPushButton(self.conteudo_top_frame)
        self.btn_virepro_button.setObjectName(u"btn_virepro_button")
        self.btn_virepro_button.setMinimumSize(QSize(240, 45))
        self.btn_virepro_button.setMaximumSize(QSize(200, 16777215))
        self.btn_virepro_button.setFont(font7)
        self.btn_virepro_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_virepro_button.setStyleSheet(u"QPushButton{\n"
"	border:0;\n"
"	border-radius:5px;\n"
"	background-color: rgb(242, 242, 242);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(160, 255, 163);\n"
"}")
        self.btn_virepro_button.setText(u"Utilize a vers\u00e3o PREMIUM")
        icon8 = QIcon()
        icon8.addFile(u":/icons/crown-solid (2).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_virepro_button.setIcon(icon8)
        self.btn_virepro_button.setIconSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.btn_virepro_button, 1, 0, 1, 1, Qt.AlignVCenter)


        self.horizontalLayout.addWidget(self.conteudo_top_frame, 0, Qt.AlignRight)


        self.gridLayout.addWidget(self.top_frame, 1, 0, 1, 2)

        self.principal_frame = QFrame(self.centralwidget)
        self.principal_frame.setObjectName(u"principal_frame")
        self.principal_frame.setFont(font2)
        self.principal_frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.principal_frame.setFrameShape(QFrame.NoFrame)
        self.principal_frame.setFrameShadow(QFrame.Raised)
        self.principal_frame.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.principal_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.info_frame = QFrame(self.principal_frame)
        self.info_frame.setObjectName(u"info_frame")
        self.info_frame.setMaximumSize(QSize(16777215, 40))
        self.info_frame.setFont(font2)
        self.info_frame.setCursor(QCursor(Qt.ArrowCursor))
        self.info_frame.setFocusPolicy(Qt.NoFocus)
        self.info_frame.setStyleSheet(u"background-color: rgb(48, 48, 48);")
        self.info_frame.setFrameShape(QFrame.NoFrame)
        self.info_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.info_frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.info_frame)

        self.stackedWidget = QStackedWidget(self.principal_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFont(font2)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(231, 231, 231);\n"
"")
        self.page_relatorio_entradaesaida = QWidget()
        self.page_relatorio_entradaesaida.setObjectName(u"page_relatorio_entradaesaida")
        self.verticalLayout_11 = QVBoxLayout(self.page_relatorio_entradaesaida)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_127 = QFrame(self.page_relatorio_entradaesaida)
        self.frame_127.setObjectName(u"frame_127")
        self.frame_127.setFont(font2)
        self.frame_127.setStyleSheet(u"border:0")
        self.frame_127.setFrameShape(QFrame.NoFrame)
        self.frame_127.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_127)
        self.verticalLayout_45.setSpacing(7)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.frame_143 = QFrame(self.frame_127)
        self.frame_143.setObjectName(u"frame_143")
        self.frame_143.setMinimumSize(QSize(0, 37))
        self.frame_143.setMaximumSize(QSize(16777215, 37))
        self.frame_143.setFont(font2)
        self.frame_143.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(43, 43, 43);")
        self.frame_143.setFrameShape(QFrame.NoFrame)
        self.frame_143.setFrameShadow(QFrame.Raised)
        self.verticalLayout_112 = QVBoxLayout(self.frame_143)
        self.verticalLayout_112.setSpacing(7)
        self.verticalLayout_112.setObjectName(u"verticalLayout_112")
        self.verticalLayout_112.setContentsMargins(0, 0, 0, 0)
        self.aba_relatorio_button_14 = QPushButton(self.frame_143)
        self.aba_relatorio_button_14.setObjectName(u"aba_relatorio_button_14")
        self.aba_relatorio_button_14.setMinimumSize(QSize(160, 37))
        self.aba_relatorio_button_14.setMaximumSize(QSize(5555, 37))
        self.aba_relatorio_button_14.setBaseSize(QSize(555, 2))
        font10 = QFont()
        font10.setFamily(u"Segoe UI")
        font10.setPointSize(16)
        font10.setBold(True)
        font10.setWeight(75)
        self.aba_relatorio_button_14.setFont(font10)
        self.aba_relatorio_button_14.setLayoutDirection(Qt.LeftToRight)
        self.aba_relatorio_button_14.setStyleSheet(u"QPushButton{\n"
"	border:0;\n"
"}")
        self.aba_relatorio_button_14.setIcon(icon3)
        self.aba_relatorio_button_14.setIconSize(QSize(30, 30))
        self.aba_relatorio_button_14.setFlat(False)

        self.verticalLayout_112.addWidget(self.aba_relatorio_button_14, 0, Qt.AlignTop)


        self.verticalLayout_45.addWidget(self.frame_143)

        self.frame_144 = QFrame(self.frame_127)
        self.frame_144.setObjectName(u"frame_144")
        self.frame_144.setMaximumSize(QSize(16777215, 105))
        self.frame_144.setFont(font2)
        self.frame_144.setFrameShape(QFrame.NoFrame)
        self.frame_144.setFrameShadow(QFrame.Raised)
        self.gridLayout_30 = QGridLayout(self.frame_144)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setHorizontalSpacing(9)
        self.gridLayout_30.setVerticalSpacing(4)
        self.gridLayout_30.setContentsMargins(7, 0, 0, 0)
        self.label_93 = QLabel(self.frame_144)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setMaximumSize(QSize(16777215, 13))
        self.label_93.setFont(font7)

        self.gridLayout_30.addWidget(self.label_93, 2, 1, 1, 1)

        self.frame_145 = QFrame(self.frame_144)
        self.frame_145.setObjectName(u"frame_145")
        self.frame_145.setMinimumSize(QSize(0, 26))
        self.frame_145.setMaximumSize(QSize(250, 37))
        self.frame_145.setFont(font2)
        self.frame_145.setFrameShape(QFrame.NoFrame)
        self.frame_145.setFrameShadow(QFrame.Raised)
        self.gridLayout_31 = QGridLayout(self.frame_145)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_31.setVerticalSpacing(3)
        self.gridLayout_31.setContentsMargins(0, 0, 0, 0)
        self.text_filtro_id_6 = QLineEdit(self.frame_145)
        self.text_filtro_id_6.setObjectName(u"text_filtro_id_6")
        self.text_filtro_id_6.setMaximumSize(QSize(50, 16777215))
        self.text_filtro_id_6.setFont(font8)
        self.text_filtro_id_6.setStyleSheet(u"\n"
"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"border:1px solid rgb(203, 203, 203);\n"
"padding:5px;\n"
"	font: 10pt \"Segoe UI\";\n"
"\n"
"}\n"
"\n"
"QLineEdit::focus{\n"
"	border:1px solid rgb(67, 202, 0)\n"
"}\n"
"")
        self.text_filtro_id_6.setMaxLength(6)

        self.gridLayout_31.addWidget(self.text_filtro_id_6, 2, 0, 1, 1)

        self.btn_filtro_id_6 = QPushButton(self.frame_145)
        self.btn_filtro_id_6.setObjectName(u"btn_filtro_id_6")
        self.btn_filtro_id_6.setMaximumSize(QSize(16, 16))
        self.btn_filtro_id_6.setFont(font2)
        self.btn_filtro_id_6.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/icons/magnifying-glass-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_filtro_id_6.setIcon(icon9)
        self.btn_filtro_id_6.setIconSize(QSize(16, 16))

        self.gridLayout_31.addWidget(self.btn_filtro_id_6, 2, 1, 1, 1)


        self.gridLayout_30.addWidget(self.frame_145, 3, 0, 1, 1, Qt.AlignLeft)

        self.frame_146 = QFrame(self.frame_144)
        self.frame_146.setObjectName(u"frame_146")
        self.frame_146.setMinimumSize(QSize(200, 64))
        self.frame_146.setMaximumSize(QSize(188, 16777215))
        self.frame_146.setFont(font2)
        self.frame_146.setFrameShape(QFrame.StyledPanel)
        self.frame_146.setFrameShadow(QFrame.Raised)
        self.gridLayout_32 = QGridLayout(self.frame_146)
        self.gridLayout_32.setSpacing(0)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.gridLayout_32.setContentsMargins(0, 0, 10, 0)
        self.data_fixa_6 = QRadioButton(self.frame_146)
        self.data_fixa_6.setObjectName(u"data_fixa_6")
        font11 = QFont()
        font11.setFamily(u"Segoe UI")
        font11.setPointSize(10)
        font11.setBold(False)
        font11.setItalic(False)
        font11.setWeight(50)
        self.data_fixa_6.setFont(font11)

        self.gridLayout_32.addWidget(self.data_fixa_6, 0, 0, 1, 1)

        self.data_antes_de_6 = QRadioButton(self.frame_146)
        self.data_antes_de_6.setObjectName(u"data_antes_de_6")
        self.data_antes_de_6.setMinimumSize(QSize(0, 1))
        self.data_antes_de_6.setFont(font11)

        self.gridLayout_32.addWidget(self.data_antes_de_6, 1, 0, 1, 1)

        self.text_date_6 = QDateEdit(self.frame_146)
        self.text_date_6.setObjectName(u"text_date_6")
        self.text_date_6.setMinimumSize(QSize(0, 27))
        self.text_date_6.setFont(font11)
        self.text_date_6.setStyleSheet(u"QDateEdit{\n"
"	border:1px solid rgb(15, 202, 2);\n"
"	padding-left:10px;\n"
"	font-size:13px;\n"
"	\n"
"	font: 10pt \"Segoe UI\";\n"
"	background-color: rgb(250, 252, 250);\n"
"}\n"
"\n"
"QDateEdit::drop-down{\n"
"	border:0px;\n"
"}\n"
"\n"
"QDateEdit::down-arrow{\n"
"	image: url(:/icons/angle-down-solid.svg);\n"
"	width:12px;\n"
"	height:12px;\n"
"	margin-right:15px;\n"
"}\n"
"\n"
"QDateEdit::up-arrow{\n"
"	image: url(:/icons/angle-down-solid.svg);\n"
"	width:12px;\n"
"	height:12px;\n"
"	margin-right:15px;\n"
"}\n"
"\n"
"")
        self.text_date_6.setWrapping(False)
        self.text_date_6.setAlignment(Qt.AlignCenter)
        self.text_date_6.setReadOnly(False)
        self.text_date_6.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.text_date_6.setAccelerated(True)
        self.text_date_6.setKeyboardTracking(True)
        self.text_date_6.setProperty("showGroupSeparator", True)
        self.text_date_6.setDateTime(QDateTime(QDate(2022, 1, 1), QTime(0, 0, 0)))

        self.gridLayout_32.addWidget(self.text_date_6, 1, 1, 1, 1)

        self.data_depois_de_6 = QRadioButton(self.frame_146)
        self.data_depois_de_6.setObjectName(u"data_depois_de_6")
        self.data_depois_de_6.setMinimumSize(QSize(0, 1))
        self.data_depois_de_6.setFont(font11)

        self.gridLayout_32.addWidget(self.data_depois_de_6, 2, 0, 1, 1)


        self.gridLayout_30.addWidget(self.frame_146, 1, 8, 3, 1)

        self.label_95 = QLabel(self.frame_144)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setMinimumSize(QSize(0, 13))
        self.label_95.setFont(font7)

        self.gridLayout_30.addWidget(self.label_95, 0, 8, 1, 1)

        self.comboBox_veiculo_6 = QComboBox(self.frame_144)
        self.comboBox_veiculo_6.addItem("")
        self.comboBox_veiculo_6.setObjectName(u"comboBox_veiculo_6")
        self.comboBox_veiculo_6.setMinimumSize(QSize(0, 27))
        self.comboBox_veiculo_6.setFont(font11)
        self.comboBox_veiculo_6.setStyleSheet(u"QComboBox{\n"
"	border:1px solid rgb(15, 202, 2);\n"
"	padding-left:10px;\n"
"	font-size:13px;\n"
"	font: 10pt \"Segoe UI\";\n"
"	background-color: rgb(250, 252, 250);\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"	border:0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
"	image: url(:/icons/angle-down-solid.svg);\n"
"	width:12px;\n"
"	height:12px;\n"
"	margin-right:15px;\n"
"}\n"
"\n"
"QComboBox::on{\n"
"	border:2px solid rgb(67, 202, 0);\n"
"}\n"
"\n"
"QComboBox QListView{\n"
"	padding:5px;\n"
"	border:1px solid;\n"
"	background-color: rgba(255, 255, 255, 50%);\n"
"	outline:0;\n"
"}\n"
"")
        self.comboBox_veiculo_6.setMaxVisibleItems(10)
        self.comboBox_veiculo_6.setInsertPolicy(QComboBox.NoInsert)
        self.comboBox_veiculo_6.setIconSize(QSize(32, 32))
        self.comboBox_veiculo_6.setDuplicatesEnabled(True)
        self.comboBox_veiculo_6.setFrame(True)

        self.gridLayout_30.addWidget(self.comboBox_veiculo_6, 3, 3, 1, 1)

        self.comboBox_produto_6 = QComboBox(self.frame_144)
        self.comboBox_produto_6.addItem("")
        self.comboBox_produto_6.setObjectName(u"comboBox_produto_6")
        self.comboBox_produto_6.setMinimumSize(QSize(0, 27))
        self.comboBox_produto_6.setFont(font11)
        self.comboBox_produto_6.setStyleSheet(u"QComboBox{\n"
"	border:1px solid rgb(15, 202, 2);\n"
"	padding-left:10px;\n"
"	font-size:13px;\n"
"	font: 10pt \"Segoe UI\";\n"
"	background-color: rgb(250, 252, 250);\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"	border:0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
"	image: url(:/icons/angle-down-solid.svg);\n"
"	width:12px;\n"
"	height:12px;\n"
"	margin-right:15px;\n"
"}\n"
"\n"
"QComboBox::on{\n"
"	border:2px solid rgb(67, 202, 0);\n"
"}\n"
"\n"
"QComboBox QListView{\n"
"	padding:5px;\n"
"	border:1px solid;\n"
"	background-color: rgba(255, 255, 255, 50%);\n"
"	outline:0;\n"
"}\n"
"")
        self.comboBox_produto_6.setMaxVisibleItems(10)
        self.comboBox_produto_6.setInsertPolicy(QComboBox.NoInsert)
        self.comboBox_produto_6.setIconSize(QSize(32, 32))
        self.comboBox_produto_6.setDuplicatesEnabled(True)
        self.comboBox_produto_6.setFrame(True)

        self.gridLayout_30.addWidget(self.comboBox_produto_6, 3, 2, 1, 1)

        self.lineEdit_11 = QLineEdit(self.frame_144)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setMinimumSize(QSize(0, 27))
        self.lineEdit_11.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_11.setFont(font11)
        self.lineEdit_11.setStyleSheet(u"QLineEdit{\n"
"	padding-left:10px;\n"
"	font-size:13px;\n"
"	border:1px solid;\n"
"	background-color: rgb(250, 252, 250);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:1px solid rgb(15, 202, 2);\n"
"\n"
"}")

        self.gridLayout_30.addWidget(self.lineEdit_11, 3, 4, 1, 1)

        self.comboBox_cliente_6 = QComboBox(self.frame_144)
        self.comboBox_cliente_6.addItem("")
        self.comboBox_cliente_6.setObjectName(u"comboBox_cliente_6")
        self.comboBox_cliente_6.setMinimumSize(QSize(0, 27))
        self.comboBox_cliente_6.setFont(font11)
        self.comboBox_cliente_6.setStyleSheet(u"QComboBox{\n"
"	border:1px solid rgb(15, 202, 2);\n"
"	padding-left:10px;\n"
"	font-size:13px;\n"
"	font: 10pt \"Segoe UI\";\n"
"	background-color: rgb(250, 252, 250);\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"	border:0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
"	image: url(:/icons/angle-down-solid.svg);\n"
"	width:12px;\n"
"	height:12px;\n"
"	margin-right:15px;\n"
"}\n"
"\n"
"QComboBox::on{\n"
"	border:2px solid rgb(67, 202, 0);\n"
"}\n"
"\n"
"QComboBox QListView{\n"
"	padding:5px;\n"
"	border:1px solid;\n"
"	background-color: rgba(255, 255, 255, 50%);\n"
"	outline:0;\n"
"}\n"
"")
        self.comboBox_cliente_6.setMaxVisibleItems(10)
        self.comboBox_cliente_6.setInsertPolicy(QComboBox.NoInsert)
        self.comboBox_cliente_6.setIconSize(QSize(32, 32))
        self.comboBox_cliente_6.setDuplicatesEnabled(True)
        self.comboBox_cliente_6.setFrame(True)

        self.gridLayout_30.addWidget(self.comboBox_cliente_6, 3, 1, 1, 1)

        self.label_98 = QLabel(self.frame_144)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setMaximumSize(QSize(16777215, 13))
        self.label_98.setFont(font7)

        self.gridLayout_30.addWidget(self.label_98, 2, 3, 1, 1)

        self.label_94 = QLabel(self.frame_144)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setMaximumSize(QSize(16777215, 13))
        self.label_94.setFont(font7)

        self.gridLayout_30.addWidget(self.label_94, 2, 2, 1, 1)

        self.label_96 = QLabel(self.frame_144)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setMaximumSize(QSize(16777215, 13))
        self.label_96.setFont(font7)

        self.gridLayout_30.addWidget(self.label_96, 2, 4, 1, 1)

        self.radioButton = QRadioButton(self.frame_144)
        self.radioButton.setObjectName(u"radioButton")
        font12 = QFont()
        font12.setFamily(u"Segoe UI")
        font12.setPointSize(8)
        font12.setBold(False)
        font12.setWeight(50)
        self.radioButton.setFont(font12)
        self.radioButton.setStyleSheet(u"\n"
"QRadioButton::indicator {\n"
"    width:                  12px;\n"
"    height:                 12px;\n"
"    border-radius:          6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"	image: url(:/icons/check-solid.svg);\n"
"	background-color: rgb(6, 180, 20);\n"
"    border:                 1px solid rgb(88, 88, 88);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    border:                 1px solid rgb(88, 88, 88);\n"
"}")
        self.radioButton.setAutoExclusive(False)

        self.gridLayout_30.addWidget(self.radioButton, 2, 0, 1, 1)

        self.digite_um_id_2 = QLabel(self.frame_144)
        self.digite_um_id_2.setObjectName(u"digite_um_id_2")
        font13 = QFont()
        font13.setFamily(u"Segoe UI")
        font13.setPointSize(9)
        self.digite_um_id_2.setFont(font13)
        self.digite_um_id_2.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_30.addWidget(self.digite_um_id_2, 5, 0, 1, 2)


        self.verticalLayout_45.addWidget(self.frame_144)

        self.frame_147 = QFrame(self.frame_127)
        self.frame_147.setObjectName(u"frame_147")
        self.frame_147.setMinimumSize(QSize(0, 26))
        self.frame_147.setFont(font2)
        self.frame_147.setFrameShape(QFrame.NoFrame)
        self.frame_147.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_147)
        self.horizontalLayout_37.setSpacing(15)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.btn_Aplicar_filtro_geral_6 = QPushButton(self.frame_147)
        self.btn_Aplicar_filtro_geral_6.setObjectName(u"btn_Aplicar_filtro_geral_6")
        self.btn_Aplicar_filtro_geral_6.setMaximumSize(QSize(5000, 30))
        self.btn_Aplicar_filtro_geral_6.setFont(font7)
        self.btn_Aplicar_filtro_geral_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Aplicar_filtro_geral_6.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(250, 250, 250);\n"
"	border:1px solid rgb(67, 202, 0);\n"
"	padding:5px\n"
"}\n"
"QPushButton::hover{\n"
"	color: rgb(15, 202, 2)\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/icons/filter-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Aplicar_filtro_geral_6.setIcon(icon10)

        self.horizontalLayout_37.addWidget(self.btn_Aplicar_filtro_geral_6)

        self.btn_inprimir_6 = QPushButton(self.frame_147)
        self.btn_inprimir_6.setObjectName(u"btn_inprimir_6")
        self.btn_inprimir_6.setMaximumSize(QSize(5000, 30))
        self.btn_inprimir_6.setFont(font7)
        self.btn_inprimir_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_inprimir_6.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(250, 250, 250);\n"
"	border:1px solid;\n"
"	padding:5px\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(209, 209, 209);\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/icons/print-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_inprimir_6.setIcon(icon11)

        self.horizontalLayout_37.addWidget(self.btn_inprimir_6)

        self.pushButton_6 = QPushButton(self.frame_147)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMaximumSize(QSize(5000, 16777215))
        self.pushButton_6.setFont(font7)
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet(u"\n"
"QPushButton{\n"
"border: 1px solid rgb(255, 33, 33);\n"
"padding:5px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color:rgb(255, 33, 33)\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/icons/trash-can-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon12)

        self.horizontalLayout_37.addWidget(self.pushButton_6)


        self.verticalLayout_45.addWidget(self.frame_147)

        self.tableWidget_7 = QTableWidget(self.frame_127)
        if (self.tableWidget_7.columnCount() < 10):
            self.tableWidget_7.setColumnCount(10)
        font14 = QFont()
        font14.setPointSize(6)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font14);
        self.tableWidget_7.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        if (self.tableWidget_7.rowCount() < 2):
            self.tableWidget_7.setRowCount(2)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_7.setVerticalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_7.setVerticalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setCheckState(Qt.Unchecked);
        self.tableWidget_7.setItem(0, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_7.setItem(0, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_7.setItem(0, 2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_7.setItem(0, 3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_7.setItem(0, 4, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_7.setItem(0, 5, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_7.setItem(0, 6, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_7.setItem(0, 7, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_7.setItem(0, 8, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_7.setItem(0, 9, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setCheckState(Qt.Unchecked);
        self.tableWidget_7.setItem(1, 0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_7.setItem(1, 1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_7.setItem(1, 2, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_7.setItem(1, 3, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_7.setItem(1, 4, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_7.setItem(1, 5, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_7.setItem(1, 6, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_7.setItem(1, 7, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_7.setItem(1, 8, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_7.setItem(1, 9, __qtablewidgetitem31)
        self.tableWidget_7.setObjectName(u"tableWidget_7")
        self.tableWidget_7.setStyleSheet(u"QTableWidget{\n"
"	font: 10pt \"Century Gothic\";\n"
"	outline:0;\n"
"}\n"
"QHeaderView::section {\n"
"	color:white;\n"
"	border:1px solid white;\n"
"	background-color: rgb(43, 43, 43);\n"
"padding:0px 8px;\n"
"	font: -50 9pt \"Dubai\";\n"
"}\n"
"\n"
"QTableView::item:focus{\n"
"    border: 1px solid ;\n"
"	color:rgb(67, 202, 0)\n"
"}\n"
"QScrollBar:vertical {\n"
"    border: 1px solid #999999;\n"
"    background:white;\n"
"    width:15px;    \n"
"    margin: 1px\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(43, 43, 43);\n"
"    min-height: 0px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    background:rgb(50, 50, 50);\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"	height:0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: 1px solid #999999;\n"
"    background:white;\n"
"    height:15px;    \n"
"    margin: 1px\n"
" }\n"
"\n"
" QScrollBar::handle:horizontal {\n"
"    background: rgb(43, 43, 43);\n"
"    min-width: 0px;\n"
" }\n"
"QScrollBar::add-line:horizontal {\n"
"    background:rgb(50, 50, 50);\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"	height:0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
" }\n"
"\n"
"")
        self.tableWidget_7.setFrameShape(QFrame.NoFrame)
        self.tableWidget_7.setAutoScrollMargin(20)
        self.tableWidget_7.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_7.setAlternatingRowColors(True)
        self.tableWidget_7.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_7.setSortingEnabled(True)
        self.tableWidget_7.setRowCount(2)
        self.tableWidget_7.horizontalHeader().setDefaultSectionSize(109)
        self.tableWidget_7.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_7.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_45.addWidget(self.tableWidget_7)


        self.verticalLayout_11.addWidget(self.frame_127)

        self.stackedWidget.addWidget(self.page_relatorio_entradaesaida)
        self.page_relatorio_avulsas = QWidget()
        self.page_relatorio_avulsas.setObjectName(u"page_relatorio_avulsas")
        self.verticalLayout_98 = QVBoxLayout(self.page_relatorio_avulsas)
        self.verticalLayout_98.setSpacing(0)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.verticalLayout_98.setContentsMargins(0, 0, 0, 0)
        self.frame_121 = QFrame(self.page_relatorio_avulsas)
        self.frame_121.setObjectName(u"frame_121")
        self.frame_121.setFont(font2)
        self.frame_121.setStyleSheet(u"border:0")
        self.frame_121.setFrameShape(QFrame.NoFrame)
        self.frame_121.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_121)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, -1)
        self.frame_122 = QFrame(self.frame_121)
        self.frame_122.setObjectName(u"frame_122")
        self.frame_122.setMinimumSize(QSize(0, 37))
        self.frame_122.setMaximumSize(QSize(16777215, 37))
        self.frame_122.setFont(font2)
        self.frame_122.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(43, 43, 43);")
        self.frame_122.setFrameShape(QFrame.NoFrame)
        self.frame_122.setFrameShadow(QFrame.Raised)
        self.verticalLayout_97 = QVBoxLayout(self.frame_122)
        self.verticalLayout_97.setSpacing(7)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.verticalLayout_97.setContentsMargins(0, 0, 0, 0)
        self.aba_relatorio_button_5 = QPushButton(self.frame_122)
        self.aba_relatorio_button_5.setObjectName(u"aba_relatorio_button_5")
        self.aba_relatorio_button_5.setMinimumSize(QSize(160, 37))
        self.aba_relatorio_button_5.setMaximumSize(QSize(5555, 37))
        self.aba_relatorio_button_5.setBaseSize(QSize(555, 2))
        self.aba_relatorio_button_5.setFont(font10)
        self.aba_relatorio_button_5.setLayoutDirection(Qt.LeftToRight)
        self.aba_relatorio_button_5.setStyleSheet(u"QPushButton{\n"
"	border:0;\n"
"}")
        self.aba_relatorio_button_5.setIcon(icon3)
        self.aba_relatorio_button_5.setIconSize(QSize(30, 30))
        self.aba_relatorio_button_5.setFlat(False)

        self.verticalLayout_97.addWidget(self.aba_relatorio_button_5, 0, Qt.AlignTop)


        self.verticalLayout_27.addWidget(self.frame_122)

        self.frame_123 = QFrame(self.frame_121)
        self.frame_123.setObjectName(u"frame_123")
        self.frame_123.setMaximumSize(QSize(16777215, 105))
        self.frame_123.setFont(font2)
        self.frame_123.setFrameShape(QFrame.NoFrame)
        self.frame_123.setFrameShadow(QFrame.Raised)
        self.gridLayout_18 = QGridLayout(self.frame_123)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setHorizontalSpacing(9)
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_125 = QFrame(self.frame_123)
        self.frame_125.setObjectName(u"frame_125")
        self.frame_125.setMinimumSize(QSize(200, 63))
        self.frame_125.setMaximumSize(QSize(188, 16777215))
        self.frame_125.setFont(font2)
        self.frame_125.setFrameShape(QFrame.StyledPanel)
        self.frame_125.setFrameShadow(QFrame.Raised)
        self.gridLayout_20 = QGridLayout(self.frame_125)
        self.gridLayout_20.setSpacing(0)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(0, 0, 10, 0)
        self.data_depois_de_2 = QRadioButton(self.frame_125)
        self.data_depois_de_2.setObjectName(u"data_depois_de_2")
        self.data_depois_de_2.setMinimumSize(QSize(0, 1))
        self.data_depois_de_2.setFont(font11)

        self.gridLayout_20.addWidget(self.data_depois_de_2, 2, 0, 1, 1)

        self.data_fixa_2 = QRadioButton(self.frame_125)
        self.data_fixa_2.setObjectName(u"data_fixa_2")
        self.data_fixa_2.setFont(font11)

        self.gridLayout_20.addWidget(self.data_fixa_2, 0, 0, 1, 1)

        self.data_antes_de_2 = QRadioButton(self.frame_125)
        self.data_antes_de_2.setObjectName(u"data_antes_de_2")
        self.data_antes_de_2.setMinimumSize(QSize(0, 1))
        self.data_antes_de_2.setFont(font11)

        self.gridLayout_20.addWidget(self.data_antes_de_2, 1, 0, 1, 1)

        self.text_date_2 = QDateEdit(self.frame_125)
        self.text_date_2.setObjectName(u"text_date_2")
        self.text_date_2.setMinimumSize(QSize(0, 27))
        self.text_date_2.setFont(font11)
        self.text_date_2.setStyleSheet(u"QDateEdit{\n"
"	border:1px solid rgb(15, 202, 2);\n"
"	padding-left:10px;\n"
"	font-size:13px;\n"
"	\n"
"	font: 10pt \"Segoe UI\";\n"
"	background-color: rgb(250, 252, 250);\n"
"}\n"
"\n"
"QDateEdit::drop-down{\n"
"	border:0px;\n"
"}\n"
"\n"
"QDateEdit::down-arrow{\n"
"	image: url(:/icons/angle-down-solid.svg);\n"
"	width:12px;\n"
"	height:12px;\n"
"	margin-right:15px;\n"
"}\n"
"\n"
"QDateEdit::up-arrow{\n"
"	image: url(:/icons/angle-down-solid.svg);\n"
"	width:12px;\n"
"	height:12px;\n"
"	margin-right:15px;\n"
"}\n"
"\n"
"")
        self.text_date_2.setWrapping(False)
        self.text_date_2.setAlignment(Qt.AlignCenter)
        self.text_date_2.setReadOnly(False)
        self.text_date_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.text_date_2.setAccelerated(True)
        self.text_date_2.setKeyboardTracking(True)
        self.text_date_2.setProperty("showGroupSeparator", True)
        self.text_date_2.setDateTime(QDateTime(QDate(2022, 1, 1), QTime(0, 0, 0)))

        self.gridLayout_20.addWidget(self.text_date_2, 1, 1, 1, 1)


        self.gridLayout_18.addWidget(self.frame_125, 1, 15, 2, 1)

        self.label_69 = QLabel(self.frame_123)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setFont(font8)

        self.gridLayout_18.addWidget(self.label_69, 2, 5, 1, 1)

        self.label_43 = QLabel(self.frame_123)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMaximumSize(QSize(16777215, 13))
        self.label_43.setFont(font7)

        self.gridLayout_18.addWidget(self.label_43, 1, 1, 1, 1, Qt.AlignBottom)

        self.comboBox_cliente_2 = QComboBox(self.frame_123)
        self.comboBox_cliente_2.addItem("")
        self.comboBox_cliente_2.setObjectName(u"comboBox_cliente_2")
        self.comboBox_cliente_2.setMinimumSize(QSize(0, 27))
        self.comboBox_cliente_2.setMaximumSize(QSize(500, 16777215))
        self.comboBox_cliente_2.setFont(font11)
        self.comboBox_cliente_2.setStyleSheet(u"QComboBox{\n"
"	border:1px solid rgb(15, 202, 2);\n"
"	padding-left:10px;\n"
"	font-size:13px;\n"
"	font: 10pt \"Segoe UI\";\n"
"	background-color: rgb(250, 252, 250);\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"	border:0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
"	image: url(:/icons/angle-down-solid.svg);\n"
"	width:12px;\n"
"	height:12px;\n"
"	margin-right:15px;\n"
"}\n"
"\n"
"QComboBox::on{\n"
"	border:2px solid rgb(67, 202, 0);\n"
"}\n"
"\n"
"QComboBox QListView{\n"
"	padding:5px;\n"
"	border:1px solid;\n"
"	background-color: rgba(255, 255, 255, 50%);\n"
"	outline:0;\n"
"}\n"
"")
        self.comboBox_cliente_2.setMaxVisibleItems(10)
        self.comboBox_cliente_2.setInsertPolicy(QComboBox.NoInsert)
        self.comboBox_cliente_2.setIconSize(QSize(32, 32))
        self.comboBox_cliente_2.setDuplicatesEnabled(True)
        self.comboBox_cliente_2.setFrame(True)

        self.gridLayout_18.addWidget(self.comboBox_cliente_2, 2, 1, 1, 1)

        self.comboBox_produto_2 = QComboBox(self.frame_123)
        self.comboBox_produto_2.addItem("")
        self.comboBox_produto_2.setObjectName(u"comboBox_produto_2")
        self.comboBox_produto_2.setMinimumSize(QSize(0, 27))
        self.comboBox_produto_2.setMaximumSize(QSize(500, 16777215))
        self.comboBox_produto_2.setFont(font11)
        self.comboBox_produto_2.setStyleSheet(u"QComboBox{\n"
"	border:1px solid rgb(15, 202, 2);\n"
"	padding-left:10px;\n"
"	font-size:13px;\n"
"	font: 10pt \"Segoe UI\";\n"
"	background-color: rgb(250, 252, 250);\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"	border:0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
"	image: url(:/icons/angle-down-solid.svg);\n"
"	width:12px;\n"
"	height:12px;\n"
"	margin-right:15px;\n"
"}\n"
"\n"
"QComboBox::on{\n"
"	border:2px solid rgb(67, 202, 0);\n"
"}\n"
"\n"
"QComboBox QListView{\n"
"	padding:5px;\n"
"	border:1px solid;\n"
"	background-color: rgba(255, 255, 255, 50%);\n"
"	outline:0;\n"
"}\n"
"")
        self.comboBox_produto_2.setMaxVisibleItems(10)
        self.comboBox_produto_2.setInsertPolicy(QComboBox.NoInsert)
        self.comboBox_produto_2.setIconSize(QSize(32, 32))
        self.comboBox_produto_2.setDuplicatesEnabled(True)
        self.comboBox_produto_2.setFrame(True)

        self.gridLayout_18.addWidget(self.comboBox_produto_2, 2, 3, 1, 1)

        self.label_49 = QLabel(self.frame_123)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMaximumSize(QSize(16777215, 13))
        self.label_49.setFont(font7)

        self.gridLayout_18.addWidget(self.label_49, 1, 2, 1, 1, Qt.AlignBottom)

        self.comboBox_veiculo_2 = QComboBox(self.frame_123)
        self.comboBox_veiculo_2.addItem("")
        self.comboBox_veiculo_2.setObjectName(u"comboBox_veiculo_2")
        self.comboBox_veiculo_2.setMinimumSize(QSize(0, 27))
        self.comboBox_veiculo_2.setMaximumSize(QSize(500, 16777215))
        self.comboBox_veiculo_2.setFont(font11)
        self.comboBox_veiculo_2.setStyleSheet(u"QComboBox{\n"
"	border:1px solid rgb(15, 202, 2);\n"
"	padding-left:10px;\n"
"	font-size:13px;\n"
"	font: 10pt \"Segoe UI\";\n"
"	background-color: rgb(250, 252, 250);\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"	border:0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
"	image: url(:/icons/angle-down-solid.svg);\n"
"	width:12px;\n"
"	height:12px;\n"
"	margin-right:15px;\n"
"}\n"
"\n"
"QComboBox::on{\n"
"	border:2px solid rgb(67, 202, 0);\n"
"}\n"
"\n"
"QComboBox QListView{\n"
"	padding:5px;\n"
"	border:1px solid;\n"
"	background-color: rgba(255, 255, 255, 50%);\n"
"	outline:0;\n"
"}\n"
"")
        self.comboBox_veiculo_2.setMaxVisibleItems(10)
        self.comboBox_veiculo_2.setInsertPolicy(QComboBox.NoInsert)
        self.comboBox_veiculo_2.setIconSize(QSize(32, 32))
        self.comboBox_veiculo_2.setDuplicatesEnabled(True)
        self.comboBox_veiculo_2.setFrame(True)

        self.gridLayout_18.addWidget(self.comboBox_veiculo_2, 2, 2, 1, 1)

        self.label_70 = QLabel(self.frame_123)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setMaximumSize(QSize(16777215, 13))
        self.label_70.setFont(font7)

        self.gridLayout_18.addWidget(self.label_70, 1, 3, 1, 1, Qt.AlignBottom)

        self.lineEdit_7 = QLineEdit(self.frame_123)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(0, 27))
        self.lineEdit_7.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_7.setFont(font11)
        self.lineEdit_7.setStyleSheet(u"QLineEdit{\n"
"	padding-left:10px;\n"
"	font-size:13px;\n"
"	border:1px solid;\n"
"	font: 10pt \"Segoe UI\";\n"
"\n"
"	background-color: rgb(250, 252, 250);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:1px solid rgb(15, 202, 2);\n"
"\n"
"}")

        self.gridLayout_18.addWidget(self.lineEdit_7, 2, 4, 1, 1)

        self.label_62 = QLabel(self.frame_123)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMinimumSize(QSize(0, 13))
        self.label_62.setFont(font7)

        self.gridLayout_18.addWidget(self.label_62, 0, 15, 1, 1)

        self.frame_124 = QFrame(self.frame_123)
        self.frame_124.setObjectName(u"frame_124")
        self.frame_124.setMaximumSize(QSize(100, 16777215))
        self.frame_124.setFont(font2)
        self.frame_124.setFrameShape(QFrame.NoFrame)
        self.frame_124.setFrameShadow(QFrame.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_124)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setVerticalSpacing(0)
        self.gridLayout_19.setContentsMargins(7, 0, 0, 0)
        self.btn_filtro_id_2 = QPushButton(self.frame_124)
        self.btn_filtro_id_2.setObjectName(u"btn_filtro_id_2")
        self.btn_filtro_id_2.setMaximumSize(QSize(16777215, 16))
        self.btn_filtro_id_2.setFont(font2)
        self.btn_filtro_id_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_filtro_id_2.setIcon(icon9)
        self.btn_filtro_id_2.setIconSize(QSize(16, 16))

        self.gridLayout_19.addWidget(self.btn_filtro_id_2, 1, 1, 1, 1, Qt.AlignLeft)

        self.text_filtro_id_2 = QLineEdit(self.frame_124)
        self.text_filtro_id_2.setObjectName(u"text_filtro_id_2")
        self.text_filtro_id_2.setMaximumSize(QSize(50, 16777215))
        self.text_filtro_id_2.setFont(font8)
        self.text_filtro_id_2.setStyleSheet(u"\n"
"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"border:1px solid rgb(203, 203, 203);\n"
"padding:5px;\n"
"\n"
"}\n"
"\n"
"QLineEdit::focus{\n"
"	border:1px solid rgb(67, 202, 0)\n"
"}\n"
"")
        self.text_filtro_id_2.setMaxLength(6)

        self.gridLayout_19.addWidget(self.text_filtro_id_2, 1, 0, 1, 1)


        self.gridLayout_18.addWidget(self.frame_124, 2, 0, 1, 1, Qt.AlignLeft)

        self.label_68 = QLabel(self.frame_123)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setMaximumSize(QSize(16777215, 13))
        self.label_68.setFont(font7)

        self.gridLayout_18.addWidget(self.label_68, 1, 4, 1, 1, Qt.AlignBottom)


        self.verticalLayout_27.addWidget(self.frame_123)

        self.digite_um_id = QLabel(self.frame_121)
        self.digite_um_id.setObjectName(u"digite_um_id")
        self.digite_um_id.setFont(font13)
        self.digite_um_id.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.verticalLayout_27.addWidget(self.digite_um_id)

        self.frame_126 = QFrame(self.frame_121)
        self.frame_126.setObjectName(u"frame_126")
        self.frame_126.setMinimumSize(QSize(0, 26))
        self.frame_126.setFont(font2)
        self.frame_126.setFrameShape(QFrame.NoFrame)
        self.frame_126.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_126)
        self.horizontalLayout_31.setSpacing(15)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.btn_Aplicar_filtro_geral_2 = QPushButton(self.frame_126)
        self.btn_Aplicar_filtro_geral_2.setObjectName(u"btn_Aplicar_filtro_geral_2")
        self.btn_Aplicar_filtro_geral_2.setFont(font7)
        self.btn_Aplicar_filtro_geral_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Aplicar_filtro_geral_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(250, 250, 250);\n"
"	border:1px solid rgb(67, 202, 0);\n"
"	padding:5px\n"
"}\n"
"QPushButton::hover{\n"
"	color: rgb(15, 202, 2)\n"
"}")
        self.btn_Aplicar_filtro_geral_2.setIcon(icon10)

        self.horizontalLayout_31.addWidget(self.btn_Aplicar_filtro_geral_2)

        self.btn_inprimir_2 = QPushButton(self.frame_126)
        self.btn_inprimir_2.setObjectName(u"btn_inprimir_2")
        self.btn_inprimir_2.setFont(font7)
        self.btn_inprimir_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_inprimir_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(250, 250, 250);\n"
"	border:1px solid;\n"
"	padding:5px\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(209, 209, 209);\n"
"}")
        self.btn_inprimir_2.setIcon(icon11)

        self.horizontalLayout_31.addWidget(self.btn_inprimir_2)

        self.pushButton_8 = QPushButton(self.frame_126)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setFont(font7)
        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet(u"\n"
"QPushButton{\n"
"border: 1px solid rgb(255, 33, 33);\n"
"padding:5px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color:rgb(255, 33, 33)\n"
"}")
        self.pushButton_8.setIcon(icon12)

        self.horizontalLayout_31.addWidget(self.pushButton_8)


        self.verticalLayout_27.addWidget(self.frame_126)

        self.tableWidget_4 = QTableWidget(self.frame_121)
        if (self.tableWidget_4.columnCount() < 7):
            self.tableWidget_4.setColumnCount(7)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setFont(font14);
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(5, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(6, __qtablewidgetitem38)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setStyleSheet(u"QTableWidget{\n"
"	font: 10pt \"Century Gothic\";\n"
"	outline:0;\n"
"}\n"
"QHeaderView::section {\n"
"	color:white;\n"
"	border:1px solid white;\n"
"	background-color: rgb(43, 43, 43);\n"
"padding:0px 8px;\n"
"	font: -50 10pt \"Dubai\";\n"
"}\n"
"\n"
"QTableView::item:focus{\n"
"    border: 1px solid ;\n"
"	color:rgb(67, 202, 0)\n"
"}\n"
"QScrollBar:vertical {\n"
"    border: 1px solid #999999;\n"
"    background:white;\n"
"    width:15px;    \n"
"    margin: 1px\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(43, 43, 43);\n"
"    min-height: 0px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    background:rgb(50, 50, 50);\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"	height:0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}"
                        "\n"
"\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: 1px solid #999999;\n"
"    background:white;\n"
"    height:15px;    \n"
"    margin: 1px\n"
" }\n"
"\n"
" QScrollBar::handle:horizontal {\n"
"    background: rgb(43, 43, 43);\n"
"    min-width: 0px;\n"
" }\n"
"QScrollBar::add-line:horizontal {\n"
"    background:rgb(50, 50, 50);\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"	height:0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
" }\n"
"\n"
"")
        self.tableWidget_4.setAlternatingRowColors(True)
        self.tableWidget_4.setSortingEnabled(True)
        self.tableWidget_4.setRowCount(0)
        self.tableWidget_4.horizontalHeader().setDefaultSectionSize(152)
        self.tableWidget_4.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_4.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_27.addWidget(self.tableWidget_4)


        self.verticalLayout_98.addWidget(self.frame_121)

        self.stackedWidget.addWidget(self.page_relatorio_avulsas)
        self.page_clientes = QWidget()
        self.page_clientes.setObjectName(u"page_clientes")
        self.page_clientes.setStyleSheet(u"border:0")
        self.verticalLayout_22 = QVBoxLayout(self.page_clientes)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.page_clientes)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFont(font2)
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_22)
        self.verticalLayout_24.setSpacing(7)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.frame_22)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(0, 37))
        self.frame_23.setMaximumSize(QSize(16777215, 37))
        font15 = QFont()
        font15.setFamily(u"Segoe UI")
        font15.setPointSize(13)
        self.frame_23.setFont(font15)
        self.frame_23.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(43, 43, 43);")
        self.frame_23.setFrameShape(QFrame.NoFrame)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_23)
        self.verticalLayout_23.setSpacing(7)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.aba_relatorio_button_3 = QPushButton(self.frame_23)
        self.aba_relatorio_button_3.setObjectName(u"aba_relatorio_button_3")
        self.aba_relatorio_button_3.setMinimumSize(QSize(160, 37))
        self.aba_relatorio_button_3.setMaximumSize(QSize(5555, 37))
        self.aba_relatorio_button_3.setBaseSize(QSize(555, 2))
        self.aba_relatorio_button_3.setFont(font10)
        self.aba_relatorio_button_3.setLayoutDirection(Qt.LeftToRight)
        self.aba_relatorio_button_3.setStyleSheet(u"QPushButton{\n"
"	border:0;\n"
"}")
        self.aba_relatorio_button_3.setIcon(icon2)
        self.aba_relatorio_button_3.setIconSize(QSize(30, 30))
        self.aba_relatorio_button_3.setFlat(False)

        self.verticalLayout_23.addWidget(self.aba_relatorio_button_3, 0, Qt.AlignTop)


        self.verticalLayout_24.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.frame_22)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMaximumSize(QSize(1677777, 16777215))
        self.frame_24.setFont(font2)
        self.frame_24.setFrameShape(QFrame.NoFrame)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_43 = QFrame(self.frame_24)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setMinimumSize(QSize(0, 0))
        self.frame_43.setMaximumSize(QSize(300, 16777215))
        self.frame_43.setFont(font2)
        self.frame_43.setFrameShape(QFrame.Panel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_43)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.frame_47 = QFrame(self.frame_43)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setMinimumSize(QSize(0, 0))
        self.frame_47.setMaximumSize(QSize(16777215, 30))
        self.frame_47.setFont(font2)
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_47)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.frame_47)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font5)

        self.verticalLayout_47.addWidget(self.label_18, 0, Qt.AlignHCenter)


        self.verticalLayout_46.addWidget(self.frame_47)

        self.frame_48 = QFrame(self.frame_43)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFont(font2)
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_48)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.frame_51 = QFrame(self.frame_48)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setFont(font2)
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_51)
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.input_clientes_nome = QLineEdit(self.frame_51)
        self.input_clientes_nome.setObjectName(u"input_clientes_nome")
        self.input_clientes_nome.setFont(font9)
        self.input_clientes_nome.setStyleSheet(u"QLineEdit{padding:3px;border:1px solid;background-color: rgb(243, 243, 243);}\n"
"\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")
        self.input_clientes_nome.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_50.addWidget(self.input_clientes_nome)


        self.verticalLayout_49.addWidget(self.frame_51)

        self.frame_56 = QFrame(self.frame_48)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setFont(font2)
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_56)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, -1, 0, 0)
        self.input_clientes_cpf = QLineEdit(self.frame_56)
        self.input_clientes_cpf.setObjectName(u"input_clientes_cpf")
        self.input_clientes_cpf.setFont(font9)
        self.input_clientes_cpf.setStyleSheet(u"QLineEdit{padding:3px;border:1px solid;background-color: rgb(243, 243, 243);}\n"
"\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")
        self.input_clientes_cpf.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_48.addWidget(self.input_clientes_cpf)


        self.verticalLayout_49.addWidget(self.frame_56)

        self.frame_50 = QFrame(self.frame_48)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFont(font2)
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_50)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.input_clientes_rg = QLineEdit(self.frame_50)
        self.input_clientes_rg.setObjectName(u"input_clientes_rg")
        self.input_clientes_rg.setFont(font9)
        self.input_clientes_rg.setStyleSheet(u"QLineEdit{padding:3px;border:1px solid;background-color: rgb(243, 243, 243);}\n"
"\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")
        self.input_clientes_rg.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_51.addWidget(self.input_clientes_rg)


        self.verticalLayout_49.addWidget(self.frame_50)

        self.frame_55 = QFrame(self.frame_48)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setFont(font2)
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_55)
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.input_clientes_cep = QLineEdit(self.frame_55)
        self.input_clientes_cep.setObjectName(u"input_clientes_cep")
        self.input_clientes_cep.setFont(font9)
        self.input_clientes_cep.setStyleSheet(u"QLineEdit{padding:3px;border:1px solid;background-color: rgb(243, 243, 243);}\n"
"\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")
        self.input_clientes_cep.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_4.addWidget(self.input_clientes_cep)

        self.input_clientes_endereco = QLineEdit(self.frame_55)
        self.input_clientes_endereco.setObjectName(u"input_clientes_endereco")
        self.input_clientes_endereco.setMaximumSize(QSize(140, 16777215))
        self.input_clientes_endereco.setFont(font1)
        self.input_clientes_endereco.setStyleSheet(u"QLineEdit{padding:3px;border:1px solid;background-color: rgb(243, 243, 243);}\n"
"\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")

        self.horizontalLayout_4.addWidget(self.input_clientes_endereco)


        self.verticalLayout_49.addWidget(self.frame_55)

        self.frame_52 = QFrame(self.frame_48)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFont(font2)
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_52)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.horizontalLayout_39.addWidget(self.label_8)

        self.input_clientes_telefone = QLineEdit(self.frame_52)
        self.input_clientes_telefone.setObjectName(u"input_clientes_telefone")
        self.input_clientes_telefone.setFont(font9)
        self.input_clientes_telefone.setStyleSheet(u"QLineEdit{padding:3px;border:1px solid;background-color: rgb(243, 243, 243);}\n"
"\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")
        self.input_clientes_telefone.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_39.addWidget(self.input_clientes_telefone)


        self.verticalLayout_49.addWidget(self.frame_52)

        self.btn_registrar_clientes = QPushButton(self.frame_48)
        self.btn_registrar_clientes.setObjectName(u"btn_registrar_clientes")
        self.btn_registrar_clientes.setFont(font7)
        self.btn_registrar_clientes.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_registrar_clientes.setStyleSheet(u"QPushButton{\n"
"	border:1px solid rgb(15, 202, 2);\n"
"	padding:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(122, 229, 105);\n"
"}")

        self.verticalLayout_49.addWidget(self.btn_registrar_clientes)


        self.verticalLayout_46.addWidget(self.frame_48)


        self.horizontalLayout_6.addWidget(self.frame_43)

        self.btn_menu_registrar_clientes = QPushButton(self.frame_24)
        self.btn_menu_registrar_clientes.setObjectName(u"btn_menu_registrar_clientes")
        self.btn_menu_registrar_clientes.setMinimumSize(QSize(0, 485))
        self.btn_menu_registrar_clientes.setMaximumSize(QSize(30, 16777215))
        self.btn_menu_registrar_clientes.setFont(font2)
        self.btn_menu_registrar_clientes.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu_registrar_clientes.setStyleSheet(u"border-radius:2px;\n"
"background-color: rgb(43, 43, 43);")
        icon13 = QIcon()
        icon13.addFile(u":/icons/caret-left-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu_registrar_clientes.setIcon(icon13)

        self.horizontalLayout_6.addWidget(self.btn_menu_registrar_clientes)

        self.frame_46 = QFrame(self.frame_24)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_46)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.widget = QWidget(self.frame_46)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 60))
        self.gridLayout_10 = QGridLayout(self.widget)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_16 = QLabel(self.widget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(30, 30))
        self.label_16.setFont(font2)
        self.label_16.setPixmap(QPixmap(u":/icons/clock-rotate-left-solid.svg"))
        self.label_16.setScaledContents(True)

        self.gridLayout_10.addWidget(self.label_16, 0, 0, 1, 1)

        self.label_14 = QLabel(self.widget)
        self.label_14.setObjectName(u"label_14")
        font16 = QFont()
        font16.setFamily(u"Segoe UI")
        font16.setPointSize(13)
        font16.setBold(True)
        font16.setWeight(75)
        self.label_14.setFont(font16)

        self.gridLayout_10.addWidget(self.label_14, 0, 1, 1, 1)


        self.verticalLayout_26.addWidget(self.widget, 0, Qt.AlignHCenter)

        self.btn_remover_clientes = QPushButton(self.frame_46)
        self.btn_remover_clientes.setObjectName(u"btn_remover_clientes")
        self.btn_remover_clientes.setMaximumSize(QSize(270, 16777215))
        self.btn_remover_clientes.setFont(font7)
        self.btn_remover_clientes.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_remover_clientes.setStyleSheet(u"\n"
"QPushButton{\n"
"border: 1px solid rgb(255, 33, 33);\n"
"padding:5px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color:rgb(255, 33, 33)\n"
"}")
        self.btn_remover_clientes.setIcon(icon12)
        self.btn_remover_clientes.setIconSize(QSize(25, 22))

        self.verticalLayout_26.addWidget(self.btn_remover_clientes)

        self.tableWidget_2 = QTableWidget(self.frame_46)
        if (self.tableWidget_2.columnCount() < 7):
            self.tableWidget_2.setColumnCount(7)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setFont(font14);
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem45)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setStyleSheet(u"QTableWidget{\n"
"	font: 10pt \"Century Gothic\";\n"
"	outline:0;\n"
"}\n"
"QHeaderView::section {\n"
"	color:white;\n"
"	border:1px solid white;\n"
"	background-color: rgb(43, 43, 43);\n"
"padding:0px 8px;\n"
"	font: -50 10pt \"Dubai\";\n"
"}\n"
"\n"
"QTableView::item:focus{\n"
"    border: 1px solid ;\n"
"	color:rgb(67, 202, 0)\n"
"}\n"
"QScrollBar:vertical {\n"
"    border: 1px solid #999999;\n"
"    background:white;\n"
"    width:15px;    \n"
"    margin: 1px\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(43, 43, 43);\n"
"    min-height: 0px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    background:rgb(50, 50, 50);\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"	height:0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}"
                        "\n"
"\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: 1px solid #999999;\n"
"    background:white;\n"
"    height:15px;    \n"
"    margin: 1px\n"
" }\n"
"\n"
" QScrollBar::handle:horizontal {\n"
"    background: rgb(43, 43, 43);\n"
"    min-width: 0px;\n"
" }\n"
"QScrollBar::add-line:horizontal {\n"
"    background:rgb(50, 50, 50);\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"	height:0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
" }\n"
"\n"
"")
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.setSortingEnabled(True)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(135)
        self.tableWidget_2.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_26.addWidget(self.tableWidget_2)


        self.horizontalLayout_6.addWidget(self.frame_46)


        self.verticalLayout_24.addWidget(self.frame_24)


        self.verticalLayout_22.addWidget(self.frame_22)

        self.stackedWidget.addWidget(self.page_clientes)
        self.page_veiculos = QWidget()
        self.page_veiculos.setObjectName(u"page_veiculos")
        self.page_veiculos.setStyleSheet(u"border:0")
        self.verticalLayout_33 = QVBoxLayout(self.page_veiculos)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.frame_31 = QFrame(self.page_veiculos)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFont(font2)
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_31)
        self.verticalLayout_31.setSpacing(7)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.frame_32 = QFrame(self.frame_31)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(0, 37))
        self.frame_32.setMaximumSize(QSize(16777215, 37))
        self.frame_32.setFont(font2)
        self.frame_32.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(43, 43, 43);")
        self.frame_32.setFrameShape(QFrame.NoFrame)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_32)
        self.verticalLayout_32.setSpacing(7)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.aba_relatorio_button_6 = QPushButton(self.frame_32)
        self.aba_relatorio_button_6.setObjectName(u"aba_relatorio_button_6")
        self.aba_relatorio_button_6.setMinimumSize(QSize(160, 37))
        self.aba_relatorio_button_6.setMaximumSize(QSize(5555, 37))
        self.aba_relatorio_button_6.setBaseSize(QSize(555, 2))
        self.aba_relatorio_button_6.setFont(font10)
        self.aba_relatorio_button_6.setLayoutDirection(Qt.LeftToRight)
        self.aba_relatorio_button_6.setStyleSheet(u"QPushButton{\n"
"	border:0;\n"
"}")
        self.aba_relatorio_button_6.setIcon(icon2)
        self.aba_relatorio_button_6.setIconSize(QSize(30, 30))
        self.aba_relatorio_button_6.setFlat(False)

        self.verticalLayout_32.addWidget(self.aba_relatorio_button_6, 0, Qt.AlignTop)


        self.verticalLayout_31.addWidget(self.frame_32)

        self.frame_33 = QFrame(self.frame_31)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMaximumSize(QSize(1677777, 16777215))
        self.frame_33.setFont(font2)
        self.frame_33.setFrameShape(QFrame.NoFrame)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_68 = QFrame(self.frame_33)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setMinimumSize(QSize(0, 0))
        self.frame_68.setMaximumSize(QSize(300, 16777215))
        self.frame_68.setFont(font2)
        self.frame_68.setFrameShape(QFrame.Panel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.verticalLayout_68 = QVBoxLayout(self.frame_68)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.frame_69 = QFrame(self.frame_68)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setMinimumSize(QSize(0, 0))
        self.frame_69.setMaximumSize(QSize(16777215, 30))
        self.frame_69.setFont(font2)
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_69)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel(self.frame_69)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font5)

        self.horizontalLayout_15.addWidget(self.label_26)


        self.verticalLayout_68.addWidget(self.frame_69, 0, Qt.AlignHCenter)

        self.frame_70 = QFrame(self.frame_68)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setFont(font2)
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_70)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_148 = QFrame(self.frame_70)
        self.frame_148.setObjectName(u"frame_148")
        self.frame_148.setFont(font2)
        self.frame_148.setFrameShape(QFrame.StyledPanel)
        self.frame_148.setFrameShadow(QFrame.Raised)
        self.verticalLayout_113 = QVBoxLayout(self.frame_148)
        self.verticalLayout_113.setSpacing(0)
        self.verticalLayout_113.setObjectName(u"verticalLayout_113")
        self.verticalLayout_113.setContentsMargins(0, -1, 0, 0)
        self.input_veiculos_valor_2 = QLineEdit(self.frame_148)
        self.input_veiculos_valor_2.setObjectName(u"input_veiculos_valor_2")
        self.input_veiculos_valor_2.setFont(font9)
        self.input_veiculos_valor_2.setStyleSheet(u"QLineEdit{padding:3px;border:1px solid;background-color: rgb(243, 243, 243);}\n"
"\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")
        self.input_veiculos_valor_2.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_113.addWidget(self.input_veiculos_valor_2)


        self.verticalLayout_12.addWidget(self.frame_148)

        self.frame_71 = QFrame(self.frame_70)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setFont(font2)
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.verticalLayout_71 = QVBoxLayout(self.frame_71)
        self.verticalLayout_71.setSpacing(0)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.input_veiculos_nome = QLineEdit(self.frame_71)
        self.input_veiculos_nome.setObjectName(u"input_veiculos_nome")
        self.input_veiculos_nome.setFont(font9)
        self.input_veiculos_nome.setStyleSheet(u"QLineEdit{padding:3px;border:1px solid;background-color: rgb(243, 243, 243);}\n"
"\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")
        self.input_veiculos_nome.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_71.addWidget(self.input_veiculos_nome)


        self.verticalLayout_12.addWidget(self.frame_71)

        self.frame_73 = QFrame(self.frame_70)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setFont(font2)
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.verticalLayout_73 = QVBoxLayout(self.frame_73)
        self.verticalLayout_73.setSpacing(0)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.verticalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.input_veiculos_placa = QLineEdit(self.frame_73)
        self.input_veiculos_placa.setObjectName(u"input_veiculos_placa")
        self.input_veiculos_placa.setFont(font9)
        self.input_veiculos_placa.setStyleSheet(u"QLineEdit{padding:3px;border:1px solid;background-color: rgb(243, 243, 243);}\n"
"\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")
        self.input_veiculos_placa.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_73.addWidget(self.input_veiculos_placa)


        self.verticalLayout_12.addWidget(self.frame_73)

        self.frame_74 = QFrame(self.frame_70)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setFont(font2)
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_74)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.comboBox_veiculos_produtos = QComboBox(self.frame_74)
        self.comboBox_veiculos_produtos.addItem("")
        self.comboBox_veiculos_produtos.setObjectName(u"comboBox_veiculos_produtos")
        self.comboBox_veiculos_produtos.setMinimumSize(QSize(154, 33))
        font17 = QFont()
        font17.setFamily(u"Century Gothic")
        font17.setPointSize(11)
        font17.setBold(False)
        font17.setItalic(False)
        font17.setWeight(50)
        self.comboBox_veiculos_produtos.setFont(font17)
        self.comboBox_veiculos_produtos.setCursor(QCursor(Qt.ArrowCursor))
        self.comboBox_veiculos_produtos.setStyleSheet(u"QComboBox{\n"
"	border:1px solid rgb(15, 202, 2);\n"
"	padding-left:10px;\n"
"	font: 11pt \"Century Gothic\";\n"
"	background-color: rgb(250, 252, 250);\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"	border:0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
"	image: url(:/icons/angle-down-solid.svg);\n"
"	width:12px;\n"
"	height:12px;\n"
"	margin-right:15px;\n"
"}\n"
"\n"
"QComboBox::on{\n"
"	border:2px solid rgb(67, 202, 0);\n"
"}\n"
"\n"
"QComboBox QListView{\n"
"	padding:5px;\n"
"	border:1px solid;\n"
"	background-color: rgba(255, 255, 255, 50%);\n"
"	outline:0;\n"
"}\n"
"")
        self.comboBox_veiculos_produtos.setMaxVisibleItems(6)
        self.comboBox_veiculos_produtos.setInsertPolicy(QComboBox.NoInsert)
        self.comboBox_veiculos_produtos.setIconSize(QSize(32, 32))
        self.comboBox_veiculos_produtos.setDuplicatesEnabled(True)
        self.comboBox_veiculos_produtos.setFrame(True)

        self.gridLayout_16.addWidget(self.comboBox_veiculos_produtos, 1, 0, 1, 1)

        self.label_5 = QLabel(self.frame_74)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 25))
        self.label_5.setFont(font5)

        self.gridLayout_16.addWidget(self.label_5, 0, 0, 1, 1, Qt.AlignTop)


        self.verticalLayout_12.addWidget(self.frame_74, 0, Qt.AlignVCenter)

        self.btn_registrar_veiculos = QPushButton(self.frame_70)
        self.btn_registrar_veiculos.setObjectName(u"btn_registrar_veiculos")
        self.btn_registrar_veiculos.setFont(font7)
        self.btn_registrar_veiculos.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_registrar_veiculos.setStyleSheet(u"QPushButton{\n"
"	border:1px solid rgb(15, 202, 2);\n"
"	padding:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(122, 229, 105);\n"
"}")

        self.verticalLayout_12.addWidget(self.btn_registrar_veiculos)


        self.verticalLayout_68.addWidget(self.frame_70)


        self.horizontalLayout_8.addWidget(self.frame_68)

        self.btn_menu_registrar_veiculos = QPushButton(self.frame_33)
        self.btn_menu_registrar_veiculos.setObjectName(u"btn_menu_registrar_veiculos")
        self.btn_menu_registrar_veiculos.setMinimumSize(QSize(0, 485))
        self.btn_menu_registrar_veiculos.setMaximumSize(QSize(30, 16777215))
        self.btn_menu_registrar_veiculos.setFont(font2)
        self.btn_menu_registrar_veiculos.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu_registrar_veiculos.setStyleSheet(u"border-radius:2px;\n"
"background-color: rgb(43, 43, 43);")
        self.btn_menu_registrar_veiculos.setIcon(icon13)

        self.horizontalLayout_8.addWidget(self.btn_menu_registrar_veiculos)

        self.frame_78 = QFrame(self.frame_33)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setFont(font2)
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_78)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.widget_3 = QWidget(self.frame_78)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 60))
        self.widget_3.setFont(font2)
        self.gridLayout_12 = QGridLayout(self.widget_3)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_27 = QLabel(self.widget_3)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(30, 30))
        self.label_27.setFont(font2)
        self.label_27.setPixmap(QPixmap(u":/icons/clock-rotate-left-solid.svg"))
        self.label_27.setScaledContents(True)

        self.gridLayout_12.addWidget(self.label_27, 0, 0, 1, 1)

        self.label_28 = QLabel(self.widget_3)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font16)

        self.gridLayout_12.addWidget(self.label_28, 0, 1, 1, 1)


        self.verticalLayout_25.addWidget(self.widget_3, 0, Qt.AlignHCenter)

        self.btn_remover_veiculos = QPushButton(self.frame_78)
        self.btn_remover_veiculos.setObjectName(u"btn_remover_veiculos")
        self.btn_remover_veiculos.setMaximumSize(QSize(270, 16777215))
        self.btn_remover_veiculos.setFont(font7)
        self.btn_remover_veiculos.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_remover_veiculos.setStyleSheet(u"\n"
"QPushButton{\n"
"border: 1px solid rgb(255, 33, 33);\n"
"padding:5px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color:rgb(255, 33, 33)\n"
"}")
        self.btn_remover_veiculos.setIcon(icon12)
        self.btn_remover_veiculos.setIconSize(QSize(25, 22))

        self.verticalLayout_25.addWidget(self.btn_remover_veiculos)

        self.tableWidget_3 = QTableWidget(self.frame_78)
        if (self.tableWidget_3.columnCount() < 5):
            self.tableWidget_3.setColumnCount(5)
        __qtablewidgetitem46 = QTableWidgetItem()
        __qtablewidgetitem46.setFont(font14);
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem50)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setStyleSheet(u"QTableWidget{\n"
"	font: 10pt \"Century Gothic\";\n"
"	outline:0;\n"
"}\n"
"QHeaderView::section {\n"
"	color:white;\n"
"	border:1px solid white;\n"
"	background-color: rgb(43, 43, 43);\n"
"padding:0px 8px;\n"
"	font: -50 10pt \"Dubai\";\n"
"}\n"
"\n"
"QTableView::item:focus{\n"
"    border: 1px solid ;\n"
"	color:rgb(67, 202, 0)\n"
"}\n"
"QScrollBar:vertical {\n"
"    border: 1px solid #999999;\n"
"    background:white;\n"
"    width:15px;    \n"
"    margin: 1px\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(43, 43, 43);\n"
"    min-height: 0px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    background:rgb(50, 50, 50);\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"	height:0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}"
                        "\n"
"\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: 1px solid #999999;\n"
"    background:white;\n"
"    height:15px;    \n"
"    margin: 1px\n"
" }\n"
"\n"
" QScrollBar::handle:horizontal {\n"
"    background: rgb(43, 43, 43);\n"
"    min-width: 0px;\n"
" }\n"
"QScrollBar::add-line:horizontal {\n"
"    background:rgb(50, 50, 50);\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"	height:0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
" }\n"
"\n"
"")
        self.tableWidget_3.setAlternatingRowColors(True)
        self.tableWidget_3.setSortingEnabled(True)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(152)
        self.tableWidget_3.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_25.addWidget(self.tableWidget_3)


        self.horizontalLayout_8.addWidget(self.frame_78)


        self.verticalLayout_31.addWidget(self.frame_33)


        self.verticalLayout_33.addWidget(self.frame_31)

        self.stackedWidget.addWidget(self.page_veiculos)
        self.page_produtos = QWidget()
        self.page_produtos.setObjectName(u"page_produtos")
        self.page_produtos.setMinimumSize(QSize(0, 45))
        self.page_produtos.setStyleSheet(u"border:0")
        self.verticalLayout_115 = QVBoxLayout(self.page_produtos)
        self.verticalLayout_115.setSpacing(0)
        self.verticalLayout_115.setObjectName(u"verticalLayout_115")
        self.verticalLayout_115.setContentsMargins(0, 0, 0, 0)
        self.frame_28 = QFrame(self.page_produtos)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFont(font2)
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_28)
        self.verticalLayout_30.setSpacing(7)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frame_103 = QFrame(self.frame_28)
        self.frame_103.setObjectName(u"frame_103")
        self.frame_103.setMinimumSize(QSize(0, 37))
        self.frame_103.setMaximumSize(QSize(16777215, 37))
        self.frame_103.setFont(font2)
        self.frame_103.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(43, 43, 43);")
        self.frame_103.setFrameShape(QFrame.NoFrame)
        self.frame_103.setFrameShadow(QFrame.Raised)
        self.verticalLayout_103 = QVBoxLayout(self.frame_103)
        self.verticalLayout_103.setSpacing(0)
        self.verticalLayout_103.setObjectName(u"verticalLayout_103")
        self.verticalLayout_103.setContentsMargins(0, 0, 0, 0)
        self.aba_relatorio_button_12 = QPushButton(self.frame_103)
        self.aba_relatorio_button_12.setObjectName(u"aba_relatorio_button_12")
        self.aba_relatorio_button_12.setMinimumSize(QSize(160, 37))
        self.aba_relatorio_button_12.setMaximumSize(QSize(5555, 37))
        self.aba_relatorio_button_12.setBaseSize(QSize(555, 2))
        self.aba_relatorio_button_12.setFont(font10)
        self.aba_relatorio_button_12.setLayoutDirection(Qt.LeftToRight)
        self.aba_relatorio_button_12.setStyleSheet(u"QPushButton{\n"
"	border:0;\n"
"}")
        self.aba_relatorio_button_12.setIcon(icon2)
        self.aba_relatorio_button_12.setIconSize(QSize(30, 30))
        self.aba_relatorio_button_12.setFlat(False)

        self.verticalLayout_103.addWidget(self.aba_relatorio_button_12, 0, Qt.AlignTop)


        self.verticalLayout_30.addWidget(self.frame_103)

        self.frame_104 = QFrame(self.frame_28)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setMaximumSize(QSize(1677777, 16777215))
        self.frame_104.setFont(font2)
        self.frame_104.setFrameShape(QFrame.NoFrame)
        self.frame_104.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_104)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_105 = QFrame(self.frame_104)
        self.frame_105.setObjectName(u"frame_105")
        self.frame_105.setMinimumSize(QSize(0, 0))
        self.frame_105.setMaximumSize(QSize(300, 16777215))
        self.frame_105.setFont(font2)
        self.frame_105.setFrameShape(QFrame.Panel)
        self.frame_105.setFrameShadow(QFrame.Raised)
        self.verticalLayout_104 = QVBoxLayout(self.frame_105)
        self.verticalLayout_104.setObjectName(u"verticalLayout_104")
        self.frame_106 = QFrame(self.frame_105)
        self.frame_106.setObjectName(u"frame_106")
        self.frame_106.setMinimumSize(QSize(0, 0))
        self.frame_106.setMaximumSize(QSize(16777215, 30))
        self.frame_106.setFont(font2)
        self.frame_106.setFrameShape(QFrame.StyledPanel)
        self.frame_106.setFrameShadow(QFrame.Raised)
        self.verticalLayout_105 = QVBoxLayout(self.frame_106)
        self.verticalLayout_105.setSpacing(0)
        self.verticalLayout_105.setObjectName(u"verticalLayout_105")
        self.verticalLayout_105.setContentsMargins(0, 0, 0, 0)
        self.label_35 = QLabel(self.frame_106)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font5)

        self.verticalLayout_105.addWidget(self.label_35, 0, Qt.AlignHCenter)


        self.verticalLayout_104.addWidget(self.frame_106)

        self.frame_107 = QFrame(self.frame_105)
        self.frame_107.setObjectName(u"frame_107")
        self.frame_107.setFont(font2)
        self.frame_107.setFrameShape(QFrame.StyledPanel)
        self.frame_107.setFrameShadow(QFrame.Raised)
        self.verticalLayout_106 = QVBoxLayout(self.frame_107)
        self.verticalLayout_106.setObjectName(u"verticalLayout_106")
        self.frame_108 = QFrame(self.frame_107)
        self.frame_108.setObjectName(u"frame_108")
        self.frame_108.setFont(font2)
        self.frame_108.setFrameShape(QFrame.StyledPanel)
        self.frame_108.setFrameShadow(QFrame.Raised)
        self.verticalLayout_107 = QVBoxLayout(self.frame_108)
        self.verticalLayout_107.setSpacing(0)
        self.verticalLayout_107.setObjectName(u"verticalLayout_107")
        self.verticalLayout_107.setContentsMargins(0, 0, 0, 0)
        self.input_produtos_nome = QLineEdit(self.frame_108)
        self.input_produtos_nome.setObjectName(u"input_produtos_nome")
        self.input_produtos_nome.setFont(font9)
        self.input_produtos_nome.setMouseTracking(False)
        self.input_produtos_nome.setAcceptDrops(False)
        self.input_produtos_nome.setStyleSheet(u"QLineEdit{padding:3px;border:1px solid;background-color: rgb(243, 243, 243);}\n"
"\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")
        self.input_produtos_nome.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_107.addWidget(self.input_produtos_nome)


        self.verticalLayout_106.addWidget(self.frame_108)

        self.frame_109 = QFrame(self.frame_107)
        self.frame_109.setObjectName(u"frame_109")
        self.frame_109.setFont(font2)
        self.frame_109.setFrameShape(QFrame.NoFrame)
        self.frame_109.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_109)
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, -1, 0, 0)
        self.input_produtos_estoqueKG = QLineEdit(self.frame_109)
        self.input_produtos_estoqueKG.setObjectName(u"input_produtos_estoqueKG")
        self.input_produtos_estoqueKG.setFont(font9)
        self.input_produtos_estoqueKG.setMouseTracking(False)
        self.input_produtos_estoqueKG.setAcceptDrops(False)
        self.input_produtos_estoqueKG.setStyleSheet(u"QLineEdit{padding:3px;border:1px solid;background-color: rgb(243, 243, 243);}\n"
"\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")
        self.input_produtos_estoqueKG.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_12.addWidget(self.input_produtos_estoqueKG)

        self.label_38 = QLabel(self.frame_109)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font5)
        self.label_38.setStyleSheet(u"color: rgb(15, 202, 2);")

        self.horizontalLayout_12.addWidget(self.label_38)


        self.verticalLayout_106.addWidget(self.frame_109)

        self.frame_111 = QFrame(self.frame_107)
        self.frame_111.setObjectName(u"frame_111")
        self.frame_111.setFont(font2)
        self.frame_111.setFrameShape(QFrame.NoFrame)
        self.frame_111.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_111)
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.input_produtos_densidade = QLineEdit(self.frame_111)
        self.input_produtos_densidade.setObjectName(u"input_produtos_densidade")
        self.input_produtos_densidade.setFont(font9)
        self.input_produtos_densidade.setMouseTracking(False)
        self.input_produtos_densidade.setAcceptDrops(False)
        self.input_produtos_densidade.setStyleSheet(u"QLineEdit{padding:3px;border:1px solid;background-color: rgb(243, 243, 243);}\n"
"\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")
        self.input_produtos_densidade.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_13.addWidget(self.input_produtos_densidade)

        self.label_39 = QLabel(self.frame_111)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font5)
        self.label_39.setStyleSheet(u"color: rgb(15, 202, 2);")

        self.horizontalLayout_13.addWidget(self.label_39)


        self.verticalLayout_106.addWidget(self.frame_111)

        self.frame_112 = QFrame(self.frame_107)
        self.frame_112.setObjectName(u"frame_112")
        self.frame_112.setFont(font2)
        self.frame_112.setFrameShape(QFrame.NoFrame)
        self.frame_112.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_112)
        self.horizontalLayout_14.setSpacing(5)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.input_produtos_embalagemKG = QLineEdit(self.frame_112)
        self.input_produtos_embalagemKG.setObjectName(u"input_produtos_embalagemKG")
        self.input_produtos_embalagemKG.setFont(font9)
        self.input_produtos_embalagemKG.setMouseTracking(False)
        self.input_produtos_embalagemKG.setAcceptDrops(False)
        self.input_produtos_embalagemKG.setStyleSheet(u"QLineEdit{padding:3px;border:1px solid;background-color: rgb(243, 243, 243);}\n"
"\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")
        self.input_produtos_embalagemKG.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_14.addWidget(self.input_produtos_embalagemKG)

        self.label_40 = QLabel(self.frame_112)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font5)
        self.label_40.setStyleSheet(u"color: rgb(15, 202, 2);")

        self.horizontalLayout_14.addWidget(self.label_40)


        self.verticalLayout_106.addWidget(self.frame_112)

        self.frame_8 = QFrame(self.frame_107)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_38.setSpacing(5)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.input_produtos_desconto = QLineEdit(self.frame_8)
        self.input_produtos_desconto.setObjectName(u"input_produtos_desconto")
        self.input_produtos_desconto.setFont(font9)
        self.input_produtos_desconto.setMouseTracking(False)
        self.input_produtos_desconto.setAcceptDrops(False)
        self.input_produtos_desconto.setStyleSheet(u"QLineEdit{padding:3px;border:1px solid;background-color: rgb(243, 243, 243);}\n"
"\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")
        self.input_produtos_desconto.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_38.addWidget(self.input_produtos_desconto)

        self.label_42 = QLabel(self.frame_8)
        self.label_42.setObjectName(u"label_42")
        font18 = QFont()
        font18.setFamily(u"Segoe UI")
        font18.setPointSize(14)
        font18.setBold(True)
        font18.setWeight(75)
        self.label_42.setFont(font18)
        self.label_42.setStyleSheet(u"color: rgb(15, 202, 2);")

        self.horizontalLayout_38.addWidget(self.label_42)


        self.verticalLayout_106.addWidget(self.frame_8)

        self.btn_registrar_produtos = QPushButton(self.frame_107)
        self.btn_registrar_produtos.setObjectName(u"btn_registrar_produtos")
        self.btn_registrar_produtos.setFont(font7)
        self.btn_registrar_produtos.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_registrar_produtos.setMouseTracking(False)
        self.btn_registrar_produtos.setAcceptDrops(False)
        self.btn_registrar_produtos.setStyleSheet(u"QPushButton{\n"
"	border:1px solid rgb(15, 202, 2);\n"
"	padding:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(122, 229, 105);\n"
"}")

        self.verticalLayout_106.addWidget(self.btn_registrar_produtos)


        self.verticalLayout_104.addWidget(self.frame_107)


        self.horizontalLayout_11.addWidget(self.frame_105)

        self.btn_menu_registrar_produtos = QPushButton(self.frame_104)
        self.btn_menu_registrar_produtos.setObjectName(u"btn_menu_registrar_produtos")
        self.btn_menu_registrar_produtos.setMinimumSize(QSize(0, 485))
        self.btn_menu_registrar_produtos.setMaximumSize(QSize(30, 16777215))
        self.btn_menu_registrar_produtos.setFont(font2)
        self.btn_menu_registrar_produtos.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu_registrar_produtos.setStyleSheet(u"border-radius:2px;\n"
"background-color: rgb(43, 43, 43);")
        self.btn_menu_registrar_produtos.setIcon(icon13)

        self.horizontalLayout_11.addWidget(self.btn_menu_registrar_produtos)

        self.frame_115 = QFrame(self.frame_104)
        self.frame_115.setObjectName(u"frame_115")
        self.frame_115.setFont(font2)
        self.frame_115.setFrameShape(QFrame.StyledPanel)
        self.frame_115.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_115)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.widget_6 = QWidget(self.frame_115)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(0, 60))
        self.widget_6.setFont(font2)
        self.gridLayout_15 = QGridLayout(self.widget_6)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_36 = QLabel(self.widget_6)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMaximumSize(QSize(30, 30))
        self.label_36.setFont(font2)
        self.label_36.setPixmap(QPixmap(u":/icons/clock-rotate-left-solid.svg"))
        self.label_36.setScaledContents(True)

        self.gridLayout_15.addWidget(self.label_36, 0, 0, 1, 1)

        self.label_37 = QLabel(self.widget_6)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font16)

        self.gridLayout_15.addWidget(self.label_37, 0, 1, 1, 1)


        self.verticalLayout_13.addWidget(self.widget_6, 0, Qt.AlignHCenter)

        self.btn_remover_produtos = QPushButton(self.frame_115)
        self.btn_remover_produtos.setObjectName(u"btn_remover_produtos")
        self.btn_remover_produtos.setMaximumSize(QSize(270, 16777215))
        self.btn_remover_produtos.setFont(font7)
        self.btn_remover_produtos.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_remover_produtos.setStyleSheet(u"\n"
"QPushButton{\n"
"border: 1px solid rgb(255, 33, 33);\n"
"padding:5px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color:rgb(255, 33, 33)\n"
"}")
        self.btn_remover_produtos.setIcon(icon12)
        self.btn_remover_produtos.setIconSize(QSize(25, 22))

        self.verticalLayout_13.addWidget(self.btn_remover_produtos)

        self.tableWidget = QTableWidget(self.frame_115)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem51 = QTableWidgetItem()
        __qtablewidgetitem51.setFont(font14);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem56)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QTableWidget{\n"
"	font: 10pt \"Century Gothic\";\n"
"	outline:0;\n"
"}\n"
"QHeaderView::section {\n"
"	color:white;\n"
"	border:1px solid white;\n"
"	background-color: rgb(43, 43, 43);\n"
"padding:0px 8px;\n"
"	font: -50 10pt \"Dubai\";\n"
"}\n"
"\n"
"QTableView::item:focus{\n"
"    border: 1px solid ;\n"
"	color:rgb(67, 202, 0)\n"
"}\n"
"QScrollBar:vertical {\n"
"    border: 1px solid #999999;\n"
"    background:white;\n"
"    width:15px;    \n"
"    margin: 1px\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(43, 43, 43);\n"
"    min-height: 0px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    background:rgb(50, 50, 50);\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"	height:0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}"
                        "\n"
"\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: 1px solid #999999;\n"
"    background:white;\n"
"    height:15px;    \n"
"    margin: 1px\n"
" }\n"
"\n"
" QScrollBar::handle:horizontal {\n"
"    background: rgb(43, 43, 43);\n"
"    min-width: 0px;\n"
" }\n"
"QScrollBar::add-line:horizontal {\n"
"    background:rgb(50, 50, 50);\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"	height:0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
" }\n"
"\n"
"")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_13.addWidget(self.tableWidget)


        self.horizontalLayout_11.addWidget(self.frame_115)


        self.verticalLayout_30.addWidget(self.frame_104)


        self.verticalLayout_115.addWidget(self.frame_28)

        self.stackedWidget.addWidget(self.page_produtos)
        self.page_avulsas = QWidget()
        self.page_avulsas.setObjectName(u"page_avulsas")
        self.page_avulsas.setStyleSheet(u"border:0")
        self.verticalLayout_39 = QVBoxLayout(self.page_avulsas)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.frame_37 = QFrame(self.page_avulsas)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFont(font2)
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_37)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.frame_38 = QFrame(self.frame_37)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMinimumSize(QSize(0, 37))
        self.frame_38.setMaximumSize(QSize(16777215, 37))
        self.frame_38.setFont(font2)
        self.frame_38.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(43, 43, 43);")
        self.frame_38.setFrameShape(QFrame.NoFrame)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_38)
        self.verticalLayout_38.setSpacing(7)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.aba_relatorio_button_8 = QPushButton(self.frame_38)
        self.aba_relatorio_button_8.setObjectName(u"aba_relatorio_button_8")
        self.aba_relatorio_button_8.setMinimumSize(QSize(160, 37))
        self.aba_relatorio_button_8.setMaximumSize(QSize(5555, 37))
        self.aba_relatorio_button_8.setBaseSize(QSize(555, 2))
        self.aba_relatorio_button_8.setFont(font10)
        self.aba_relatorio_button_8.setLayoutDirection(Qt.LeftToRight)
        self.aba_relatorio_button_8.setStyleSheet(u"QPushButton{\n"
"	border:0;\n"
"}")
        self.aba_relatorio_button_8.setIcon(icon1)
        self.aba_relatorio_button_8.setIconSize(QSize(30, 30))
        self.aba_relatorio_button_8.setFlat(False)

        self.verticalLayout_38.addWidget(self.aba_relatorio_button_8, 0, Qt.AlignTop)


        self.verticalLayout_37.addWidget(self.frame_38)

        self.frame_39 = QFrame(self.frame_37)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFont(font2)
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_83 = QVBoxLayout(self.frame_39)
        self.verticalLayout_83.setSpacing(0)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.verticalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.frame_40 = QFrame(self.frame_39)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFont(font2)
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_40)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.frame_79 = QFrame(self.frame_40)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setMinimumSize(QSize(210, 0))
        self.frame_79.setMaximumSize(QSize(16777215, 210))
        self.frame_79.setFont(font2)
        self.frame_79.setStyleSheet(u"")
        self.frame_79.setFrameShape(QFrame.NoFrame)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.verticalLayout_74 = QVBoxLayout(self.frame_79)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.frame_86 = QFrame(self.frame_79)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setFont(font2)
        self.frame_86.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.verticalLayout_76 = QVBoxLayout(self.frame_86)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.label_33 = QLabel(self.frame_86)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMaximumSize(QSize(16777215, 20))
        self.label_33.setFont(font10)
        self.label_33.setStyleSheet(u"")
        self.label_33.setAlignment(Qt.AlignCenter)

        self.verticalLayout_76.addWidget(self.label_33)

        self.frame_87 = QFrame(self.frame_86)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setFont(font2)
        self.frame_87.setStyleSheet(u"background-color: rgb(231, 231, 231);\\n")
        self.frame_87.setFrameShape(QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_87)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.lcdNumber_2 = QLCDNumber(self.frame_87)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        self.lcdNumber_2.setMinimumSize(QSize(0, 100))
        self.lcdNumber_2.setMaximumSize(QSize(16777215, 19999))
        font19 = QFont()
        font19.setFamily(u"Segoe UI")
        font19.setPointSize(4)
        self.lcdNumber_2.setFont(font19)
        self.lcdNumber_2.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_2.setSmallDecimalPoint(True)
        self.lcdNumber_2.setDigitCount(13)
        self.lcdNumber_2.setMode(QLCDNumber.Dec)
        self.lcdNumber_2.setSegmentStyle(QLCDNumber.Filled)
        self.lcdNumber_2.setProperty("value", 0.000000000000000)
        self.lcdNumber_2.setProperty("intValue", 0)

        self.horizontalLayout_22.addWidget(self.lcdNumber_2)

        self.label_50 = QLabel(self.frame_87)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMaximumSize(QSize(50, 50))
        font20 = QFont()
        font20.setFamily(u"Segoe UI")
        font20.setPointSize(26)
        font20.setBold(True)
        font20.setWeight(75)
        self.label_50.setFont(font20)

        self.horizontalLayout_22.addWidget(self.label_50)


        self.verticalLayout_76.addWidget(self.frame_87)


        self.verticalLayout_74.addWidget(self.frame_86)


        self.verticalLayout_42.addWidget(self.frame_79)

        self.frame_88 = QFrame(self.frame_40)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setFont(font2)
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Raised)
        self.verticalLayout_77 = QVBoxLayout(self.frame_88)
        self.verticalLayout_77.setSpacing(0)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.verticalLayout_77.setContentsMargins(-1, 0, -1, 0)
        self.frame_dados_avulsa_2 = QFrame(self.frame_88)
        self.frame_dados_avulsa_2.setObjectName(u"frame_dados_avulsa_2")
        self.frame_dados_avulsa_2.setMinimumSize(QSize(0, 0))
        self.frame_dados_avulsa_2.setMaximumSize(QSize(16777215, 265))
        self.frame_dados_avulsa_2.setFont(font2)
        self.frame_dados_avulsa_2.setFrameShape(QFrame.StyledPanel)
        self.frame_dados_avulsa_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_79 = QVBoxLayout(self.frame_dados_avulsa_2)
        self.verticalLayout_79.setSpacing(0)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.verticalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.frame_93 = QFrame(self.frame_dados_avulsa_2)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setMaximumSize(QSize(16777215, 42))
        self.frame_93.setFont(font2)
        self.frame_93.setFrameShape(QFrame.NoFrame)
        self.frame_93.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_93)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.btn_peso_manualmente_2 = QRadioButton(self.frame_93)
        self.btn_peso_manualmente_2.setObjectName(u"btn_peso_manualmente_2")
        self.btn_peso_manualmente_2.setFont(font9)
        self.btn_peso_manualmente_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_peso_manualmente_2.setStyleSheet(u"\n"
"QRadioButton::indicator {\n"
"    width:                  22px;\n"
"    height:                 22px;\n"
"    border-radius:          11px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"	image: url(:/icons/check-solid.svg);\n"
"	background-color: rgb(6, 180, 20);\n"
"    border:                 1px solid rgb(88, 88, 88);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    border:                 1px solid rgb(88, 88, 88);\n"
"}")

        self.horizontalLayout_25.addWidget(self.btn_peso_manualmente_2, 0, Qt.AlignHCenter)

        self.peso_manualmente_2 = QLineEdit(self.frame_93)
        self.peso_manualmente_2.setObjectName(u"peso_manualmente_2")
        self.peso_manualmente_2.setMinimumSize(QSize(0, 30))
        self.peso_manualmente_2.setMaximumSize(QSize(0, 16777215))
        self.peso_manualmente_2.setFont(font17)
        self.peso_manualmente_2.setStyleSheet(u"QLineEdit{\n"
"	padding-left:10px;\n"
"	font-size:13px;\n"
"	border:1px solid;\n"
"	font: 11pt \"Century Gothic\";\n"
"	background-color: rgb(250, 252, 250);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:1px solid rgb(15, 202, 2);\n"
"\n"
"}")
        self.peso_manualmente_2.setMaxLength(8)

        self.horizontalLayout_25.addWidget(self.peso_manualmente_2, 0, Qt.AlignHCenter)


        self.verticalLayout_79.addWidget(self.frame_93, 0, Qt.AlignHCenter)

        self.label_67 = QLabel(self.frame_dados_avulsa_2)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setFont(font16)
        self.label_67.setAlignment(Qt.AlignCenter)

        self.verticalLayout_79.addWidget(self.label_67)

        self.frame_89 = QFrame(self.frame_dados_avulsa_2)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setMinimumSize(QSize(0, 0))
        self.frame_89.setFont(font2)
        self.frame_89.setFrameShape(QFrame.NoFrame)
        self.frame_89.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_89)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setHorizontalSpacing(15)
        self.gridLayout_14.setVerticalSpacing(6)
        self.gridLayout_14.setContentsMargins(-1, 0, -1, -1)
        self.input_avulsas_motorista = QLineEdit(self.frame_89)
        self.input_avulsas_motorista.setObjectName(u"input_avulsas_motorista")
        self.input_avulsas_motorista.setMinimumSize(QSize(0, 30))
        self.input_avulsas_motorista.setMaximumSize(QSize(200, 16777215))
        font21 = QFont()
        self.input_avulsas_motorista.setFont(font21)
        self.input_avulsas_motorista.setStyleSheet(u"QLineEdit{\n"
"	padding-left:10px;\n"
"	font-size:15px;\n"
"	border:1px solid;\n"
"	background-color: rgb(250, 252, 250);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:1px solid rgb(15, 202, 2);\n"
"\n"
"}")

        self.gridLayout_14.addWidget(self.input_avulsas_motorista, 3, 0, 1, 1)

        self.label_55 = QLabel(self.frame_89)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMinimumSize(QSize(0, 19))
        self.label_55.setMaximumSize(QSize(16777215, 13))
        self.label_55.setFont(font5)

        self.gridLayout_14.addWidget(self.label_55, 1, 1, 1, 1)

        self.label_54 = QLabel(self.frame_89)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMinimumSize(QSize(0, 19))
        self.label_54.setMaximumSize(QSize(16777215, 13))
        self.label_54.setFont(font5)

        self.gridLayout_14.addWidget(self.label_54, 0, 0, 2, 1)

        self.comboBox_avulsas_veiculo = QComboBox(self.frame_89)
        self.comboBox_avulsas_veiculo.addItem("")
        self.comboBox_avulsas_veiculo.setObjectName(u"comboBox_avulsas_veiculo")
        self.comboBox_avulsas_veiculo.setMinimumSize(QSize(0, 30))
        self.comboBox_avulsas_veiculo.setFont(font21)
        self.comboBox_avulsas_veiculo.setStyleSheet(u"QComboBox{\n"
"	border:1px solid rgb(15, 202, 2);\n"
"	padding-left:10px;\n"
"	font-size:15px;\n"
"	\n"
"	background-color: rgb(250, 252, 250);\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"	border:0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
"	image: url(:/icons/angle-down-solid.svg);\n"
"	width:12px;\n"
"	height:12px;\n"
"	margin-right:15px;\n"
"}\n"
"\n"
"QComboBox::on{\n"
"	border:2px solid rgb(67, 202, 0);\n"
"}\n"
"\n"
"QComboBox QListView{\n"
"	padding:5px;\n"
"	border:1px solid;\n"
"	background-color: rgba(255, 255, 255, 50%);\n"
"	outline:0;\n"
"}\n"
"")
        self.comboBox_avulsas_veiculo.setMaxVisibleItems(10)
        self.comboBox_avulsas_veiculo.setInsertPolicy(QComboBox.NoInsert)
        self.comboBox_avulsas_veiculo.setIconSize(QSize(32, 32))
        self.comboBox_avulsas_veiculo.setDuplicatesEnabled(True)
        self.comboBox_avulsas_veiculo.setFrame(True)

        self.gridLayout_14.addWidget(self.comboBox_avulsas_veiculo, 3, 1, 1, 1)

        self.label_51 = QLabel(self.frame_89)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMinimumSize(QSize(0, 19))
        self.label_51.setMaximumSize(QSize(16777215, 13))
        self.label_51.setFont(font5)

        self.gridLayout_14.addWidget(self.label_51, 1, 2, 1, 1)

        self.comboBox_avulsas_cliente = QComboBox(self.frame_89)
        self.comboBox_avulsas_cliente.addItem("")
        self.comboBox_avulsas_cliente.setObjectName(u"comboBox_avulsas_cliente")
        self.comboBox_avulsas_cliente.setMinimumSize(QSize(0, 30))
        self.comboBox_avulsas_cliente.setFont(font21)
        self.comboBox_avulsas_cliente.setStyleSheet(u"QComboBox{\n"
"	border:1px solid rgb(15, 202, 2);\n"
"	padding-left:10px;\n"
"	font-size:15px;\n"
"	\n"
"	background-color: rgb(250, 252, 250);\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"	border:0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
"	image: url(:/icons/angle-down-solid.svg);\n"
"	width:12px;\n"
"	height:12px;\n"
"	margin-right:15px;\n"
"}\n"
"\n"
"QComboBox::on{\n"
"	border:2px solid rgb(67, 202, 0);\n"
"}\n"
"\n"
"QComboBox QListView{\n"
"	padding:5px;\n"
"	border:1px solid;\n"
"	background-color: rgba(255, 255, 255, 50%);\n"
"	outline:0;\n"
"}\n"
"")
        self.comboBox_avulsas_cliente.setMaxVisibleItems(10)
        self.comboBox_avulsas_cliente.setInsertPolicy(QComboBox.NoInsert)
        self.comboBox_avulsas_cliente.setIconSize(QSize(32, 32))
        self.comboBox_avulsas_cliente.setDuplicatesEnabled(True)
        self.comboBox_avulsas_cliente.setFrame(True)

        self.gridLayout_14.addWidget(self.comboBox_avulsas_cliente, 3, 2, 1, 1)

        self.comboBox_avulsas_carga = QComboBox(self.frame_89)
        self.comboBox_avulsas_carga.addItem("")
        self.comboBox_avulsas_carga.setObjectName(u"comboBox_avulsas_carga")
        self.comboBox_avulsas_carga.setMinimumSize(QSize(0, 30))
        self.comboBox_avulsas_carga.setFont(font21)
        self.comboBox_avulsas_carga.setStyleSheet(u"QComboBox{\n"
"	border:1px solid rgb(15, 202, 2);\n"
"	padding-left:10px;\n"
"	font-size:15px;\n"
"	\n"
"	background-color: rgb(250, 252, 250);\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"	border:0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
"	image: url(:/icons/angle-down-solid.svg);\n"
"	width:12px;\n"
"	height:12px;\n"
"	margin-right:15px;\n"
"}\n"
"\n"
"QComboBox::on{\n"
"	border:2px solid rgb(67, 202, 0);\n"
"}\n"
"\n"
"QComboBox QListView{\n"
"	padding:5px;\n"
"	border:1px solid;\n"
"	background-color: rgba(255, 255, 255, 50%);\n"
"	outline:0;\n"
"}\n"
"")
        self.comboBox_avulsas_carga.setMaxVisibleItems(10)
        self.comboBox_avulsas_carga.setInsertPolicy(QComboBox.NoInsert)
        self.comboBox_avulsas_carga.setIconSize(QSize(32, 32))
        self.comboBox_avulsas_carga.setDuplicatesEnabled(True)
        self.comboBox_avulsas_carga.setFrame(True)

        self.gridLayout_14.addWidget(self.comboBox_avulsas_carga, 3, 3, 1, 1)

        self.label_52 = QLabel(self.frame_89)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMinimumSize(QSize(0, 19))
        self.label_52.setMaximumSize(QSize(16777215, 13))
        self.label_52.setFont(font5)

        self.gridLayout_14.addWidget(self.label_52, 1, 3, 1, 1, Qt.AlignTop)


        self.verticalLayout_79.addWidget(self.frame_89, 0, Qt.AlignTop)

        self.frame_90 = QFrame(self.frame_dados_avulsa_2)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setMaximumSize(QSize(16777215, 35))
        self.frame_90.setFont(font2)
        self.frame_90.setFrameShape(QFrame.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_90)
        self.horizontalLayout_23.setSpacing(10)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_91 = QFrame(self.frame_90)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setFont(font2)
        self.frame_91.setFrameShape(QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Raised)
        self.verticalLayout_80 = QVBoxLayout(self.frame_91)
        self.verticalLayout_80.setSpacing(0)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.verticalLayout_80.setContentsMargins(0, 0, 60, 0)

        self.horizontalLayout_23.addWidget(self.frame_91, 0, Qt.AlignHCenter)


        self.verticalLayout_79.addWidget(self.frame_90, 0, Qt.AlignHCenter)

        self.frame_120 = QFrame(self.frame_dados_avulsa_2)
        self.frame_120.setObjectName(u"frame_120")
        self.frame_120.setFont(font2)
        self.frame_120.setFrameShape(QFrame.StyledPanel)
        self.frame_120.setFrameShadow(QFrame.Raised)
        self.verticalLayout_95 = QVBoxLayout(self.frame_120)
        self.verticalLayout_95.setSpacing(0)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.verticalLayout_95.setContentsMargins(-1, 5, -1, 0)
        self.input_avulsas_obs = QLineEdit(self.frame_120)
        self.input_avulsas_obs.setObjectName(u"input_avulsas_obs")
        self.input_avulsas_obs.setMinimumSize(QSize(400, 30))
        self.input_avulsas_obs.setMaximumSize(QSize(16777215, 16777215))
        self.input_avulsas_obs.setFont(font21)
        self.input_avulsas_obs.setStyleSheet(u"QLineEdit{\n"
"	padding-left:10px;\n"
"	font-size:15px;\n"
"	border:1px solid;\n"
"	background-color: rgb(250, 252, 250);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:1px solid rgb(15, 202, 2);\n"
"\n"
"}")

        self.verticalLayout_95.addWidget(self.input_avulsas_obs)


        self.verticalLayout_79.addWidget(self.frame_120)

        self.frame_92 = QFrame(self.frame_dados_avulsa_2)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setFont(font2)
        self.frame_92.setFrameShape(QFrame.NoFrame)
        self.frame_92.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_92)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(-1, 20, -1, -1)
        self.btn_fazer_pesagem_avulsa = QPushButton(self.frame_92)
        self.btn_fazer_pesagem_avulsa.setObjectName(u"btn_fazer_pesagem_avulsa")
        self.btn_fazer_pesagem_avulsa.setMinimumSize(QSize(219, 50))
        self.btn_fazer_pesagem_avulsa.setMaximumSize(QSize(250, 16777215))
        self.btn_fazer_pesagem_avulsa.setFont(font5)
        self.btn_fazer_pesagem_avulsa.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_fazer_pesagem_avulsa.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"background-color: rgb(6, 180, 20);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(5, 161, 15);\n"
"}\n"
"")

        self.horizontalLayout_24.addWidget(self.btn_fazer_pesagem_avulsa)

        self.radioButton_2 = QRadioButton(self.frame_92)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setFont(font9)
        self.radioButton_2.setStyleSheet(u"\n"
"QRadioButton::indicator {\n"
"    width:                  12px;\n"
"    height:                 12px;\n"
"    border-radius:          6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"	image: url(:/icons/check-solid.svg);\n"
"	background-color: rgb(6, 180, 20);\n"
"    border:                 1px solid rgb(88, 88, 88);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    border:                 1px solid rgb(88, 88, 88);\n"
"}")

        self.horizontalLayout_24.addWidget(self.radioButton_2)


        self.verticalLayout_79.addWidget(self.frame_92, 0, Qt.AlignHCenter)


        self.verticalLayout_77.addWidget(self.frame_dados_avulsa_2)

        self.frame_94 = QFrame(self.frame_88)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setFont(font2)
        self.frame_94.setFrameShape(QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Raised)
        self.verticalLayout_81 = QVBoxLayout(self.frame_94)
        self.verticalLayout_81.setSpacing(0)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.verticalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.label_34 = QLabel(self.frame_94)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(0, 26))
        self.label_34.setMaximumSize(QSize(16777215, 26))
        self.label_34.setFont(font7)
        self.label_34.setStyleSheet(u"color: rgb(109, 109, 109);background-color: rgb(43, 43, 43);")
        self.label_34.setAlignment(Qt.AlignCenter)

        self.verticalLayout_81.addWidget(self.label_34)

        self.frame_obs = QFrame(self.frame_94)
        self.frame_obs.setObjectName(u"frame_obs")
        self.frame_obs.setMinimumSize(QSize(0, 0))
        self.frame_obs.setMaximumSize(QSize(16777215, 0))
        self.frame_obs.setFont(font2)
        self.frame_obs.setStyleSheet(u"background-color: rgb(43, 43, 43);")
        self.frame_obs.setFrameShape(QFrame.StyledPanel)
        self.frame_obs.setFrameShadow(QFrame.Raised)
        self.verticalLayout_82 = QVBoxLayout(self.frame_obs)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.frame_42 = QFrame(self.frame_obs)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFont(font2)
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_56 = QLabel(self.frame_42)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMaximumSize(QSize(32, 32))
        self.label_56.setFont(font2)
        self.label_56.setPixmap(QPixmap(u":/icons/clock-rotate-left-solid.svg"))
        self.label_56.setScaledContents(True)

        self.horizontalLayout_26.addWidget(self.label_56, 0, Qt.AlignRight)

        self.label_57 = QLabel(self.frame_42)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMinimumSize(QSize(0, 30))
        self.label_57.setMaximumSize(QSize(16777215, 30))
        self.label_57.setFont(font10)
        self.label_57.setStyleSheet(u"	color:white;\n"
"")
        self.label_57.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.label_57)


        self.verticalLayout_82.addWidget(self.frame_42, 0, Qt.AlignHCenter)

        self.tableWidget_6 = QTableWidget(self.frame_obs)
        if (self.tableWidget_6.columnCount() < 3):
            self.tableWidget_6.setColumnCount(3)
        font22 = QFont()
        font22.setBold(True)
        font22.setWeight(75)
        __qtablewidgetitem57 = QTableWidgetItem()
        __qtablewidgetitem57.setFont(font22);
        self.tableWidget_6.setHorizontalHeaderItem(0, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        __qtablewidgetitem58.setFont(font22);
        self.tableWidget_6.setHorizontalHeaderItem(1, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        __qtablewidgetitem59.setFont(font22);
        self.tableWidget_6.setHorizontalHeaderItem(2, __qtablewidgetitem59)
        self.tableWidget_6.setObjectName(u"tableWidget_6")
        self.tableWidget_6.setMaximumSize(QSize(16777215, 1999999))
        font23 = QFont()
        font23.setFamily(u"Century Gothic")
        font23.setPointSize(10)
        font23.setBold(False)
        font23.setItalic(False)
        font23.setWeight(50)
        self.tableWidget_6.setFont(font23)
        self.tableWidget_6.setStyleSheet(u"QTableWidget{\n"
"	font: 10pt \"Century Gothic\";\n"
"	outline:0;	color:white;\n"
"\n"
"}\n"
"QHeaderView::section {\n"
"	border:1px solid ;\n"
"}\n"
"\n"
"QTableView::item:focus{\n"
"    border: 1px solid ;\n"
"	color:rgb(67, 202, 0)\n"
"}\n"
"QScrollBar:vertical {\n"
"    border: 1px solid #999999;\n"
"    background:white;\n"
"    width:15px;    \n"
"    margin: 1px\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(43, 43, 43);\n"
"    min-height: 0px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    background:rgb(50, 50, 50);\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"	height:0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: 1px solid #999999;\n"
"    background:whit"
                        "e;\n"
"    height:15px;    \n"
"    margin: 1px\n"
" }\n"
"\n"
" QScrollBar::handle:horizontal {\n"
"    background: rgb(43, 43, 43);\n"
"    min-width: 0px;\n"
" }\n"
"QScrollBar::add-line:horizontal {\n"
"    background:rgb(50, 50, 50);\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"	height:0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
" }\n"
"\n"
"")
        self.tableWidget_6.setFrameShape(QFrame.NoFrame)
        self.tableWidget_6.setAutoScroll(True)
        self.tableWidget_6.setAutoScrollMargin(20)
        self.tableWidget_6.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_6.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.tableWidget_6.setDefaultDropAction(Qt.IgnoreAction)
        self.tableWidget_6.setAlternatingRowColors(False)
        self.tableWidget_6.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_6.setTextElideMode(Qt.ElideRight)
        self.tableWidget_6.setSortingEnabled(True)
        self.tableWidget_6.setRowCount(0)
        self.tableWidget_6.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_6.horizontalHeader().setMinimumSectionSize(95)
        self.tableWidget_6.horizontalHeader().setDefaultSectionSize(115)
        self.tableWidget_6.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_6.verticalHeader().setVisible(False)

        self.verticalLayout_82.addWidget(self.tableWidget_6)


        self.verticalLayout_81.addWidget(self.frame_obs)


        self.verticalLayout_77.addWidget(self.frame_94, 0, Qt.AlignBottom)


        self.verticalLayout_42.addWidget(self.frame_88)


        self.verticalLayout_83.addWidget(self.frame_40)


        self.verticalLayout_37.addWidget(self.frame_39)


        self.verticalLayout_39.addWidget(self.frame_37)

        self.stackedWidget.addWidget(self.page_avulsas)
        self.page_entrada = QWidget()
        self.page_entrada.setObjectName(u"page_entrada")
        self.page_entrada.setStyleSheet(u"border:0")
        self.verticalLayout_36 = QVBoxLayout(self.page_entrada)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.frame_34 = QFrame(self.page_entrada)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFont(font2)
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_34)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.frame_35 = QFrame(self.frame_34)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMinimumSize(QSize(0, 36))
        self.frame_35.setMaximumSize(QSize(16777215, 37))
        self.frame_35.setFont(font2)
        self.frame_35.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(43, 43, 43);")
        self.frame_35.setFrameShape(QFrame.NoFrame)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_35)
        self.verticalLayout_35.setSpacing(7)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.aba_relatorio_button_7 = QPushButton(self.frame_35)
        self.aba_relatorio_button_7.setObjectName(u"aba_relatorio_button_7")
        self.aba_relatorio_button_7.setMinimumSize(QSize(160, 37))
        self.aba_relatorio_button_7.setMaximumSize(QSize(5555, 45))
        self.aba_relatorio_button_7.setBaseSize(QSize(555, 2))
        self.aba_relatorio_button_7.setFont(font10)
        self.aba_relatorio_button_7.setLayoutDirection(Qt.LeftToRight)
        self.aba_relatorio_button_7.setStyleSheet(u"QPushButton{\n"
"	border:0;\n"
"}")
        self.aba_relatorio_button_7.setIcon(icon1)
        self.aba_relatorio_button_7.setIconSize(QSize(30, 30))
        self.aba_relatorio_button_7.setFlat(False)

        self.verticalLayout_35.addWidget(self.aba_relatorio_button_7, 0, Qt.AlignTop)


        self.verticalLayout_34.addWidget(self.frame_35)

        self.frame_36 = QFrame(self.frame_34)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFont(font2)
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_36)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frame_45 = QFrame(self.frame_36)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMinimumSize(QSize(210, 250))
        self.frame_45.setMaximumSize(QSize(16777215, 300))
        self.frame_45.setFont(font2)
        self.frame_45.setStyleSheet(u"")
        self.frame_45.setFrameShape(QFrame.NoFrame)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_45)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.frame_76 = QFrame(self.frame_45)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setFont(font2)
        self.frame_76.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_76)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.frame_116 = QFrame(self.frame_76)
        self.frame_116.setObjectName(u"frame_116")
        self.frame_116.setMaximumSize(QSize(16777215, 25))
        self.frame_116.setFont(font2)
        self.frame_116.setFrameShape(QFrame.StyledPanel)
        self.frame_116.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_116)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_32 = QLabel(self.frame_116)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMaximumSize(QSize(16777215, 20))
        self.label_32.setFont(font10)
        self.label_32.setStyleSheet(u"")
        self.label_32.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.label_32)

        self.label_61 = QLabel(self.frame_116)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMaximumSize(QSize(16777215, 20))
        self.label_61.setFont(font10)
        self.label_61.setStyleSheet(u"color: rgb(6, 180, 20);")
        self.label_61.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.label_61)


        self.verticalLayout_43.addWidget(self.frame_116, 0, Qt.AlignHCenter)

        self.frame_77 = QFrame(self.frame_76)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setMinimumSize(QSize(0, 74))
        self.frame_77.setFont(font2)
        self.frame_77.setStyleSheet(u"background-color: rgb(231, 231, 231);\\n")
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_77)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.lcdNumber = QLCDNumber(self.frame_77)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setMinimumSize(QSize(0, 90))
        self.lcdNumber.setMaximumSize(QSize(16777215, 19999))
        self.lcdNumber.setFont(font19)
        self.lcdNumber.setFrameShape(QFrame.NoFrame)
        self.lcdNumber.setSmallDecimalPoint(True)
        self.lcdNumber.setDigitCount(13)
        self.lcdNumber.setMode(QLCDNumber.Dec)
        self.lcdNumber.setSegmentStyle(QLCDNumber.Filled)
        self.lcdNumber.setProperty("value", 0.000000000000000)
        self.lcdNumber.setProperty("intValue", 0)

        self.horizontalLayout_17.addWidget(self.lcdNumber)

        self.label_31 = QLabel(self.frame_77)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMaximumSize(QSize(50, 50))
        self.label_31.setFont(font20)

        self.horizontalLayout_17.addWidget(self.label_31)


        self.verticalLayout_43.addWidget(self.frame_77)


        self.verticalLayout_29.addWidget(self.frame_76)


        self.verticalLayout_28.addWidget(self.frame_45)

        self.frame_75 = QFrame(self.frame_36)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setFont(font2)
        self.frame_75.setFrameShape(QFrame.NoFrame)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_75)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(-1, 0, -1, 0)
        self.frame_dados_avulsa = QFrame(self.frame_75)
        self.frame_dados_avulsa.setObjectName(u"frame_dados_avulsa")
        self.frame_dados_avulsa.setMinimumSize(QSize(0, 0))
        self.frame_dados_avulsa.setMaximumSize(QSize(16777215, 250))
        self.frame_dados_avulsa.setFont(font2)
        self.frame_dados_avulsa.setFrameShape(QFrame.NoFrame)
        self.frame_dados_avulsa.setFrameShadow(QFrame.Raised)
        self.verticalLayout_69 = QVBoxLayout(self.frame_dados_avulsa)
        self.verticalLayout_69.setSpacing(0)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.label_60 = QLabel(self.frame_dados_avulsa)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMinimumSize(QSize(458, 0))
        self.label_60.setFont(font16)
        self.label_60.setAlignment(Qt.AlignCenter)

        self.verticalLayout_69.addWidget(self.label_60)

        self.frame_80 = QFrame(self.frame_dados_avulsa)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setFont(font2)
        self.frame_80.setFrameShape(QFrame.NoFrame)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_80)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setHorizontalSpacing(15)
        self.gridLayout_13.setVerticalSpacing(6)
        self.gridLayout_13.setContentsMargins(-1, 0, -1, -1)
        self.input_entrada_motorista = QLineEdit(self.frame_80)
        self.input_entrada_motorista.setObjectName(u"input_entrada_motorista")
        self.input_entrada_motorista.setMinimumSize(QSize(0, 30))
        self.input_entrada_motorista.setMaximumSize(QSize(200, 16777215))
        self.input_entrada_motorista.setFont(font21)
        self.input_entrada_motorista.setStyleSheet(u"QLineEdit{\n"
"	padding-left:10px;\n"
"	font-size:15px;\n"
"	border:1px solid;\n"
"	background-color: rgb(250, 252, 250);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:1px solid rgb(15, 202, 2);\n"
"\n"
"}")

        self.gridLayout_13.addWidget(self.input_entrada_motorista, 4, 0, 1, 1)

        self.label_41 = QLabel(self.frame_80)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(0, 18))
        self.label_41.setMaximumSize(QSize(16777215, 13))
        self.label_41.setFont(font5)

        self.gridLayout_13.addWidget(self.label_41, 1, 0, 2, 1)

        self.label_44 = QLabel(self.frame_80)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(0, 18))
        self.label_44.setMaximumSize(QSize(16777215, 13))
        self.label_44.setFont(font5)

        self.gridLayout_13.addWidget(self.label_44, 2, 2, 1, 1)

        self.comboBox_entrada_cliente = QComboBox(self.frame_80)
        self.comboBox_entrada_cliente.addItem("")
        self.comboBox_entrada_cliente.setObjectName(u"comboBox_entrada_cliente")
        self.comboBox_entrada_cliente.setMinimumSize(QSize(0, 30))
        self.comboBox_entrada_cliente.setFont(font21)
        self.comboBox_entrada_cliente.setStyleSheet(u"QComboBox{\n"
"	border:1px solid rgb(15, 202, 2);\n"
"	padding-left:10px;\n"
"	font-size:15px;\n"
"	\n"
"	background-color: rgb(250, 252, 250);\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"	border:0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
"	image: url(:/icons/angle-down-solid.svg);\n"
"	width:12px;\n"
"	height:12px;\n"
"	margin-right:15px;\n"
"}\n"
"\n"
"QComboBox::on{\n"
"	border:2px solid rgb(67, 202, 0);\n"
"}\n"
"\n"
"QComboBox QListView{\n"
"	padding:5px;\n"
"	border:1px solid;\n"
"	background-color: rgba(255, 255, 255, 50%);\n"
"	outline:0;\n"
"}\n"
"")
        self.comboBox_entrada_cliente.setMaxVisibleItems(10)
        self.comboBox_entrada_cliente.setInsertPolicy(QComboBox.NoInsert)
        self.comboBox_entrada_cliente.setIconSize(QSize(32, 32))
        self.comboBox_entrada_cliente.setDuplicatesEnabled(True)
        self.comboBox_entrada_cliente.setFrame(True)

        self.gridLayout_13.addWidget(self.comboBox_entrada_cliente, 4, 2, 1, 1)

        self.label_45 = QLabel(self.frame_80)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMinimumSize(QSize(0, 18))
        self.label_45.setMaximumSize(QSize(16777215, 13))
        self.label_45.setFont(font5)

        self.gridLayout_13.addWidget(self.label_45, 2, 3, 1, 1)

        self.comboBox_entrada_carga = QComboBox(self.frame_80)
        self.comboBox_entrada_carga.addItem("")
        self.comboBox_entrada_carga.setObjectName(u"comboBox_entrada_carga")
        self.comboBox_entrada_carga.setMinimumSize(QSize(0, 30))
        self.comboBox_entrada_carga.setFont(font21)
        self.comboBox_entrada_carga.setStyleSheet(u"QComboBox{\n"
"	border:1px solid rgb(15, 202, 2);\n"
"	padding-left:10px;\n"
"	font-size:15px;\n"
"	\n"
"	background-color: rgb(250, 252, 250);\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"	border:0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
"	image: url(:/icons/angle-down-solid.svg);\n"
"	width:12px;\n"
"	height:12px;\n"
"	margin-right:15px;\n"
"}\n"
"\n"
"QComboBox::on{\n"
"	border:2px solid rgb(67, 202, 0);\n"
"}\n"
"\n"
"QComboBox QListView{\n"
"	padding:5px;\n"
"	border:1px solid;\n"
"	background-color: rgba(255, 255, 255, 50%);\n"
"	outline:0;\n"
"}\n"
"")
        self.comboBox_entrada_carga.setMaxVisibleItems(10)
        self.comboBox_entrada_carga.setInsertPolicy(QComboBox.NoInsert)
        self.comboBox_entrada_carga.setIconSize(QSize(32, 32))
        self.comboBox_entrada_carga.setDuplicatesEnabled(True)
        self.comboBox_entrada_carga.setFrame(True)

        self.gridLayout_13.addWidget(self.comboBox_entrada_carga, 4, 3, 1, 1)

        self.label_47 = QLabel(self.frame_80)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMinimumSize(QSize(0, 18))
        self.label_47.setMaximumSize(QSize(16777215, 13))
        self.label_47.setFont(font5)

        self.gridLayout_13.addWidget(self.label_47, 2, 1, 1, 1)

        self.comboBox_entrada_veiculo = QComboBox(self.frame_80)
        self.comboBox_entrada_veiculo.addItem("")
        self.comboBox_entrada_veiculo.setObjectName(u"comboBox_entrada_veiculo")
        self.comboBox_entrada_veiculo.setMinimumSize(QSize(0, 30))
        self.comboBox_entrada_veiculo.setFont(font21)
        self.comboBox_entrada_veiculo.setStyleSheet(u"QComboBox{\n"
"	border:1px solid rgb(15, 202, 2);\n"
"	padding-left:10px;\n"
"	font-size:15px;\n"
"	\n"
"	background-color: rgb(250, 252, 250);\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"	border:0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
"	image: url(:/icons/angle-down-solid.svg);\n"
"	width:12px;\n"
"	height:12px;\n"
"	margin-right:15px;\n"
"}\n"
"\n"
"QComboBox::on{\n"
"	border:2px solid rgb(67, 202, 0);\n"
"}\n"
"\n"
"QComboBox QListView{\n"
"	padding:5px;\n"
"	border:1px solid;\n"
"	background-color: rgba(255, 255, 255, 50%);\n"
"	outline:0;\n"
"}\n"
"")
        self.comboBox_entrada_veiculo.setMaxVisibleItems(10)
        self.comboBox_entrada_veiculo.setInsertPolicy(QComboBox.NoInsert)
        self.comboBox_entrada_veiculo.setIconSize(QSize(32, 32))
        self.comboBox_entrada_veiculo.setDuplicatesEnabled(True)
        self.comboBox_entrada_veiculo.setFrame(True)

        self.gridLayout_13.addWidget(self.comboBox_entrada_veiculo, 4, 1, 1, 1)


        self.verticalLayout_69.addWidget(self.frame_80)

        self.frame_119 = QFrame(self.frame_dados_avulsa)
        self.frame_119.setObjectName(u"frame_119")
        self.frame_119.setFont(font2)
        self.frame_119.setFrameShape(QFrame.NoFrame)
        self.frame_119.setFrameShadow(QFrame.Raised)
        self.verticalLayout_94 = QVBoxLayout(self.frame_119)
        self.verticalLayout_94.setSpacing(0)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.verticalLayout_94.setContentsMargins(9, 5, 9, 0)
        self.input_entrada_obs = QLineEdit(self.frame_119)
        self.input_entrada_obs.setObjectName(u"input_entrada_obs")
        self.input_entrada_obs.setMinimumSize(QSize(400, 30))
        self.input_entrada_obs.setMaximumSize(QSize(16777215, 16777215))
        self.input_entrada_obs.setFont(font21)
        self.input_entrada_obs.setStyleSheet(u"QLineEdit{\n"
"	padding-left:10px;\n"
"	font-size:15px;\n"
"	border:1px solid;\n"
"	background-color: rgb(250, 252, 250);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:1px solid rgb(15, 202, 2);\n"
"\n"
"}")

        self.verticalLayout_94.addWidget(self.input_entrada_obs)


        self.verticalLayout_69.addWidget(self.frame_119)

        self.frame_83 = QFrame(self.frame_dados_avulsa)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setMaximumSize(QSize(16777215, 35))
        self.frame_83.setFont(font2)
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_83)
        self.horizontalLayout_18.setSpacing(10)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_69.addWidget(self.frame_83, 0, Qt.AlignHCenter)

        self.frame_81 = QFrame(self.frame_dados_avulsa)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setFont(font2)
        self.frame_81.setFrameShape(QFrame.NoFrame)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_81)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(-1, 20, -1, -1)
        self.btn_salvar_entrada = QPushButton(self.frame_81)
        self.btn_salvar_entrada.setObjectName(u"btn_salvar_entrada")
        self.btn_salvar_entrada.setMinimumSize(QSize(219, 50))
        self.btn_salvar_entrada.setMaximumSize(QSize(250, 16777215))
        self.btn_salvar_entrada.setFont(font5)
        self.btn_salvar_entrada.setCursor(QCursor(Qt.ForbiddenCursor))
        self.btn_salvar_entrada.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(6, 180, 20);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(5, 161, 15);\n"
"}\n"
"")

        self.horizontalLayout_21.addWidget(self.btn_salvar_entrada)


        self.verticalLayout_69.addWidget(self.frame_81, 0, Qt.AlignHCenter)


        self.verticalLayout_44.addWidget(self.frame_dados_avulsa)

        self.frame_82 = QFrame(self.frame_75)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setFont(font2)
        self.frame_82.setFrameShape(QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_82)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.btn_historico_obs = QPushButton(self.frame_82)
        self.btn_historico_obs.setObjectName(u"btn_historico_obs")
        sizePolicy1.setHeightForWidth(self.btn_historico_obs.sizePolicy().hasHeightForWidth())
        self.btn_historico_obs.setSizePolicy(sizePolicy1)
        self.btn_historico_obs.setMinimumSize(QSize(0, 26))
        self.btn_historico_obs.setMaximumSize(QSize(16777215, 26))
        self.btn_historico_obs.setFont(font21)
        self.btn_historico_obs.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_historico_obs.setStyleSheet(u"\n"
"QPushButton{\n"
"background-color: rgb(43, 43, 43);color: rgb(255, 255, 255);\n"
"image: url(:/icons/angle-up-solid_white.svg);\n"
"font-size:10px;\n"
"color:white;\n"
"	width:5px;\n"
"	height:5px;}\n"
"QPushButton:hover{\n"
"background-color: rgb(60, 60, 60);\n"
"}\n"
"")
        self.btn_historico_obs.setIconSize(QSize(23, 23))
        self.btn_historico_obs.setAutoRepeatDelay(1)
        self.btn_historico_obs.setAutoDefault(False)
        self.btn_historico_obs.setFlat(False)

        self.verticalLayout_40.addWidget(self.btn_historico_obs, 0, Qt.AlignBottom)

        self.frame_pendentes = QFrame(self.frame_82)
        self.frame_pendentes.setObjectName(u"frame_pendentes")
        self.frame_pendentes.setMinimumSize(QSize(0, 0))
        self.frame_pendentes.setMaximumSize(QSize(16777215, 0))
        self.frame_pendentes.setFont(font2)
        self.frame_pendentes.setStyleSheet(u"background-color: rgb(43, 43, 43);")
        self.frame_pendentes.setFrameShape(QFrame.NoFrame)
        self.frame_pendentes.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_pendentes)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(-1, 0, -1, -1)
        self.frame_41 = QFrame(self.frame_pendentes)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFont(font2)
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_48 = QLabel(self.frame_41)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMinimumSize(QSize(0, 30))
        self.label_48.setMaximumSize(QSize(16777215, 30))
        self.label_48.setFont(font18)
        self.label_48.setStyleSheet(u"	color:white;\n"
"")
        self.label_48.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.label_48)

        self.label_25 = QLabel(self.frame_41)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font18)
        self.label_25.setStyleSheet(u"color: rgb(6, 180, 20);")

        self.horizontalLayout_20.addWidget(self.label_25)

        self.label_29 = QLabel(self.frame_41)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font18)
        self.label_29.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_20.addWidget(self.label_29)


        self.verticalLayout_41.addWidget(self.frame_41, 0, Qt.AlignHCenter)

        self.frame_26 = QFrame(self.frame_pendentes)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 5)
        self.pushButton_2 = QPushButton(self.frame_26)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font7)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"\n"
"QPushButton{\n"
"border: 1px solid rgb(255, 33, 33);\n"
"padding:5px;\n"
"color:white;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color:rgb(255, 33, 33)\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/icons/trash-can-solid-white.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon14)
        self.pushButton_2.setIconSize(QSize(19, 19))

        self.horizontalLayout_41.addWidget(self.pushButton_2, 0, Qt.AlignRight)


        self.verticalLayout_41.addWidget(self.frame_26)

        self.tableWidget_5 = QTableWidget(self.frame_pendentes)
        if (self.tableWidget_5.columnCount() < 4):
            self.tableWidget_5.setColumnCount(4)
        __qtablewidgetitem60 = QTableWidgetItem()
        __qtablewidgetitem60.setFont(font7);
        self.tableWidget_5.setHorizontalHeaderItem(0, __qtablewidgetitem60)
        brush = QBrush(QColor(43, 43, 43, 255))
        brush.setStyle(Qt.SolidPattern)
        __qtablewidgetitem61 = QTableWidgetItem()
        __qtablewidgetitem61.setFont(font7);
        __qtablewidgetitem61.setForeground(brush);
        self.tableWidget_5.setHorizontalHeaderItem(1, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        __qtablewidgetitem62.setFont(font7);
        __qtablewidgetitem62.setForeground(brush);
        self.tableWidget_5.setHorizontalHeaderItem(2, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        __qtablewidgetitem63.setFont(font7);
        __qtablewidgetitem63.setForeground(brush);
        self.tableWidget_5.setHorizontalHeaderItem(3, __qtablewidgetitem63)
        self.tableWidget_5.setObjectName(u"tableWidget_5")
        self.tableWidget_5.setMaximumSize(QSize(16777215, 1999999))
        self.tableWidget_5.setFont(font23)
        self.tableWidget_5.setStyleSheet(u"QTableWidget{\n"
"	font: 10pt \"Century Gothic\";\n"
"	outline:0;	color:white;\n"
"\n"
"}\n"
"QHeaderView::section {\n"
"	border:1px solid;\n"
"}\n"
"\n"
"QTableView::item:focus{\n"
"    border: 1px solid ;\n"
"	color:rgb(67, 202, 0)\n"
"}\n"
"QScrollBar:vertical {\n"
"    border: 1px solid #999999;\n"
"    background:white;\n"
"    width:15px;    \n"
"    margin: 3px\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(43, 43, 43);\n"
"    min-height: 0px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    background:rgb(50, 50, 50);\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"	height:0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: 1px solid #999999;\n"
"    background:white"
                        ";\n"
"    height:15px;    \n"
"    margin: 3px\n"
" }\n"
"\n"
" QScrollBar::handle:horizontal {\n"
"    background: rgb(43, 43, 43);\n"
"    min-width: 0px;\n"
" }\n"
"QScrollBar::add-line:horizontal {\n"
"    background:rgb(50, 50, 50);\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"	height:0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
" }\n"
"\n"
"")
        self.tableWidget_5.setAutoScroll(True)
        self.tableWidget_5.setAutoScrollMargin(20)
        self.tableWidget_5.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_5.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.tableWidget_5.setDefaultDropAction(Qt.IgnoreAction)
        self.tableWidget_5.setAlternatingRowColors(False)
        self.tableWidget_5.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_5.setTextElideMode(Qt.ElideRight)
        self.tableWidget_5.setSortingEnabled(True)
        self.tableWidget_5.setRowCount(0)
        self.tableWidget_5.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_5.horizontalHeader().setMinimumSectionSize(95)
        self.tableWidget_5.horizontalHeader().setDefaultSectionSize(115)
        self.tableWidget_5.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_5.verticalHeader().setVisible(False)

        self.verticalLayout_41.addWidget(self.tableWidget_5)


        self.verticalLayout_40.addWidget(self.frame_pendentes)


        self.verticalLayout_44.addWidget(self.frame_82, 0, Qt.AlignBottom)


        self.verticalLayout_28.addWidget(self.frame_75)


        self.verticalLayout_34.addWidget(self.frame_36)


        self.verticalLayout_36.addWidget(self.frame_34)

        self.stackedWidget.addWidget(self.page_entrada)
        self.page_saida = QWidget()
        self.page_saida.setObjectName(u"page_saida")
        self.verticalLayout_92 = QVBoxLayout(self.page_saida)
        self.verticalLayout_92.setSpacing(0)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.verticalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.frame_84 = QFrame(self.page_saida)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setFont(font2)
        self.frame_84.setFrameShape(QFrame.NoFrame)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.verticalLayout_75 = QVBoxLayout(self.frame_84)
        self.verticalLayout_75.setSpacing(0)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.frame_85 = QFrame(self.frame_84)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setMinimumSize(QSize(0, 37))
        self.frame_85.setMaximumSize(QSize(16777215, 37))
        self.frame_85.setFont(font2)
        self.frame_85.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(43, 43, 43);")
        self.frame_85.setFrameShape(QFrame.NoFrame)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.verticalLayout_84 = QVBoxLayout(self.frame_85)
        self.verticalLayout_84.setSpacing(7)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.verticalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.aba_relatorio_button_9 = QPushButton(self.frame_85)
        self.aba_relatorio_button_9.setObjectName(u"aba_relatorio_button_9")
        self.aba_relatorio_button_9.setMinimumSize(QSize(160, 37))
        self.aba_relatorio_button_9.setMaximumSize(QSize(5555, 37))
        self.aba_relatorio_button_9.setBaseSize(QSize(555, 2))
        self.aba_relatorio_button_9.setFont(font10)
        self.aba_relatorio_button_9.setLayoutDirection(Qt.LeftToRight)
        self.aba_relatorio_button_9.setStyleSheet(u"QPushButton{\n"
"	border:0;\n"
"}")
        self.aba_relatorio_button_9.setIcon(icon1)
        self.aba_relatorio_button_9.setIconSize(QSize(30, 30))
        self.aba_relatorio_button_9.setFlat(False)

        self.verticalLayout_84.addWidget(self.aba_relatorio_button_9, 0, Qt.AlignTop)


        self.verticalLayout_75.addWidget(self.frame_85)

        self.frame_95 = QFrame(self.frame_84)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setFont(font2)
        self.frame_95.setFrameShape(QFrame.NoFrame)
        self.frame_95.setFrameShadow(QFrame.Raised)
        self.verticalLayout_85 = QVBoxLayout(self.frame_95)
        self.verticalLayout_85.setSpacing(0)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.verticalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.frame_96 = QFrame(self.frame_95)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setMinimumSize(QSize(210, 250))
        self.frame_96.setMaximumSize(QSize(16777215, 300))
        self.frame_96.setFont(font2)
        self.frame_96.setStyleSheet(u"")
        self.frame_96.setFrameShape(QFrame.NoFrame)
        self.frame_96.setFrameShadow(QFrame.Raised)
        self.verticalLayout_86 = QVBoxLayout(self.frame_96)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.frame_97 = QFrame(self.frame_96)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setFont(font2)
        self.frame_97.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame_97.setFrameShape(QFrame.NoFrame)
        self.frame_97.setFrameShadow(QFrame.Raised)
        self.verticalLayout_87 = QVBoxLayout(self.frame_97)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.frame_117 = QFrame(self.frame_97)
        self.frame_117.setObjectName(u"frame_117")
        self.frame_117.setMaximumSize(QSize(16777215, 25))
        self.frame_117.setFont(font2)
        self.frame_117.setFrameShape(QFrame.StyledPanel)
        self.frame_117.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_117)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.frame_118 = QFrame(self.frame_117)
        self.frame_118.setObjectName(u"frame_118")
        self.frame_118.setMaximumSize(QSize(16777215, 29))
        self.frame_118.setFont(font2)
        self.frame_118.setFrameShape(QFrame.StyledPanel)
        self.frame_118.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_118)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_65 = QLabel(self.frame_118)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setMaximumSize(QSize(16777215, 20))
        self.label_65.setFont(font10)
        self.label_65.setStyleSheet(u"")
        self.label_65.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.label_65, 0, Qt.AlignRight)

        self.label_66 = QLabel(self.frame_118)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMaximumSize(QSize(16777215, 20))
        self.label_66.setFont(font10)
        self.label_66.setStyleSheet(u"color: rgb(255, 48, 48);")
        self.label_66.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.label_66, 0, Qt.AlignLeft)


        self.horizontalLayout_33.addWidget(self.frame_118)


        self.verticalLayout_87.addWidget(self.frame_117)

        self.frame_98 = QFrame(self.frame_97)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setMinimumSize(QSize(0, 74))
        self.frame_98.setFont(font2)
        self.frame_98.setStyleSheet(u"background-color: rgb(231, 231, 231);\\n")
        self.frame_98.setFrameShape(QFrame.StyledPanel)
        self.frame_98.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_98)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.lcdNumber_3 = QLCDNumber(self.frame_98)
        self.lcdNumber_3.setObjectName(u"lcdNumber_3")
        self.lcdNumber_3.setMinimumSize(QSize(0, 90))
        self.lcdNumber_3.setMaximumSize(QSize(16777215, 19999))
        self.lcdNumber_3.setFont(font19)
        self.lcdNumber_3.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_3.setSmallDecimalPoint(True)
        self.lcdNumber_3.setDigitCount(13)
        self.lcdNumber_3.setMode(QLCDNumber.Dec)
        self.lcdNumber_3.setSegmentStyle(QLCDNumber.Filled)
        self.lcdNumber_3.setProperty("value", 0.000000000000000)
        self.lcdNumber_3.setProperty("intValue", 0)

        self.horizontalLayout_19.addWidget(self.lcdNumber_3)

        self.label_58 = QLabel(self.frame_98)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMaximumSize(QSize(50, 50))
        self.label_58.setFont(font20)

        self.horizontalLayout_19.addWidget(self.label_58)


        self.verticalLayout_87.addWidget(self.frame_98)


        self.verticalLayout_86.addWidget(self.frame_97)


        self.verticalLayout_85.addWidget(self.frame_96)

        self.frame_99 = QFrame(self.frame_95)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setFont(font2)
        self.frame_99.setFrameShape(QFrame.NoFrame)
        self.frame_99.setFrameShadow(QFrame.Raised)
        self.verticalLayout_88 = QVBoxLayout(self.frame_99)
        self.verticalLayout_88.setSpacing(0)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.frame_dados_avulsa_3 = QFrame(self.frame_99)
        self.frame_dados_avulsa_3.setObjectName(u"frame_dados_avulsa_3")
        self.frame_dados_avulsa_3.setMinimumSize(QSize(0, 0))
        self.frame_dados_avulsa_3.setMaximumSize(QSize(16777215, 255))
        self.frame_dados_avulsa_3.setFont(font2)
        self.frame_dados_avulsa_3.setFrameShape(QFrame.NoFrame)
        self.frame_dados_avulsa_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_89 = QVBoxLayout(self.frame_dados_avulsa_3)
        self.verticalLayout_89.setSpacing(0)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.verticalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.frame_100 = QFrame(self.frame_dados_avulsa_3)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setFont(font2)
        self.frame_100.setFrameShape(QFrame.NoFrame)
        self.frame_100.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_100)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setHorizontalSpacing(0)
        self.gridLayout_17.setVerticalSpacing(6)
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.comboBox_pesagem_entrada = QComboBox(self.frame_100)
        self.comboBox_pesagem_entrada.addItem("")
        self.comboBox_pesagem_entrada.addItem("")
        self.comboBox_pesagem_entrada.setObjectName(u"comboBox_pesagem_entrada")
        self.comboBox_pesagem_entrada.setMinimumSize(QSize(0, 30))
        self.comboBox_pesagem_entrada.setFont(font21)
        self.comboBox_pesagem_entrada.setStyleSheet(u"QComboBox{\n"
"	border:1px solid;\n"
"	padding-left:10px;\n"
"	font-size:15px;\n"
"	\n"
"	background-color: rgb(250, 252, 250);\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"	border:0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
"	image: url(:/icons/angle-down-solid.svg);\n"
"	width:12px;\n"
"	height:12px;\n"
"	margin-right:15px;\n"
"}\n"
"\n"
"QComboBox::on{\n"
"	border:2px solid rgb(67, 202, 0);\n"
"}\n"
"\n"
"QComboBox QListView{\n"
"	padding:5px;\n"
"	border:1px solid;\n"
"	background-color: rgba(255, 255, 255, 50%);\n"
"	outline:0;\n"
"}\n"
"")
        self.comboBox_pesagem_entrada.setMaxVisibleItems(10)
        self.comboBox_pesagem_entrada.setInsertPolicy(QComboBox.NoInsert)
        self.comboBox_pesagem_entrada.setIconSize(QSize(32, 32))
        self.comboBox_pesagem_entrada.setDuplicatesEnabled(True)
        self.comboBox_pesagem_entrada.setFrame(True)

        self.gridLayout_17.addWidget(self.comboBox_pesagem_entrada, 3, 0, 1, 1)

        self.label_59 = QLabel(self.frame_100)
        self.label_59.setObjectName(u"label_59")
        font24 = QFont()
        font24.setFamily(u"Segoe UI")
        font24.setPointSize(13)
        font24.setBold(True)
        font24.setUnderline(False)
        font24.setWeight(75)
        font24.setKerning(True)
        font24.setStyleStrategy(QFont.PreferDefault)
        self.label_59.setFont(font24)
        self.label_59.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.label_59, 0, 0, 1, 1)

        self.label_63 = QLabel(self.frame_100)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMaximumSize(QSize(16777215, 20))
        self.label_63.setFont(font5)

        self.gridLayout_17.addWidget(self.label_63, 1, 0, 1, 1)


        self.verticalLayout_89.addWidget(self.frame_100, 0, Qt.AlignTop)

        self.frame_101 = QFrame(self.frame_dados_avulsa_3)
        self.frame_101.setObjectName(u"frame_101")
        self.frame_101.setMaximumSize(QSize(16777215, 35))
        self.frame_101.setFont(font2)
        self.frame_101.setFrameShape(QFrame.StyledPanel)
        self.frame_101.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_101)
        self.horizontalLayout_27.setSpacing(10)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_89.addWidget(self.frame_101, 0, Qt.AlignHCenter)

        self.frame_saida_detalhes = QFrame(self.frame_dados_avulsa_3)
        self.frame_saida_detalhes.setObjectName(u"frame_saida_detalhes")
        self.frame_saida_detalhes.setMinimumSize(QSize(0, 0))
        self.frame_saida_detalhes.setMaximumSize(QSize(16777215, 80))
        self.frame_saida_detalhes.setFrameShape(QFrame.NoFrame)
        self.frame_saida_detalhes.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_saida_detalhes)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_53 = QFrame(self.frame_saida_detalhes)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.NoFrame)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.segundos_7 = QLabel(self.frame_53)
        self.segundos_7.setObjectName(u"segundos_7")
        self.segundos_7.setFont(font5)
        self.segundos_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_44.addWidget(self.segundos_7)

        self.text_saida_cliente = QLabel(self.frame_53)
        self.text_saida_cliente.setObjectName(u"text_saida_cliente")
        self.text_saida_cliente.setFont(font5)
        self.text_saida_cliente.setStyleSheet(u"color: rgb(109, 109, 109);")

        self.horizontalLayout_44.addWidget(self.text_saida_cliente)


        self.gridLayout_3.addWidget(self.frame_53, 1, 2, 1, 1)

        self.frame_49 = QFrame(self.frame_saida_detalhes)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.NoFrame)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.segundos_5 = QLabel(self.frame_49)
        self.segundos_5.setObjectName(u"segundos_5")
        self.segundos_5.setFont(font5)
        self.segundos_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_43.addWidget(self.segundos_5)

        self.text_saida_veiculo = QLabel(self.frame_49)
        self.text_saida_veiculo.setObjectName(u"text_saida_veiculo")
        self.text_saida_veiculo.setFont(font5)
        self.text_saida_veiculo.setStyleSheet(u"color: rgb(109, 109, 109);")

        self.horizontalLayout_43.addWidget(self.text_saida_veiculo)


        self.gridLayout_3.addWidget(self.frame_49, 1, 1, 1, 1)

        self.frame_54 = QFrame(self.frame_saida_detalhes)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setFrameShape(QFrame.NoFrame)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.segundos_9 = QLabel(self.frame_54)
        self.segundos_9.setObjectName(u"segundos_9")
        self.segundos_9.setFont(font5)
        self.segundos_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_45.addWidget(self.segundos_9)

        self.text_saida_carga = QLabel(self.frame_54)
        self.text_saida_carga.setObjectName(u"text_saida_carga")
        self.text_saida_carga.setFont(font5)
        self.text_saida_carga.setStyleSheet(u"color: rgb(109, 109, 109);")

        self.horizontalLayout_45.addWidget(self.text_saida_carga)


        self.gridLayout_3.addWidget(self.frame_54, 1, 3, 1, 1)

        self.frame_27 = QFrame(self.frame_saida_detalhes)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.NoFrame)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.segundos_3 = QLabel(self.frame_27)
        self.segundos_3.setObjectName(u"segundos_3")
        self.segundos_3.setFont(font5)
        self.segundos_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_42.addWidget(self.segundos_3)

        self.text_saida_motorista = QLabel(self.frame_27)
        self.text_saida_motorista.setObjectName(u"text_saida_motorista")
        self.text_saida_motorista.setFont(font5)
        self.text_saida_motorista.setStyleSheet(u"color: rgb(109, 109, 109);")

        self.horizontalLayout_42.addWidget(self.text_saida_motorista)


        self.gridLayout_3.addWidget(self.frame_27, 1, 0, 1, 1)

        self.frame_57 = QFrame(self.frame_saida_detalhes)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setFrameShape(QFrame.NoFrame)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_46.setSpacing(0)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.frame_58 = QFrame(self.frame_57)
        self.frame_58.setObjectName(u"frame_58")
        font25 = QFont()
        font25.setPointSize(11)
        self.frame_58.setFont(font25)
        self.frame_58.setFrameShape(QFrame.NoFrame)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_58)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, -1, 0)
        self.segundos_11 = QLabel(self.frame_58)
        self.segundos_11.setObjectName(u"segundos_11")
        self.segundos_11.setFont(font5)
        self.segundos_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_47.addWidget(self.segundos_11)

        self.label_10 = QLabel(self.frame_58)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font5)
        self.label_10.setStyleSheet(u"color: rgb(6, 180, 20);")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_47.addWidget(self.label_10)

        self.label_19 = QLabel(self.frame_58)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font5)
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_47.addWidget(self.label_19)


        self.horizontalLayout_46.addWidget(self.frame_58)

        self.text_saida_pesoentrada = QLabel(self.frame_57)
        self.text_saida_pesoentrada.setObjectName(u"text_saida_pesoentrada")
        self.text_saida_pesoentrada.setFont(font5)
        self.text_saida_pesoentrada.setStyleSheet(u"color: rgb(109, 109, 109);")

        self.horizontalLayout_46.addWidget(self.text_saida_pesoentrada)


        self.gridLayout_3.addWidget(self.frame_57, 1, 4, 1, 1)

        self.label_24 = QLabel(self.frame_saida_detalhes)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font5)
        self.label_24.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_24, 0, 2, 1, 1)


        self.verticalLayout_89.addWidget(self.frame_saida_detalhes)

        self.frame_102 = QFrame(self.frame_dados_avulsa_3)
        self.frame_102.setObjectName(u"frame_102")
        self.frame_102.setFont(font2)
        self.frame_102.setFrameShape(QFrame.NoFrame)
        self.frame_102.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_102)
        self.horizontalLayout_28.setSpacing(8)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 20, 0, 0)
        self.btn_finalizar_pesagem = QPushButton(self.frame_102)
        self.btn_finalizar_pesagem.setObjectName(u"btn_finalizar_pesagem")
        self.btn_finalizar_pesagem.setMinimumSize(QSize(219, 50))
        self.btn_finalizar_pesagem.setMaximumSize(QSize(250, 16777215))
        self.btn_finalizar_pesagem.setFont(font5)
        self.btn_finalizar_pesagem.setCursor(QCursor(Qt.ForbiddenCursor))
        self.btn_finalizar_pesagem.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"background-color: rgb(6, 180, 20);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(5, 161, 15);\n"
"}\n"
"")

        self.horizontalLayout_28.addWidget(self.btn_finalizar_pesagem)

        self.radioButton_3 = QRadioButton(self.frame_102)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setFont(font9)
        self.radioButton_3.setStyleSheet(u"\n"
"QRadioButton::indicator {\n"
"    width:                  12px;\n"
"    height:                 12px;\n"
"    border-radius:          6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"	image: url(:/icons/check-solid.svg);\n"
"	background-color: rgb(6, 180, 20);\n"
"    border:                 1px solid rgb(88, 88, 88);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    border:                 1px solid rgb(88, 88, 88);\n"
"}")
        self.radioButton_3.setChecked(True)

        self.horizontalLayout_28.addWidget(self.radioButton_3)


        self.verticalLayout_89.addWidget(self.frame_102, 0, Qt.AlignHCenter)


        self.verticalLayout_88.addWidget(self.frame_dados_avulsa_3)

        self.frame_113 = QFrame(self.frame_99)
        self.frame_113.setObjectName(u"frame_113")
        self.frame_113.setFont(font2)
        self.frame_113.setFrameShape(QFrame.NoFrame)
        self.frame_113.setFrameShadow(QFrame.Raised)
        self.verticalLayout_90 = QVBoxLayout(self.frame_113)
        self.verticalLayout_90.setSpacing(0)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.verticalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.frame_historico_avulsas_3 = QFrame(self.frame_113)
        self.frame_historico_avulsas_3.setObjectName(u"frame_historico_avulsas_3")
        self.frame_historico_avulsas_3.setMinimumSize(QSize(0, 0))
        self.frame_historico_avulsas_3.setMaximumSize(QSize(16777215, 0))
        self.frame_historico_avulsas_3.setFont(font2)
        self.frame_historico_avulsas_3.setStyleSheet(u"background-color: rgb(43, 43, 43);")
        self.frame_historico_avulsas_3.setFrameShape(QFrame.NoFrame)
        self.frame_historico_avulsas_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_91 = QVBoxLayout(self.frame_historico_avulsas_3)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.frame_114 = QFrame(self.frame_historico_avulsas_3)
        self.frame_114.setObjectName(u"frame_114")
        self.frame_114.setFont(font2)
        self.frame_114.setFrameShape(QFrame.NoFrame)
        self.frame_114.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_114)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_64 = QLabel(self.frame_114)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMinimumSize(QSize(0, 30))
        self.label_64.setMaximumSize(QSize(16777215, 30))
        self.label_64.setFont(font10)
        self.label_64.setStyleSheet(u"	color:white;\n"
"")
        self.label_64.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.label_64)


        self.verticalLayout_91.addWidget(self.frame_114, 0, Qt.AlignHCenter)

        self.tableWidget_8 = QTableWidget(self.frame_historico_avulsas_3)
        if (self.tableWidget_8.columnCount() < 3):
            self.tableWidget_8.setColumnCount(3)
        __qtablewidgetitem64 = QTableWidgetItem()
        __qtablewidgetitem64.setFont(font22);
        self.tableWidget_8.setHorizontalHeaderItem(0, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        __qtablewidgetitem65.setFont(font22);
        self.tableWidget_8.setHorizontalHeaderItem(1, __qtablewidgetitem65)
        brush1 = QBrush(QColor(255, 170, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        __qtablewidgetitem66 = QTableWidgetItem()
        __qtablewidgetitem66.setFont(font22);
        __qtablewidgetitem66.setForeground(brush1);
        self.tableWidget_8.setHorizontalHeaderItem(2, __qtablewidgetitem66)
        self.tableWidget_8.setObjectName(u"tableWidget_8")
        self.tableWidget_8.setMaximumSize(QSize(16777215, 1999999))
        self.tableWidget_8.setFont(font23)
        self.tableWidget_8.setStyleSheet(u"QTableWidget{\n"
"	font: 10pt \"Century Gothic\";\n"
"	outline:0;	color:white;\n"
"\n"
"}\n"
"QHeaderView::section {\n"
"	border:1px solid;\n"
"}\n"
"\n"
"QTableView::item:focus{\n"
"    border: 1px solid ;\n"
"	color:rgb(67, 202, 0)\n"
"}\n"
"QScrollBar:vertical {\n"
"    border: 1px solid #999999;\n"
"    background:white;\n"
"    width:15px;    \n"
"    margin: 3px\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(43, 43, 43);\n"
"    min-height: 0px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    background:rgb(50, 50, 50);\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"	height:0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: 1px solid #999999;\n"
"    background:white"
                        ";\n"
"    height:15px;    \n"
"    margin: 3px\n"
" }\n"
"\n"
" QScrollBar::handle:horizontal {\n"
"    background: rgb(43, 43, 43);\n"
"    min-width: 0px;\n"
" }\n"
"QScrollBar::add-line:horizontal {\n"
"    background:rgb(50, 50, 50);\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"	height:0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
" }\n"
"\n"
"")
        self.tableWidget_8.setAutoScroll(True)
        self.tableWidget_8.setAutoScrollMargin(20)
        self.tableWidget_8.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_8.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.tableWidget_8.setDefaultDropAction(Qt.IgnoreAction)
        self.tableWidget_8.setAlternatingRowColors(False)
        self.tableWidget_8.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_8.setTextElideMode(Qt.ElideRight)
        self.tableWidget_8.setSortingEnabled(True)
        self.tableWidget_8.setRowCount(0)
        self.tableWidget_8.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_8.horizontalHeader().setMinimumSectionSize(95)
        self.tableWidget_8.horizontalHeader().setDefaultSectionSize(115)
        self.tableWidget_8.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_8.verticalHeader().setVisible(False)

        self.verticalLayout_91.addWidget(self.tableWidget_8)


        self.verticalLayout_90.addWidget(self.frame_historico_avulsas_3)


        self.verticalLayout_88.addWidget(self.frame_113, 0, Qt.AlignBottom)


        self.verticalLayout_85.addWidget(self.frame_99)


        self.verticalLayout_75.addWidget(self.frame_95)


        self.verticalLayout_92.addWidget(self.frame_84)

        self.stackedWidget.addWidget(self.page_saida)
        self.page_conta = QWidget()
        self.page_conta.setObjectName(u"page_conta")
        self.page_conta.setStyleSheet(u"border:0")
        self.verticalLayout_14 = QVBoxLayout(self.page_conta)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.page_conta)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFont(font2)
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_11)
        self.verticalLayout_16.setSpacing(9)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 37))
        self.frame_12.setMaximumSize(QSize(16777215, 37))
        self.frame_12.setFont(font2)
        self.frame_12.setStyleSheet(u"background-color: rgb(25, 25, 25);color: rgb(255, 255, 255);")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_12)
        self.verticalLayout_15.setSpacing(7)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.title = QPushButton(self.frame_12)
        self.title.setObjectName(u"title")
        self.title.setMinimumSize(QSize(160, 37))
        self.title.setMaximumSize(QSize(5555, 37))
        self.title.setBaseSize(QSize(555, 2))
        self.title.setFont(font10)
        self.title.setLayoutDirection(Qt.LeftToRight)
        self.title.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(43, 43, 43);")
        self.title.setIcon(icon4)
        self.title.setIconSize(QSize(30, 30))
        self.title.setFlat(False)

        self.verticalLayout_15.addWidget(self.title)


        self.verticalLayout_16.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFont(font13)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_13)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(180, 0, 180, -1)
        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 260))
        self.frame_14.setFont(font2)
        self.frame_14.setStyleSheet(u"border-radius:15px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_14)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_2 = QFrame(self.frame_14)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 35))
        self.frame_2.setFont(font2)
        self.frame_2.setStyleSheet(u"border:0")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setSpacing(8)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(127, 0))
        self.label_3.setMaximumSize(QSize(241, 30))
        font26 = QFont()
        font26.setFamily(u"Segoe UI")
        font26.setPointSize(15)
        font26.setBold(True)
        font26.setWeight(75)
        self.label_3.setFont(font26)
        self.label_3.setStyleSheet(u"color:  rgb(15, 202, 2);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(30, 30))
        self.label_12.setFont(font2)
        self.label_12.setPixmap(QPixmap(u":/icons/cubes-solid.svg"))
        self.label_12.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_12)


        self.verticalLayout_18.addWidget(self.frame_2, 0, Qt.AlignHCenter)

        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFont(font2)
        self.frame_16.setStyleSheet(u"background-color: rgb(235, 235, 235);\n"
"border:0")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_16)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, -1)
        self.frame_17 = QFrame(self.frame_16)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFont(font2)
        self.frame_17.setStyleSheet(u"border:0")
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_17)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(9, 6, -1, 0)
        self.label_11 = QLabel(self.frame_17)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font7)

        self.gridLayout_6.addWidget(self.label_11, 0, 0, 1, 1, Qt.AlignBottom)

        self.text_empresa_pessoal = QLabel(self.frame_17)
        self.text_empresa_pessoal.setObjectName(u"text_empresa_pessoal")
        self.text_empresa_pessoal.setFont(font8)

        self.gridLayout_6.addWidget(self.text_empresa_pessoal, 1, 0, 1, 1)

        self.btn_alterar_nome = QPushButton(self.frame_17)
        self.btn_alterar_nome.setObjectName(u"btn_alterar_nome")
        self.btn_alterar_nome.setMinimumSize(QSize(100, 0))
        self.btn_alterar_nome.setMaximumSize(QSize(16777215, 100))
        self.btn_alterar_nome.setFont(font7)
        self.btn_alterar_nome.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_nome.setStyleSheet(u"QPushButton{\n"
"	border:1px solid;\n"
"	padding:10px;\n"
"	border-radius:10px;\n"
"	background-color: rgb(250, 250, 250);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(209, 209, 209);\n"
"}")

        self.gridLayout_6.addWidget(self.btn_alterar_nome, 1, 1, 1, 1, Qt.AlignRight)


        self.verticalLayout_19.addWidget(self.frame_17)

        self.frame_19 = QFrame(self.frame_16)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFont(font2)
        self.frame_19.setStyleSheet(u"border:0")
        self.frame_19.setFrameShape(QFrame.NoFrame)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_19)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(0)
        self.gridLayout_8.setVerticalSpacing(9)
        self.gridLayout_8.setContentsMargins(9, 0, -1, 9)
        self.label_13 = QLabel(self.frame_19)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font7)

        self.gridLayout_8.addWidget(self.label_13, 0, 0, 1, 1)

        self.text_email = QLabel(self.frame_19)
        self.text_email.setObjectName(u"text_email")
        self.text_email.setFont(font8)

        self.gridLayout_8.addWidget(self.text_email, 1, 0, 1, 1, Qt.AlignTop)


        self.verticalLayout_19.addWidget(self.frame_19)

        self.frame_18 = QFrame(self.frame_16)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFont(font2)
        self.frame_18.setStyleSheet(u"border:0")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_18)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(-1, 0, 9, 0)
        self.label_15 = QLabel(self.frame_18)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font7)

        self.gridLayout_7.addWidget(self.label_15, 0, 0, 1, 1, Qt.AlignBottom)

        self.text_telefone = QLabel(self.frame_18)
        self.text_telefone.setObjectName(u"text_telefone")
        self.text_telefone.setFont(font8)

        self.gridLayout_7.addWidget(self.text_telefone, 1, 0, 1, 1)

        self.btn_alterar_telefone = QPushButton(self.frame_18)
        self.btn_alterar_telefone.setObjectName(u"btn_alterar_telefone")
        self.btn_alterar_telefone.setMinimumSize(QSize(100, 0))
        self.btn_alterar_telefone.setMaximumSize(QSize(16777215, 100))
        self.btn_alterar_telefone.setFont(font7)
        self.btn_alterar_telefone.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_telefone.setStyleSheet(u"QPushButton{\n"
"	border:1px solid;\n"
"	padding:10px;\n"
"	border-radius:10px;\n"
"	background-color: rgb(250, 250, 250);\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(209, 209, 209);\n"
"}")

        self.gridLayout_7.addWidget(self.btn_alterar_telefone, 1, 1, 1, 1, Qt.AlignRight)


        self.verticalLayout_19.addWidget(self.frame_18)

        self.frame_20 = QFrame(self.frame_16)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFont(font2)
        self.frame_20.setStyleSheet(u"border:0")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_20)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.label_17 = QLabel(self.frame_20)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font7)

        self.gridLayout_9.addWidget(self.label_17, 0, 0, 1, 1, Qt.AlignBottom)

        self.btn_atualizar_licenca = QPushButton(self.frame_20)
        self.btn_atualizar_licenca.setObjectName(u"btn_atualizar_licenca")
        self.btn_atualizar_licenca.setMinimumSize(QSize(100, 0))
        self.btn_atualizar_licenca.setMaximumSize(QSize(20000, 16777215))
        self.btn_atualizar_licenca.setFont(font7)
        self.btn_atualizar_licenca.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_atualizar_licenca.setStyleSheet(u"QPushButton{\n"
"	border:1px solid rgb(15, 202, 2);\n"
"	padding:10px;\n"
"	border-radius:10px;\n"
"	background-color: rgb(250, 250, 250);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(145, 255, 133);\n"
"}")

        self.gridLayout_9.addWidget(self.btn_atualizar_licenca, 1, 1, 1, 1, Qt.AlignRight)

        self.text_licenca = QLabel(self.frame_20)
        self.text_licenca.setObjectName(u"text_licenca")
        self.text_licenca.setMinimumSize(QSize(0, 0))
        self.text_licenca.setFont(font8)

        self.gridLayout_9.addWidget(self.text_licenca, 1, 0, 1, 1)


        self.verticalLayout_19.addWidget(self.frame_20)


        self.verticalLayout_18.addWidget(self.frame_16)


        self.verticalLayout_17.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_13)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 0))
        self.frame_15.setMaximumSize(QSize(16777215, 80))
        self.frame_15.setFont(font2)
        self.frame_15.setStyleSheet(u"border-top:1px solid rgb(176, 176, 176)")
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_15)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.frame_15)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(16777215, 20))
        self.label_20.setFont(font7)
        self.label_20.setStyleSheet(u"border:0")

        self.verticalLayout_20.addWidget(self.label_20)

        self.label_23 = QLabel(self.frame_15)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font8)
        self.label_23.setStyleSheet(u"border:0")

        self.verticalLayout_20.addWidget(self.label_23)

        self.btn_alterar_senha = QPushButton(self.frame_15)
        self.btn_alterar_senha.setObjectName(u"btn_alterar_senha")
        self.btn_alterar_senha.setMinimumSize(QSize(100, 0))
        self.btn_alterar_senha.setMaximumSize(QSize(100, 32))
        self.btn_alterar_senha.setFont(font7)
        self.btn_alterar_senha.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_senha.setStyleSheet(u"QPushButton{\n"
"	border:1px solid;\n"
"	padding:8px;\n"
"	background-color: rgb(250, 250, 250);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(209, 209, 209);\n"
"}")

        self.verticalLayout_20.addWidget(self.btn_alterar_senha)


        self.verticalLayout_17.addWidget(self.frame_15)

        self.frame_21 = QFrame(self.frame_13)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMaximumSize(QSize(16777215, 80))
        self.frame_21.setFont(font2)
        self.frame_21.setStyleSheet(u"border-top:1px solid rgb(176, 176, 176)")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_21)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 2, 0, 0)
        self.label_21 = QLabel(self.frame_21)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(16777215, 20))
        self.label_21.setFont(font7)
        self.label_21.setStyleSheet(u"border:0")

        self.verticalLayout_21.addWidget(self.label_21)

        self.label_22 = QLabel(self.frame_21)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font8)
        self.label_22.setStyleSheet(u"border:0")

        self.verticalLayout_21.addWidget(self.label_22)

        self.btn_excluir_conta = QPushButton(self.frame_21)
        self.btn_excluir_conta.setObjectName(u"btn_excluir_conta")
        self.btn_excluir_conta.setMinimumSize(QSize(100, 0))
        self.btn_excluir_conta.setMaximumSize(QSize(100, 32))
        self.btn_excluir_conta.setFont(font7)
        self.btn_excluir_conta.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir_conta.setStyleSheet(u"QPushButton{\n"
"	border:1px solid red;\n"
"	padding:7px;\n"
"	background-color: rgb(250, 250, 250);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 147, 147);\n"
"}")

        self.verticalLayout_21.addWidget(self.btn_excluir_conta)


        self.verticalLayout_17.addWidget(self.frame_21)


        self.verticalLayout_16.addWidget(self.frame_13)


        self.verticalLayout_14.addWidget(self.frame_11)

        self.stackedWidget.addWidget(self.page_conta)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.principal_frame, 2, 1, 1, 1)

        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 35))
        self.frame_5.setMaximumSize(QSize(16777215, 35))
        self.frame_5.setStyleSheet(u"background-color: rgb(15, 15, 15);")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.frame_saida = QFrame(self.frame_7)
        self.frame_saida.setObjectName(u"frame_saida")
        font27 = QFont()
        font27.setPointSize(1)
        self.frame_saida.setFont(font27)
        self.frame_saida.setStyleSheet(u"")
        self.frame_saida.setFrameShape(QFrame.NoFrame)
        self.frame_saida.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_saida)
        self.horizontalLayout_36.setSpacing(10)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(10, 0, 5, 0)
        self.label_logo_saida = QLabel(self.frame_saida)
        self.label_logo_saida.setObjectName(u"label_logo_saida")
        self.label_logo_saida.setMaximumSize(QSize(25, 25))
        font28 = QFont()
        font28.setFamily(u"MS Outlook")
        font28.setPointSize(15)
        self.label_logo_saida.setFont(font28)
        self.label_logo_saida.setStyleSheet(u"border:0")
        self.label_logo_saida.setPixmap(QPixmap(u":/icons/check-solid_green.svg"))
        self.label_logo_saida.setScaledContents(True)

        self.horizontalLayout_36.addWidget(self.label_logo_saida)

        self.label_realizada_ou_erro = QLabel(self.frame_saida)
        self.label_realizada_ou_erro.setObjectName(u"label_realizada_ou_erro")
        self.label_realizada_ou_erro.setFont(font16)
        self.label_realizada_ou_erro.setStyleSheet(u"color:rgb(6, 180, 20);")

        self.horizontalLayout_36.addWidget(self.label_realizada_ou_erro)

        self.label_veja_no_relatorio = QLabel(self.frame_saida)
        self.label_veja_no_relatorio.setObjectName(u"label_veja_no_relatorio")
        self.label_veja_no_relatorio.setFont(font7)
        self.label_veja_no_relatorio.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_36.addWidget(self.label_veja_no_relatorio)

        self.frame_9 = QFrame(self.frame_saida)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(100, 0))
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(22, 0, 1, 0)
        self.pushButton_3 = QPushButton(self.frame_9)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"border:0")
        icon15 = QIcon()
        icon15.addFile(u":/icons/eye-slash-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon15)
        self.pushButton_3.setIconSize(QSize(20, 20))

        self.horizontalLayout_40.addWidget(self.pushButton_3, 0, Qt.AlignRight)

        self.segundos = QLabel(self.frame_9)
        self.segundos.setObjectName(u"segundos")
        self.segundos.setFont(font7)
        self.segundos.setStyleSheet(u"color: rgb(109, 109, 109);")

        self.horizontalLayout_40.addWidget(self.segundos)


        self.horizontalLayout_36.addWidget(self.frame_9, 0, Qt.AlignRight)


        self.horizontalLayout_35.addWidget(self.frame_saida, 0, Qt.AlignRight)


        self.horizontalLayout_7.addWidget(self.frame_7, 0, Qt.AlignLeft)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 32))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(-1, 0, -1, 0)
        self.label_9 = QLabel(self.frame_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(26, 31))
        self.label_9.setMaximumSize(QSize(30, 30))
        self.label_9.setPixmap(QPixmap(u":/icons/free_icon_1 (3).svg"))
        self.label_9.setScaledContents(True)
        self.label_9.setWordWrap(True)

        self.horizontalLayout_34.addWidget(self.label_9, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_10 = QFrame(self.frame_6)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(100, 0))
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_10)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(-1, 0, -1, 0)
        self.label_6 = QLabel(self.frame_10)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font7)
        self.label_6.setStyleSheet(u"color: rgb(109, 109, 109);")

        self.verticalLayout_53.addWidget(self.label_6)

        self.hora = QLabel(self.frame_10)
        self.hora.setObjectName(u"hora")
        self.hora.setFont(font7)
        self.hora.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_53.addWidget(self.hora, 0, Qt.AlignTop)


        self.horizontalLayout_34.addWidget(self.frame_10)

        self.frame_25 = QFrame(self.frame_6)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(100, 0))
        self.frame_25.setFrameShape(QFrame.NoFrame)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.frame_25)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(-1, 0, -1, 0)
        self.label_7 = QLabel(self.frame_25)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font7)
        self.label_7.setStyleSheet(u"color: rgb(109, 109, 109);")

        self.verticalLayout_52.addWidget(self.label_7)

        self.data = QLabel(self.frame_25)
        self.data.setObjectName(u"data")
        self.data.setFont(font7)
        self.data.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_52.addWidget(self.data)


        self.horizontalLayout_34.addWidget(self.frame_25)


        self.horizontalLayout_7.addWidget(self.frame_6, 0, Qt.AlignRight)


        self.gridLayout.addWidget(self.frame_5, 3, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
        self.label_30.setBuddy(self.pushButton)
        self.nome_pc.setBuddy(self.btn_minimize_window)
        self.label_69.setBuddy(self.data_depois_de_2)
        self.label_8.setBuddy(self.input_clientes_telefone)
        self.text_empresa_pessoal.setBuddy(self.btn_alterar_nome)
        self.text_telefone.setBuddy(self.btn_alterar_telefone)
        self.text_licenca.setBuddy(self.btn_atualizar_licenca)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainWindow)

        self.aba_pesagem_button.setDefault(False)
        self.stackedWidget.setCurrentIndex(6)
        self.comboBox_veiculo_6.setCurrentIndex(0)
        self.comboBox_produto_6.setCurrentIndex(0)
        self.comboBox_cliente_6.setCurrentIndex(0)
        self.comboBox_cliente_2.setCurrentIndex(0)
        self.comboBox_produto_2.setCurrentIndex(0)
        self.comboBox_veiculo_2.setCurrentIndex(0)
        self.comboBox_veiculos_produtos.setCurrentIndex(0)
        self.comboBox_avulsas_veiculo.setCurrentIndex(0)
        self.comboBox_avulsas_cliente.setCurrentIndex(0)
        self.comboBox_avulsas_carga.setCurrentIndex(0)
        self.comboBox_entrada_cliente.setCurrentIndex(0)
        self.comboBox_entrada_carga.setCurrentIndex(0)
        self.comboBox_entrada_veiculo.setCurrentIndex(0)
        self.btn_historico_obs.setDefault(False)
        self.comboBox_pesagem_entrada.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Caltec - Software de pesagem", None))
        self.adicionar_balanca.setText(QCoreApplication.translate("MainWindow", u"Conectar balan\u00e7a", None))
        self.fechar_aplicativo.setText(QCoreApplication.translate("MainWindow", u"Fechar aplicativo", None))
        self.actionAvan_adas.setText(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es Avan\u00e7adas", None))
        self.aba_pesagem_button.setText(QCoreApplication.translate("MainWindow", u"Pesagens               \u25bc", None))
        self.button_avulsas_pesagens.setText(QCoreApplication.translate("MainWindow", u"Avulsa", None))
        self.button_entsaid_pesagens.setText(QCoreApplication.translate("MainWindow", u"Entrada", None))
        self.btn_alterar_saida.setText(QCoreApplication.translate("MainWindow", u"Sa\u00edda", None))
        self.aba_grupo_button.setText(QCoreApplication.translate("MainWindow", u"Grupos                  \u25bc", None))
        self.button_clientes_grupos.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.button_produtos_grupos.setText(QCoreApplication.translate("MainWindow", u"Carga", None))
        self.button_veiculos_grupos.setText(QCoreApplication.translate("MainWindow", u"Veiculos", None))
        self.aba_relatorio_button.setText(QCoreApplication.translate("MainWindow", u"Relat\u00f3rios             \u25bc", None))
        self.button_avulsas_relatorio.setText(QCoreApplication.translate("MainWindow", u"Avulsas", None))
        self.button_entsaid_relatorio.setText(QCoreApplication.translate("MainWindow", u"Entradas e Sa\u00eddas", None))
        self.aba_conta_button.setText(QCoreApplication.translate("MainWindow", u"Conta                       ", None))
        self.label_4.setText("")
        self.restantes_label.setText(QCoreApplication.translate("MainWindow", u"Pesagens restantes: 30", None))
        self.info_pro_label.setText(QCoreApplication.translate("MainWindow", u"Atualize para a vers\u00e3o PREMIUM e aproveite todos os recursos sem limita\u00e7\u00f5es.", None))
        self.aba_sair_button.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.label_30.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Conectar balan\u00e7a", None))
        self.nome_pc.setText(QCoreApplication.translate("MainWindow", u"ryanl - Software de pesagem", None))
        self.btn_minimize_window.setText("")
        self.btn_close_windows.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Status balan\u00e7a:", None))
        self.conexao_label.setText(QCoreApplication.translate("MainWindow", u"Ainda sem conex\u00e3o", None))
        self.aba_relatorio_button_14.setText(QCoreApplication.translate("MainWindow", u"Relat\u00f3rio Entradas e Sa\u00eddas", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"Cliente:", None))
        self.text_filtro_id_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.btn_filtro_id_6.setText("")
        self.data_fixa_6.setText(QCoreApplication.translate("MainWindow", u"Data fixa", None))
        self.data_antes_de_6.setText(QCoreApplication.translate("MainWindow", u"Antes de", None))
        self.data_depois_de_6.setText(QCoreApplication.translate("MainWindow", u"Depois de", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"Data:", None))
        self.comboBox_veiculo_6.setItemText(0, QCoreApplication.translate("MainWindow", u"Todos", None))

        self.comboBox_produto_6.setItemText(0, QCoreApplication.translate("MainWindow", u"Todos", None))

        self.comboBox_cliente_6.setItemText(0, QCoreApplication.translate("MainWindow", u"Todos", None))

        self.label_98.setText(QCoreApplication.translate("MainWindow", u"Placa do Ve\u00edculo:", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"Produto:", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"Motorista:", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Calcular valor e quantidade da carga          ", None))
        self.digite_um_id_2.setText(QCoreApplication.translate("MainWindow", u"Digite um ID", None))
        self.btn_Aplicar_filtro_geral_6.setText(QCoreApplication.translate("MainWindow", u"Aplicar Filtragem", None))
        self.btn_inprimir_6.setText(QCoreApplication.translate("MainWindow", u"Imprimir relat\u00f3rio", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Remover relat\u00f3rio(s) selecionado(s)", None))
        ___qtablewidgetitem = self.tableWidget_7.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"EXCLUIR", None));
        ___qtablewidgetitem1 = self.tableWidget_7.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"MOTORISTA", None));
        ___qtablewidgetitem2 = self.tableWidget_7.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"CLIENTE", None));
        ___qtablewidgetitem3 = self.tableWidget_7.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"PRODUTO", None));
        ___qtablewidgetitem4 = self.tableWidget_7.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"PLACA VE\u00cdCULO", None));
        ___qtablewidgetitem5 = self.tableWidget_7.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"PESO(ENTRADA)", None));
        ___qtablewidgetitem6 = self.tableWidget_7.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"PESO(SA\u00cdDA)", None));
        ___qtablewidgetitem7 = self.tableWidget_7.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"DATA(ENTRADA)", None));
        ___qtablewidgetitem8 = self.tableWidget_7.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"DATA(SA\u00cdDA)", None));
        ___qtablewidgetitem9 = self.tableWidget_7.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"PESO L\u00cdQUIDO", None));
        ___qtablewidgetitem10 = self.tableWidget_7.verticalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem11 = self.tableWidget_7.verticalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"2", None));

        __sortingEnabled = self.tableWidget_7.isSortingEnabled()
        self.tableWidget_7.setSortingEnabled(False)
        ___qtablewidgetitem12 = self.tableWidget_7.item(0, 1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Ryan", None));
        ___qtablewidgetitem13 = self.tableWidget_7.item(0, 2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Caltec", None));
        ___qtablewidgetitem14 = self.tableWidget_7.item(0, 3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Whisky", None));
        ___qtablewidgetitem15 = self.tableWidget_7.item(0, 4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"546GHY", None));
        ___qtablewidgetitem16 = self.tableWidget_7.item(0, 5)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"5000", None));
        ___qtablewidgetitem17 = self.tableWidget_7.item(0, 6)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"1000", None));
        ___qtablewidgetitem18 = self.tableWidget_7.item(0, 7)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"12:00 07/06/2022", None));
        ___qtablewidgetitem19 = self.tableWidget_7.item(0, 8)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"12:45 07/06/2022", None));
        ___qtablewidgetitem20 = self.tableWidget_7.item(0, 9)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"4000", None));
        ___qtablewidgetitem21 = self.tableWidget_7.item(1, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Jo\u00e3o", None));
        ___qtablewidgetitem22 = self.tableWidget_7.item(1, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Caltec", None));
        ___qtablewidgetitem23 = self.tableWidget_7.item(1, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Whisky", None));
        ___qtablewidgetitem24 = self.tableWidget_7.item(1, 4)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"852IKM", None));
        ___qtablewidgetitem25 = self.tableWidget_7.item(1, 5)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"5000", None));
        ___qtablewidgetitem26 = self.tableWidget_7.item(1, 6)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"1000", None));
        ___qtablewidgetitem27 = self.tableWidget_7.item(1, 7)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"12:50 07/09/2022", None));
        ___qtablewidgetitem28 = self.tableWidget_7.item(1, 8)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"13:30 07/06/2022", None));
        ___qtablewidgetitem29 = self.tableWidget_7.item(1, 9)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"4000", None));
        self.tableWidget_7.setSortingEnabled(__sortingEnabled)

        self.aba_relatorio_button_5.setText(QCoreApplication.translate("MainWindow", u"Relat\u00f3rio Avulsas", None))
        self.data_depois_de_2.setText(QCoreApplication.translate("MainWindow", u"Depois de", None))
        self.data_fixa_2.setText(QCoreApplication.translate("MainWindow", u"Data fixa", None))
        self.data_antes_de_2.setText(QCoreApplication.translate("MainWindow", u"Antes de", None))
        self.label_69.setText("")
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Cliente:", None))
        self.comboBox_cliente_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Todos", None))

        self.comboBox_produto_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Todos", None))

        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Produto:", None))
        self.comboBox_veiculo_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Todos", None))

        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Placa do Ve\u00edculo:", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Data:", None))
        self.btn_filtro_id_2.setText("")
        self.text_filtro_id_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Motorista:", None))
        self.digite_um_id.setText(QCoreApplication.translate("MainWindow", u"    Digite um ID", None))
        self.btn_Aplicar_filtro_geral_2.setText(QCoreApplication.translate("MainWindow", u"Aplicar Filtragem", None))
        self.btn_inprimir_2.setText(QCoreApplication.translate("MainWindow", u"Imprimir relat\u00f3rio", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Remover relat\u00f3rio(s) selecionado(s)", None))
        ___qtablewidgetitem30 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"EXCLUIR", None));
        ___qtablewidgetitem31 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"MOTORISTA", None));
        ___qtablewidgetitem32 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"PRODUTO", None));
        ___qtablewidgetitem33 = self.tableWidget_4.horizontalHeaderItem(3)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"CLIENTE", None));
        ___qtablewidgetitem34 = self.tableWidget_4.horizontalHeaderItem(4)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"PESO BRUTO", None));
        ___qtablewidgetitem35 = self.tableWidget_4.horizontalHeaderItem(5)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"DATA", None));
        ___qtablewidgetitem36 = self.tableWidget_4.horizontalHeaderItem(6)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"PLACA VE\u00cdCULO", None));
        self.aba_relatorio_button_3.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Adicionar novos clientes", None))
        self.input_clientes_nome.setText("")
        self.input_clientes_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.input_clientes_cpf.setText("")
        self.input_clientes_cpf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF / CNPJ (OPCIONAL)", None))
        self.input_clientes_rg.setText("")
        self.input_clientes_rg.setPlaceholderText(QCoreApplication.translate("MainWindow", u"RG (OPCIONAL)", None))
        self.input_clientes_cep.setText("")
        self.input_clientes_cep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP (OPCIONAL)", None))
        self.input_clientes_endereco.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"+55", None))
        self.input_clientes_telefone.setText("")
        self.input_clientes_telefone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.btn_registrar_clientes.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.btn_menu_registrar_clientes.setText("")
        self.label_16.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Historico de Clientes adicionados", None))
        self.btn_remover_clientes.setText(QCoreApplication.translate("MainWindow", u"Remover cliente(s) selecionado(s)", None))
        ___qtablewidgetitem37 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"EXCLUIR", None));
        ___qtablewidgetitem38 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem39 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"CPF / CNPJ", None));
        ___qtablewidgetitem40 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"RG", None));
        ___qtablewidgetitem41 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None));
        ___qtablewidgetitem42 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"CEP", None));
        ___qtablewidgetitem43 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"ENDERE\u00c7O", None));
        self.aba_relatorio_button_6.setText(QCoreApplication.translate("MainWindow", u"Ve\u00edculos", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Adicionar novos ve\u00edculos", None))
        self.input_veiculos_valor_2.setText("")
        self.input_veiculos_valor_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Propriet\u00e1rio", None))
        self.input_veiculos_nome.setText("")
        self.input_veiculos_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Modelo", None))
        self.input_veiculos_placa.setText("")
        self.input_veiculos_placa.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Placa", None))
        self.comboBox_veiculos_produtos.setItemText(0, QCoreApplication.translate("MainWindow", u"Nenhum", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Carga:", None))
        self.btn_registrar_veiculos.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.btn_menu_registrar_veiculos.setText("")
        self.label_27.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Historico de Ve\u00edculos adicionados", None))
        self.btn_remover_veiculos.setText(QCoreApplication.translate("MainWindow", u"Remover ve\u00edculo(s) selecionado(s)", None))
        ___qtablewidgetitem44 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"EXCLUIR", None));
        ___qtablewidgetitem45 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"PLACA", None));
        ___qtablewidgetitem46 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"PROPRIET\u00c1RIO", None));
        ___qtablewidgetitem47 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem48 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"CARGA", None));
        self.aba_relatorio_button_12.setText(QCoreApplication.translate("MainWindow", u"Carga", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Adicionar nova carga", None))
        self.input_produtos_nome.setText("")
        self.input_produtos_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.input_produtos_estoqueKG.setText("")
        self.input_produtos_estoqueKG.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o unit\u00e1rio (OPCIONAL)", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"R$", None))
        self.input_produtos_densidade.setText("")
        self.input_produtos_densidade.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Densidade (OPCIONAL)", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"T / M3", None))
        self.input_produtos_embalagemKG.setText("")
        self.input_produtos_embalagemKG.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Embalagem (OPCIONAL)", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"KG", None))
        self.input_produtos_desconto.setText("")
        self.input_produtos_desconto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Desconto (OPCIONAL)", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.btn_registrar_produtos.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.btn_menu_registrar_produtos.setText("")
        self.label_36.setText("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Historico de Cargas adicionadas", None))
        self.btn_remover_produtos.setText(QCoreApplication.translate("MainWindow", u"Remover Carga(s) selecionado(s)", None))
        ___qtablewidgetitem49 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"EXCLUIR", None));
        ___qtablewidgetitem50 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem51 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"PRE\u00c7O UNIT\u00c1RIO", None));
        ___qtablewidgetitem52 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"DENSIDADE", None));
        ___qtablewidgetitem53 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"EMBALAGEM", None));
        ___qtablewidgetitem54 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"DESCONTO", None));
        self.aba_relatorio_button_8.setText(QCoreApplication.translate("MainWindow", u"Avulsa", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Peso bruto", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"KG", None))
        self.btn_peso_manualmente_2.setText(QCoreApplication.translate("MainWindow", u"Capturar peso manualmente", None))
        self.peso_manualmente_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PESO (KG)", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Insira os dados para a pesagem Avulsa", None))
        self.input_avulsas_motorista.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Veiculo:", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Motorista:", None))
        self.comboBox_avulsas_veiculo.setItemText(0, QCoreApplication.translate("MainWindow", u"Nenhum", None))

        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Cliente:", None))
        self.comboBox_avulsas_cliente.setItemText(0, QCoreApplication.translate("MainWindow", u"Nenhum", None))

        self.comboBox_avulsas_carga.setItemText(0, QCoreApplication.translate("MainWindow", u"Nenhum", None))

        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Carga:", None))
        self.input_avulsas_obs.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Observa\u00e7\u00e3o (Opcional)", None))
        self.btn_fazer_pesagem_avulsa.setText(QCoreApplication.translate("MainWindow", u"Realizar pesagem", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Imprimir pesagem", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Ultima pesagem realizada em: Ainda n\u00e3o houve pesagem", None))
        self.label_56.setText("")
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Historico de Observa\u00e7\u00f5es", None))
        ___qtablewidgetitem55 = self.tableWidget_6.horizontalHeaderItem(0)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem56 = self.tableWidget_6.horizontalHeaderItem(1)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"Motorista", None));
        ___qtablewidgetitem57 = self.tableWidget_6.horizontalHeaderItem(2)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"OBSERVA\u00c7\u00c3O", None));
        self.aba_relatorio_button_7.setText(QCoreApplication.translate("MainWindow", u"Entrada", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Peso bruto ", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"(Entrada)", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"KG", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Insira os dados para a pesagem de entrada", None))
        self.input_entrada_motorista.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Motorista:", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Cliente:", None))
        self.comboBox_entrada_cliente.setItemText(0, QCoreApplication.translate("MainWindow", u"Nenhum", None))

        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Carga:", None))
        self.comboBox_entrada_carga.setItemText(0, QCoreApplication.translate("MainWindow", u"Nenhum", None))

        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Veiculo:", None))
        self.comboBox_entrada_veiculo.setItemText(0, QCoreApplication.translate("MainWindow", u"Nenhum", None))

        self.input_entrada_obs.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Observa\u00e7\u00e3o (Opcional)", None))
        self.btn_salvar_entrada.setText(QCoreApplication.translate("MainWindow", u"Salvar entrada", None))
        self.btn_historico_obs.setText("")
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Pesagens de ", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"(Entrada) ", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Realizadas", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Remover pesagem(s) Selecionada(s)", None))
        ___qtablewidgetitem58 = self.tableWidget_5.horizontalHeaderItem(0)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"Excluir", None));
        ___qtablewidgetitem59 = self.tableWidget_5.horizontalHeaderItem(1)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem60 = self.tableWidget_5.horizontalHeaderItem(2)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"Motorista", None));
        ___qtablewidgetitem61 = self.tableWidget_5.horizontalHeaderItem(3)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"Data da pesagem", None));
        self.aba_relatorio_button_9.setText(QCoreApplication.translate("MainWindow", u"Sa\u00edda", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Peso bruto ", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"(Sa\u00edda)", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"KG", None))
        self.comboBox_pesagem_entrada.setItemText(0, QCoreApplication.translate("MainWindow", u"Nenhum", None))
        self.comboBox_pesagem_entrada.setItemText(1, QCoreApplication.translate("MainWindow", u"New Item", None))

        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Selecione uma pesagem de entrada, e finalize com o peso de sa\u00edda.", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Pesagem:", None))
        self.segundos_7.setText(QCoreApplication.translate("MainWindow", u"Cliente:", None))
        self.text_saida_cliente.setText(QCoreApplication.translate("MainWindow", u"Caltec", None))
        self.segundos_5.setText(QCoreApplication.translate("MainWindow", u"Ve\u00edculo:", None))
        self.text_saida_veiculo.setText(QCoreApplication.translate("MainWindow", u"VOLVO", None))
        self.segundos_9.setText(QCoreApplication.translate("MainWindow", u"Carga:", None))
        self.text_saida_carga.setText(QCoreApplication.translate("MainWindow", u"Whisky", None))
        self.segundos_3.setText(QCoreApplication.translate("MainWindow", u"Motorista:", None))
        self.text_saida_motorista.setText(QCoreApplication.translate("MainWindow", u"Ryan", None))
        self.segundos_11.setText(QCoreApplication.translate("MainWindow", u"Peso ", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"(Entrada)", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.text_saida_pesoentrada.setText(QCoreApplication.translate("MainWindow", u"4000", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Abaixo Informa\u00e7\u00f5es da pesagem de entrada", None))
        self.btn_finalizar_pesagem.setText(QCoreApplication.translate("MainWindow", u"Finalizar pesagem", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Imprimir pesagem", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Pesagens pendentes", None))
        ___qtablewidgetitem62 = self.tableWidget_8.horizontalHeaderItem(0)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem63 = self.tableWidget_8.horizontalHeaderItem(1)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"Motorista", None));
        ___qtablewidgetitem64 = self.tableWidget_8.horizontalHeaderItem(2)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        self.title.setText(QCoreApplication.translate("MainWindow", u"Conta", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Informa\u00e7\u00f5es da conta", None))
        self.label_12.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"NOME EMPRESA / PESSOAL", None))
        self.text_empresa_pessoal.setText(QCoreApplication.translate("MainWindow", u"rbsservices", None))
        self.btn_alterar_nome.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"E-MAIL", None))
        self.text_email.setText(QCoreApplication.translate("MainWindow", u"rybala63@gmail.com", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"TELEFONE / WHATSAPP", None))
        self.text_telefone.setText(QCoreApplication.translate("MainWindow", u"11990132993", None))
        self.btn_alterar_telefone.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"LICEN\u00c7A", None))
        self.btn_atualizar_licenca.setText(QCoreApplication.translate("MainWindow", u"Atualizar para vers\u00e3o PREMIUM", None))
        self.text_licenca.setText(QCoreApplication.translate("MainWindow", u"Gratuita", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"SENHA", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Deseja alterar a senha de acesso?", None))
        self.btn_alterar_senha.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"REMO\u00c7\u00c3O DA CONTA", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Deseja excluir sua conta permanentemente?", None))
        self.btn_excluir_conta.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.label_logo_saida.setText("")
        self.label_realizada_ou_erro.setText(QCoreApplication.translate("MainWindow", u"Pesagem realizada", None))
        self.label_veja_no_relatorio.setText(QCoreApplication.translate("MainWindow", u"Veja em relat\u00f3rio avulsas", None))
        self.pushButton_3.setText("")
        self.segundos.setText(QCoreApplication.translate("MainWindow", u"30 Segundos", None))
        self.label_9.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Hor\u00e1rio", None))
        self.hora.setText(QCoreApplication.translate("MainWindow", u"14:14:50", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.data.setText(QCoreApplication.translate("MainWindow", u"17/06/2022", None))
    # retranslateUi

