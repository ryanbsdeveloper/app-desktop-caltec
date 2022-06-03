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
        MainWindow.resize(950, 640)
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
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setWeight(50)
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
        self.button_simples_pesagens.setFont(font2)
        self.button_simples_pesagens.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(250, 250, 250);\n"
"	border:1px solid\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(231, 231, 231);\n"
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
        font3 = QFont()
        font3.setFamily(u"Century Gothic")
        font3.setPointSize(10)
        self.aba_grupo_button.setFont(font3)
        self.aba_grupo_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.aba_grupo_button.setStyleSheet(u"QPushButton{\n"
"	border:0;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(250, 250, 250);\n"
"	border:1px solid\n"
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
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(231, 231, 231);\n"
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
        self.aba_relatorio_button.setFont(font3)
        self.aba_relatorio_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.aba_relatorio_button.setLayoutDirection(Qt.LeftToRight)
        self.aba_relatorio_button.setStyleSheet(u"QPushButton{\n"
"	border:0;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(250, 250, 250);\n"
"	border:1px solid\n"
"}\n"
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
        self.aba_conta_button.setFont(font3)
        self.aba_conta_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.aba_conta_button.setStyleSheet(u"QPushButton{\n"
"	border:0;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(250, 250, 250);\n"
"	border:1px solid\n"
"}\n"
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
        font4 = QFont()
        font4.setFamily(u"Century Gothic")
        font4.setBold(True)
        font4.setWeight(75)
        self.restantes_label.setFont(font4)
        self.restantes_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.restantes_label)


        self.verticalLayout_5.addWidget(self.info_pro_frame)

        self.info_pro_label = QLabel(self.info_menu_pro_frame)
        self.info_pro_label.setObjectName(u"info_pro_label")
        font5 = QFont()
        font5.setFamily(u"Century Gothic")
        font5.setPointSize(11)
        self.info_pro_label.setFont(font5)
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
        self.aba_sair_button.setFont(font3)
        self.aba_sair_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.aba_sair_button.setStyleSheet(u"QPushButton{\n"
"	border:0;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(250, 250, 250);\n"
"	border:1px solid\n"
"}\n"
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

        self.gridLayout.addWidget(self.menu_frame, 1, 0, 1, 1)

        self.top_frame = QFrame(self.centralwidget)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setMaximumSize(QSize(16777215, 90))
        self.top_frame.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-bottom: 1px solid rgb(181, 181, 181)")
        self.top_frame.setFrameShape(QFrame.NoFrame)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.top_frame.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.top_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
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
        self.label.setMinimumSize(QSize(250, 0))
        self.label.setMaximumSize(QSize(199, 16777215))
        self.label.setPixmap(QPixmap(u":/icons/logo.png"))
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(True)

        self.horizontalLayout_2.addWidget(self.label)


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
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(0, 0, 20, 0)
        self.btn_virepro_button = QPushButton(self.conteudo_top_frame)
        self.btn_virepro_button.setObjectName(u"btn_virepro_button")
        self.btn_virepro_button.setMinimumSize(QSize(210, 45))
        self.btn_virepro_button.setMaximumSize(QSize(170, 16777215))
        font6 = QFont()
        font6.setFamily(u"Century Gothic")
        font6.setPointSize(10)
        font6.setBold(True)
        font6.setWeight(75)
        self.btn_virepro_button.setFont(font6)
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
        icon6 = QIcon()
        icon6.addFile(u":/icons/crown-solid (2).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_virepro_button.setIcon(icon6)
        self.btn_virepro_button.setIconSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.btn_virepro_button, 1, 0, 1, 1)

        self.label_2 = QLabel(self.conteudo_top_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 20))
        self.label_2.setFont(font6)
        self.label_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-bottom: 1px solidrgb(0, 255, 0)")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)

        self.conexao_label = QPushButton(self.conteudo_top_frame)
        self.conexao_label.setObjectName(u"conexao_label")
        self.conexao_label.setEnabled(False)
        self.conexao_label.setMinimumSize(QSize(0, 45))
        self.conexao_label.setMaximumSize(QSize(150, 16777215))
        font7 = QFont()
        font7.setFamily(u"Nirmala UI")
        font7.setPointSize(9)
        font7.setBold(True)
        font7.setWeight(75)
        self.conexao_label.setFont(font7)
        self.conexao_label.setMouseTracking(False)
        self.conexao_label.setAcceptDrops(False)
        self.conexao_label.setLayoutDirection(Qt.LeftToRight)
        self.conexao_label.setStyleSheet(u"QPushButton{\n"
"	border:0;\n"
"	color:;\n"
"	color: rgb(255, 83, 83);\n"
"	border-radius:5px;\n"
"	background-color: rgb(48, 48, 48);\n"
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

        self.gridLayout_2.addWidget(self.conexao_label, 1, 1, 1, 1)


        self.horizontalLayout.addWidget(self.conteudo_top_frame, 0, Qt.AlignRight)


        self.gridLayout.addWidget(self.top_frame, 0, 0, 1, 2)

        self.principal_frame = QFrame(self.centralwidget)
        self.principal_frame.setObjectName(u"principal_frame")
        self.principal_frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.principal_frame.setFrameShape(QFrame.NoFrame)
        self.principal_frame.setFrameShadow(QFrame.Raised)
        self.principal_frame.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.principal_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
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
"border: 1px solid rgb(181, 181, 181)")
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
        self.verticalLayout_13.setContentsMargins(9, 9, 9, 0)
        self.frame_5 = QFrame(self.frame_6)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 40))
        self.frame_5.setStyleSheet(u"border-bottom:1px solid rgb(154, 154, 154)")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_5)
        self.verticalLayout_12.setSpacing(7)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.aba_relatorio_button_2 = QPushButton(self.frame_5)
        self.aba_relatorio_button_2.setObjectName(u"aba_relatorio_button_2")
        self.aba_relatorio_button_2.setMinimumSize(QSize(160, 17))
        self.aba_relatorio_button_2.setMaximumSize(QSize(5555, 40))
        self.aba_relatorio_button_2.setBaseSize(QSize(555, 2))
        font8 = QFont()
        font8.setFamily(u"Century Gothic")
        font8.setPointSize(19)
        self.aba_relatorio_button_2.setFont(font8)
        self.aba_relatorio_button_2.setLayoutDirection(Qt.LeftToRight)
        self.aba_relatorio_button_2.setStyleSheet(u"QPushButton{\n"
"	border:0;\n"
"}")
        self.aba_relatorio_button_2.setIcon(icon3)
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
        self.label_5.setFont(font3)

        self.gridLayout_3.addWidget(self.label_5, 0, 2, 1, 1)

        self.comboBox_produto = QComboBox(self.frame_7)
        self.comboBox_produto.addItem("")
        self.comboBox_produto.addItem("")
        self.comboBox_produto.addItem("")
        self.comboBox_produto.setObjectName(u"comboBox_produto")
        self.comboBox_produto.setStyleSheet(u"QComboBox{\n"
"	border:1px solid rgb(67, 202, 0);\n"
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
"	border:1px solid rgb(67, 202, 0);\n"
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
"	border:1px solid rgb(67, 202, 0);\n"
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
"	border:1px solid rgb(67, 202, 0);\n"
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
        self.label_6.setFont(font3)

        self.gridLayout_3.addWidget(self.label_6, 0, 3, 1, 1)

        self.label_7 = QLabel(self.frame_7)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 13))
        self.label_7.setFont(font3)

        self.gridLayout_3.addWidget(self.label_7, 0, 4, 1, 1)

        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 13))
        self.label_8.setFont(font3)

        self.gridLayout_3.addWidget(self.label_8, 0, 5, 1, 1)

        self.label_9 = QLabel(self.frame_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)

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
        icon8 = QIcon()
        icon8.addFile(u":/icons/magnifying-glass-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_filtro_id.setIcon(icon8)
        self.btn_filtro_id.setIconSize(QSize(16, 16))

        self.gridLayout_4.addWidget(self.btn_filtro_id, 1, 1, 1, 1)

        self.text_filtro_id = QLineEdit(self.frame_8)
        self.text_filtro_id.setObjectName(u"text_filtro_id")
        self.text_filtro_id.setMaximumSize(QSize(50, 16777215))
        self.text_filtro_id.setFont(font3)
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
        font9 = QFont()
        font9.setFamily(u"Microsoft Yi Baiti")
        self.frame_10.setFont(font9)
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_10)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 10, 0)
        self.data_fixa = QRadioButton(self.frame_10)
        self.data_fixa.setObjectName(u"data_fixa")
        font10 = QFont()
        font10.setFamily(u"Century Gothic")
        font10.setPointSize(9)
        font10.setBold(False)
        font10.setItalic(False)
        font10.setWeight(50)
        self.data_fixa.setFont(font10)

        self.gridLayout_5.addWidget(self.data_fixa, 0, 0, 1, 1)

        self.data_antes_de = QRadioButton(self.frame_10)
        self.data_antes_de.setObjectName(u"data_antes_de")
        self.data_antes_de.setMinimumSize(QSize(0, 1))
        self.data_antes_de.setFont(font10)

        self.gridLayout_5.addWidget(self.data_antes_de, 1, 0, 1, 1)

        self.text_date = QDateEdit(self.frame_10)
        self.text_date.setObjectName(u"text_date")
        self.text_date.setMinimumSize(QSize(0, 19))
        self.text_date.setStyleSheet(u"QDateEdit{\n"
"	border:1px solid rgb(67, 202, 0);\n"
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
        self.data_depois_de.setFont(font10)

        self.gridLayout_5.addWidget(self.data_depois_de, 2, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_10, 1, 7, 1, 1)

        self.label_10 = QLabel(self.frame_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 13))
        self.label_10.setFont(font3)

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
        font11 = QFont()
        font11.setFamily(u"Century Gothic")
        font11.setPointSize(11)
        font11.setBold(True)
        font11.setWeight(75)
        self.btn_Aplicar_filtro_geral.setFont(font11)
        self.btn_Aplicar_filtro_geral.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Aplicar_filtro_geral.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(250, 250, 250);\n"
"	border:1px solid rgb(67, 202, 0);\n"
"	padding:5px\n"
"}\n"
"QPushButton::hover{\n"
"	color: rgb(67, 202, 0)\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/icons/filter-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Aplicar_filtro_geral.setIcon(icon9)

        self.horizontalLayout_4.addWidget(self.btn_Aplicar_filtro_geral)

        self.btn_inprimir = QPushButton(self.frame_9)
        self.btn_inprimir.setObjectName(u"btn_inprimir")
        self.btn_inprimir.setFont(font11)
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
        icon10 = QIcon()
        icon10.addFile(u":/icons/print-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_inprimir.setIcon(icon10)

        self.horizontalLayout_4.addWidget(self.btn_inprimir)


        self.gridLayout_3.addWidget(self.frame_9, 3, 2, 1, 4)


        self.verticalLayout_13.addWidget(self.frame_7)

        self.tableWidget = QTableWidget(self.frame_6)
        if (self.tableWidget.columnCount() < 11):
            self.tableWidget.setColumnCount(11)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        font12 = QFont()
        font12.setFamily(u"Century Gothic")
        font12.setPointSize(10)
        font12.setBold(True)
        font12.setItalic(False)
        font12.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font12);
        __qtablewidgetitem.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        font13 = QFont()
        font13.setFamily(u"Century Gothic")
        font13.setPointSize(10)
        font13.setBold(True)
        font13.setItalic(False)
        font13.setWeight(75)
        font13.setKerning(False)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font13);
        __qtablewidgetitem1.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        font14 = QFont()
        font14.setFamily(u"Century Gothic")
        font14.setPointSize(10)
        font14.setBold(True)
        font14.setItalic(False)
        font14.setWeight(75)
        font14.setStrikeOut(False)
        font14.setKerning(False)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font14);
        __qtablewidgetitem2.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font12);
        __qtablewidgetitem3.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font12);
        __qtablewidgetitem4.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font12);
        __qtablewidgetitem5.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font12);
        __qtablewidgetitem6.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font12);
        __qtablewidgetitem7.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font12);
        __qtablewidgetitem8.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font12);
        __qtablewidgetitem9.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font12);
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
        font15 = QFont()
        font15.setFamily(u"Century Gothic")
        font15.setPointSize(11)
        font15.setBold(False)
        font15.setItalic(False)
        font15.setWeight(50)
        self.tableWidget.setFont(font15)
        self.tableWidget.setStyleSheet(u"\n"
"QTableWidget{\n"
"	font: 11pt \"Century Gothic\";\n"
"	outline:0;\n"
"}\n"
"QHeaderView::section {\n"
"   	padding: 5px 0px;\n"
"	color:white;\n"
"	border:1px solid white;\n"
"	background-color: rgb(43, 43, 43);\n"
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
"QScrol"
                        "lBar:horizontal {\n"
"    border: 1px solid #999999;\n"
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
        self.tableWidget.setAutoScroll(False)
        self.tableWidget.setAutoScrollMargin(22)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(True)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setDragDropOverwriteMode(True)
        self.tableWidget.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setTextElideMode(Qt.ElideLeft)
        self.tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(11)
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
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
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
        self.verticalLayout_16.setContentsMargins(9, 9, 9, 0)
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(16777215, 40))
        self.frame_12.setStyleSheet(u"border-bottom:1px solid rgb(154, 154, 154)")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_12)
        self.verticalLayout_15.setSpacing(7)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.title = QPushButton(self.frame_12)
        self.title.setObjectName(u"title")
        self.title.setMinimumSize(QSize(160, 29))
        self.title.setMaximumSize(QSize(5555, 40))
        self.title.setBaseSize(QSize(555, 2))
        self.title.setFont(font8)
        self.title.setLayoutDirection(Qt.LeftToRight)
        self.title.setStyleSheet(u"QPushButton{\n"
"	border:0;\n"
"}")
        self.title.setIcon(icon4)
        self.title.setIconSize(QSize(29, 28))
        self.title.setFlat(False)

        self.verticalLayout_15.addWidget(self.title, 0, Qt.AlignTop)


        self.verticalLayout_16.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        font16 = QFont()
        font16.setPointSize(9)
        self.frame_13.setFont(font16)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_13)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(180, 0, 180, -1)
        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 260))
        self.frame_14.setStyleSheet(u"background-color: rgb(43, 43, 43);\n"
"border-radius:20px")
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_14)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_2 = QFrame(self.frame_14)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 35))
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
        font17 = QFont()
        font17.setFamily(u"Century Gothic")
        font17.setPointSize(14)
        font17.setBold(True)
        font17.setWeight(75)
        self.label_3.setFont(font17)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
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
        self.frame_16.setStyleSheet(u"background-color: rgb(235, 235, 235);")
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
        self.label_11.setFont(font6)

        self.gridLayout_6.addWidget(self.label_11, 0, 0, 1, 1, Qt.AlignBottom)

        self.text_empresa_pessoal = QLabel(self.frame_17)
        self.text_empresa_pessoal.setObjectName(u"text_empresa_pessoal")
        self.text_empresa_pessoal.setFont(font3)

        self.gridLayout_6.addWidget(self.text_empresa_pessoal, 1, 0, 1, 1)

        self.btn_alterar_nome = QPushButton(self.frame_17)
        self.btn_alterar_nome.setObjectName(u"btn_alterar_nome")
        self.btn_alterar_nome.setMinimumSize(QSize(100, 0))
        self.btn_alterar_nome.setMaximumSize(QSize(16777215, 100))
        self.btn_alterar_nome.setFont(font6)
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
        self.frame_19.setFrameShape(QFrame.NoFrame)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_19)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(0)
        self.gridLayout_8.setVerticalSpacing(9)
        self.gridLayout_8.setContentsMargins(9, 0, -1, 9)
        self.label_13 = QLabel(self.frame_19)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font6)

        self.gridLayout_8.addWidget(self.label_13, 0, 0, 1, 1)

        self.text_email = QLabel(self.frame_19)
        self.text_email.setObjectName(u"text_email")
        self.text_email.setFont(font3)

        self.gridLayout_8.addWidget(self.text_email, 1, 0, 1, 1, Qt.AlignTop)


        self.verticalLayout_19.addWidget(self.frame_19)

        self.frame_18 = QFrame(self.frame_16)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_18)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(-1, 0, 9, 0)
        self.label_15 = QLabel(self.frame_18)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font6)

        self.gridLayout_7.addWidget(self.label_15, 0, 0, 1, 1, Qt.AlignBottom)

        self.text_telefone = QLabel(self.frame_18)
        self.text_telefone.setObjectName(u"text_telefone")
        self.text_telefone.setFont(font2)

        self.gridLayout_7.addWidget(self.text_telefone, 1, 0, 1, 1)

        self.btn_alterar_telefone = QPushButton(self.frame_18)
        self.btn_alterar_telefone.setObjectName(u"btn_alterar_telefone")
        self.btn_alterar_telefone.setMinimumSize(QSize(100, 0))
        self.btn_alterar_telefone.setMaximumSize(QSize(16777215, 100))
        self.btn_alterar_telefone.setFont(font6)
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
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_20)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.label_17 = QLabel(self.frame_20)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font6)

        self.gridLayout_9.addWidget(self.label_17, 0, 0, 1, 1, Qt.AlignBottom)

        self.btn_atualizar_licenca = QPushButton(self.frame_20)
        self.btn_atualizar_licenca.setObjectName(u"btn_atualizar_licenca")
        self.btn_atualizar_licenca.setMinimumSize(QSize(100, 0))
        self.btn_atualizar_licenca.setMaximumSize(QSize(20000, 16777215))
        self.btn_atualizar_licenca.setFont(font6)
        self.btn_atualizar_licenca.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_atualizar_licenca.setStyleSheet(u"QPushButton{\n"
"	border:1px solid rgb(67, 202, 0);\n"
"	padding:10px;\n"
"	border-radius:10px;\n"
"	background-color: rgb(250, 250, 250);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(145, 255, 133);\n"
"}")

        self.gridLayout_9.addWidget(self.btn_atualizar_licenca, 1, 1, 1, 1, Qt.AlignRight)

        self.text_licenca = QLabel(self.frame_20)
        self.text_licenca.setObjectName(u"text_licenca")
        self.text_licenca.setMinimumSize(QSize(0, 0))
        self.text_licenca.setFont(font3)

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
        self.label_20.setFont(font6)
        self.label_20.setStyleSheet(u"border:0")

        self.verticalLayout_20.addWidget(self.label_20)

        self.label_23 = QLabel(self.frame_15)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font2)
        self.label_23.setStyleSheet(u"border:0")

        self.verticalLayout_20.addWidget(self.label_23)

        self.btn_alterar_senha = QPushButton(self.frame_15)
        self.btn_alterar_senha.setObjectName(u"btn_alterar_senha")
        self.btn_alterar_senha.setMinimumSize(QSize(100, 0))
        self.btn_alterar_senha.setMaximumSize(QSize(100, 32))
        self.btn_alterar_senha.setFont(font6)
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
        self.label_21.setFont(font6)
        self.label_21.setStyleSheet(u"border:0")

        self.verticalLayout_21.addWidget(self.label_21)

        self.label_22 = QLabel(self.frame_21)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font2)
        self.label_22.setStyleSheet(u"border:0")

        self.verticalLayout_21.addWidget(self.label_22)

        self.btn_excluir_conta = QPushButton(self.frame_21)
        self.btn_excluir_conta.setObjectName(u"btn_excluir_conta")
        self.btn_excluir_conta.setMinimumSize(QSize(100, 0))
        self.btn_excluir_conta.setMaximumSize(QSize(100, 32))
        self.btn_excluir_conta.setFont(font6)
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


        self.gridLayout.addWidget(self.principal_frame, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 950, 21))
        self.menuConfiguracoes = QMenu(self.menuBar)
        self.menuConfiguracoes.setObjectName(u"menuConfiguracoes")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuConfiguracoes.menuAction())
        self.menuConfiguracoes.addSeparator()
        self.menuConfiguracoes.addAction(self.adicionar_balanca)
        self.menuConfiguracoes.addAction(self.actionAvan_adas)
        self.menuConfiguracoes.addSeparator()
        self.menuConfiguracoes.addAction(self.fechar_aplicativo)

        self.retranslateUi(MainWindow)

        self.aba_pesagem_button.setDefault(False)
        self.stackedWidget.setCurrentIndex(3)
        self.comboBox_produto.setCurrentIndex(0)
        self.comboBox_cliente.setCurrentIndex(0)
        self.comboBox_fornecedor.setCurrentIndex(0)
        self.comboBox_veiculo.setCurrentIndex(0)


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
        self.restantes_label.setText(QCoreApplication.translate("MainWindow", u"Pesagens restantes: 30", None))
        self.info_pro_label.setText(QCoreApplication.translate("MainWindow", u"Atualize para a vers\u00e3o PRO e aproveite todos os recursos sem limita\u00e7\u00f5es.", None))
        self.aba_sair_button.setText(QCoreApplication.translate("MainWindow", u"Sair        ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Status Balan\u00e7a:", None))
        self.conexao_label.setText(QCoreApplication.translate("MainWindow", u"Sem Conex\u00e3o", None))
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
        self.menuConfiguracoes.setTitle(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es", None))
    # retranslateUi

