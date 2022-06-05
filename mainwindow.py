import os
from atexit import register
import sys
from time import sleep
from turtle import width
from PySide2.QtWidgets import QMainWindow, QApplication, QWidget, QDialog
from PySide2.QtCore import QPropertyAnimation, Qt
from PySide2.QtGui import QRegion

from Windows.MainWindow import Ui_MainWindow
from Windows.Premium import Ui_Dialog
from Windows.Login import Ui_Login_Widget
from Windows.Dialog_invalido import Ui_AcessoNegado
from Windows.DialogAtualizarNome import Ui_AtualizarNome
from Windows.DialogAtualizarSenha import Ui_AtualizarSenha
from Windows.DialogAtualizarTelefone import Ui_AtualizarTelefone
from Windows.DialogExcluirConta import Ui_ExcluirConta
from Windows.DialogSairConta import Ui_SairConta
from Utils import utils
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


class DialogAtualizarSenha(QDialog, Ui_AtualizarSenha):
    def __init__(self):
        super(DialogAtualizarSenha, self).__init__()
        self.setupUi(self)
        self.text_info.hide()
        self.btn_cancelar.clicked.connect(lambda: self.close())




class DialogAtualizarTelefone(QDialog, Ui_AtualizarTelefone):
    def __init__(self):
        super(DialogAtualizarTelefone, self).__init__()
        self.setupUi(self)
        self.text_info.hide()
        self.bt_cancelar.clicked.connect(lambda: self.close())




class DialogExcluirConta(QDialog, Ui_ExcluirConta):
    def __init__(self):
        super(DialogExcluirConta, self).__init__()
        self.setupUi(self)
        self.text_info.hide()
        self.nao.clicked.connect(lambda: self.close())


class DialogSairConta(QDialog, Ui_SairConta):
    def __init__(self):
        super(DialogSairConta, self).__init__()
        self.setupUi(self)
        self.nao.clicked.connect(lambda: self.close())

        

#######################################################################


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # MENU TOP
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.btn_close_windows.clicked.connect(lambda: self.close())
        self.btn_minimize_window.clicked.connect(lambda: self.showMinimized())

        # MENUS
        self.menu_grupos_frame.setMaximumHeight(0)
        self.menu_pesagem_frame.setMaximumHeight(0)
        self.aba_pesagem_button.clicked.connect(self.menu_pesagem)
        self.aba_grupo_button.clicked.connect(self.menu_grupos)
        self.btn_menu_registrar_clientes.clicked.connect(self.animation_menu_clientes)
        self.btn_menu_registrar_forne.clicked.connect(self.animation_menu_forne)
        self.btn_menu_registrar_produtos.clicked.connect(self.animation_menu_produtos)
        self.btn_menu_registrar_veiculos.clicked.connect(self.animation_menu_veiculos)

        # DIALOGS
        self.dialog_sair_conta = DialogSairConta()
        self.dialog_excluir_conta = DialogExcluirConta()
        self.dialog_atualizar_nome = DialogAtualizarNome()
        self.dialog_atualizar_senha = DialogAtualizarSenha()
        self.dialog_atualizar_telefone = DialogAtualizarTelefone()
        self.premium = PremiumWindow()
        self.btn_virepro_button.clicked.connect(lambda: self.premium.showMaximized())


        # PAGES
        self.aba_conta_button.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_conta))
        self.aba_relatorio_button.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_relatorio))
        self.button_clientes_grupos.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_clientes))
        self.button_produtos_grupos.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_produtos))
        self.button_fornecedores_grupos.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_fornecedores))
        self.button_veiculos_grupos.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_veiculos))


        # BUTTONS CONTA
        self.aba_sair_button.clicked.connect(self.show_sair_conta)   
        self.btn_excluir_conta.clicked.connect(self.show_excluir_conta)
        self.btn_alterar_nome.clicked.connect(self.show_atualizar_nome) 
        self.btn_alterar_senha.clicked.connect(self.show_atualizar_senha) 
        self.btn_alterar_telefone.clicked.connect(self.show_atualizar_telefone) 
        self.btn_atualizar_licenca.clicked.connect(lambda: self.premium.showMaximized())

    def menu_grupos(self):
        self.animation_grupo()
        if self.menu_grupos_frame.isHidden():
            self.aba_grupo_button.setText('Grupos                    ▲')
        else:
            self.aba_grupo_button.setText('Grupos                    ▼')

    def menu_pesagem(self):
        self.animation_pesagem()
        if self.menu_pesagem_frame.isHidden():
            self.aba_pesagem_button.setText('Pesagens                 ▲')
        else:
            self.aba_pesagem_button.setText('Pesagens                 ▼')

    ## SHOW DIALOGS
    def show_sair_conta(self):
        self.dialog_sair_conta.show()
    
    def show_excluir_conta(self):
        self.dialog_excluir_conta.show()
    
    def show_atualizar_nome(self):
        self.dialog_atualizar_nome.show()
    
    def show_atualizar_senha(self):
        self.dialog_atualizar_senha.show()
        
    def show_atualizar_telefone(self):
        self.dialog_atualizar_telefone.show()

    ## ANIMATIONS FUNCTIONS
    def animation_pesagem(self):
        height = self.menu_pesagem_frame.maximumHeight()

        if height == 0:
            height_extend = 79
        else:
            height_extend = 0

        self.animation = QPropertyAnimation(self.menu_pesagem_frame, b'maximumHeight')
        self.animation.setDuration(150)
        self.animation.setStartValue(height)
        self.animation.setEndValue(height_extend)
        self.animation.start()

    def animation_grupo(self):
        height = self.menu_grupos_frame.maximumHeight()

        if height == 0:
            height_extend = 106
        else:
            height_extend = 0

        self.animation = QPropertyAnimation(self.menu_grupos_frame, b'maximumHeight')
        self.animation.setDuration(150)
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
        self.animation.setDuration(150)
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
        self.animation.setDuration(150)
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
        self.animation.setDuration(150)
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
        self.animation.setDuration(150)
        self.animation.setStartValue(width)
        self.animation.setEndValue(width_extend)
        self.animation.start() 


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
        db = utils.DB()
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = LoginWindow()
    Window.show()
    app.exec_()
