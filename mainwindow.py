import os
from atexit import register
from sre_parse import expand_template
import sys
from time import sleep
from turtle import width
from PySide2.QtWidgets import QMainWindow, QApplication, QWidget, QDialog
from PySide2.QtCore import QPropertyAnimation, Qt, QParallelAnimationGroup, QAbstractAnimation, QSize
from PySide2.QtGui import QRegion, QIcon, QFont

from Windows.MainWindow import Ui_MainWindow
from Windows.Premium import Ui_Dialog
from Windows.Login import Ui_Login_Widget
from Windows.Dialog_invalido import Ui_AcessoNegado
from Windows.DialogAtualizarNome import Ui_AtualizarNome
from Windows.DialogAtualizarSenha import Ui_AtualizarSenha
from Windows.DialogAtualizarTelefone import Ui_AtualizarTelefone
from Windows.DialogExcluirConta import Ui_ExcluirConta
from Windows.DialogSairConta import Ui_SairConta
from utils import utils
from models import database
import resources_rc

# DIALOGs

class DialogLogin(QDialog, Ui_AcessoNegado):
    def __init__(self):
        super(DialogLogin, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.exit)

    def exit(self):
        self.close()


class DialogAtualizarNome(QDialog, Ui_AtualizarNome):
    def __init__(self):
        super(DialogAtualizarNome, self).__init__()
        self.setupUi(self)
        self.text_info.hide()
        self.bt_cancelar.clicked.connect(lambda: self.close())
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)


class DialogAtualizarSenha(QDialog, Ui_AtualizarSenha):
    def __init__(self):
        super(DialogAtualizarSenha, self).__init__()
        self.setupUi(self)
        self.text_info.hide()
        self.btn_cancelar.clicked.connect(lambda: self.close())
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)


class DialogAtualizarTelefone(QDialog, Ui_AtualizarTelefone):
    def __init__(self):
        super(DialogAtualizarTelefone, self).__init__()
        self.setupUi(self)
        self.text_info.hide()
        self.bt_cancelar.clicked.connect(lambda: self.close())
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)


class DialogExcluirConta(QDialog, Ui_ExcluirConta):
    def __init__(self):
        super(DialogExcluirConta, self).__init__()
        self.setupUi(self)
        self.text_info.hide()
        self.nao.clicked.connect(lambda: self.close())
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)


class DialogSairConta(QDialog, Ui_SairConta):
    def __init__(self):
        super(DialogSairConta, self).__init__()
        self.setupUi(self)
        self.nao.clicked.connect(lambda: self.close())
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)


#######################################################################


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        
        # HIDE
        self.digite_um_id.hide()
        self.digite_um_id_2.hide()

        # MENU TOP
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.btn_close_windows.clicked.connect(lambda: self.close())
        self.btn_minimize_window.clicked.connect(lambda: self.showMinimized())

        # MENUS
        self.menu_grupos_frame.setMaximumHeight(0)
        self.menu_relatorio_frame.setMaximumHeight(0)
        self.aba_pesagem_button.clicked.connect(self.menu_pesagem)
        self.aba_grupo_button.clicked.connect(self.menu_grupos)
        self.aba_relatorio_button.clicked.connect(self.menu_relatorio)

        self.btn_menu_registrar_clientes.clicked.connect(
            self.animation_menu_clientes)
        self.btn_menu_registrar_produtos.clicked.connect(
            self.animation_menu_produtos)
        self.btn_menu_registrar_veiculos.clicked.connect(
            self.animation_menu_veiculos)

        # DIALOGS
        self.dialog_sair_conta = DialogSairConta()
        self.dialog_excluir_conta = DialogExcluirConta()
        self.dialog_atualizar_nome = DialogAtualizarNome()
        self.dialog_atualizar_senha = DialogAtualizarSenha()
        self.dialog_atualizar_telefone = DialogAtualizarTelefone()
        self.premium = PremiumWindow()
        self.btn_virepro_button.clicked.connect(
            lambda: self.premium.showMaximized())

        # PAGES
        self.aba_conta_button.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_conta))
        self.button_clientes_grupos.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_clientes))
        self.button_produtos_grupos.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_produtos))
        self.button_veiculos_grupos.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_veiculos))
        self.button_avulsas_pesagens.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_avulsas))
        self.button_entsaid_pesagens.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_entrada))
        self.button_entsaid_relatorio.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_relatorio_entradaesaida))
        self.button_avulsas_relatorio.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_relatorio_avulsas))
        self.btn_alterar_saida.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_saida))
        self.btn_alterar_entrada.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_entrada))

        # BUTTONS CONTA
        self.aba_sair_button.clicked.connect(self.show_sair_conta)
        self.btn_excluir_conta.clicked.connect(self.show_excluir_conta)
        self.btn_alterar_nome.clicked.connect(self.show_atualizar_nome)
        self.btn_alterar_senha.clicked.connect(self.show_atualizar_senha)
        self.btn_alterar_telefone.clicked.connect(self.show_atualizar_telefone)
        self.btn_atualizar_licenca.clicked.connect(
            lambda: self.premium.showMaximized())

        # BUTTONS AVULSAS
        self.btn_peso_manualmente_2.toggled.connect(self.func_peso_manualmente)
        self.btn_historico_obs.clicked.connect(self.animation_obs_avulsas)
        self.btn_historico_obs_2.clicked.connect(self.animation_obs_avulsas_2)

        # FUCTIONS BUTTONS
        self.peso_manualmente_2.textChanged.connect(self.peso_manual)

    def menu_grupos(self):
        self.animation_grupo()
        if self.menu_grupos_frame.width() == 0:
            self.aba_grupo_button.setText('Grupos                    ▲')
        else:
            self.aba_grupo_button.setText('Grupos                    ▼')

    def menu_pesagem(self):
        self.animation_pesagem()
        if self.menu_pesagem_frame.width() == 0:
            self.aba_pesagem_button.setText('Pesagens                 ▲')
        else:
            self.aba_pesagem_button.setText('Pesagens                 ▼')

    def menu_relatorio(self):
        self.animatio_relatorio()
        if self.menu_relatorio_frame.width() == 0:
            self.aba_relatorio_button.setText('Relatórios                 ▲')
        else:
            self.aba_relatorio_button.setText('Relatórios                 ▼')

    # SHOW DIALOGS
    def show_sair_conta(self):
        self.dialog_sair_conta.showMaximized()

    def show_excluir_conta(self):
        self.dialog_excluir_conta.showMaximized()

    def show_atualizar_nome(self):
        self.dialog_atualizar_nome.showMaximized()

    def show_atualizar_senha(self):
        self.dialog_atualizar_senha.showMaximized()

    def show_atualizar_telefone(self):
        self.dialog_atualizar_telefone.showMaximized()

    # ANIMATIONS FUNCTIONS
    def animation_pesagem(self):
        height = self.menu_pesagem_frame.maximumHeight()

        if height == 0:
            height_extend = 79
        else:
            height_extend = 0

        self.animation = QPropertyAnimation(
            self.menu_pesagem_frame, b'maximumHeight')
        self.animation.setDuration(300)
        self.animation.setStartValue(height)
        self.animation.setEndValue(height_extend)
        self.animation.start()

    def animation_grupo(self):
        height = self.menu_grupos_frame.maximumHeight()

        if height == 0:
            height_extend = 106
        else:
            height_extend = 0

        self.animation = QPropertyAnimation(
            self.menu_grupos_frame, b'maximumHeight')
        self.animation.setDuration(300)
        self.animation.setStartValue(height)
        self.animation.setEndValue(height_extend)
        self.animation.start()

    def animatio_relatorio(self):
        height = self.menu_relatorio_frame.maximumHeight()

        if height == 0:
            height_extend = 106
        else:
            height_extend = 0

        self.animation = QPropertyAnimation(
            self.menu_relatorio_frame, b'maximumHeight')
        self.animation.setDuration(300)
        self.animation.setStartValue(height)
        self.animation.setEndValue(height_extend)
        self.animation.start()

    def animation_menu_clientes(self):
        width = self.frame_43.maximumWidth()

        if width == 0:
            width_extend = 300
        else:
            width_extend = 0

        self.animation = QPropertyAnimation(self.frame_43, b'maximumWidth')
        self.animation.setDuration(300)
        self.animation.setStartValue(width)
        self.animation.setEndValue(width_extend)
        self.animation.start()

    def animation_menu_produtos(self):
        width = self.frame_105.maximumWidth()

        if width == 0:
            width_extend = 300
        else:
            width_extend = 0

        self.animation = QPropertyAnimation(self.frame_105, b'maximumWidth')
        self.animation.setDuration(300)
        self.animation.setStartValue(width)
        self.animation.setEndValue(width_extend)
        self.animation.start()

    def animation_menu_forne(self):
        width = self.frame_57.maximumWidth()

        if width == 0:
            width_extend = 300
        else:
            width_extend = 0

        self.animation = QPropertyAnimation(self.frame_57, b'maximumWidth')
        self.animation.setDuration(300)
        self.animation.setStartValue(width)
        self.animation.setEndValue(width_extend)
        self.animation.start()

    def animation_menu_veiculos(self):
        width = self.frame_68.maximumWidth()

        if width == 0:
            width_extend = 300
        else:
            width_extend = 0

        self.animation = QPropertyAnimation(self.frame_68, b'maximumWidth')
        self.animation.setDuration(300)
        self.animation.setStartValue(width)
        self.animation.setEndValue(width_extend)
        self.animation.start()

    def func_peso_manualmente(self):
        width = self.peso_manualmente_2.width()

        if width == 135:
            self.peso_manualmente_2.setText('')
            self.lcdNumber_2.display(0)
            expand = 0
        else:
            expand = 150

        self.animation = QPropertyAnimation(
            self.peso_manualmente_2, b'maximumWidth')
        self.animation.setDuration(300)
        self.animation.setStartValue(width)
        self.animation.setEndValue(expand)
        self.animation.start()

    def animation_obs_avulsas(self):
        height_frame_dados = self.frame_dados_avulsa.height()
        height_frame_obs = self.frame_pendentes.height()

        if height_frame_dados > 210:
            expand_dados = 0
            expand_obs = 220
            icon18 = QIcon()
            icon18.addFile(u":/icons/sort-down-solid.svg",
                           QSize(), QIcon.Normal, QIcon.Off)
            self.btn_historico_obs.setIcon(icon18)
            self.btn_historico_obs.setIconSize(QSize(23, 23))
            self.btn_historico_obs.setAutoRepeatDelay(1)
            self.btn_historico_obs.setAutoDefault(False)
            self.btn_historico_obs.setFlat(False)
        else:
            expand_dados = 220
            expand_obs = 0
            icon18 = QIcon()
            icon18.addFile(u":/icons/sort-up-solid.svg",
                           QSize(), QIcon.Normal, QIcon.Off)
            self.btn_historico_obs.setIcon(icon18)
            self.btn_historico_obs.setIconSize(QSize(23, 23))
            self.btn_historico_obs.setAutoRepeatDelay(1)
            self.btn_historico_obs.setAutoDefault(False)
            self.btn_historico_obs.setFlat(False)

        animation_dados = QPropertyAnimation(
            self.frame_dados_avulsa, b'maximumHeight')
        animation_dados.setDuration(300)
        animation_dados.setStartValue(height_frame_dados)
        animation_dados.setEndValue(expand_dados)

        animation_obs = QPropertyAnimation(
            self.frame_pendentes, b'maximumHeight')
        animation_obs.setDuration(300)
        animation_obs.setStartValue(height_frame_obs)
        animation_obs.setEndValue(expand_obs)

        group = QParallelAnimationGroup(self.frame_dados_avulsa)
        group.addAnimation(animation_dados)
        group.addAnimation(animation_obs)
        group.start(QAbstractAnimation.DeleteWhenStopped)

    def animation_obs_avulsas_2(self):
        height_frame_dados = self.frame_dados_avulsa_2.height()
        height_frame_obs = self.frame_obs.height()

        if height_frame_dados > 210:
            expand_dados = 0
            expand_obs = 265
            icon18 = QIcon()
            icon18.addFile(u":/icons/sort-down-solid.svg",
                           QSize(), QIcon.Normal, QIcon.Off)
            self.btn_historico_obs_2.setIcon(icon18)
            self.btn_historico_obs_2.setIconSize(QSize(23, 23))
            self.btn_historico_obs_2.setFlat(False)
        else:
            expand_dados = 250
            expand_obs = 0
            icon18 = QIcon()
            icon18.addFile(u":/icons/sort-up-solid.svg",
                           QSize(), QIcon.Normal, QIcon.Off)
            self.btn_historico_obs_2.setIcon(icon18)
            self.btn_historico_obs_2.setIconSize(QSize(23, 23))
            self.btn_historico_obs_2.setFlat(False)

        animation_dados = QPropertyAnimation(
            self.frame_dados_avulsa_2, b'maximumHeight')
        animation_dados.setDuration(300)
        animation_dados.setStartValue(height_frame_dados)
        animation_dados.setEndValue(expand_dados)

        animation_obs = QPropertyAnimation(self.frame_obs, b'maximumHeight')
        animation_obs.setDuration(300)
        animation_obs.setStartValue(height_frame_obs)
        animation_obs.setEndValue(expand_obs)

        group = QParallelAnimationGroup(self.frame_dados_avulsa_2)
        group.addAnimation(animation_dados)
        group.addAnimation(animation_obs)
        group.start(QAbstractAnimation.DeleteWhenStopped)

    # FUNCTIONS
    def peso_manual(self):
        text = self.peso_manualmente_2.text()
        self.lcdNumber_2.display(text)


class LoginWindow(QWidget, Ui_Login_Widget, QRegion):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)

        self._senha_input.setEchoMode(self._senha_input.Password)
        self.entrar_button.setDisabled(True)
        self.email_input.textChanged.connect(self.disableButton)
        self._senha_input.textChanged.connect(self.disableButton)
        self.mais_servicos_button.clicked.connect(self.more_services)
        self.entrar_button.clicked.connect(self.login)

        self.premium = PremiumWindow()
        self.main_window = MainWindow()
        self.dialog_login = DialogLogin()

    def disableButton(self):
        if len(self.email_input.text()) > 0 and len(self._senha_input.text()) > 0:
            self.entrar_button.setDisabled(False)
        else:
            self.entrar_button.setDisabled(True)

    def login(self):
        db = database.DB()
        email = self.email_input.text()
        senha = self._senha_input.text()
        register = db.user_log(email, senha)
        if register:
            self.close()
            self.main_window.showMaximized()
            sleep(1)
            self.premium.showMaximized()
        else:
            self.dialog_login.show()
            self.email_input.setText('')
            self._senha_input.setText('')

    def more_services(self):
        utils.open_link('https://www.caltecbalancas.com.br/servicos.html')


class PremiumWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super(PremiumWindow, self).__init__()
        self.setupUi(self)
        self.btn_voltar.clicked.connect(self.voltar)
        self.btn_comprar.clicked.connect(self.comprar)
        self.btn_pular.clicked.connect(lambda: self.close())
        self.pushButton_2.clicked.connect(self.comprar)
        self.btn_licenca.clicked.connect(self.licenca)
        self.btn_close_window.clicked.connect(lambda: self.close())
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.radioButton_anual.toggled.connect(self.anual)
        self.radioButton_6m.toggled.connect(self.sixmeses)

    def licenca(self):
        self.animation = QPropertyAnimation(self.page, b'maximumHeight')
        self.animation.setDuration(100)
        self.animation.setStartValue(398)
        self.animation.setEndValue(265)
        self.animation.start()
        self.stackedWidget.setCurrentWidget(self.page)

    def comprar(self):
        self.stackedWidget.setCurrentWidget(self.page_plano)

    def voltar(self):
        self.stackedWidget.setCurrentWidget(self.page_inicial)

    def anual(self):
        """bold"""
        font = QFont()
        font.setFamily(u"Dubai")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        """end"""

        """light"""
        fontl = QFont()
        fontl.setFamily(u"Dubai")
        fontl.setPointSize(14)
        fontl.setBold(False)
        fontl.setWeight(50)
        """end"""

        self.radioButton_anual.setFont(font)
        self.label_10.setFont(font)

        self.radioButton_6m.setFont(fontl)
        self.label_13.setFont(fontl)

        self.text_valor_total.setText('R$ 119,99')

    def sixmeses(self):
        """bold"""
        font = QFont()
        font.setFamily(u"Dubai")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        """end"""

        """light"""
        fontl = QFont()
        fontl.setFamily(u"Dubai")
        fontl.setPointSize(14)
        fontl.setBold(False)
        fontl.setWeight(50)
        """end"""

        self.radioButton_6m.setFont(font)
        self.label_13.setFont(font)

        self.radioButton_anual.setFont(fontl)
        self.label_10.setFont(fontl)

        self.text_valor_total.setText('R$ 79,99')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = LoginWindow()
    Window.show()
    app.exec_()
 