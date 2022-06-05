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
        MainWindow.resize(950, 718)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
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
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.menu_frame = QFrame(self.centralwidget)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setMaximumSize(QSize(200, 999999))
        font = QFont()
        font.setPointSize(11)
        self.menu_frame.setFont(font)
        self.menu_frame.setStyleSheet(u"background-color: rgb(231, 231, 231);\n"
"")
        self.menu_frame.setFrameShape(QFrame.NoFrame)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.menu_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menuTop_frame = QFrame(self.menu_frame)
        self.menuTop_frame.setObjectName(u"menuTop_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.menuTop_frame.sizePolicy().hasHeightForWidth())
        self.menuTop_frame.setSizePolicy(sizePolicy1)
        self.menuTop_frame.setFrameShape(QFrame.NoFrame)
        self.menuTop_frame.setFrameShadow(QFrame.Plain)
        self.menuTop_frame.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.menuTop_frame)
        self.verticalLayout_3.setSpacing(9)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, 9, -1)
        self.frame_3 = QFrame(self.menuTop_frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_3)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.aba_pesagem_button = QPushButton(self.frame_3)
        self.aba_pesagem_button.setObjectName(u"aba_pesagem_button")
        self.aba_pesagem_button.setMinimumSize(QSize(160, 40))
        font1 = QFont()
        font1.setFamily(u"Century Gothic")
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.aba_pesagem_button.setFont(font1)
        self.aba_pesagem_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.aba_pesagem_button.setFocusPolicy(Qt.ClickFocus)
        self.aba_pesagem_button.setLayoutDirection(Qt.LeftToRight)
        self.aba_pesagem_button.setAutoFillBackground(False)
        self.aba_pesagem_button.setStyleSheet(u"QPushButton{\n"
"	border:0;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(250, 250, 250);\n"
"	border:1px solid;\n"
"	\n"
"}\n"
"")
        icon1 = QIcon()
        iconThemeName = u"lumos"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u":/icons/scale-balanced-solid (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        
        self.aba_pesagem_button.setIcon(icon1)
        self.aba_pesagem_button.setIconSize(QSize(20, 20))
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
        self.menu_pesagem_frame.setFrameShape(QFrame.NoFrame)
        self.menu_pesagem_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.menu_pesagem_frame)
        self.verticalLayout_8.setSpacing(2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.button_simples_pesagens = QPushButton(self.menu_pesagem_frame)
        self.button_simples_pesagens.setObjectName(u"button_simples_pesagens")
        self.button_simples_pesagens.setMinimumSize(QSize(0, 25))
        font2 = QFont()
        font2.setFamily(u"Century Gothic")
        font2.setPointSize(9)
        font2.setBold(False)
        font2.setWeight(50)
        self.button_simples_pesagens.setFont(font2)
        self.button_simples_pesagens.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(250, 250, 250);\n"
"	border:1px solid\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(231, 231, 231);\n"
"	color: rgb(15, 202, 2);\n"
"\n"
"}\n"
"")

        self.verticalLayout_8.addWidget(self.button_simples_pesagens)

        self.button_entsaid_pesagens = QPushButton(self.menu_pesagem_frame)
        self.button_entsaid_pesagens.setObjectName(u"button_entsaid_pesagens")
        self.button_entsaid_pesagens.setMinimumSize(QSize(0, 25))
        self.button_entsaid_pesagens.setFont(font2)
        self.button_entsaid_pesagens.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(250, 250, 250);\n"
"	border:1px solid\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(231, 231, 231);\n"
"	color: rgb(15, 202, 2);\n"
"\n"
"}\n"
"")

        self.verticalLayout_8.addWidget(self.button_entsaid_pesagens)

        self.button_avulsas_pesagens = QPushButton(self.menu_pesagem_frame)
        self.button_avulsas_pesagens.setObjectName(u"button_avulsas_pesagens")
        self.button_avulsas_pesagens.setMinimumSize(QSize(130, 25))
        self.button_avulsas_pesagens.setMaximumSize(QSize(100, 16777215))
        self.button_avulsas_pesagens.setFont(font2)
        self.button_avulsas_pesagens.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(250, 250, 250);\n"
"	border:1px solid\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(231, 231, 231);\n"
"	color: rgb(15, 202, 2);\n"
"\n"
"}\n"
"")

        self.verticalLayout_8.addWidget(self.button_avulsas_pesagens)


        self.verticalLayout_9.addWidget(self.menu_pesagem_frame, 0, Qt.AlignRight)


        self.verticalLayout_3.addWidget(self.frame_3, 0, Qt.AlignTop)

        self.frame_4 = QFrame(self.menuTop_frame)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy2.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy2)
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_4)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.aba_grupo_button = QPushButton(self.frame_4)
        self.aba_grupo_button.setObjectName(u"aba_grupo_button")
        self.aba_grupo_button.setMinimumSize(QSize(160, 40))
        self.aba_grupo_button.setFont(font1)
        self.aba_grupo_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.aba_grupo_button.setStyleSheet(u"QPushButton{\n"
"	border:0;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(250, 250, 250);\n"
"	border:1px solid;\n"
"\n"
"}\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/layer-group-solid (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.aba_grupo_button.setIcon(icon2)
        self.aba_grupo_button.setIconSize(QSize(20, 20))
        self.aba_grupo_button.setFlat(False)

        self.verticalLayout_10.addWidget(self.aba_grupo_button)

        self.menu_grupos_frame = QFrame(self.frame_4)
        self.menu_grupos_frame.setObjectName(u"menu_grupos_frame")
        sizePolicy3.setHeightForWidth(self.menu_grupos_frame.sizePolicy().hasHeightForWidth())
        self.menu_grupos_frame.setSizePolicy(sizePolicy3)
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
        self.button_clientes_grupos.setFont(font2)
        self.button_clientes_grupos.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(250, 250, 250);\n"
"	border:1px solid\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(231, 231, 231);\n"
"	color: rgb(15, 202, 2);\n"
"\n"
"}\n"
"")

        self.verticalLayout_7.addWidget(self.button_clientes_grupos)

        self.button_produtos_grupos = QPushButton(self.menu_grupos_frame)
        self.button_produtos_grupos.setObjectName(u"button_produtos_grupos")
        self.button_produtos_grupos.setMinimumSize(QSize(0, 25))
        self.button_produtos_grupos.setFont(font2)
        self.button_produtos_grupos.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(250, 250, 250);\n"
"	border:1px solid\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(231, 231, 231);\n"
"	color: rgb(15, 202, 2);\n"
"\n"
"}\n"
"")

        self.verticalLayout_7.addWidget(self.button_produtos_grupos)

        self.button_fornecedores_grupos = QPushButton(self.menu_grupos_frame)
        self.button_fornecedores_grupos.setObjectName(u"button_fornecedores_grupos")
        self.button_fornecedores_grupos.setMinimumSize(QSize(0, 25))
        self.button_fornecedores_grupos.setFont(font2)
        self.button_fornecedores_grupos.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(250, 250, 250);\n"
"	border:1px solid\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(231, 231, 231);\n"
"	color: rgb(15, 202, 2);\n"
"\n"
"}\n"
"")

        self.verticalLayout_7.addWidget(self.button_fornecedores_grupos)

        self.button_veiculos_grupos = QPushButton(self.menu_grupos_frame)
        self.button_veiculos_grupos.setObjectName(u"button_veiculos_grupos")
        self.button_veiculos_grupos.setMinimumSize(QSize(130, 25))
        self.button_veiculos_grupos.setMaximumSize(QSize(100, 16777215))
        self.button_veiculos_grupos.setFont(font2)
        self.button_veiculos_grupos.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(250, 250, 250);\n"
"	border:1px solid\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(231, 231, 231);\n"
"	color: rgb(15, 202, 2);\n"
"\n"
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
        self.aba_relatorio_button.setFont(font1)
        self.aba_relatorio_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.aba_relatorio_button.setLayoutDirection(Qt.LeftToRight)
        self.aba_relatorio_button.setStyleSheet(u"QPushButton{\n"
"	border:0;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(250, 250, 250);\n"
"	border:1px solid;\n"
"\n"
"}\n"
"\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/file-lines-solid (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.aba_relatorio_button.setIcon(icon3)
        self.aba_relatorio_button.setIconSize(QSize(20, 20))
        self.aba_relatorio_button.setFlat(False)

        self.verticalLayout_3.addWidget(self.aba_relatorio_button)

        self.aba_conta_button = QPushButton(self.menuTop_frame)
        self.aba_conta_button.setObjectName(u"aba_conta_button")
        self.aba_conta_button.setMinimumSize(QSize(160, 40))
        self.aba_conta_button.setFont(font1)
        self.aba_conta_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.aba_conta_button.setStyleSheet(u"QPushButton{\n"
"	border:0;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(250, 250, 250);\n"
"	border:1px solid;\n"
"\n"
"}\n"
"\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/person-walking-solid (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.aba_conta_button.setIcon(icon4)
        self.aba_conta_button.setIconSize(QSize(20, 20))
        self.aba_conta_button.setAutoExclusive(True)
        self.aba_conta_button.setFlat(False)

        self.verticalLayout_3.addWidget(self.aba_conta_button)


        self.verticalLayout_2.addWidget(self.menuTop_frame, 0, Qt.AlignVCenter)

        self.info_menu_pro_frame = QFrame(self.menu_frame)
        self.info_menu_pro_frame.setObjectName(u"info_menu_pro_frame")
        self.info_menu_pro_frame.setMaximumSize(QSize(16777215, 115))
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
        self.info_pro_frame.setMaximumSize(QSize(16777215, 30))
        self.info_pro_frame.setFrameShape(QFrame.StyledPanel)
        self.info_pro_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.info_pro_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.info_pro_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(25, 25))
        self.label_4.setTextFormat(Qt.AutoText)
        self.label_4.setPixmap(QPixmap(u":/icons/circle-info-solid.svg"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.restantes_label = QLabel(self.info_pro_frame)
        self.restantes_label.setObjectName(u"restantes_label")
        self.restantes_label.setMaximumSize(QSize(122, 150))
        font3 = QFont()
        font3.setFamily(u"Century Gothic")
        font3.setBold(True)
        font3.setWeight(75)
        self.restantes_label.setFont(font3)
        self.restantes_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.restantes_label)


        self.verticalLayout_5.addWidget(self.info_pro_frame)

        self.info_pro_label = QLabel(self.info_menu_pro_frame)
        self.info_pro_label.setObjectName(u"info_pro_label")
        font4 = QFont()
        font4.setFamily(u"Century Gothic")
        font4.setPointSize(11)
        self.info_pro_label.setFont(font4)
        self.info_pro_label.setLineWidth(0)
        self.info_pro_label.setAlignment(Qt.AlignCenter)
        self.info_pro_label.setWordWrap(True)
        self.info_pro_label.setMargin(1)

        self.verticalLayout_5.addWidget(self.info_pro_label)


        self.verticalLayout_2.addWidget(self.info_menu_pro_frame, 0, Qt.AlignBottom)

        self.menuEnd_frame = QFrame(self.menu_frame)
        self.menuEnd_frame.setObjectName(u"menuEnd_frame")
        self.menuEnd_frame.setFrameShape(QFrame.NoFrame)
        self.menuEnd_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.menuEnd_frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.aba_sair_button = QPushButton(self.menuEnd_frame)
        self.aba_sair_button.setObjectName(u"aba_sair_button")
        self.aba_sair_button.setMinimumSize(QSize(60, 40))
        self.aba_sair_button.setFont(font1)
        self.aba_sair_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.aba_sair_button.setStyleSheet(u"QPushButton{\n"
"	border:0;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(250, 250, 250);\n"
"	border:1px solid;\n"
"\n"
"}\n"
"\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/person-walking-arrow-right-solid (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.aba_sair_button.setIcon(icon5)
        self.aba_sair_button.setIconSize(QSize(25, 25))
        self.aba_sair_button.setFlat(False)

        self.verticalLayout_4.addWidget(self.aba_sair_button, 0, Qt.AlignBottom)


        self.verticalLayout_2.addWidget(self.menuEnd_frame, 0, Qt.AlignBottom)

        self.menuEnd_frame.raise_()
        self.menuTop_frame.raise_()
        self.info_menu_pro_frame.raise_()

        self.gridLayout.addWidget(self.menu_frame, 2, 0, 1, 1)

        self.principal_frame = QFrame(self.centralwidget)
        self.principal_frame.setObjectName(u"principal_frame")
        self.principal_frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.principal_frame.setFrameShape(QFrame.NoFrame)
        self.principal_frame.setFrameShadow(QFrame.Raised)
        self.principal_frame.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.principal_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.info_frame = QFrame(self.principal_frame)
        self.info_frame.setObjectName(u"info_frame")
        self.info_frame.setMaximumSize(QSize(16777215, 40))
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
        self.stackedWidget.setStyleSheet(u"background-color: rgb(231, 231, 231);\n"
"")
        self.page_relatorio = QWidget()
        self.page_relatorio.setObjectName(u"page_relatorio")
        self.page_relatorio.setStyleSheet(u"background-color: rgb(231, 231, 231);\n"
"border: 1px solid rgb(181, 181, 181)")
        self.verticalLayout_11 = QVBoxLayout(self.page_relatorio)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.page_relatorio)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"border:0")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_6)
        self.verticalLayout_13.setSpacing(11)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_6)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 45))
        self.frame_5.setMaximumSize(QSize(16777215, 45))
        self.frame_5.setStyleSheet(u"background-color: rgb(43, 43, 43);\n"
"color: rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_5)
        self.verticalLayout_12.setSpacing(7)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.aba_relatorio_button_2 = QPushButton(self.frame_5)
        self.aba_relatorio_button_2.setObjectName(u"aba_relatorio_button_2")
        self.aba_relatorio_button_2.setMinimumSize(QSize(160, 45))
        self.aba_relatorio_button_2.setMaximumSize(QSize(5555, 45))
        self.aba_relatorio_button_2.setBaseSize(QSize(555, 2))
        font5 = QFont()
        font5.setFamily(u"Century Gothic")
        font5.setPointSize(17)
        font5.setBold(True)
        font5.setWeight(75)
        self.aba_relatorio_button_2.setFont(font5)
        self.aba_relatorio_button_2.setLayoutDirection(Qt.LeftToRight)
        self.aba_relatorio_button_2.setStyleSheet(u"QPushButton{\n"
"	border:0;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/file-lines-solid (2).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.aba_relatorio_button_2.setIcon(icon6)
        self.aba_relatorio_button_2.setIconSize(QSize(29, 28))
        self.aba_relatorio_button_2.setFlat(False)

        self.verticalLayout_12.addWidget(self.aba_relatorio_button_2, 0, Qt.AlignTop)


        self.verticalLayout_13.addWidget(self.frame_5)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 105))
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_7)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(10)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 13))
        font6 = QFont()
        font6.setFamily(u"Century Gothic")
        font6.setPointSize(10)
        self.label_5.setFont(font6)

        self.gridLayout_3.addWidget(self.label_5, 0, 2, 1, 1)

        self.comboBox_produto = QComboBox(self.frame_7)
        self.comboBox_produto.addItem("")
        self.comboBox_produto.addItem("")
        self.comboBox_produto.addItem("")
        self.comboBox_produto.setObjectName(u"comboBox_produto")
        self.comboBox_produto.setStyleSheet(u"QComboBox{\n"
"	border:1px solid rgb(15, 202, 2);\n"
"	padding-left:10px;\n"
"	font-size:13px;\n"
"	\n"
"	font: 10pt \"Century Gothic\";\n"
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
        self.comboBox_produto.setMaxVisibleItems(10)
        self.comboBox_produto.setInsertPolicy(QComboBox.NoInsert)
        self.comboBox_produto.setIconSize(QSize(32, 32))
        self.comboBox_produto.setDuplicatesEnabled(True)
        self.comboBox_produto.setFrame(True)

        self.gridLayout_3.addWidget(self.comboBox_produto, 1, 3, 1, 1)

        self.comboBox_cliente = QComboBox(self.frame_7)
        self.comboBox_cliente.addItem("")
        self.comboBox_cliente.addItem("")
        self.comboBox_cliente.addItem("")
        self.comboBox_cliente.setObjectName(u"comboBox_cliente")
        self.comboBox_cliente.setStyleSheet(u"QComboBox{\n"
"	border:1px solid rgb(15, 202, 2);\n"
"	padding-left:10px;\n"
"	font-size:13px;\n"
"	\n"
"	font: 10pt \"Century Gothic\";\n"
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
        self.comboBox_cliente.setMaxVisibleItems(10)
        self.comboBox_cliente.setInsertPolicy(QComboBox.NoInsert)
        self.comboBox_cliente.setIconSize(QSize(32, 32))
        self.comboBox_cliente.setDuplicatesEnabled(True)
        self.comboBox_cliente.setFrame(True)

        self.gridLayout_3.addWidget(self.comboBox_cliente, 1, 2, 1, 1)

        self.comboBox_fornecedor = QComboBox(self.frame_7)
        self.comboBox_fornecedor.addItem("")
        self.comboBox_fornecedor.addItem("")
        self.comboBox_fornecedor.addItem("")
        self.comboBox_fornecedor.setObjectName(u"comboBox_fornecedor")
        self.comboBox_fornecedor.setStyleSheet(u"QComboBox{\n"
"	border:1px solid rgb(15, 202, 2);\n"
"	padding-left:10px;\n"
"	font-size:13px;\n"
"	\n"
"	font: 10pt \"Century Gothic\";\n"
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
        self.comboBox_fornecedor.setMaxVisibleItems(10)
        self.comboBox_fornecedor.setInsertPolicy(QComboBox.NoInsert)
        self.comboBox_fornecedor.setIconSize(QSize(32, 32))
        self.comboBox_fornecedor.setDuplicatesEnabled(True)
        self.comboBox_fornecedor.setFrame(True)

        self.gridLayout_3.addWidget(self.comboBox_fornecedor, 1, 4, 1, 1)

        self.comboBox_veiculo = QComboBox(self.frame_7)
        self.comboBox_veiculo.addItem("")
        self.comboBox_veiculo.addItem("")
        self.comboBox_veiculo.addItem("")
        self.comboBox_veiculo.setObjectName(u"comboBox_veiculo")
        self.comboBox_veiculo.setStyleSheet(u"QComboBox{\n"
"	border:1px solid rgb(15, 202, 2);\n"
"	padding-left:10px;\n"
"	font-size:13px;\n"
"	\n"
"	font: 10pt \"Century Gothic\";\n"
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
        self.comboBox_veiculo.setMaxVisibleItems(10)
        self.comboBox_veiculo.setInsertPolicy(QComboBox.NoInsert)
        self.comboBox_veiculo.setIconSize(QSize(32, 32))
        self.comboBox_veiculo.setDuplicatesEnabled(True)
        self.comboBox_veiculo.setFrame(True)

        self.gridLayout_3.addWidget(self.comboBox_veiculo, 1, 5, 1, 1)

        self.label_6 = QLabel(self.frame_7)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 13))
        self.label_6.setFont(font6)

        self.gridLayout_3.addWidget(self.label_6, 0, 3, 1, 1)

        self.label_7 = QLabel(self.frame_7)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 13))
        self.label_7.setFont(font6)

        self.gridLayout_3.addWidget(self.label_7, 0, 4, 1, 1)

        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 13))
        self.label_8.setFont(font6)

        self.gridLayout_3.addWidget(self.label_8, 0, 5, 1, 1)

        self.label_9 = QLabel(self.frame_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font6)

        self.gridLayout_3.addWidget(self.label_9, 2, 0, 1, 1)

        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(100, 16777215))
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_8)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(0)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_filtro_id = QPushButton(self.frame_8)
        self.btn_filtro_id.setObjectName(u"btn_filtro_id")
        self.btn_filtro_id.setMaximumSize(QSize(16777215, 16))
        self.btn_filtro_id.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/magnifying-glass-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_filtro_id.setIcon(icon7)
        self.btn_filtro_id.setIconSize(QSize(16, 16))

        self.gridLayout_4.addWidget(self.btn_filtro_id, 1, 1, 1, 1)

        self.text_filtro_id = QLineEdit(self.frame_8)
        self.text_filtro_id.setObjectName(u"text_filtro_id")
        self.text_filtro_id.setMaximumSize(QSize(50, 16777215))
        self.text_filtro_id.setFont(font6)
        self.text_filtro_id.setStyleSheet(u"\n"
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
        self.text_filtro_id.setMaxLength(6)

        self.gridLayout_4.addWidget(self.text_filtro_id, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_8, 3, 0, 1, 1, Qt.AlignLeft)

        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(200, 57))
        self.frame_10.setMaximumSize(QSize(188, 16777215))
        font7 = QFont()
        font7.setFamily(u"Microsoft Yi Baiti")
        self.frame_10.setFont(font7)
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_10)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 10, 0)
        self.data_fixa = QRadioButton(self.frame_10)
        self.data_fixa.setObjectName(u"data_fixa")
        font8 = QFont()
        font8.setFamily(u"Century Gothic")
        font8.setPointSize(9)
        font8.setBold(False)
        font8.setItalic(False)
        font8.setWeight(50)
        self.data_fixa.setFont(font8)

        self.gridLayout_5.addWidget(self.data_fixa, 0, 0, 1, 1)

        self.data_antes_de = QRadioButton(self.frame_10)
        self.data_antes_de.setObjectName(u"data_antes_de")
        self.data_antes_de.setMinimumSize(QSize(0, 1))
        self.data_antes_de.setFont(font8)

        self.gridLayout_5.addWidget(self.data_antes_de, 1, 0, 1, 1)

        self.text_date = QDateEdit(self.frame_10)
        self.text_date.setObjectName(u"text_date")
        self.text_date.setMinimumSize(QSize(0, 19))
        self.text_date.setStyleSheet(u"QDateEdit{\n"
"	border:1px solid rgb(15, 202, 2);\n"
"	padding-left:10px;\n"
"	font-size:13px;\n"
"	\n"
"	font: 10pt \"Century Gothic\";\n"
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
        self.text_date.setWrapping(False)
        self.text_date.setAlignment(Qt.AlignCenter)
        self.text_date.setReadOnly(False)
        self.text_date.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.text_date.setAccelerated(True)
        self.text_date.setKeyboardTracking(True)
        self.text_date.setProperty("showGroupSeparator", True)
        self.text_date.setDateTime(QDateTime(QDate(2022, 1, 1), QTime(0, 0, 0)))

        self.gridLayout_5.addWidget(self.text_date, 1, 1, 1, 1)

        self.data_depois_de = QRadioButton(self.frame_10)
        self.data_depois_de.setObjectName(u"data_depois_de")
        self.data_depois_de.setMinimumSize(QSize(0, 1))
        self.data_depois_de.setFont(font8)

        self.gridLayout_5.addWidget(self.data_depois_de, 2, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_10, 1, 7, 1, 1)

        self.label_10 = QLabel(self.frame_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 13))
        self.label_10.setFont(font6)

        self.gridLayout_3.addWidget(self.label_10, 0, 7, 1, 1)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 26))
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_Aplicar_filtro_geral = QPushButton(self.frame_9)
        self.btn_Aplicar_filtro_geral.setObjectName(u"btn_Aplicar_filtro_geral")
        self.btn_Aplicar_filtro_geral.setFont(font1)
        self.btn_Aplicar_filtro_geral.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Aplicar_filtro_geral.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(250, 250, 250);\n"
"	border:1px solid rgb(67, 202, 0);\n"
"	padding:5px\n"
"}\n"
"QPushButton::hover{\n"
"	color: rgb(15, 202, 2)\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/icons/filter-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Aplicar_filtro_geral.setIcon(icon8)

        self.horizontalLayout_4.addWidget(self.btn_Aplicar_filtro_geral)

        self.btn_inprimir = QPushButton(self.frame_9)
        self.btn_inprimir.setObjectName(u"btn_inprimir")
        self.btn_inprimir.setFont(font1)
        self.btn_inprimir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_inprimir.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(250, 250, 250);\n"
"	border:1px solid;\n"
"	padding:5px\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(209, 209, 209);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/icons/print-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_inprimir.setIcon(icon9)

        self.horizontalLayout_4.addWidget(self.btn_inprimir)


        self.gridLayout_3.addWidget(self.frame_9, 3, 2, 1, 4)


        self.verticalLayout_13.addWidget(self.frame_7)

        self.tableWidget = QTableWidget(self.frame_6)
        if (self.tableWidget.columnCount() < 11):
            self.tableWidget.setColumnCount(11)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        font9 = QFont()
        font9.setBold(True)
        font9.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font9);
        __qtablewidgetitem.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font9);
        __qtablewidgetitem1.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font9);
        __qtablewidgetitem2.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font9);
        __qtablewidgetitem3.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font9);
        __qtablewidgetitem4.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font9);
        __qtablewidgetitem5.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font9);
        __qtablewidgetitem6.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font9);
        __qtablewidgetitem7.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font9);
        __qtablewidgetitem8.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font9);
        __qtablewidgetitem9.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font9);
        __qtablewidgetitem10.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        if (self.tableWidget.rowCount() < 4):
            self.tableWidget.setRowCount(4)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setItem(0, 4, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 5, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 6, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 7, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 8, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setItem(0, 9, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget.setItem(0, 10, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget.setItem(1, 2, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget.setItem(1, 3, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget.setItem(1, 4, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget.setItem(1, 5, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget.setItem(1, 6, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget.setItem(1, 7, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget.setItem(1, 8, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget.setItem(1, 9, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget.setItem(1, 10, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget.setItem(2, 2, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget.setItem(2, 3, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget.setItem(2, 4, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget.setItem(2, 5, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget.setItem(2, 6, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget.setItem(2, 7, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget.setItem(2, 8, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget.setItem(2, 9, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget.setItem(2, 10, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tableWidget.setItem(3, 0, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tableWidget.setItem(3, 1, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tableWidget.setItem(3, 2, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tableWidget.setItem(3, 3, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tableWidget.setItem(3, 4, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tableWidget.setItem(3, 5, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tableWidget.setItem(3, 6, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tableWidget.setItem(3, 7, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tableWidget.setItem(3, 8, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tableWidget.setItem(3, 9, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tableWidget.setItem(3, 10, __qtablewidgetitem58)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy4)
        self.tableWidget.setMinimumSize(QSize(0, 120))
        self.tableWidget.setMaximumSize(QSize(20000, 16777215))
        font10 = QFont()
        font10.setFamily(u"Century Gothic")
        font10.setPointSize(10)
        font10.setBold(False)
        font10.setItalic(False)
        font10.setWeight(50)
        self.tableWidget.setFont(font10)
        self.tableWidget.setStyleSheet(u"QTableWidget{\n"
"	font: 10pt \"Century Gothic\";\n"
"	outline:0;\n"
"}\n"
"QHeaderView::section {\n"
"	color:white;\n"
"	border:1px solid white;\n"
"	background-color: rgb(15, 202, 2);\n"
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
"    borde"
                        "r: 1px solid #999999;\n"
"    background:white;\n"
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
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setAutoScrollMargin(22)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(True)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setDragDropOverwriteMode(True)
        self.tableWidget.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setTextElideMode(Qt.ElideRight)
        self.tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(11)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(90)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(98)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_13.addWidget(self.tableWidget)


        self.verticalLayout_11.addWidget(self.frame_6)

        self.stackedWidget.addWidget(self.page_relatorio)
        self.page_clientes = QWidget()
        self.page_clientes.setObjectName(u"page_clientes")
        self.page_clientes.setStyleSheet(u"border:0")
        self.verticalLayout_22 = QVBoxLayout(self.page_clientes)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.page_clientes)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_22)
        self.verticalLayout_24.setSpacing(7)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.frame_22)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(0, 45))
        self.frame_23.setMaximumSize(QSize(16777215, 45))
        font11 = QFont()
        font11.setPointSize(13)
        self.frame_23.setFont(font11)
        self.frame_23.setStyleSheet(u"background-color: rgb(43, 43, 43);\n"
"color: rgb(255, 255, 255);")
        self.frame_23.setFrameShape(QFrame.NoFrame)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_23)
        self.verticalLayout_23.setSpacing(7)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.aba_relatorio_button_3 = QPushButton(self.frame_23)
        self.aba_relatorio_button_3.setObjectName(u"aba_relatorio_button_3")
        self.aba_relatorio_button_3.setMinimumSize(QSize(160, 45))
        self.aba_relatorio_button_3.setMaximumSize(QSize(5555, 45))
        self.aba_relatorio_button_3.setBaseSize(QSize(555, 2))
        self.aba_relatorio_button_3.setFont(font5)
        self.aba_relatorio_button_3.setLayoutDirection(Qt.LeftToRight)
        self.aba_relatorio_button_3.setStyleSheet(u"QPushButton{\n"
"	border:0;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/icons/layer-group-solid .svg", QSize(), QIcon.Normal, QIcon.Off)
        self.aba_relatorio_button_3.setIcon(icon10)
        self.aba_relatorio_button_3.setIconSize(QSize(29, 28))
        self.aba_relatorio_button_3.setFlat(False)

        self.verticalLayout_23.addWidget(self.aba_relatorio_button_3, 0, Qt.AlignTop)


        self.verticalLayout_24.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.frame_22)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMaximumSize(QSize(1677777, 16777215))
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
        self.frame_43.setFrameShape(QFrame.Panel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_43)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.frame_47 = QFrame(self.frame_43)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setMinimumSize(QSize(0, 0))
        self.frame_47.setMaximumSize(QSize(16777215, 30))
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_47)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.frame_47)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font1)

        self.verticalLayout_47.addWidget(self.label_18, 0, Qt.AlignHCenter)


        self.verticalLayout_46.addWidget(self.frame_47)

        self.frame_48 = QFrame(self.frame_43)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_48)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.frame_51 = QFrame(self.frame_48)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_51)
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.input_clientes_nome = QLineEdit(self.frame_51)
        self.input_clientes_nome.setObjectName(u"input_clientes_nome")
        font12 = QFont()
        font12.setFamily(u"Century Gothic")
        font12.setPointSize(11)
        font12.setBold(False)
        font12.setWeight(50)
        self.input_clientes_nome.setFont(font12)
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
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_56)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, -1, 0, 0)
        self.input_clientes_cpf = QLineEdit(self.frame_56)
        self.input_clientes_cpf.setObjectName(u"input_clientes_cpf")
        self.input_clientes_cpf.setFont(font12)
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
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_50)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.input_clientes_rg = QLineEdit(self.frame_50)
        self.input_clientes_rg.setObjectName(u"input_clientes_rg")
        self.input_clientes_rg.setFont(font12)
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
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.frame_55)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.input_clientes_endereco = QLineEdit(self.frame_55)
        self.input_clientes_endereco.setObjectName(u"input_clientes_endereco")
        self.input_clientes_endereco.setFont(font12)
        self.input_clientes_endereco.setStyleSheet(u"QLineEdit{padding:3px;border:1px solid;background-color: rgb(243, 243, 243);}\n"
"\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")
        self.input_clientes_endereco.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_52.addWidget(self.input_clientes_endereco)


        self.verticalLayout_49.addWidget(self.frame_55)

        self.frame_53 = QFrame(self.frame_48)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_53)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.input_clientes_cidade = QLineEdit(self.frame_53)
        self.input_clientes_cidade.setObjectName(u"input_clientes_cidade")
        self.input_clientes_cidade.setFont(font12)
        self.input_clientes_cidade.setStyleSheet(u"QLineEdit{padding:3px;border:1px solid;background-color: rgb(243, 243, 243);}\n"
"\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")
        self.input_clientes_cidade.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_53.addWidget(self.input_clientes_cidade)


        self.verticalLayout_49.addWidget(self.frame_53)

        self.frame_54 = QFrame(self.frame_48)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.frame_54)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.input_clientes_estado = QLineEdit(self.frame_54)
        self.input_clientes_estado.setObjectName(u"input_clientes_estado")
        self.input_clientes_estado.setFont(font12)
        self.input_clientes_estado.setStyleSheet(u"QLineEdit{padding:3px;border:1px solid;background-color: rgb(243, 243, 243);}\n"
"\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")
        self.input_clientes_estado.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_54.addWidget(self.input_clientes_estado)


        self.verticalLayout_49.addWidget(self.frame_54)

        self.frame_52 = QFrame(self.frame_48)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_52)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.input_clientes_telefone = QLineEdit(self.frame_52)
        self.input_clientes_telefone.setObjectName(u"input_clientes_telefone")
        self.input_clientes_telefone.setFont(font12)
        self.input_clientes_telefone.setStyleSheet(u"QLineEdit{padding:3px;border:1px solid;background-color: rgb(243, 243, 243);}\n"
"\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")
        self.input_clientes_telefone.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_55.addWidget(self.input_clientes_telefone)


        self.verticalLayout_49.addWidget(self.frame_52)

        self.btn_registrar_clientes = QPushButton(self.frame_48)
        self.btn_registrar_clientes.setObjectName(u"btn_registrar_clientes")
        font13 = QFont()
        font13.setFamily(u"Century Gothic")
        font13.setPointSize(10)
        font13.setBold(True)
        font13.setWeight(75)
        self.btn_registrar_clientes.setFont(font13)
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
        self.btn_menu_registrar_clientes.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu_registrar_clientes.setStyleSheet(u"border-radius:2px;\n"
"background-color: rgb(43, 43, 43);")
        icon11 = QIcon()
        icon11.addFile(u":/icons/caret-left-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu_registrar_clientes.setIcon(icon11)

        self.horizontalLayout_6.addWidget(self.btn_menu_registrar_clientes)

        self.frame_46 = QFrame(self.frame_24)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_46)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(9, -1, -1, -1)
        self.widget = QWidget(self.frame_46)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 60))
        self.gridLayout_10 = QGridLayout(self.widget)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_16 = QLabel(self.widget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(30, 30))
        self.label_16.setPixmap(QPixmap(u":/icons/clock-rotate-left-solid.svg"))
        self.label_16.setScaledContents(True)

        self.gridLayout_10.addWidget(self.label_16, 0, 0, 1, 1)

        self.label_14 = QLabel(self.widget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)

        self.gridLayout_10.addWidget(self.label_14, 0, 1, 1, 1)


        self.verticalLayout_45.addWidget(self.widget, 0, Qt.AlignHCenter)

        self.btn_remover_clientes = QPushButton(self.frame_46)
        self.btn_remover_clientes.setObjectName(u"btn_remover_clientes")
        self.btn_remover_clientes.setMaximumSize(QSize(240, 16777215))
        self.btn_remover_clientes.setFont(font2)
        self.btn_remover_clientes.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_remover_clientes.setStyleSheet(u"QPushButton{\n"
"border:1px solid red;\n"
"padding:5px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	background-color: rgb(255, 135, 135);\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/icons/trash-can-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_remover_clientes.setIcon(icon12)
        self.btn_remover_clientes.setIconSize(QSize(25, 22))

        self.verticalLayout_45.addWidget(self.btn_remover_clientes, 0, Qt.AlignRight)

        self.tableWidget_2 = QTableWidget(self.frame_46)
        if (self.tableWidget_2.columnCount() < 9):
            self.tableWidget_2.setColumnCount(9)
        __qtablewidgetitem59 = QTableWidgetItem()
        __qtablewidgetitem59.setFont(font9);
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        __qtablewidgetitem60.setFont(font9);
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        __qtablewidgetitem61.setFont(font9);
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        __qtablewidgetitem62.setFont(font9);
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        __qtablewidgetitem63.setFont(font9);
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        __qtablewidgetitem64.setFont(font9);
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        __qtablewidgetitem65.setFont(font9);
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        __qtablewidgetitem66.setFont(font9);
        self.tableWidget_2.setHorizontalHeaderItem(7, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        __qtablewidgetitem67.setFont(font9);
        self.tableWidget_2.setHorizontalHeaderItem(8, __qtablewidgetitem67)
        if (self.tableWidget_2.rowCount() < 2):
            self.tableWidget_2.setRowCount(2)
        __qtablewidgetitem68 = QTableWidgetItem()
        __qtablewidgetitem68.setCheckState(Qt.Unchecked);
        self.tableWidget_2.setItem(0, 0, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 1, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 2, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 3, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 4, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 5, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 6, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 7, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 8, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        __qtablewidgetitem77.setCheckState(Qt.Unchecked);
        self.tableWidget_2.setItem(1, 0, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 1, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 2, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 3, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 4, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 5, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 6, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 7, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 8, __qtablewidgetitem85)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setMaximumSize(QSize(16777215, 1999999))
        self.tableWidget_2.setStyleSheet(u"QTableWidget{\n"
"	font: 10pt \"Century Gothic\";\n"
"	outline:0;\n"
"}\n"
"QHeaderView::section {\n"
"	color:white;\n"
"	border:1px solid white;\n"
"	background-color: rgb(15, 202, 2);\n"
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
"    borde"
                        "r: 1px solid #999999;\n"
"    background:white;\n"
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
        self.tableWidget_2.setAutoScroll(True)
        self.tableWidget_2.setAutoScrollMargin(20)
        self.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.tableWidget_2.setDefaultDropAction(Qt.IgnoreAction)
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_2.setTextElideMode(Qt.ElideRight)
        self.tableWidget_2.setSortingEnabled(True)
        self.tableWidget_2.setRowCount(2)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(95)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(115)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)

        self.verticalLayout_45.addWidget(self.tableWidget_2)


        self.horizontalLayout_6.addWidget(self.frame_46)


        self.verticalLayout_24.addWidget(self.frame_24)


        self.verticalLayout_22.addWidget(self.frame_22)

        self.stackedWidget.addWidget(self.page_clientes)
        self.page_fornecedores = QWidget()
        self.page_fornecedores.setObjectName(u"page_fornecedores")
        self.page_fornecedores.setStyleSheet(u"border:0")
        self.verticalLayout_27 = QVBoxLayout(self.page_fornecedores)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frame_25 = QFrame(self.page_fornecedores)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_25)
        self.verticalLayout_25.setSpacing(7)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_26 = QFrame(self.frame_25)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMinimumSize(QSize(0, 45))
        self.frame_26.setMaximumSize(QSize(16777215, 45))
        self.frame_26.setStyleSheet(u"background-color: rgb(43, 43, 43);\n"
"color: rgb(255, 255, 255);")
        self.frame_26.setFrameShape(QFrame.NoFrame)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_26)
        self.verticalLayout_26.setSpacing(7)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.aba_relatorio_button_4 = QPushButton(self.frame_26)
        self.aba_relatorio_button_4.setObjectName(u"aba_relatorio_button_4")
        self.aba_relatorio_button_4.setMinimumSize(QSize(160, 45))
        self.aba_relatorio_button_4.setMaximumSize(QSize(5555, 45))
        self.aba_relatorio_button_4.setBaseSize(QSize(555, 2))
        self.aba_relatorio_button_4.setFont(font5)
        self.aba_relatorio_button_4.setLayoutDirection(Qt.LeftToRight)
        self.aba_relatorio_button_4.setStyleSheet(u"QPushButton{\n"
"	border:0;\n"
"}")
        self.aba_relatorio_button_4.setIcon(icon10)
        self.aba_relatorio_button_4.setIconSize(QSize(29, 28))
        self.aba_relatorio_button_4.setFlat(False)

        self.verticalLayout_26.addWidget(self.aba_relatorio_button_4, 0, Qt.AlignTop)


        self.verticalLayout_25.addWidget(self.frame_26)

        self.frame_27 = QFrame(self.frame_25)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_67 = QVBoxLayout(self.frame_27)
        self.verticalLayout_67.setSpacing(0)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.frame_49 = QFrame(self.frame_27)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setMaximumSize(QSize(1677777, 16777215))
        self.frame_49.setFrameShape(QFrame.NoFrame)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_57 = QFrame(self.frame_49)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setMinimumSize(QSize(0, 0))
        self.frame_57.setMaximumSize(QSize(300, 16777215))
        self.frame_57.setFrameShape(QFrame.Panel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.frame_57)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.frame_58 = QFrame(self.frame_57)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setMinimumSize(QSize(0, 0))
        self.frame_58.setMaximumSize(QSize(16777215, 30))
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.frame_58)
        self.verticalLayout_57.setSpacing(0)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.frame_58)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)

        self.verticalLayout_57.addWidget(self.label_19, 0, Qt.AlignHCenter)


        self.verticalLayout_56.addWidget(self.frame_58)

        self.frame_59 = QFrame(self.frame_57)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.frame_59)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.frame_60 = QFrame(self.frame_59)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.frame_60)
        self.verticalLayout_59.setSpacing(0)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.input_forne_nome = QLineEdit(self.frame_60)
        self.input_forne_nome.setObjectName(u"input_forne_nome")
        self.input_forne_nome.setFont(font12)
        self.input_forne_nome.setStyleSheet(u"QLineEdit{padding:3px;border:1px solid;background-color: rgb(243, 243, 243);}\n"
"\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")
        self.input_forne_nome.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_59.addWidget(self.input_forne_nome)


        self.verticalLayout_58.addWidget(self.frame_60)

        self.frame_61 = QFrame(self.frame_59)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.frame_61)
        self.verticalLayout_60.setSpacing(0)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, -1, 0, 0)
        self.input_forne_cpf = QLineEdit(self.frame_61)
        self.input_forne_cpf.setObjectName(u"input_forne_cpf")
        self.input_forne_cpf.setFont(font12)
        self.input_forne_cpf.setStyleSheet(u"QLineEdit{padding:3px;border:1px solid;background-color: rgb(243, 243, 243);}\n"
"\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")
        self.input_forne_cpf.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_60.addWidget(self.input_forne_cpf)


        self.verticalLayout_58.addWidget(self.frame_61)

        self.frame_62 = QFrame(self.frame_59)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.frame_62)
        self.verticalLayout_61.setSpacing(0)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.input_forne_rg = QLineEdit(self.frame_62)
        self.input_forne_rg.setObjectName(u"input_forne_rg")
        self.input_forne_rg.setFont(font12)
        self.input_forne_rg.setStyleSheet(u"QLineEdit{padding:3px;border:1px solid;background-color: rgb(243, 243, 243);}\n"
"\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")
        self.input_forne_rg.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_61.addWidget(self.input_forne_rg)


        self.verticalLayout_58.addWidget(self.frame_62)

        self.frame_63 = QFrame(self.frame_59)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.frame_63)
        self.verticalLayout_62.setSpacing(0)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.input_forne_endereco = QLineEdit(self.frame_63)
        self.input_forne_endereco.setObjectName(u"input_forne_endereco")
        self.input_forne_endereco.setFont(font12)
        self.input_forne_endereco.setStyleSheet(u"QLineEdit{padding:3px;border:1px solid;background-color: rgb(243, 243, 243);}\n"
"\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")
        self.input_forne_endereco.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_62.addWidget(self.input_forne_endereco)


        self.verticalLayout_58.addWidget(self.frame_63)

        self.frame_64 = QFrame(self.frame_59)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.verticalLayout_63 = QVBoxLayout(self.frame_64)
        self.verticalLayout_63.setSpacing(0)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.input_forne_cidade = QLineEdit(self.frame_64)
        self.input_forne_cidade.setObjectName(u"input_forne_cidade")
        self.input_forne_cidade.setFont(font12)
        self.input_forne_cidade.setStyleSheet(u"QLineEdit{padding:3px;border:1px solid;background-color: rgb(243, 243, 243);}\n"
"\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")
        self.input_forne_cidade.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_63.addWidget(self.input_forne_cidade)


        self.verticalLayout_58.addWidget(self.frame_64)

        self.frame_65 = QFrame(self.frame_59)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.verticalLayout_64 = QVBoxLayout(self.frame_65)
        self.verticalLayout_64.setSpacing(0)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.input_forne_estado = QLineEdit(self.frame_65)
        self.input_forne_estado.setObjectName(u"input_forne_estado")
        self.input_forne_estado.setFont(font12)
        self.input_forne_estado.setStyleSheet(u"QLineEdit{padding:3px;border:1px solid;background-color: rgb(243, 243, 243);}\n"
"\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")
        self.input_forne_estado.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_64.addWidget(self.input_forne_estado)


        self.verticalLayout_58.addWidget(self.frame_65)

        self.frame_66 = QFrame(self.frame_59)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.frame_66)
        self.verticalLayout_65.setSpacing(0)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.input_forne_telefone = QLineEdit(self.frame_66)
        self.input_forne_telefone.setObjectName(u"input_forne_telefone")
        self.input_forne_telefone.setFont(font12)
        self.input_forne_telefone.setStyleSheet(u"QLineEdit{padding:3px;border:1px solid;background-color: rgb(243, 243, 243);}\n"
"\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")
        self.input_forne_telefone.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_65.addWidget(self.input_forne_telefone)


        self.verticalLayout_58.addWidget(self.frame_66)

        self.btn_registrar_forne = QPushButton(self.frame_59)
        self.btn_registrar_forne.setObjectName(u"btn_registrar_forne")
        self.btn_registrar_forne.setFont(font13)
        self.btn_registrar_forne.setStyleSheet(u"QPushButton{\n"
"	border:1px solid rgb(15, 202, 2);\n"
"	padding:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(122, 229, 105);\n"
"}")

        self.verticalLayout_58.addWidget(self.btn_registrar_forne)


        self.verticalLayout_56.addWidget(self.frame_59)


        self.horizontalLayout_7.addWidget(self.frame_57)

        self.btn_menu_registrar_forne = QPushButton(self.frame_49)
        self.btn_menu_registrar_forne.setObjectName(u"btn_menu_registrar_forne")
        self.btn_menu_registrar_forne.setMinimumSize(QSize(0, 485))
        self.btn_menu_registrar_forne.setMaximumSize(QSize(30, 16777215))
        self.btn_menu_registrar_forne.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu_registrar_forne.setStyleSheet(u"border-radius:2px;\n"
"background-color: rgb(43, 43, 43);")
        self.btn_menu_registrar_forne.setIcon(icon11)

        self.horizontalLayout_7.addWidget(self.btn_menu_registrar_forne)

        self.frame_67 = QFrame(self.frame_49)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.verticalLayout_66 = QVBoxLayout(self.frame_67)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(9, -1, -1, -1)
        self.widget_2 = QWidget(self.frame_67)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 60))
        self.gridLayout_11 = QGridLayout(self.widget_2)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_24 = QLabel(self.widget_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(30, 30))
        self.label_24.setPixmap(QPixmap(u":/icons/clock-rotate-left-solid.svg"))
        self.label_24.setScaledContents(True)

        self.gridLayout_11.addWidget(self.label_24, 0, 0, 1, 1)

        self.label_25 = QLabel(self.widget_2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font1)

        self.gridLayout_11.addWidget(self.label_25, 0, 1, 1, 1)


        self.verticalLayout_66.addWidget(self.widget_2, 0, Qt.AlignHCenter)

        self.btn_remover_forne = QPushButton(self.frame_67)
        self.btn_remover_forne.setObjectName(u"btn_remover_forne")
        self.btn_remover_forne.setMaximumSize(QSize(271, 16777215))
        self.btn_remover_forne.setFont(font2)
        self.btn_remover_forne.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_remover_forne.setStyleSheet(u"QPushButton{\n"
"border:1px solid red;\n"
"padding:5px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	background-color: rgb(255, 135, 135);\n"
"}")
        self.btn_remover_forne.setIcon(icon12)
        self.btn_remover_forne.setIconSize(QSize(25, 22))

        self.verticalLayout_66.addWidget(self.btn_remover_forne, 0, Qt.AlignRight)

        self.tableWidget_3 = QTableWidget(self.frame_67)
        if (self.tableWidget_3.columnCount() < 9):
            self.tableWidget_3.setColumnCount(9)
        __qtablewidgetitem86 = QTableWidgetItem()
        __qtablewidgetitem86.setFont(font9);
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        __qtablewidgetitem87.setFont(font9);
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        __qtablewidgetitem88.setFont(font9);
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        __qtablewidgetitem89.setFont(font9);
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        __qtablewidgetitem90.setFont(font9);
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        __qtablewidgetitem91.setFont(font9);
        self.tableWidget_3.setHorizontalHeaderItem(5, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        __qtablewidgetitem92.setFont(font9);
        self.tableWidget_3.setHorizontalHeaderItem(6, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        __qtablewidgetitem93.setFont(font9);
        self.tableWidget_3.setHorizontalHeaderItem(7, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        __qtablewidgetitem94.setFont(font9);
        self.tableWidget_3.setHorizontalHeaderItem(8, __qtablewidgetitem94)
        if (self.tableWidget_3.rowCount() < 1):
            self.tableWidget_3.setRowCount(1)
        __qtablewidgetitem95 = QTableWidgetItem()
        __qtablewidgetitem95.setCheckState(Qt.Unchecked);
        self.tableWidget_3.setItem(0, 0, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 1, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 2, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 3, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 4, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 5, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 6, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 7, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 8, __qtablewidgetitem103)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setMaximumSize(QSize(16777215, 1999999))
        self.tableWidget_3.setStyleSheet(u"QTableWidget{\n"
"	font: 10pt \"Century Gothic\";\n"
"	outline:0;\n"
"}\n"
"QHeaderView::section {\n"
"	color:white;\n"
"	border:1px solid white;\n"
"	background-color: rgb(15, 202, 2);\n"
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
"    borde"
                        "r: 1px solid #999999;\n"
"    background:white;\n"
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
        self.tableWidget_3.setAutoScroll(True)
        self.tableWidget_3.setAutoScrollMargin(20)
        self.tableWidget_3.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_3.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.tableWidget_3.setDefaultDropAction(Qt.IgnoreAction)
        self.tableWidget_3.setAlternatingRowColors(True)
        self.tableWidget_3.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_3.setTextElideMode(Qt.ElideRight)
        self.tableWidget_3.setSortingEnabled(True)
        self.tableWidget_3.setRowCount(1)
        self.tableWidget_3.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_3.horizontalHeader().setMinimumSectionSize(95)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(115)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_3.verticalHeader().setVisible(False)

        self.verticalLayout_66.addWidget(self.tableWidget_3)


        self.horizontalLayout_7.addWidget(self.frame_67)


        self.verticalLayout_67.addWidget(self.frame_49)


        self.verticalLayout_25.addWidget(self.frame_27)


        self.verticalLayout_27.addWidget(self.frame_25)

        self.stackedWidget.addWidget(self.page_fornecedores)
        self.page_veiculos = QWidget()
        self.page_veiculos.setObjectName(u"page_veiculos")
        self.page_veiculos.setStyleSheet(u"border:0")
        self.verticalLayout_33 = QVBoxLayout(self.page_veiculos)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.frame_31 = QFrame(self.page_veiculos)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_31)
        self.verticalLayout_31.setSpacing(7)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.frame_32 = QFrame(self.frame_31)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(0, 45))
        self.frame_32.setMaximumSize(QSize(16777215, 45))
        self.frame_32.setStyleSheet(u"background-color: rgb(43, 43, 43);\n"
"color: rgb(255, 255, 255);")
        self.frame_32.setFrameShape(QFrame.NoFrame)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_32)
        self.verticalLayout_32.setSpacing(7)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.aba_relatorio_button_6 = QPushButton(self.frame_32)
        self.aba_relatorio_button_6.setObjectName(u"aba_relatorio_button_6")
        self.aba_relatorio_button_6.setMinimumSize(QSize(160, 45))
        self.aba_relatorio_button_6.setMaximumSize(QSize(5555, 45))
        self.aba_relatorio_button_6.setBaseSize(QSize(555, 2))
        self.aba_relatorio_button_6.setFont(font5)
        self.aba_relatorio_button_6.setLayoutDirection(Qt.LeftToRight)
        self.aba_relatorio_button_6.setStyleSheet(u"QPushButton{\n"
"	border:0;\n"
"}")
        self.aba_relatorio_button_6.setIcon(icon10)
        self.aba_relatorio_button_6.setIconSize(QSize(29, 28))
        self.aba_relatorio_button_6.setFlat(False)

        self.verticalLayout_32.addWidget(self.aba_relatorio_button_6, 0, Qt.AlignTop)


        self.verticalLayout_31.addWidget(self.frame_32)

        self.frame_33 = QFrame(self.frame_31)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMaximumSize(QSize(1677777, 16777215))
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
        self.frame_68.setFrameShape(QFrame.Panel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.verticalLayout_68 = QVBoxLayout(self.frame_68)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.frame_69 = QFrame(self.frame_68)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setMinimumSize(QSize(0, 0))
        self.frame_69.setMaximumSize(QSize(16777215, 30))
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_69)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel(self.frame_69)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font1)

        self.horizontalLayout_15.addWidget(self.label_26)


        self.verticalLayout_68.addWidget(self.frame_69, 0, Qt.AlignHCenter)

        self.frame_70 = QFrame(self.frame_68)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.verticalLayout_70 = QVBoxLayout(self.frame_70)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.frame_71 = QFrame(self.frame_70)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.verticalLayout_71 = QVBoxLayout(self.frame_71)
        self.verticalLayout_71.setSpacing(0)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.input_veiculos_nome = QLineEdit(self.frame_71)
        self.input_veiculos_nome.setObjectName(u"input_veiculos_nome")
        self.input_veiculos_nome.setFont(font12)
        self.input_veiculos_nome.setStyleSheet(u"QLineEdit{padding:3px;border:1px solid;background-color: rgb(243, 243, 243);}\n"
"\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")
        self.input_veiculos_nome.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_71.addWidget(self.input_veiculos_nome)


        self.verticalLayout_70.addWidget(self.frame_71)

        self.frame_72 = QFrame(self.frame_70)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.verticalLayout_72 = QVBoxLayout(self.frame_72)
        self.verticalLayout_72.setSpacing(0)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(0, -1, 0, 0)
        self.input_veiculos_valor = QLineEdit(self.frame_72)
        self.input_veiculos_valor.setObjectName(u"input_veiculos_valor")
        self.input_veiculos_valor.setFont(font12)
        self.input_veiculos_valor.setStyleSheet(u"QLineEdit{padding:3px;border:1px solid;background-color: rgb(243, 243, 243);}\n"
"\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")
        self.input_veiculos_valor.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_72.addWidget(self.input_veiculos_valor)


        self.verticalLayout_70.addWidget(self.frame_72)

        self.frame_73 = QFrame(self.frame_70)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.verticalLayout_73 = QVBoxLayout(self.frame_73)
        self.verticalLayout_73.setSpacing(0)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.verticalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.input_veiculos_placa = QLineEdit(self.frame_73)
        self.input_veiculos_placa.setObjectName(u"input_veiculos_placa")
        self.input_veiculos_placa.setFont(font12)
        self.input_veiculos_placa.setStyleSheet(u"QLineEdit{padding:3px;border:1px solid;background-color: rgb(243, 243, 243);}\n"
"\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")
        self.input_veiculos_placa.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_73.addWidget(self.input_veiculos_placa)


        self.verticalLayout_70.addWidget(self.frame_73)

        self.frame_74 = QFrame(self.frame_70)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_74)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.comboBox_veiculos_produtos = QComboBox(self.frame_74)
        self.comboBox_veiculos_produtos.addItem("")
        self.comboBox_veiculos_produtos.addItem("")
        self.comboBox_veiculos_produtos.addItem("")
        self.comboBox_veiculos_produtos.setObjectName(u"comboBox_veiculos_produtos")
        self.comboBox_veiculos_produtos.setMinimumSize(QSize(154, 33))
        self.comboBox_veiculos_produtos.setFont(font12)
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
        self.comboBox_veiculos_produtos.setMaxVisibleItems(5)
        self.comboBox_veiculos_produtos.setInsertPolicy(QComboBox.NoInsert)
        self.comboBox_veiculos_produtos.setIconSize(QSize(32, 32))
        self.comboBox_veiculos_produtos.setDuplicatesEnabled(True)
        self.comboBox_veiculos_produtos.setFrame(True)

        self.gridLayout_16.addWidget(self.comboBox_veiculos_produtos, 0, 0, 1, 1)


        self.verticalLayout_70.addWidget(self.frame_74)

        self.btn_registrar_veiculos = QPushButton(self.frame_70)
        self.btn_registrar_veiculos.setObjectName(u"btn_registrar_veiculos")
        self.btn_registrar_veiculos.setFont(font13)
        self.btn_registrar_veiculos.setStyleSheet(u"QPushButton{\n"
"	border:1px solid rgb(15, 202, 2);\n"
"	padding:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(122, 229, 105);\n"
"}")

        self.verticalLayout_70.addWidget(self.btn_registrar_veiculos)


        self.verticalLayout_68.addWidget(self.frame_70)


        self.horizontalLayout_8.addWidget(self.frame_68)

        self.btn_menu_registrar_veiculos = QPushButton(self.frame_33)
        self.btn_menu_registrar_veiculos.setObjectName(u"btn_menu_registrar_veiculos")
        self.btn_menu_registrar_veiculos.setMinimumSize(QSize(0, 485))
        self.btn_menu_registrar_veiculos.setMaximumSize(QSize(30, 16777215))
        self.btn_menu_registrar_veiculos.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu_registrar_veiculos.setStyleSheet(u"border-radius:2px;\n"
"background-color: rgb(43, 43, 43);")
        self.btn_menu_registrar_veiculos.setIcon(icon11)

        self.horizontalLayout_8.addWidget(self.btn_menu_registrar_veiculos)

        self.frame_78 = QFrame(self.frame_33)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.verticalLayout_78 = QVBoxLayout(self.frame_78)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.verticalLayout_78.setContentsMargins(9, -1, -1, -1)
        self.widget_3 = QWidget(self.frame_78)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 60))
        self.gridLayout_12 = QGridLayout(self.widget_3)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_27 = QLabel(self.widget_3)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(30, 30))
        self.label_27.setPixmap(QPixmap(u":/icons/clock-rotate-left-solid.svg"))
        self.label_27.setScaledContents(True)

        self.gridLayout_12.addWidget(self.label_27, 0, 0, 1, 1)

        self.label_28 = QLabel(self.widget_3)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font1)

        self.gridLayout_12.addWidget(self.label_28, 0, 1, 1, 1)


        self.verticalLayout_78.addWidget(self.widget_3, 0, Qt.AlignHCenter)

        self.btn_remover_veiculos = QPushButton(self.frame_78)
        self.btn_remover_veiculos.setObjectName(u"btn_remover_veiculos")
        self.btn_remover_veiculos.setMaximumSize(QSize(240, 16777215))
        self.btn_remover_veiculos.setFont(font2)
        self.btn_remover_veiculos.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_remover_veiculos.setStyleSheet(u"QPushButton{\n"
"border:1px solid red;\n"
"padding:5px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	background-color: rgb(255, 135, 135);\n"
"}")
        self.btn_remover_veiculos.setIcon(icon12)
        self.btn_remover_veiculos.setIconSize(QSize(25, 22))

        self.verticalLayout_78.addWidget(self.btn_remover_veiculos, 0, Qt.AlignRight)

        self.tableWidget_4 = QTableWidget(self.frame_78)
        if (self.tableWidget_4.columnCount() < 6):
            self.tableWidget_4.setColumnCount(6)
        __qtablewidgetitem104 = QTableWidgetItem()
        __qtablewidgetitem104.setFont(font9);
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        __qtablewidgetitem105.setFont(font9);
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        __qtablewidgetitem106.setFont(font9);
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        __qtablewidgetitem107.setFont(font9);
        self.tableWidget_4.setHorizontalHeaderItem(3, __qtablewidgetitem107)
        __qtablewidgetitem108 = QTableWidgetItem()
        __qtablewidgetitem108.setFont(font9);
        self.tableWidget_4.setHorizontalHeaderItem(4, __qtablewidgetitem108)
        __qtablewidgetitem109 = QTableWidgetItem()
        __qtablewidgetitem109.setFont(font9);
        self.tableWidget_4.setHorizontalHeaderItem(5, __qtablewidgetitem109)
        if (self.tableWidget_4.rowCount() < 2):
            self.tableWidget_4.setRowCount(2)
        __qtablewidgetitem110 = QTableWidgetItem()
        __qtablewidgetitem110.setCheckState(Qt.Unchecked);
        self.tableWidget_4.setItem(0, 0, __qtablewidgetitem110)
        __qtablewidgetitem111 = QTableWidgetItem()
        self.tableWidget_4.setItem(0, 1, __qtablewidgetitem111)
        __qtablewidgetitem112 = QTableWidgetItem()
        self.tableWidget_4.setItem(0, 2, __qtablewidgetitem112)
        __qtablewidgetitem113 = QTableWidgetItem()
        self.tableWidget_4.setItem(0, 3, __qtablewidgetitem113)
        __qtablewidgetitem114 = QTableWidgetItem()
        self.tableWidget_4.setItem(0, 4, __qtablewidgetitem114)
        __qtablewidgetitem115 = QTableWidgetItem()
        self.tableWidget_4.setItem(0, 5, __qtablewidgetitem115)
        __qtablewidgetitem116 = QTableWidgetItem()
        __qtablewidgetitem116.setCheckState(Qt.Unchecked);
        self.tableWidget_4.setItem(1, 0, __qtablewidgetitem116)
        __qtablewidgetitem117 = QTableWidgetItem()
        self.tableWidget_4.setItem(1, 1, __qtablewidgetitem117)
        __qtablewidgetitem118 = QTableWidgetItem()
        self.tableWidget_4.setItem(1, 2, __qtablewidgetitem118)
        __qtablewidgetitem119 = QTableWidgetItem()
        self.tableWidget_4.setItem(1, 3, __qtablewidgetitem119)
        __qtablewidgetitem120 = QTableWidgetItem()
        self.tableWidget_4.setItem(1, 4, __qtablewidgetitem120)
        __qtablewidgetitem121 = QTableWidgetItem()
        self.tableWidget_4.setItem(1, 5, __qtablewidgetitem121)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setMaximumSize(QSize(16777215, 1999999))
        self.tableWidget_4.setStyleSheet(u"QTableWidget{\n"
"	font: 10pt \"Century Gothic\";\n"
"	outline:0;\n"
"}\n"
"QHeaderView::section {\n"
"	color:white;\n"
"	border:1px solid white;\n"
"	background-color: rgb(15, 202, 2);\n"
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
"    borde"
                        "r: 1px solid #999999;\n"
"    background:white;\n"
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
        self.tableWidget_4.setAutoScroll(True)
        self.tableWidget_4.setAutoScrollMargin(20)
        self.tableWidget_4.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_4.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.tableWidget_4.setDefaultDropAction(Qt.IgnoreAction)
        self.tableWidget_4.setAlternatingRowColors(True)
        self.tableWidget_4.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_4.setTextElideMode(Qt.ElideRight)
        self.tableWidget_4.setSortingEnabled(True)
        self.tableWidget_4.setRowCount(2)
        self.tableWidget_4.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_4.horizontalHeader().setMinimumSectionSize(95)
        self.tableWidget_4.horizontalHeader().setDefaultSectionSize(115)
        self.tableWidget_4.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_4.verticalHeader().setVisible(False)

        self.verticalLayout_78.addWidget(self.tableWidget_4)


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
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_28)
        self.verticalLayout_30.setSpacing(7)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frame_103 = QFrame(self.frame_28)
        self.frame_103.setObjectName(u"frame_103")
        self.frame_103.setMinimumSize(QSize(0, 45))
        self.frame_103.setMaximumSize(QSize(16777215, 40))
        self.frame_103.setStyleSheet(u"background-color: rgb(43, 43, 43);\n"
"color: rgb(255, 255, 255);")
        self.frame_103.setFrameShape(QFrame.NoFrame)
        self.frame_103.setFrameShadow(QFrame.Raised)
        self.verticalLayout_103 = QVBoxLayout(self.frame_103)
        self.verticalLayout_103.setSpacing(7)
        self.verticalLayout_103.setObjectName(u"verticalLayout_103")
        self.verticalLayout_103.setContentsMargins(0, 0, 0, 0)
        self.aba_relatorio_button_12 = QPushButton(self.frame_103)
        self.aba_relatorio_button_12.setObjectName(u"aba_relatorio_button_12")
        self.aba_relatorio_button_12.setMinimumSize(QSize(160, 45))
        self.aba_relatorio_button_12.setMaximumSize(QSize(5555, 45))
        self.aba_relatorio_button_12.setBaseSize(QSize(555, 2))
        self.aba_relatorio_button_12.setFont(font5)
        self.aba_relatorio_button_12.setLayoutDirection(Qt.LeftToRight)
        self.aba_relatorio_button_12.setStyleSheet(u"QPushButton{\n"
"	border:0;\n"
"}")
        self.aba_relatorio_button_12.setIcon(icon10)
        self.aba_relatorio_button_12.setIconSize(QSize(29, 28))
        self.aba_relatorio_button_12.setFlat(False)

        self.verticalLayout_103.addWidget(self.aba_relatorio_button_12, 0, Qt.AlignTop)


        self.verticalLayout_30.addWidget(self.frame_103)

        self.frame_104 = QFrame(self.frame_28)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setMaximumSize(QSize(1677777, 16777215))
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
        self.frame_105.setFrameShape(QFrame.Panel)
        self.frame_105.setFrameShadow(QFrame.Raised)
        self.verticalLayout_104 = QVBoxLayout(self.frame_105)
        self.verticalLayout_104.setObjectName(u"verticalLayout_104")
        self.frame_106 = QFrame(self.frame_105)
        self.frame_106.setObjectName(u"frame_106")
        self.frame_106.setMinimumSize(QSize(0, 0))
        self.frame_106.setMaximumSize(QSize(16777215, 30))
        self.frame_106.setFrameShape(QFrame.StyledPanel)
        self.frame_106.setFrameShadow(QFrame.Raised)
        self.verticalLayout_105 = QVBoxLayout(self.frame_106)
        self.verticalLayout_105.setSpacing(0)
        self.verticalLayout_105.setObjectName(u"verticalLayout_105")
        self.verticalLayout_105.setContentsMargins(0, 0, 0, 0)
        self.label_35 = QLabel(self.frame_106)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font1)

        self.verticalLayout_105.addWidget(self.label_35, 0, Qt.AlignHCenter)


        self.verticalLayout_104.addWidget(self.frame_106)

        self.frame_107 = QFrame(self.frame_105)
        self.frame_107.setObjectName(u"frame_107")
        self.frame_107.setFrameShape(QFrame.StyledPanel)
        self.frame_107.setFrameShadow(QFrame.Raised)
        self.verticalLayout_106 = QVBoxLayout(self.frame_107)
        self.verticalLayout_106.setObjectName(u"verticalLayout_106")
        self.frame_108 = QFrame(self.frame_107)
        self.frame_108.setObjectName(u"frame_108")
        self.frame_108.setFrameShape(QFrame.StyledPanel)
        self.frame_108.setFrameShadow(QFrame.Raised)
        self.verticalLayout_107 = QVBoxLayout(self.frame_108)
        self.verticalLayout_107.setSpacing(0)
        self.verticalLayout_107.setObjectName(u"verticalLayout_107")
        self.verticalLayout_107.setContentsMargins(0, 0, 0, 0)
        self.input_produtos_nome = QLineEdit(self.frame_108)
        self.input_produtos_nome.setObjectName(u"input_produtos_nome")
        self.input_produtos_nome.setFont(font12)
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
        self.frame_109.setFrameShape(QFrame.StyledPanel)
        self.frame_109.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_109)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, -1, 0, 0)
        self.input_produtos_estoqueKG = QLineEdit(self.frame_109)
        self.input_produtos_estoqueKG.setObjectName(u"input_produtos_estoqueKG")
        self.input_produtos_estoqueKG.setFont(font12)
        self.input_produtos_estoqueKG.setStyleSheet(u"QLineEdit{padding:3px;border:1px solid;background-color: rgb(243, 243, 243);}\n"
"\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")
        self.input_produtos_estoqueKG.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_12.addWidget(self.input_produtos_estoqueKG)

        self.label_38 = QLabel(self.frame_109)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font12)
        self.label_38.setStyleSheet(u"color: rgb(15, 202, 2);")

        self.horizontalLayout_12.addWidget(self.label_38)


        self.verticalLayout_106.addWidget(self.frame_109)

        self.frame_110 = QFrame(self.frame_107)
        self.frame_110.setObjectName(u"frame_110")
        self.frame_110.setFrameShape(QFrame.StyledPanel)
        self.frame_110.setFrameShadow(QFrame.Raised)
        self.verticalLayout_109 = QVBoxLayout(self.frame_110)
        self.verticalLayout_109.setSpacing(0)
        self.verticalLayout_109.setObjectName(u"verticalLayout_109")
        self.verticalLayout_109.setContentsMargins(0, 0, 0, 0)
        self.input_produtos_preco = QLineEdit(self.frame_110)
        self.input_produtos_preco.setObjectName(u"input_produtos_preco")
        self.input_produtos_preco.setFont(font12)
        self.input_produtos_preco.setStyleSheet(u"QLineEdit{padding:3px;border:1px solid;background-color: rgb(243, 243, 243);}\n"
"\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")
        self.input_produtos_preco.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_109.addWidget(self.input_produtos_preco)


        self.verticalLayout_106.addWidget(self.frame_110)

        self.frame_111 = QFrame(self.frame_107)
        self.frame_111.setObjectName(u"frame_111")
        self.frame_111.setFrameShape(QFrame.StyledPanel)
        self.frame_111.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_111)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.input_produtos_densidade = QLineEdit(self.frame_111)
        self.input_produtos_densidade.setObjectName(u"input_produtos_densidade")
        self.input_produtos_densidade.setFont(font12)
        self.input_produtos_densidade.setStyleSheet(u"QLineEdit{padding:3px;border:1px solid;background-color: rgb(243, 243, 243);}\n"
"\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")
        self.input_produtos_densidade.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_13.addWidget(self.input_produtos_densidade)

        self.label_39 = QLabel(self.frame_111)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font12)
        self.label_39.setStyleSheet(u"color: rgb(15, 202, 2);")

        self.horizontalLayout_13.addWidget(self.label_39)


        self.verticalLayout_106.addWidget(self.frame_111)

        self.frame_112 = QFrame(self.frame_107)
        self.frame_112.setObjectName(u"frame_112")
        self.frame_112.setFrameShape(QFrame.StyledPanel)
        self.frame_112.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_112)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.input_produtos_embalagemKG = QLineEdit(self.frame_112)
        self.input_produtos_embalagemKG.setObjectName(u"input_produtos_embalagemKG")
        self.input_produtos_embalagemKG.setFont(font12)
        self.input_produtos_embalagemKG.setStyleSheet(u"QLineEdit{padding:3px;border:1px solid;background-color: rgb(243, 243, 243);}\n"
"\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(67, 202, 0)\n"
"}")
        self.input_produtos_embalagemKG.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_14.addWidget(self.input_produtos_embalagemKG)

        self.label_40 = QLabel(self.frame_112)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font12)
        self.label_40.setStyleSheet(u"color: rgb(15, 202, 2);")

        self.horizontalLayout_14.addWidget(self.label_40)


        self.verticalLayout_106.addWidget(self.frame_112)

        self.btn_registrar_produtos = QPushButton(self.frame_107)
        self.btn_registrar_produtos.setObjectName(u"btn_registrar_produtos")
        self.btn_registrar_produtos.setFont(font13)
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
        self.btn_menu_registrar_produtos.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu_registrar_produtos.setStyleSheet(u"border-radius:2px;\n"
"background-color: rgb(43, 43, 43);")
        self.btn_menu_registrar_produtos.setIcon(icon11)

        self.horizontalLayout_11.addWidget(self.btn_menu_registrar_produtos)

        self.frame_115 = QFrame(self.frame_104)
        self.frame_115.setObjectName(u"frame_115")
        self.frame_115.setFrameShape(QFrame.StyledPanel)
        self.frame_115.setFrameShadow(QFrame.Raised)
        self.verticalLayout_114 = QVBoxLayout(self.frame_115)
        self.verticalLayout_114.setObjectName(u"verticalLayout_114")
        self.verticalLayout_114.setContentsMargins(9, -1, -1, -1)
        self.widget_6 = QWidget(self.frame_115)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(0, 60))
        self.gridLayout_15 = QGridLayout(self.widget_6)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_36 = QLabel(self.widget_6)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMaximumSize(QSize(30, 30))
        self.label_36.setPixmap(QPixmap(u":/icons/clock-rotate-left-solid.svg"))
        self.label_36.setScaledContents(True)

        self.gridLayout_15.addWidget(self.label_36, 0, 0, 1, 1)

        self.label_37 = QLabel(self.widget_6)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font1)

        self.gridLayout_15.addWidget(self.label_37, 0, 1, 1, 1)


        self.verticalLayout_114.addWidget(self.widget_6, 0, Qt.AlignHCenter)

        self.btn_remover_produtos = QPushButton(self.frame_115)
        self.btn_remover_produtos.setObjectName(u"btn_remover_produtos")
        self.btn_remover_produtos.setMaximumSize(QSize(240, 16777215))
        self.btn_remover_produtos.setFont(font2)
        self.btn_remover_produtos.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_remover_produtos.setStyleSheet(u"QPushButton{\n"
"border:1px solid red;\n"
"padding:5px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	background-color: rgb(255, 135, 135);\n"
"}")
        self.btn_remover_produtos.setIcon(icon12)
        self.btn_remover_produtos.setIconSize(QSize(25, 22))

        self.verticalLayout_114.addWidget(self.btn_remover_produtos, 0, Qt.AlignRight)

        self.tableWidget_7 = QTableWidget(self.frame_115)
        if (self.tableWidget_7.columnCount() < 7):
            self.tableWidget_7.setColumnCount(7)
        __qtablewidgetitem122 = QTableWidgetItem()
        __qtablewidgetitem122.setFont(font9);
        self.tableWidget_7.setHorizontalHeaderItem(0, __qtablewidgetitem122)
        __qtablewidgetitem123 = QTableWidgetItem()
        __qtablewidgetitem123.setFont(font9);
        self.tableWidget_7.setHorizontalHeaderItem(1, __qtablewidgetitem123)
        __qtablewidgetitem124 = QTableWidgetItem()
        __qtablewidgetitem124.setFont(font9);
        self.tableWidget_7.setHorizontalHeaderItem(2, __qtablewidgetitem124)
        __qtablewidgetitem125 = QTableWidgetItem()
        __qtablewidgetitem125.setFont(font9);
        self.tableWidget_7.setHorizontalHeaderItem(3, __qtablewidgetitem125)
        __qtablewidgetitem126 = QTableWidgetItem()
        __qtablewidgetitem126.setFont(font9);
        self.tableWidget_7.setHorizontalHeaderItem(4, __qtablewidgetitem126)
        __qtablewidgetitem127 = QTableWidgetItem()
        __qtablewidgetitem127.setFont(font9);
        self.tableWidget_7.setHorizontalHeaderItem(5, __qtablewidgetitem127)
        __qtablewidgetitem128 = QTableWidgetItem()
        __qtablewidgetitem128.setFont(font9);
        self.tableWidget_7.setHorizontalHeaderItem(6, __qtablewidgetitem128)
        if (self.tableWidget_7.rowCount() < 2):
            self.tableWidget_7.setRowCount(2)
        __qtablewidgetitem129 = QTableWidgetItem()
        __qtablewidgetitem129.setCheckState(Qt.Unchecked);
        self.tableWidget_7.setItem(0, 0, __qtablewidgetitem129)
        __qtablewidgetitem130 = QTableWidgetItem()
        self.tableWidget_7.setItem(0, 1, __qtablewidgetitem130)
        __qtablewidgetitem131 = QTableWidgetItem()
        self.tableWidget_7.setItem(0, 2, __qtablewidgetitem131)
        __qtablewidgetitem132 = QTableWidgetItem()
        self.tableWidget_7.setItem(0, 3, __qtablewidgetitem132)
        __qtablewidgetitem133 = QTableWidgetItem()
        self.tableWidget_7.setItem(0, 4, __qtablewidgetitem133)
        __qtablewidgetitem134 = QTableWidgetItem()
        self.tableWidget_7.setItem(0, 5, __qtablewidgetitem134)
        __qtablewidgetitem135 = QTableWidgetItem()
        self.tableWidget_7.setItem(0, 6, __qtablewidgetitem135)
        __qtablewidgetitem136 = QTableWidgetItem()
        __qtablewidgetitem136.setCheckState(Qt.Unchecked);
        self.tableWidget_7.setItem(1, 0, __qtablewidgetitem136)
        __qtablewidgetitem137 = QTableWidgetItem()
        self.tableWidget_7.setItem(1, 1, __qtablewidgetitem137)
        __qtablewidgetitem138 = QTableWidgetItem()
        self.tableWidget_7.setItem(1, 2, __qtablewidgetitem138)
        __qtablewidgetitem139 = QTableWidgetItem()
        self.tableWidget_7.setItem(1, 3, __qtablewidgetitem139)
        __qtablewidgetitem140 = QTableWidgetItem()
        self.tableWidget_7.setItem(1, 4, __qtablewidgetitem140)
        __qtablewidgetitem141 = QTableWidgetItem()
        self.tableWidget_7.setItem(1, 5, __qtablewidgetitem141)
        __qtablewidgetitem142 = QTableWidgetItem()
        self.tableWidget_7.setItem(1, 6, __qtablewidgetitem142)
        self.tableWidget_7.setObjectName(u"tableWidget_7")
        self.tableWidget_7.setMaximumSize(QSize(16777215, 1999999))
        self.tableWidget_7.setStyleSheet(u"QTableWidget{\n"
"	font: 10pt \"Century Gothic\";\n"
"	outline:0;\n"
"}\n"
"QHeaderView::section {\n"
"	color:white;\n"
"	border:1px solid white;\n"
"	background-color: rgb(15, 202, 2);\n"
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
"    borde"
                        "r: 1px solid #999999;\n"
"    background:white;\n"
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
        self.tableWidget_7.setAutoScroll(True)
        self.tableWidget_7.setAutoScrollMargin(20)
        self.tableWidget_7.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_7.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.tableWidget_7.setDefaultDropAction(Qt.IgnoreAction)
        self.tableWidget_7.setAlternatingRowColors(True)
        self.tableWidget_7.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_7.setTextElideMode(Qt.ElideRight)
        self.tableWidget_7.setSortingEnabled(True)
        self.tableWidget_7.setRowCount(2)
        self.tableWidget_7.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_7.horizontalHeader().setMinimumSectionSize(95)
        self.tableWidget_7.horizontalHeader().setDefaultSectionSize(115)
        self.tableWidget_7.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_7.verticalHeader().setVisible(False)

        self.verticalLayout_114.addWidget(self.tableWidget_7)


        self.horizontalLayout_11.addWidget(self.frame_115)


        self.verticalLayout_30.addWidget(self.frame_104)


        self.verticalLayout_115.addWidget(self.frame_28)

        self.stackedWidget.addWidget(self.page_produtos)
        self.page_avulsas = QWidget()
        self.page_avulsas.setObjectName(u"page_avulsas")
        self.page_avulsas.setStyleSheet(u"border:0")
        self.verticalLayout_42 = QVBoxLayout(self.page_avulsas)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.frame_40 = QFrame(self.page_avulsas)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_40)
        self.verticalLayout_40.setSpacing(7)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.frame_41 = QFrame(self.frame_40)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMinimumSize(QSize(0, 45))
        self.frame_41.setMaximumSize(QSize(16777215, 45))
        self.frame_41.setStyleSheet(u"background-color: rgb(43, 43, 43);\n"
"color: rgb(255, 255, 255);")
        self.frame_41.setFrameShape(QFrame.NoFrame)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_41)
        self.verticalLayout_41.setSpacing(7)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.aba_relatorio_button_9 = QPushButton(self.frame_41)
        self.aba_relatorio_button_9.setObjectName(u"aba_relatorio_button_9")
        self.aba_relatorio_button_9.setMinimumSize(QSize(160, 45))
        self.aba_relatorio_button_9.setMaximumSize(QSize(5555, 45))
        self.aba_relatorio_button_9.setBaseSize(QSize(555, 2))
        self.aba_relatorio_button_9.setFont(font5)
        self.aba_relatorio_button_9.setLayoutDirection(Qt.LeftToRight)
        self.aba_relatorio_button_9.setStyleSheet(u"QPushButton{\n"
"	border:0;\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/icons/scale-balanced-solid .svg", QSize(), QIcon.Normal, QIcon.Off)
        self.aba_relatorio_button_9.setIcon(icon13)
        self.aba_relatorio_button_9.setIconSize(QSize(29, 28))
        self.aba_relatorio_button_9.setFlat(False)

        self.verticalLayout_41.addWidget(self.aba_relatorio_button_9, 0, Qt.AlignTop)


        self.verticalLayout_40.addWidget(self.frame_41)

        self.frame_42 = QFrame(self.frame_40)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)

        self.verticalLayout_40.addWidget(self.frame_42)


        self.verticalLayout_42.addWidget(self.frame_40)

        self.stackedWidget.addWidget(self.page_avulsas)
        self.page_entradas_saidas = QWidget()
        self.page_entradas_saidas.setObjectName(u"page_entradas_saidas")
        self.page_entradas_saidas.setStyleSheet(u"border:0")
        self.verticalLayout_39 = QVBoxLayout(self.page_entradas_saidas)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.frame_37 = QFrame(self.page_entradas_saidas)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_37)
        self.verticalLayout_37.setSpacing(7)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.frame_38 = QFrame(self.frame_37)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMinimumSize(QSize(0, 45))
        self.frame_38.setMaximumSize(QSize(16777215, 45))
        self.frame_38.setStyleSheet(u"background-color: rgb(43, 43, 43);\n"
"color: rgb(255, 255, 255);")
        self.frame_38.setFrameShape(QFrame.NoFrame)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_38)
        self.verticalLayout_38.setSpacing(7)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.aba_relatorio_button_8 = QPushButton(self.frame_38)
        self.aba_relatorio_button_8.setObjectName(u"aba_relatorio_button_8")
        self.aba_relatorio_button_8.setMinimumSize(QSize(160, 45))
        self.aba_relatorio_button_8.setMaximumSize(QSize(5555, 45))
        self.aba_relatorio_button_8.setBaseSize(QSize(555, 2))
        self.aba_relatorio_button_8.setFont(font5)
        self.aba_relatorio_button_8.setLayoutDirection(Qt.LeftToRight)
        self.aba_relatorio_button_8.setStyleSheet(u"QPushButton{\n"
"	border:0;\n"
"}")
        self.aba_relatorio_button_8.setIcon(icon13)
        self.aba_relatorio_button_8.setIconSize(QSize(29, 28))
        self.aba_relatorio_button_8.setFlat(False)

        self.verticalLayout_38.addWidget(self.aba_relatorio_button_8, 0, Qt.AlignTop)


        self.verticalLayout_37.addWidget(self.frame_38)

        self.frame_39 = QFrame(self.frame_37)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)

        self.verticalLayout_37.addWidget(self.frame_39)


        self.verticalLayout_39.addWidget(self.frame_37)

        self.stackedWidget.addWidget(self.page_entradas_saidas)
        self.page_simples = QWidget()
        self.page_simples.setObjectName(u"page_simples")
        self.page_simples.setStyleSheet(u"border:0")
        self.verticalLayout_36 = QVBoxLayout(self.page_simples)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.frame_34 = QFrame(self.page_simples)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_34)
        self.verticalLayout_34.setSpacing(7)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.frame_35 = QFrame(self.frame_34)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMinimumSize(QSize(0, 45))
        self.frame_35.setMaximumSize(QSize(16777215, 45))
        self.frame_35.setStyleSheet(u"background-color: rgb(43, 43, 43);\n"
"color: rgb(255, 255, 255);")
        self.frame_35.setFrameShape(QFrame.NoFrame)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_35)
        self.verticalLayout_35.setSpacing(7)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.aba_relatorio_button_7 = QPushButton(self.frame_35)
        self.aba_relatorio_button_7.setObjectName(u"aba_relatorio_button_7")
        self.aba_relatorio_button_7.setMinimumSize(QSize(160, 45))
        self.aba_relatorio_button_7.setMaximumSize(QSize(5555, 45))
        self.aba_relatorio_button_7.setBaseSize(QSize(555, 2))
        self.aba_relatorio_button_7.setFont(font5)
        self.aba_relatorio_button_7.setLayoutDirection(Qt.LeftToRight)
        self.aba_relatorio_button_7.setStyleSheet(u"QPushButton{\n"
"	border:0;\n"
"}")
        self.aba_relatorio_button_7.setIcon(icon13)
        self.aba_relatorio_button_7.setIconSize(QSize(29, 28))
        self.aba_relatorio_button_7.setFlat(False)

        self.verticalLayout_35.addWidget(self.aba_relatorio_button_7, 0, Qt.AlignTop)


        self.verticalLayout_34.addWidget(self.frame_35)

        self.frame_36 = QFrame(self.frame_34)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)

        self.verticalLayout_34.addWidget(self.frame_36)


        self.verticalLayout_36.addWidget(self.frame_34)

        self.stackedWidget.addWidget(self.page_simples)
        self.page_conta = QWidget()
        self.page_conta.setObjectName(u"page_conta")
        self.page_conta.setStyleSheet(u"border:0")
        self.verticalLayout_14 = QVBoxLayout(self.page_conta)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.page_conta)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_11)
        self.verticalLayout_16.setSpacing(9)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 45))
        self.frame_12.setMaximumSize(QSize(16777215, 45))
        self.frame_12.setStyleSheet(u"background-color: rgb(43, 43, 43);\n"
"color: rgb(255, 255, 255);")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_12)
        self.verticalLayout_15.setSpacing(7)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.title = QPushButton(self.frame_12)
        self.title.setObjectName(u"title")
        self.title.setMinimumSize(QSize(160, 45))
        self.title.setMaximumSize(QSize(5555, 45))
        self.title.setBaseSize(QSize(555, 2))
        self.title.setFont(font5)
        self.title.setLayoutDirection(Qt.LeftToRight)
        self.title.setStyleSheet(u"QPushButton{\n"
"	border:0;\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/icons/person-walking-solid .svg", QSize(), QIcon.Normal, QIcon.Off)
        self.title.setIcon(icon14)
        self.title.setIconSize(QSize(29, 28))
        self.title.setFlat(False)

        self.verticalLayout_15.addWidget(self.title, 0, Qt.AlignTop)


        self.verticalLayout_16.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        font14 = QFont()
        font14.setPointSize(9)
        self.frame_13.setFont(font14)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_13)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(180, 0, 180, -1)
        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 260))
        self.frame_14.setStyleSheet(u"border-radius:15px;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_14)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_2 = QFrame(self.frame_14)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 35))
        self.frame_2.setStyleSheet(u"border:0")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(127, 0))
        self.label_3.setMaximumSize(QSize(124, 30))
        font15 = QFont()
        font15.setFamily(u"Century Gothic")
        font15.setPointSize(14)
        font15.setBold(True)
        font15.setWeight(75)
        self.label_3.setFont(font15)
        self.label_3.setStyleSheet(u"color:  rgb(15, 202, 2);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(30, 30))
        self.label_12.setPixmap(QPixmap(u":/icons/cubes-solid.svg"))
        self.label_12.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_12)


        self.verticalLayout_18.addWidget(self.frame_2, 0, Qt.AlignHCenter)

        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
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
        self.frame_17.setStyleSheet(u"border:0")
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_17)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(9, 6, -1, 0)
        self.label_11 = QLabel(self.frame_17)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font13)

        self.gridLayout_6.addWidget(self.label_11, 0, 0, 1, 1, Qt.AlignBottom)

        self.text_empresa_pessoal = QLabel(self.frame_17)
        self.text_empresa_pessoal.setObjectName(u"text_empresa_pessoal")
        self.text_empresa_pessoal.setFont(font6)

        self.gridLayout_6.addWidget(self.text_empresa_pessoal, 1, 0, 1, 1)

        self.btn_alterar_nome = QPushButton(self.frame_17)
        self.btn_alterar_nome.setObjectName(u"btn_alterar_nome")
        self.btn_alterar_nome.setMinimumSize(QSize(100, 0))
        self.btn_alterar_nome.setMaximumSize(QSize(16777215, 100))
        self.btn_alterar_nome.setFont(font13)
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
        self.label_13.setFont(font13)

        self.gridLayout_8.addWidget(self.label_13, 0, 0, 1, 1)

        self.text_email = QLabel(self.frame_19)
        self.text_email.setObjectName(u"text_email")
        self.text_email.setFont(font6)

        self.gridLayout_8.addWidget(self.text_email, 1, 0, 1, 1, Qt.AlignTop)


        self.verticalLayout_19.addWidget(self.frame_19)

        self.frame_18 = QFrame(self.frame_16)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"border:0")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_18)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(-1, 0, 9, 0)
        self.label_15 = QLabel(self.frame_18)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font13)

        self.gridLayout_7.addWidget(self.label_15, 0, 0, 1, 1, Qt.AlignBottom)

        self.text_telefone = QLabel(self.frame_18)
        self.text_telefone.setObjectName(u"text_telefone")
        font16 = QFont()
        font16.setFamily(u"Century Gothic")
        font16.setPointSize(9)
        self.text_telefone.setFont(font16)

        self.gridLayout_7.addWidget(self.text_telefone, 1, 0, 1, 1)

        self.btn_alterar_telefone = QPushButton(self.frame_18)
        self.btn_alterar_telefone.setObjectName(u"btn_alterar_telefone")
        self.btn_alterar_telefone.setMinimumSize(QSize(100, 0))
        self.btn_alterar_telefone.setMaximumSize(QSize(16777215, 100))
        self.btn_alterar_telefone.setFont(font13)
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
        self.frame_20.setStyleSheet(u"border:0")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_20)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.label_17 = QLabel(self.frame_20)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font13)

        self.gridLayout_9.addWidget(self.label_17, 0, 0, 1, 1, Qt.AlignBottom)

        self.btn_atualizar_licenca = QPushButton(self.frame_20)
        self.btn_atualizar_licenca.setObjectName(u"btn_atualizar_licenca")
        self.btn_atualizar_licenca.setMinimumSize(QSize(100, 0))
        self.btn_atualizar_licenca.setMaximumSize(QSize(20000, 16777215))
        self.btn_atualizar_licenca.setFont(font13)
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
        self.text_licenca.setFont(font6)

        self.gridLayout_9.addWidget(self.text_licenca, 1, 0, 1, 1)


        self.verticalLayout_19.addWidget(self.frame_20)


        self.verticalLayout_18.addWidget(self.frame_16)


        self.verticalLayout_17.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_13)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 0))
        self.frame_15.setMaximumSize(QSize(16777215, 80))
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
        self.label_20.setFont(font13)
        self.label_20.setStyleSheet(u"border:0")

        self.verticalLayout_20.addWidget(self.label_20)

        self.label_23 = QLabel(self.frame_15)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font16)
        self.label_23.setStyleSheet(u"border:0")

        self.verticalLayout_20.addWidget(self.label_23)

        self.btn_alterar_senha = QPushButton(self.frame_15)
        self.btn_alterar_senha.setObjectName(u"btn_alterar_senha")
        self.btn_alterar_senha.setMinimumSize(QSize(100, 0))
        self.btn_alterar_senha.setMaximumSize(QSize(100, 32))
        self.btn_alterar_senha.setFont(font13)
        self.btn_alterar_senha.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_senha.setStyleSheet(u"QPushButton{\n"
"	border:1px solid;\n"
"	padding:10px;\n"
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
        self.label_21.setFont(font13)
        self.label_21.setStyleSheet(u"border:0")

        self.verticalLayout_21.addWidget(self.label_21)

        self.label_22 = QLabel(self.frame_21)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font16)
        self.label_22.setStyleSheet(u"border:0")

        self.verticalLayout_21.addWidget(self.label_22)

        self.btn_excluir_conta = QPushButton(self.frame_21)
        self.btn_excluir_conta.setObjectName(u"btn_excluir_conta")
        self.btn_excluir_conta.setMinimumSize(QSize(100, 0))
        self.btn_excluir_conta.setMaximumSize(QSize(100, 32))
        self.btn_excluir_conta.setFont(font13)
        self.btn_excluir_conta.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir_conta.setStyleSheet(u"QPushButton{\n"
"	border:1px solid red;\n"
"	padding:10px;\n"
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

        self.top_frame = QFrame(self.centralwidget)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setMinimumSize(QSize(0, 110))
        self.top_frame.setMaximumSize(QSize(16777215, 110))
        self.top_frame.setStyleSheet(u"border-bottom: 1px solid rgb(181, 181, 181);\n"
"background-color: rgb(43, 43, 43);")
        self.top_frame.setFrameShape(QFrame.NoFrame)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.top_frame.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.top_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 0, 0)
        self.frame = QFrame(self.top_frame)
        self.frame.setObjectName(u"frame")
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
        self.label.setStyleSheet(u"border:0")
        self.label.setPixmap(QPixmap(u":/icons/ori.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(True)

        self.horizontalLayout_2.addWidget(self.label, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.frame, 0, Qt.AlignLeft)

        self.conteudo_top_frame = QFrame(self.top_frame)
        self.conteudo_top_frame.setObjectName(u"conteudo_top_frame")
        self.conteudo_top_frame.setMinimumSize(QSize(600, 70))
        self.conteudo_top_frame.setCursor(QCursor(Qt.ArrowCursor))
        self.conteudo_top_frame.setFrameShape(QFrame.NoFrame)
        self.conteudo_top_frame.setFrameShadow(QFrame.Plain)
        self.conteudo_top_frame.setLineWidth(0)
        self.gridLayout_2 = QGridLayout(self.conteudo_top_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_2.setHorizontalSpacing(15)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(0, 0, 20, 15)
        self.btn_virepro_button = QPushButton(self.conteudo_top_frame)
        self.btn_virepro_button.setObjectName(u"btn_virepro_button")
        self.btn_virepro_button.setMinimumSize(QSize(210, 45))
        self.btn_virepro_button.setMaximumSize(QSize(170, 16777215))
        self.btn_virepro_button.setFont(font13)
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
        icon15 = QIcon()
        icon15.addFile(u":/icons/crown-solid (2).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_virepro_button.setIcon(icon15)
        self.btn_virepro_button.setIconSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.btn_virepro_button, 1, 0, 1, 1)

        self.conexao_label = QPushButton(self.conteudo_top_frame)
        self.conexao_label.setObjectName(u"conexao_label")
        self.conexao_label.setEnabled(False)
        self.conexao_label.setMinimumSize(QSize(0, 45))
        self.conexao_label.setMaximumSize(QSize(150, 16777215))
        font17 = QFont()
        font17.setFamily(u"Nirmala UI")
        font17.setPointSize(9)
        font17.setBold(True)
        font17.setWeight(75)
        self.conexao_label.setFont(font17)
        self.conexao_label.setCursor(QCursor(Qt.PointingHandCursor))
        self.conexao_label.setMouseTracking(False)
        self.conexao_label.setAcceptDrops(False)
        self.conexao_label.setLayoutDirection(Qt.LeftToRight)
        self.conexao_label.setStyleSheet(u"QPushButton{\n"
"	border:1px solid white;\n"
"	color: rgb(218, 14, 14);\n"
"	border-radius:5px;\n"
"	background-color: rgb(48, 48, 48);\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u":/icons/plug-circle-exclamation-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon16.addFile(u":/icons/plug-circle-exclamation-solid.svg", QSize(), QIcon.Disabled, QIcon.Off)
        icon16.addFile(u":/icons/plug-circle-exclamation-solid.svg", QSize(), QIcon.Disabled, QIcon.On)
        icon16.addFile(u":/icons/plug-solid (1).svg", QSize(), QIcon.Active, QIcon.Off)
        icon16.addFile(u":/icons/plug-solid (1).svg", QSize(), QIcon.Active, QIcon.On)
        self.conexao_label.setIcon(icon16)
        self.conexao_label.setCheckable(False)
        self.conexao_label.setFlat(False)

        self.gridLayout_2.addWidget(self.conexao_label, 1, 1, 1, 1)

        self.label_2 = QLabel(self.conteudo_top_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 30))
        self.label_2.setFont(font13)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border:0")
        self.label_2.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)


        self.horizontalLayout.addWidget(self.conteudo_top_frame, 0, Qt.AlignRight)


        self.gridLayout.addWidget(self.top_frame, 1, 0, 1, 2)

        self.frame_29 = QFrame(self.centralwidget)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(0, 32))
        self.frame_29.setStyleSheet(u"background-color: rgb(25, 25, 25);")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(10, 0, 0, 0)
        self.frame_44 = QFrame(self.frame_29)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setMinimumSize(QSize(147, 0))
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_16.setSpacing(16)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_30 = QLabel(self.frame_44)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMaximumSize(QSize(25, 20))
        self.label_30.setPixmap(QPixmap(u":/icons/icon (2).png"))
        self.label_30.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.label_30)

        self.pushButton = QPushButton(self.frame_44)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 32))
        self.pushButton.setFont(font6)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
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

        self.label_29 = QLabel(self.frame_29)
        self.label_29.setObjectName(u"label_29")
        font18 = QFont()
        font18.setFamily(u"Ebrima")
        font18.setPointSize(10)
        font18.setBold(False)
        font18.setWeight(50)
        self.label_29.setFont(font18)
        self.label_29.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_29.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_29, 0, Qt.AlignHCenter)

        self.frame_30 = QFrame(self.frame_29)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMaximumSize(QSize(16777215, 32))
        self.frame_30.setStyleSheet(u"border:0")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize_window = QPushButton(self.frame_30)
        self.btn_minimize_window.setObjectName(u"btn_minimize_window")
        self.btn_minimize_window.setMinimumSize(QSize(50, 32))
        self.btn_minimize_window.setMaximumSize(QSize(50, 32))
        self.btn_minimize_window.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgb(43, 43, 43);\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u":/icons/remove_minimize_minus_delete_icon_219231.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize_window.setIcon(icon17)
        self.btn_minimize_window.setIconSize(QSize(25, 25))

        self.horizontalLayout_9.addWidget(self.btn_minimize_window)

        self.btn_close_windows = QPushButton(self.frame_30)
        self.btn_close_windows.setObjectName(u"btn_close_windows")
        self.btn_close_windows.setMinimumSize(QSize(50, 32))
        self.btn_close_windows.setMaximumSize(QSize(50, 32))
        self.btn_close_windows.setStyleSheet(u"QPushButton:hover{\n"
"\n"
"background-color: rgb(218, 14, 14)}")
        icon18 = QIcon()
        icon18.addFile(u":/icons/delete_cross_remove_cancel_icon_219222.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close_windows.setIcon(icon18)

        self.horizontalLayout_9.addWidget(self.btn_close_windows)


        self.horizontalLayout_10.addWidget(self.frame_30, 0, Qt.AlignRight)


        self.gridLayout.addWidget(self.frame_29, 0, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.aba_pesagem_button.setDefault(False)
        self.stackedWidget.setCurrentIndex(0)
        self.comboBox_produto.setCurrentIndex(0)
        self.comboBox_cliente.setCurrentIndex(0)
        self.comboBox_fornecedor.setCurrentIndex(0)
        self.comboBox_veiculo.setCurrentIndex(0)
        self.comboBox_veiculos_produtos.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Caltec - Software de pesagem", None))
        self.adicionar_balanca.setText(QCoreApplication.translate("MainWindow", u"Conectar balan\u00e7a", None))
        self.fechar_aplicativo.setText(QCoreApplication.translate("MainWindow", u"Fechar aplicativo", None))
        self.actionAvan_adas.setText(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es Avan\u00e7adas", None))
        self.aba_pesagem_button.setText(QCoreApplication.translate("MainWindow", u"Pesagens                 \u25bc", None))
        self.button_simples_pesagens.setText(QCoreApplication.translate("MainWindow", u"Simples", None))
        self.button_entsaid_pesagens.setText(QCoreApplication.translate("MainWindow", u"Entradas e Sa\u00eddas", None))
        self.button_avulsas_pesagens.setText(QCoreApplication.translate("MainWindow", u"Avulsas", None))
        self.aba_grupo_button.setText(QCoreApplication.translate("MainWindow", u"Grupos                    \u25bc", None))
        self.button_clientes_grupos.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.button_produtos_grupos.setText(QCoreApplication.translate("MainWindow", u"Produtos", None))
        self.button_fornecedores_grupos.setText(QCoreApplication.translate("MainWindow", u"Fornecedores", None))
        self.button_veiculos_grupos.setText(QCoreApplication.translate("MainWindow", u"Veiculos", None))
        self.aba_relatorio_button.setText(QCoreApplication.translate("MainWindow", u"Relat\u00f3rios pesagens   ", None))
        self.aba_conta_button.setText(QCoreApplication.translate("MainWindow", u"Conta                         ", None))
        self.label_4.setText("")
        self.restantes_label.setText(QCoreApplication.translate("MainWindow", u"Pesagens restantes: 26", None))
        self.info_pro_label.setText(QCoreApplication.translate("MainWindow", u"Atualize para a vers\u00e3o PRO e aproveite todos os recursos sem limita\u00e7\u00f5es.", None))
        self.aba_sair_button.setText(QCoreApplication.translate("MainWindow", u"Sair        ", None))
        self.aba_relatorio_button_2.setText(QCoreApplication.translate("MainWindow", u"Relat\u00f3rios pesagens   ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Cliente", None))
        self.comboBox_produto.setItemText(0, QCoreApplication.translate("MainWindow", u"Nenhum", None))
        self.comboBox_produto.setItemText(1, QCoreApplication.translate("MainWindow", u"Teste1", None))
        self.comboBox_produto.setItemText(2, QCoreApplication.translate("MainWindow", u"Teste2", None))

        self.comboBox_cliente.setItemText(0, QCoreApplication.translate("MainWindow", u"Nenhum", None))
        self.comboBox_cliente.setItemText(1, QCoreApplication.translate("MainWindow", u"Teste1", None))
        self.comboBox_cliente.setItemText(2, QCoreApplication.translate("MainWindow", u"Teste2", None))

        self.comboBox_fornecedor.setItemText(0, QCoreApplication.translate("MainWindow", u"Nenhum", None))
        self.comboBox_fornecedor.setItemText(1, QCoreApplication.translate("MainWindow", u"Teste1", None))
        self.comboBox_fornecedor.setItemText(2, QCoreApplication.translate("MainWindow", u"Teste2", None))

        self.comboBox_veiculo.setItemText(0, QCoreApplication.translate("MainWindow", u"Nenhum", None))
        self.comboBox_veiculo.setItemText(1, QCoreApplication.translate("MainWindow", u"Teste1", None))
        self.comboBox_veiculo.setItemText(2, QCoreApplication.translate("MainWindow", u"Teste2", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Produto", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Fornecedor", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Ve\u00edculo", None))
        self.label_9.setText("")
        self.btn_filtro_id.setText("")
        self.text_filtro_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.data_fixa.setText(QCoreApplication.translate("MainWindow", u"Data fixa", None))
        self.data_antes_de.setText(QCoreApplication.translate("MainWindow", u"Antes de", None))
        self.data_depois_de.setText(QCoreApplication.translate("MainWindow", u"Depois de", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.btn_Aplicar_filtro_geral.setText(QCoreApplication.translate("MainWindow", u"Aplicar Filtragem", None))
        self.btn_inprimir.setText(QCoreApplication.translate("MainWindow", u"Imprimir relat\u00f3rio", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PLACA", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"MOTORISTA", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"PRODUTO", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"CLIENTE", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"FORNECEDOR", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"KG (ENTRADA)", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"KG (SA\u00cdDA)", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"DATA", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"HOR\u00c1RIO", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"VE\u00cdCULO", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"3", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem15 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem16 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"1234FGH", None));
        ___qtablewidgetitem17 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Ryan Barbosa", None));
        ___qtablewidgetitem18 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Whisky", None));
        ___qtablewidgetitem19 = self.tableWidget.item(0, 4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Ambev", None));
        ___qtablewidgetitem20 = self.tableWidget.item(0, 5)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"CALTEC", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 6)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 7)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"50000", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 8)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"10/04/2022", None));
        ___qtablewidgetitem24 = self.tableWidget.item(0, 9)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"03:20", None));
        ___qtablewidgetitem25 = self.tableWidget.item(0, 10)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"VOLVO", None));
        ___qtablewidgetitem26 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem27 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"5678KJL", None));
        ___qtablewidgetitem28 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Ryan Barbosa", None));
        ___qtablewidgetitem29 = self.tableWidget.item(1, 3)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Whisky", None));
        ___qtablewidgetitem30 = self.tableWidget.item(1, 4)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Ambev", None));
        ___qtablewidgetitem31 = self.tableWidget.item(1, 5)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"CALTEC", None));
        ___qtablewidgetitem32 = self.tableWidget.item(1, 6)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem33 = self.tableWidget.item(1, 7)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"50000", None));
        ___qtablewidgetitem34 = self.tableWidget.item(1, 8)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"14/02/2022", None));
        ___qtablewidgetitem35 = self.tableWidget.item(1, 9)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"10:00", None));
        ___qtablewidgetitem36 = self.tableWidget.item(1, 10)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"NISSAN", None));
        ___qtablewidgetitem37 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem38 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"0921LSK", None));
        ___qtablewidgetitem39 = self.tableWidget.item(2, 2)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Cleber Silva", None));
        ___qtablewidgetitem40 = self.tableWidget.item(2, 3)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Cigarro", None));
        ___qtablewidgetitem41 = self.tableWidget.item(2, 4)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Padaria sol", None));
        ___qtablewidgetitem42 = self.tableWidget.item(2, 5)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"CALTEC", None));
        ___qtablewidgetitem43 = self.tableWidget.item(2, 6)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem44 = self.tableWidget.item(2, 7)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"30000", None));
        ___qtablewidgetitem45 = self.tableWidget.item(2, 8)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"20/01/2022", None));
        ___qtablewidgetitem46 = self.tableWidget.item(2, 9)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"13:27", None));
        ___qtablewidgetitem47 = self.tableWidget.item(2, 10)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"NISSAN", None));
        ___qtablewidgetitem48 = self.tableWidget.item(3, 0)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem49 = self.tableWidget.item(3, 1)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"3499WAS", None));
        ___qtablewidgetitem50 = self.tableWidget.item(3, 2)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"Cleber Silva", None));
        ___qtablewidgetitem51 = self.tableWidget.item(3, 3)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"Whisky", None));
        ___qtablewidgetitem52 = self.tableWidget.item(3, 4)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"Ambev", None));
        ___qtablewidgetitem53 = self.tableWidget.item(3, 5)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"CALTEC", None));
        ___qtablewidgetitem54 = self.tableWidget.item(3, 6)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem55 = self.tableWidget.item(3, 7)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"50000", None));
        ___qtablewidgetitem56 = self.tableWidget.item(3, 8)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"30/05/2022", None));
        ___qtablewidgetitem57 = self.tableWidget.item(3, 9)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"20:55", None));
        ___qtablewidgetitem58 = self.tableWidget.item(3, 10)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"NISSAN", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.aba_relatorio_button_3.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Registrar novos clientes", None))
        self.input_clientes_nome.setText("")
        self.input_clientes_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME", None))
        self.input_clientes_cpf.setText("")
        self.input_clientes_cpf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF / CNPJ", None))
        self.input_clientes_rg.setText("")
        self.input_clientes_rg.setPlaceholderText(QCoreApplication.translate("MainWindow", u"RG (OPCIONAL)", None))
        self.input_clientes_endereco.setText("")
        self.input_clientes_endereco.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ENDERE\u00c7O (OPCIONAL)", None))
        self.input_clientes_cidade.setText("")
        self.input_clientes_cidade.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CIDADE", None))
        self.input_clientes_estado.setText("")
        self.input_clientes_estado.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ESTADO", None))
        self.input_clientes_telefone.setText("")
        self.input_clientes_telefone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TELEFONE", None))
        self.btn_registrar_clientes.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR", None))
        self.btn_menu_registrar_clientes.setText("")
        self.label_16.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Historico de Clientes registrados", None))
        self.btn_remover_clientes.setText(QCoreApplication.translate("MainWindow", u"Remover cliente(s) selecionado(s)", None))
        ___qtablewidgetitem59 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"EXCLUIR", None));
        ___qtablewidgetitem60 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem61 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem62 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
        ___qtablewidgetitem63 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"RG", None));
        ___qtablewidgetitem64 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"ENDERE\u00c7O", None));
        ___qtablewidgetitem65 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"CIDADE", None));
        ___qtablewidgetitem66 = self.tableWidget_2.horizontalHeaderItem(7)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"ESTADO", None));
        ___qtablewidgetitem67 = self.tableWidget_2.horizontalHeaderItem(8)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None));

        __sortingEnabled1 = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        ___qtablewidgetitem68 = self.tableWidget_2.item(0, 1)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem69 = self.tableWidget_2.item(0, 2)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"Ryan Barbosa", None));
        ___qtablewidgetitem70 = self.tableWidget_2.item(0, 3)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"567.765.576-56", None));
        ___qtablewidgetitem71 = self.tableWidget_2.item(0, 4)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"50.510.954-8", None));
        ___qtablewidgetitem72 = self.tableWidget_2.item(0, 5)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"Rua Napol\u00e9s, 18", None));
        ___qtablewidgetitem73 = self.tableWidget_2.item(0, 6)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"Guarulhos", None));
        ___qtablewidgetitem74 = self.tableWidget_2.item(0, 7)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"SP", None));
        ___qtablewidgetitem75 = self.tableWidget_2.item(0, 8)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"11990901254", None));
        ___qtablewidgetitem76 = self.tableWidget_2.item(1, 1)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem77 = self.tableWidget_2.item(1, 2)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"Cleber Silva", None));
        ___qtablewidgetitem78 = self.tableWidget_2.item(1, 3)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"354.543.534-45", None));
        ___qtablewidgetitem79 = self.tableWidget_2.item(1, 4)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"40.410.684-9", None));
        ___qtablewidgetitem80 = self.tableWidget_2.item(1, 5)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"Rua da lua, 99", None));
        ___qtablewidgetitem81 = self.tableWidget_2.item(1, 6)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"Guaruj\u00e1", None));
        ___qtablewidgetitem82 = self.tableWidget_2.item(1, 7)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"SP", None));
        ___qtablewidgetitem83 = self.tableWidget_2.item(1, 8)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"11952354578", None));
        self.tableWidget_2.setSortingEnabled(__sortingEnabled1)

        self.aba_relatorio_button_4.setText(QCoreApplication.translate("MainWindow", u"Fornecedores", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Registrar novos fornecedores", None))
        self.input_forne_nome.setText("")
        self.input_forne_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME", None))
        self.input_forne_cpf.setText("")
        self.input_forne_cpf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.input_forne_rg.setText("")
        self.input_forne_rg.setPlaceholderText(QCoreApplication.translate("MainWindow", u"RG (OPCIONAL)", None))
        self.input_forne_endereco.setText("")
        self.input_forne_endereco.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ENDERE\u00c7O (OPCIONAL)", None))
        self.input_forne_cidade.setText("")
        self.input_forne_cidade.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CIDADE", None))
        self.input_forne_estado.setText("")
        self.input_forne_estado.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ESTADO", None))
        self.input_forne_telefone.setText("")
        self.input_forne_telefone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TELEFONE", None))
        self.btn_registrar_forne.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR", None))
        self.btn_menu_registrar_forne.setText("")
        self.label_24.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Historico de Fornecedores registrados", None))
        self.btn_remover_forne.setText(QCoreApplication.translate("MainWindow", u"Remover fornecedor(es) selecionado(s)", None))
        ___qtablewidgetitem84 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"EXCLUIR", None));
        ___qtablewidgetitem85 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem86 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem87 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
        ___qtablewidgetitem88 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("MainWindow", u"RG", None));
        ___qtablewidgetitem89 = self.tableWidget_3.horizontalHeaderItem(5)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("MainWindow", u"ENDERE\u00c7O", None));
        ___qtablewidgetitem90 = self.tableWidget_3.horizontalHeaderItem(6)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("MainWindow", u"CIDADE", None));
        ___qtablewidgetitem91 = self.tableWidget_3.horizontalHeaderItem(7)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("MainWindow", u"ESTADO", None));
        ___qtablewidgetitem92 = self.tableWidget_3.horizontalHeaderItem(8)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None));

        __sortingEnabled2 = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        ___qtablewidgetitem93 = self.tableWidget_3.item(0, 1)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem94 = self.tableWidget_3.item(0, 2)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("MainWindow", u"CALTEC", None));
        ___qtablewidgetitem95 = self.tableWidget_3.item(0, 3)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("MainWindow", u"222.222.222-22", None));
        ___qtablewidgetitem96 = self.tableWidget_3.item(0, 5)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("MainWindow", u"Anaoplos, 22", None));
        ___qtablewidgetitem97 = self.tableWidget_3.item(0, 6)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("MainWindow", u"Pinheiros", None));
        ___qtablewidgetitem98 = self.tableWidget_3.item(0, 7)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("MainWindow", u"SP", None));
        ___qtablewidgetitem99 = self.tableWidget_3.item(0, 8)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("MainWindow", u"1158235665", None));
        self.tableWidget_3.setSortingEnabled(__sortingEnabled2)

        self.aba_relatorio_button_6.setText(QCoreApplication.translate("MainWindow", u"Ve\u00edculos", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Registrar novos ve\u00edculos", None))
        self.input_veiculos_nome.setText("")
        self.input_veiculos_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME", None))
        self.input_veiculos_valor.setText("")
        self.input_veiculos_valor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"VALOR PESAGEM", None))
        self.input_veiculos_placa.setText("")
        self.input_veiculos_placa.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PLACA", None))
        self.comboBox_veiculos_produtos.setItemText(0, QCoreApplication.translate("MainWindow", u"Nenhum", None))
        self.comboBox_veiculos_produtos.setItemText(1, QCoreApplication.translate("MainWindow", u"Cigarro", None))
        self.comboBox_veiculos_produtos.setItemText(2, QCoreApplication.translate("MainWindow", u"Whisky", None))

        self.btn_registrar_veiculos.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR", None))
        self.btn_menu_registrar_veiculos.setText("")
        self.label_27.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Historico de Clientes registrados", None))
        self.btn_remover_veiculos.setText(QCoreApplication.translate("MainWindow", u"Remover ve\u00edculo(s) selecionado(s)", None))
        ___qtablewidgetitem100 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("MainWindow", u"EXCLUIR", None));
        ___qtablewidgetitem101 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem102 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem102.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem103 = self.tableWidget_4.horizontalHeaderItem(3)
        ___qtablewidgetitem103.setText(QCoreApplication.translate("MainWindow", u"VALOR PESAGEM", None));
        ___qtablewidgetitem104 = self.tableWidget_4.horizontalHeaderItem(4)
        ___qtablewidgetitem104.setText(QCoreApplication.translate("MainWindow", u"PLACA", None));
        ___qtablewidgetitem105 = self.tableWidget_4.horizontalHeaderItem(5)
        ___qtablewidgetitem105.setText(QCoreApplication.translate("MainWindow", u"PRODUTO", None));

        __sortingEnabled3 = self.tableWidget_4.isSortingEnabled()
        self.tableWidget_4.setSortingEnabled(False)
        ___qtablewidgetitem106 = self.tableWidget_4.item(0, 1)
        ___qtablewidgetitem106.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem107 = self.tableWidget_4.item(0, 2)
        ___qtablewidgetitem107.setText(QCoreApplication.translate("MainWindow", u"VOLVO", None));
        ___qtablewidgetitem108 = self.tableWidget_4.item(0, 3)
        ___qtablewidgetitem108.setText(QCoreApplication.translate("MainWindow", u"500", None));
        ___qtablewidgetitem109 = self.tableWidget_4.item(0, 4)
        ___qtablewidgetitem109.setText(QCoreApplication.translate("MainWindow", u"FTG567", None));
        ___qtablewidgetitem110 = self.tableWidget_4.item(0, 5)
        ___qtablewidgetitem110.setText(QCoreApplication.translate("MainWindow", u"Cigarro", None));
        ___qtablewidgetitem111 = self.tableWidget_4.item(1, 1)
        ___qtablewidgetitem111.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem112 = self.tableWidget_4.item(1, 2)
        ___qtablewidgetitem112.setText(QCoreApplication.translate("MainWindow", u"NISSAN", None));
        ___qtablewidgetitem113 = self.tableWidget_4.item(1, 3)
        ___qtablewidgetitem113.setText(QCoreApplication.translate("MainWindow", u"500", None));
        ___qtablewidgetitem114 = self.tableWidget_4.item(1, 4)
        ___qtablewidgetitem114.setText(QCoreApplication.translate("MainWindow", u"HJA899", None));
        ___qtablewidgetitem115 = self.tableWidget_4.item(1, 5)
        ___qtablewidgetitem115.setText(QCoreApplication.translate("MainWindow", u"Whisky", None));
        self.tableWidget_4.setSortingEnabled(__sortingEnabled3)

        self.aba_relatorio_button_12.setText(QCoreApplication.translate("MainWindow", u"Produtos", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Registrar novos produtos", None))
        self.input_produtos_nome.setText("")
        self.input_produtos_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME", None))
        self.input_produtos_estoqueKG.setText("")
        self.input_produtos_estoqueKG.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ESTOQUE", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"KG", None))
        self.input_produtos_preco.setText("")
        self.input_produtos_preco.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PRE\u00c7O", None))
        self.input_produtos_densidade.setText("")
        self.input_produtos_densidade.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DENSIDADE", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"T / M3", None))
        self.input_produtos_embalagemKG.setText("")
        self.input_produtos_embalagemKG.setPlaceholderText(QCoreApplication.translate("MainWindow", u"EMBALAGEM", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"KG", None))
        self.btn_registrar_produtos.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR", None))
        self.btn_menu_registrar_produtos.setText("")
        self.label_36.setText("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Historico de Produtos registrados", None))
        self.btn_remover_produtos.setText(QCoreApplication.translate("MainWindow", u"Remover produto(s) selecionado(s)", None))
        ___qtablewidgetitem116 = self.tableWidget_7.horizontalHeaderItem(0)
        ___qtablewidgetitem116.setText(QCoreApplication.translate("MainWindow", u"EXCLUIR", None));
        ___qtablewidgetitem117 = self.tableWidget_7.horizontalHeaderItem(1)
        ___qtablewidgetitem117.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem118 = self.tableWidget_7.horizontalHeaderItem(2)
        ___qtablewidgetitem118.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem119 = self.tableWidget_7.horizontalHeaderItem(3)
        ___qtablewidgetitem119.setText(QCoreApplication.translate("MainWindow", u"ESTOQUE", None));
        ___qtablewidgetitem120 = self.tableWidget_7.horizontalHeaderItem(4)
        ___qtablewidgetitem120.setText(QCoreApplication.translate("MainWindow", u"PRE\u00c7O", None));
        ___qtablewidgetitem121 = self.tableWidget_7.horizontalHeaderItem(5)
        ___qtablewidgetitem121.setText(QCoreApplication.translate("MainWindow", u"DENSIDADE", None));
        ___qtablewidgetitem122 = self.tableWidget_7.horizontalHeaderItem(6)
        ___qtablewidgetitem122.setText(QCoreApplication.translate("MainWindow", u"EMBALAGEM", None));

        __sortingEnabled4 = self.tableWidget_7.isSortingEnabled()
        self.tableWidget_7.setSortingEnabled(False)
        ___qtablewidgetitem123 = self.tableWidget_7.item(0, 1)
        ___qtablewidgetitem123.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem124 = self.tableWidget_7.item(0, 2)
        ___qtablewidgetitem124.setText(QCoreApplication.translate("MainWindow", u"Whisky", None));
        ___qtablewidgetitem125 = self.tableWidget_7.item(0, 3)
        ___qtablewidgetitem125.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem126 = self.tableWidget_7.item(0, 4)
        ___qtablewidgetitem126.setText(QCoreApplication.translate("MainWindow", u"200", None));
        ___qtablewidgetitem127 = self.tableWidget_7.item(0, 5)
        ___qtablewidgetitem127.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem128 = self.tableWidget_7.item(0, 6)
        ___qtablewidgetitem128.setText(QCoreApplication.translate("MainWindow", u"0100", None));
        ___qtablewidgetitem129 = self.tableWidget_7.item(1, 1)
        ___qtablewidgetitem129.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem130 = self.tableWidget_7.item(1, 2)
        ___qtablewidgetitem130.setText(QCoreApplication.translate("MainWindow", u"Cigarro", None));
        ___qtablewidgetitem131 = self.tableWidget_7.item(1, 3)
        ___qtablewidgetitem131.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem132 = self.tableWidget_7.item(1, 4)
        ___qtablewidgetitem132.setText(QCoreApplication.translate("MainWindow", u"50", None));
        ___qtablewidgetitem133 = self.tableWidget_7.item(1, 5)
        ___qtablewidgetitem133.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem134 = self.tableWidget_7.item(1, 6)
        ___qtablewidgetitem134.setText(QCoreApplication.translate("MainWindow", u"0020", None));
        self.tableWidget_7.setSortingEnabled(__sortingEnabled4)

        self.aba_relatorio_button_9.setText(QCoreApplication.translate("MainWindow", u"Avulsas", None))
        self.aba_relatorio_button_8.setText(QCoreApplication.translate("MainWindow", u"Entradas e Sa\u00eddas", None))
        self.aba_relatorio_button_7.setText(QCoreApplication.translate("MainWindow", u"Simples", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Conta", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"SEUS DADOS", None))
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
        self.conexao_label.setText(QCoreApplication.translate("MainWindow", u"Sem Conex\u00e3o", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Status Balan\u00e7a:", None))
        self.label_30.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Conectar balan\u00e7a", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"ryanbs - Software de pesagem", None))
        self.btn_minimize_window.setText("")
        self.btn_close_windows.setText("")
    # retranslateUi

