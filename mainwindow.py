from atexit import register
import sys
from PySide2.QtWidgets import QMainWindow, QApplication, QWidget, QDialog

from Windows.MainWindow import Ui_MainWindow
from Windows.Login import Ui_Login_Widget
from Windows.Dialog_invalido import Ui_Dialog
from Utils import utils
import resources_rc

class DialogLogin(QDialog, Ui_Dialog):
    def __init__(self):
        super(DialogLogin, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.exit)

    def exit(self):
        self.close()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.info_frame.hide()
        self.menu_grupos_frame.hide()
        self.menu_pesagem_frame.hide()
        self.aba_pesagem_button.clicked.connect(self.menu_pesagem)
        self.aba_grupo_button.clicked.connect(self.menu_grupos)
            
    def menu_grupos(self):
        if self.menu_grupos_frame.isHidden():
            self.menu_grupos_frame.show()
            self.aba_grupo_button.setText('Grupos                    ▲')
        else:
            self.menu_grupos_frame.hide()
            self.aba_grupo_button.setText('Grupos                    ▼')


    def menu_pesagem(self):
        if self.menu_pesagem_frame.isHidden():
            self.menu_pesagem_frame.show()
            self.aba_pesagem_button.setText('Pesagens                 ▲')

        else:
            self.menu_pesagem_frame.hide()
            self.aba_pesagem_button.setText('Pesagens                 ▼')

class LoginWindow(QWidget, Ui_Login_Widget):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self._senha_input.setEchoMode(self._senha_input.Password)
        self.entrar_button.setDisabled(True)
        self.email_input.textChanged.connect(self.disableButton)
        self._senha_input.textChanged.connect(self.disableButton)
        self.mais_servicos_button.clicked.connect(self.more_services)
        self.entrar_button.clicked.connect(self.login)

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
        else:
            self.dialog_login.show()
            self.email_input.setText('')
            self._senha_input.setText('')

    def more_services(self):
        utils.open_link('https://www.caltecbalancas.com.br/servicos.html')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = LoginWindow()
    Window.show()
    app.exec_()

import os

