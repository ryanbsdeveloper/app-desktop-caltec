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
        MainWindow.resize(863, 647)
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
        self.btn_virepro_button.setMinimumSize(QSize(0, 45))
        self.btn_virepro_button.setMaximumSize(QSize(170, 16777215))
        font = QFont()
        font.setFamily(u"Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_virepro_button.setFont(font)
        self.btn_virepro_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_virepro_button.setStyleSheet(u"QPushButton{\n"
"	border:0;\n"
"	border-radius:5px;\n"
"	background-color: rgb(242, 242, 242);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(48, 48, 48);\n"
"	color:white;\n"
"}\n"
"")
        self.btn_virepro_button.setText(u"Utilize a vers\u00e3o PRO")
        icon1 = QIcon()
        icon1.addFile(u":/icons/crown-solid (2).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_virepro_button.setIcon(icon1)
        self.btn_virepro_button.setIconSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.btn_virepro_button, 1, 0, 1, 1)

        self.label_2 = QLabel(self.conteudo_top_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 20))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-bottom: 1px solidrgb(0, 255, 0)")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)

        self.conexao_label = QPushButton(self.conteudo_top_frame)
        self.conexao_label.setObjectName(u"conexao_label")
        self.conexao_label.setEnabled(False)
        self.conexao_label.setMinimumSize(QSize(0, 45))
        self.conexao_label.setMaximumSize(QSize(150, 16777215))
        font1 = QFont()
        font1.setFamily(u"Nirmala UI")
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setWeight(75)
        self.conexao_label.setFont(font1)
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
        icon2 = QIcon()
        icon2.addFile(u":/icons/plug-circle-exclamation-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/icons/plug-circle-exclamation-solid.svg", QSize(), QIcon.Disabled, QIcon.Off)
        icon2.addFile(u":/icons/plug-circle-exclamation-solid.svg", QSize(), QIcon.Disabled, QIcon.On)
        icon2.addFile(u":/icons/plug-solid (1).svg", QSize(), QIcon.Active, QIcon.Off)
        icon2.addFile(u":/icons/plug-solid (1).svg", QSize(), QIcon.Active, QIcon.On)
        self.conexao_label.setIcon(icon2)
        self.conexao_label.setCheckable(False)
        self.conexao_label.setFlat(False)

        self.gridLayout_2.addWidget(self.conexao_label, 1, 1, 1, 1)


        self.horizontalLayout.addWidget(self.conteudo_top_frame, 0, Qt.AlignRight)


        self.gridLayout.addWidget(self.top_frame, 0, 0, 1, 2)

        self.menu_frame = QFrame(self.centralwidget)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setMaximumSize(QSize(200, 999999))
        font2 = QFont()
        font2.setPointSize(11)
        self.menu_frame.setFont(font2)
        self.menu_frame.setStyleSheet(u"background-color: rgb(231, 231, 231);")
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
        font3 = QFont()
        font3.setFamily(u"Century Gothic")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setWeight(50)
        self.aba_pesagem_button.setFont(font3)
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
        icon3 = QIcon()
        iconThemeName = u"lumos"
        if QIcon.hasThemeIcon(iconThemeName):
            icon3 = QIcon.fromTheme(iconThemeName)
        else:
            icon3.addFile(u":/icons/scale-balanced-solid (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        
        self.aba_pesagem_button.setIcon(icon3)
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
        self.menu_pesagem_frame.setFrameShape(QFrame.NoFrame)
        self.menu_pesagem_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.menu_pesagem_frame)
        self.verticalLayout_8.setSpacing(2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.button_simples_pesagens = QPushButton(self.menu_pesagem_frame)
        self.button_simples_pesagens.setObjectName(u"button_simples_pesagens")
        self.button_simples_pesagens.setMinimumSize(QSize(0, 25))
        font4 = QFont()
        font4.setFamily(u"Century Gothic")
        font4.setPointSize(9)
        self.button_simples_pesagens.setFont(font4)
        self.button_simples_pesagens.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(250, 250, 250);\n"
"	border:1px solid\n"
"}")

        self.verticalLayout_8.addWidget(self.button_simples_pesagens)

        self.button_entsaid_pesagens = QPushButton(self.menu_pesagem_frame)
        self.button_entsaid_pesagens.setObjectName(u"button_entsaid_pesagens")
        self.button_entsaid_pesagens.setMinimumSize(QSize(0, 25))
        self.button_entsaid_pesagens.setFont(font4)
        self.button_entsaid_pesagens.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(250, 250, 250);\n"
"	border:1px solid\n"
"}")

        self.verticalLayout_8.addWidget(self.button_entsaid_pesagens)

        self.button_avulsas_pesagens = QPushButton(self.menu_pesagem_frame)
        self.button_avulsas_pesagens.setObjectName(u"button_avulsas_pesagens")
        self.button_avulsas_pesagens.setMinimumSize(QSize(130, 25))
        self.button_avulsas_pesagens.setMaximumSize(QSize(100, 16777215))
        self.button_avulsas_pesagens.setFont(font4)
        self.button_avulsas_pesagens.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(250, 250, 250);\n"
"	border:1px solid\n"
"}")

        self.verticalLayout_8.addWidget(self.button_avulsas_pesagens)


        self.verticalLayout_9.addWidget(self.menu_pesagem_frame, 0, Qt.AlignRight)


        self.verticalLayout_3.addWidget(self.frame_3, 0, Qt.AlignTop)

        self.frame_4 = QFrame(self.menuTop_frame)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy2.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy2)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_4)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.aba_grupo_button = QPushButton(self.frame_4)
        self.aba_grupo_button.setObjectName(u"aba_grupo_button")
        self.aba_grupo_button.setMinimumSize(QSize(160, 40))
        font5 = QFont()
        font5.setFamily(u"Century Gothic")
        font5.setPointSize(10)
        self.aba_grupo_button.setFont(font5)
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
        icon4 = QIcon()
        icon4.addFile(u":/icons/layer-group-solid (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.aba_grupo_button.setIcon(icon4)
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
        self.button_clientes_grupos.setFont(font4)
        self.button_clientes_grupos.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(250, 250, 250);\n"
"	border:1px solid\n"
"}")

        self.verticalLayout_7.addWidget(self.button_clientes_grupos)

        self.button_produtos_grupos = QPushButton(self.menu_grupos_frame)
        self.button_produtos_grupos.setObjectName(u"button_produtos_grupos")
        self.button_produtos_grupos.setMinimumSize(QSize(0, 25))
        self.button_produtos_grupos.setFont(font4)
        self.button_produtos_grupos.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(250, 250, 250);\n"
"	border:1px solid\n"
"}")

        self.verticalLayout_7.addWidget(self.button_produtos_grupos)

        self.button_fornecedores_grupos = QPushButton(self.menu_grupos_frame)
        self.button_fornecedores_grupos.setObjectName(u"button_fornecedores_grupos")
        self.button_fornecedores_grupos.setMinimumSize(QSize(0, 25))
        self.button_fornecedores_grupos.setFont(font4)
        self.button_fornecedores_grupos.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(250, 250, 250);\n"
"	border:1px solid\n"
"}")

        self.verticalLayout_7.addWidget(self.button_fornecedores_grupos)

        self.button_veiculos_grupos = QPushButton(self.menu_grupos_frame)
        self.button_veiculos_grupos.setObjectName(u"button_veiculos_grupos")
        self.button_veiculos_grupos.setMinimumSize(QSize(130, 25))
        self.button_veiculos_grupos.setMaximumSize(QSize(100, 16777215))
        self.button_veiculos_grupos.setFont(font4)
        self.button_veiculos_grupos.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(250, 250, 250);\n"
"	border:1px solid\n"
"}")

        self.verticalLayout_7.addWidget(self.button_veiculos_grupos)


        self.verticalLayout_10.addWidget(self.menu_grupos_frame, 0, Qt.AlignRight)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.aba_relatorio_button = QPushButton(self.menuTop_frame)
        self.aba_relatorio_button.setObjectName(u"aba_relatorio_button")
        self.aba_relatorio_button.setMinimumSize(QSize(160, 40))
        self.aba_relatorio_button.setMaximumSize(QSize(5555, 40))
        self.aba_relatorio_button.setBaseSize(QSize(555, 2))
        self.aba_relatorio_button.setFont(font5)
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
        icon5 = QIcon()
        icon5.addFile(u":/icons/file-lines-solid (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.aba_relatorio_button.setIcon(icon5)
        self.aba_relatorio_button.setIconSize(QSize(20, 20))
        self.aba_relatorio_button.setFlat(False)

        self.verticalLayout_3.addWidget(self.aba_relatorio_button)

        self.aba_conta_button = QPushButton(self.menuTop_frame)
        self.aba_conta_button.setObjectName(u"aba_conta_button")
        self.aba_conta_button.setMinimumSize(QSize(160, 40))
        self.aba_conta_button.setFont(font5)
        self.aba_conta_button.setStyleSheet(u"QPushButton{\n"
"	border:0;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(250, 250, 250);\n"
"	border:1px solid\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/person-walking-solid (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.aba_conta_button.setIcon(icon6)
        self.aba_conta_button.setIconSize(QSize(20, 20))
        self.aba_conta_button.setAutoExclusive(True)
        self.aba_conta_button.setFlat(False)

        self.verticalLayout_3.addWidget(self.aba_conta_button)


        self.verticalLayout_2.addWidget(self.menuTop_frame, 0, Qt.AlignVCenter)

        self.info_menu_pro_frame = QFrame(self.menu_frame)
        self.info_menu_pro_frame.setObjectName(u"info_menu_pro_frame")
        self.info_menu_pro_frame.setMaximumSize(QSize(16777215, 115))
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
        font6 = QFont()
        font6.setFamily(u"Century Gothic")
        font6.setBold(True)
        font6.setWeight(75)
        self.restantes_label.setFont(font6)
        self.restantes_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.restantes_label)


        self.verticalLayout_5.addWidget(self.info_pro_frame)

        self.info_pro_label = QLabel(self.info_menu_pro_frame)
        self.info_pro_label.setObjectName(u"info_pro_label")
        font7 = QFont()
        font7.setFamily(u"Century Gothic")
        font7.setPointSize(11)
        self.info_pro_label.setFont(font7)
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
        self.aba_sair_button.setFont(font5)
        self.aba_sair_button.setStyleSheet(u"QPushButton{\n"
"	border:0;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(250, 250, 250);\n"
"	border:1px solid\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/person-walking-arrow-right-solid (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.aba_sair_button.setIcon(icon7)
        self.aba_sair_button.setIconSize(QSize(25, 25))
        self.aba_sair_button.setFlat(False)

        self.verticalLayout_4.addWidget(self.aba_sair_button, 0, Qt.AlignBottom)


        self.verticalLayout_2.addWidget(self.menuEnd_frame, 0, Qt.AlignBottom)

        self.menuEnd_frame.raise_()
        self.menuTop_frame.raise_()
        self.info_menu_pro_frame.raise_()

        self.gridLayout.addWidget(self.menu_frame, 1, 0, 1, 1)

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
        self.info_frame.setFrameShape(QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.info_frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.info_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 60))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(1000000, 60))
        font8 = QFont()
        font8.setFamily(u"Century Gothic")
        font8.setPointSize(10)
        font8.setBold(False)
        font8.setUnderline(False)
        font8.setWeight(50)
        self.pushButton.setFont(font8)
        self.pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border:0;\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/icons/circle-info-solidg.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon8)

        self.horizontalLayout_5.addWidget(self.pushButton, 0, Qt.AlignHCenter)


        self.verticalLayout_6.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.info_frame)

        self.conteudo_frame = QFrame(self.principal_frame)
        self.conteudo_frame.setObjectName(u"conteudo_frame")
        self.conteudo_frame.setEnabled(True)
        self.conteudo_frame.setMinimumSize(QSize(0, 20))
        font9 = QFont()
        font9.setBold(True)
        font9.setWeight(75)
        self.conteudo_frame.setFont(font9)
        self.conteudo_frame.setStyleSheet(u"background-color: rgb(231, 231, 231);\n"
"border: 1px solid rgb(181, 181, 181)")
        self.conteudo_frame.setFrameShape(QFrame.NoFrame)
        self.conteudo_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.conteudo_frame)


        self.gridLayout.addWidget(self.principal_frame, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 863, 21))
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


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Caltec - Software de pesagem", None))
        self.adicionar_balanca.setText(QCoreApplication.translate("MainWindow", u"Conectar balan\u00e7a", None))
        self.fechar_aplicativo.setText(QCoreApplication.translate("MainWindow", u"Fechar aplicativo", None))
        self.actionAvan_adas.setText(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es Avan\u00e7adas", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Status Balan\u00e7a:", None))
        self.conexao_label.setText(QCoreApplication.translate("MainWindow", u"Sem Conex\u00e3o", None))
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
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Nova atualiza\u00e7\u00e3o disponivel clique aqui", None))
        self.menuConfiguracoes.setTitle(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es", None))
    # retranslateUi

