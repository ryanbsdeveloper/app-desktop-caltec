from datetime import datetime
import sys
import resources_rc
from time import sleep
from PySide2.QtWidgets import QMainWindow, QApplication, QWidget, QDialog, QTableWidgetItem
from PySide2.QtCore import QPropertyAnimation, Qt, QSize, QTime, QTimer, QDate
from PySide2.QtGui import QRegion, QIcon, QFont, QPixmap, QCursor
from Windows.MainWindow import Ui_MainWindow
from Windows.Premium import Ui_Dialog
from Windows.Login import Ui_Login_Widget
from Windows.Dialog_invalido import Ui_AcessoNegado
from Windows.DialogAtualizarNome import Ui_AtualizarNome
from Windows.DialogAtualizarSenha import Ui_AtualizarSenha
from Windows.DialogAtualizarTelefone import Ui_AtualizarTelefone
from Windows.DialogExcluirConta import Ui_ExcluirConta
from Windows.DialogSairConta import Ui_SairConta
from Windows.DialogRemoverDados import Ui_RemoverDados
from utils import utils
from models import database, models

# DIALOGs

class DialogAtualizarNome(QDialog, Ui_AtualizarNome):
    def __init__(self, parent):
        super(DialogAtualizarNome, self).__init__(parent)
        self.setupUi(self)
        self.text_info.hide()
        self.bt_cancelar.clicked.connect(lambda: self.close())
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.pushButton.clicked.connect(lambda: self.close())
        self.btn_alterar.clicked.connect(self.att_nome)

    def att_nome(self):
        nome = self.input_novo_nome.text()
        if len(nome) > 6:
            models.att_user_nome(nome)
            self.close()
        else:
            self.text_info.show()


class DialogAtualizarSenha(QDialog, Ui_AtualizarSenha):
    def __init__(self, parent):
        super(DialogAtualizarSenha, self).__init__(parent)
        self.setupUi(self)
        self.text_info.hide()
        self.btn_cancelar.clicked.connect(lambda: self.close())
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.pushButton.clicked.connect(lambda: self.close())
        self.btn_alterar.clicked.connect(self.att_senha)

    def att_senha(self):
        senha_atual = self.input_senha_atual.text()
        senha_1 = self.input_senha_nova_1.text()
        senha_2 = self.input_senha_nova_2.text()
        saida = models.att_user_senha(senha_atual, senha_1, senha_2)

        if saida == True:
            self.close()
        elif saida == None:
            self.text_info.show()
            self.text_info.setText('Senhas não coincidem')
        else:
            self.text_info.show()
            self.text_info.setText('Senha atual inválida')


class DialogAtualizarTelefone(QDialog, Ui_AtualizarTelefone):
    def __init__(self, parent):
        super(DialogAtualizarTelefone, self).__init__(parent)
        self.setupUi(self)
        self.text_info.hide()
        self.bt_cancelar.clicked.connect(lambda: self.close())
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.pushButton.clicked.connect(lambda: self.close())
        self.pushButton.clicked.connect(self.att_telefone)

    def att_telefone(self):
        telefone = self.input_novo_telefone.text()
        telefone = telefone.replace(' ', '').replace(
            '-', '').replace('+55', '').replace('+', '')
        if len(telefone) < 11:
            self.text_info.show()
            self.text_info.setText('Telefone inválido')
        else:
            models.att_user_telefone(telefone)
            self.close()


class DialogExcluirConta(QDialog, Ui_ExcluirConta):
    def __init__(self, parent):
        super(DialogExcluirConta, self).__init__(parent)
        self.setupUi(self)
        self.text_info.hide()
        self.nao.clicked.connect(lambda: self.close())
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.pushButton.clicked.connect(lambda: self.close())


class DialogSairConta(QDialog, Ui_SairConta):
    def __init__(self, parent):
        super(DialogSairConta, self).__init__(parent)
        self.setupUi(self)
        self.nao.clicked.connect(lambda: self.close())
        self.sim.clicked.connect(self.sair)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.pushButton.clicked.connect(lambda: self.close())

    def sair(self):
        Login = LoginWindow()
        self.parent().close()
        self.close()
        Login.show()


class DialogRemoverDadosAvulsas(QDialog, Ui_RemoverDados):
    def __init__(self, parent):
        super(DialogRemoverDadosAvulsas, self).__init__(parent)
        self.setupUi(self)
        self.btn_remove.setDisabled(True)
        self.close_window.clicked.connect(lambda: self.close())
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.input_delete.textChanged.connect(self.disableButton)
        self.btn_remove.clicked.connect(self.delete)

    def delete(self):
        for i in range(self.parent().tableWidget_4.rowCount()):
            if self.parent().tableWidget_4.item(i, 0).checkState() == Qt.CheckState.Checked:
                indentificacao_data = self.parent().tableWidget_4.item(i, 5).text()
                self.parent().tableWidget_4.removeRow(i)
                models.del_pesagem_avulsa(indentificacao_data)
                self.close()
                self.input_delete.setText('')

        self.close()
        self.input_delete.setText('')



    
    def disableButton(self):
        if self.input_delete.text() == 'DELETE':
            self.btn_remove.setDisabled(False)
            self.btn_remove.setCursor(QCursor(Qt.PointingHandCursor))

        else:
            self.btn_remove.setCursor(QCursor(Qt.ForbiddenCursor))
            self.btn_remove.setDisabled(True)


#######################################################################


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.ss15 = 30

        # INITIAL
        self.user()
        self.cargas()
        self.clientes()
        self.veiculos()
        self.cargas_comboBox()
        self.clientes_comboBox()
        self.veiculos_comboBox()
        self.relatorio_avulsa()

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        self.timer2 = QTimer(self)
        self.timer2.timeout.connect(self.hide_segundos)

        self.nome_pc.setText(f'{utils.name_locauser()} - Software de pesagem')

        # TOOLTIP
        self.btn_finalizar_pesagem.setToolTip(
            'Conecte-se a uma balança para realizar a pesagem')
        self.btn_salvar_entrada.setToolTip(
            'Conecte-se a uma balança para realizar a pesagem')

        # HIDE
        self.digite_um_id.hide()
        self.digite_um_id_2.hide()
        self.frame_saida.hide()
        self.detalhes_saida()

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
        self.dialog_sair_conta = DialogSairConta(self)
        self.dialog_excluir_conta = DialogExcluirConta(self)
        self.dialog_atualizar_nome = DialogAtualizarNome(self)
        self.dialog_atualizar_senha = DialogAtualizarSenha(self)
        self.dialog_atualizar_telefone = DialogAtualizarTelefone(self)
        self.dialog_remover_dados = DialogRemoverDadosAvulsas(self)
        self.premium = PremiumWindow(self)
        self.btn_virepro_button.clicked.connect(
            lambda: self.premium.showFullScreen())

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

        # BUTTONS CONTA
        self.aba_sair_button.clicked.connect(self.show_sair_conta)
        self.btn_excluir_conta.clicked.connect(self.show_excluir_conta)
        self.btn_alterar_nome.clicked.connect(self.show_atualizar_nome)
        self.btn_alterar_senha.clicked.connect(self.show_atualizar_senha)
        self.btn_alterar_telefone.clicked.connect(self.show_atualizar_telefone)
        self.remove_pesagem_avulsas.clicked.connect(self.show_remover_dados_avulsas)
        self.btn_atualizar_licenca.clicked.connect(
            lambda: self.premium.showFullScreen())

        # BUTTONS AVULSAS
        self.btn_peso_manualmente_2.toggled.connect(self.func_peso_manualmente)

        # FUCTIONS BUTTONS
        self.peso_manualmente_2.textChanged.connect(self.peso_manual)
        self.btn_registrar_produtos.clicked.connect(self.get_dados_carga)
        self.btn_registrar_clientes.clicked.connect(self.get_dados_cliente)
        self.btn_registrar_veiculos.clicked.connect(self.get_dados_veiculos)
        self.btn_fazer_pesagem_avulsa.clicked.connect(self.get_pesagem_avulsas)
        self.btn_salvar_entrada.clicked.connect(self.limit)
        self.btn_finalizar_pesagem.clicked.connect(self.limit)
        self.comboBox_pesagem_entrada.currentTextChanged.connect(
            self.detalhes_saida)

    # DISABLE BUTTONS
    def disable_button_avulsa(self):
        pesagens = models.list_pesagens_avulsa()

        if pesagens:
            self.remove_pesagem_avulsas.setCursor(QCursor(Qt.PointingHandCursor))
            self.remove_pesagem_avulsas.setDisabled(False)
        else:
            self.remove_pesagem_avulsas.setCursor(QCursor(Qt.ForbiddenCursor))
            self.remove_pesagem_avulsas.setDisabled(True)

    # TIMES
    def hide_segundos(self):
        self.timer2.start(1000)
        self.segundos.setText(f'{self.ss15} Segundos')

        if self.ss15 == 0:
            self.timer2.stop()
            self.frame_saida.hide()
            self.ss15 = 30

        self.ss15 = self.ss15 - 1

    # FUCTIONS INITIAL
    def user(self):
        db = database.DBLocal()
        user = db.list_user_local()[0]
        self.text_empresa_pessoal.setText(user[2])
        self.text_email.setText(user[3])
        self.text_telefone.setText(user[4])
        self.text_licenca.setText(user[6])

    def showTime(self):
        current_time = QTime.currentTime()
        current_data = QDate.currentDate()
        label_date = current_data.toString('dd/MM/yyyy')
        label_time = current_time.toString('hh:mm:ss')
        self.hora.setText(label_time)
        self.data.setText(label_date)
        
        # FUCTIONS 
        self.disable_button_avulsa()

    def menu_grupos(self):
        if self.menu_grupos_frame.height() == 0:
            self.aba_grupo_button.setText('Grupos                  ▲')
        else:
            self.aba_grupo_button.setText('Grupos                  ▼')
        self.animation_grupo()

    def menu_pesagem(self):
        if self.menu_pesagem_frame.height() == 0:
            self.aba_pesagem_button.setText('Pesagens               ▲')
        else:
            self.aba_pesagem_button.setText('Pesagens               ▼')
        self.animation_pesagem()

    def menu_relatorio(self):
        if self.menu_relatorio_frame.height() == 0:
            self.aba_relatorio_button.setText('Relatórios             ▲')
        else:
            self.aba_relatorio_button.setText('Relatórios             ▼')
        self.animatio_relatorio()

    # SHOW DIALOGS
    def show_sair_conta(self):
        self.dialog_sair_conta.showFullScreen()

    def show_excluir_conta(self):
        self.dialog_excluir_conta.showFullScreen()

    def show_atualizar_nome(self):
        self.dialog_atualizar_nome.showFullScreen()

    def show_atualizar_senha(self):
        self.dialog_atualizar_senha.showFullScreen()

    def show_atualizar_telefone(self):
        self.dialog_atualizar_telefone.showFullScreen()

    def show_remover_dados_avulsas(self):
        self.dialog_remover_dados.showFullScreen()

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
            width_extend = 400
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
            width_extend = 400
        else:
            width_extend = 0

        self.animation = QPropertyAnimation(self.frame_105, b'maximumWidth')
        self.animation.setDuration(300)
        self.animation.setStartValue(width)
        self.animation.setEndValue(width_extend)
        self.animation.start()

    def animation_menu_veiculos(self):
        width = self.frame_68.maximumWidth()

        if width == 0:
            width_extend = 400
        else:
            width_extend = 0

        self.animation = QPropertyAnimation(self.frame_68, b'maximumWidth')
        self.animation.setDuration(300)
        self.animation.setStartValue(width)
        self.animation.setEndValue(width_extend)
        self.animation.start()

    def func_peso_manualmente(self):
        width = self.peso_manualmente_2.width()

        if width >= 135:
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

    # FUNCTIONS
    def peso_manual(self):
        text = self.peso_manualmente_2.text()
        self.lcdNumber_2.display(text)

    def is_num(self, valor, type=float):
        if type == int:
            try:
                int(valor)
            except:
                return False
            else:
                return True
        else:
            try:
                float(valor)
            except:
                return False
            else:
                return True

    # Dados adicionados
    def cargas_comboBox(self):
        cargas = models.list_cargas()
        self.comboBox_veiculos_produtos.clear()
        self.comboBox_veiculos_produtos.addItem('Nenhum')

        self.comboBox_avulsas_carga.clear()
        self.comboBox_avulsas_carga.addItem('Nenhum')

        self.comboBox_entrada_carga.clear()
        self.comboBox_entrada_carga.addItem('Nenhum')

        self.comboBox_carga.clear()
        self.comboBox_carga.addItem('Nenhum')

        self.comboBox_carga_2.clear()
        self.comboBox_carga_2.addItem('Nenhum')

        for carga in cargas:
            self.comboBox_veiculos_produtos.addItem(f'{carga}')
            self.comboBox_avulsas_carga.addItem(f'{carga}')
            self.comboBox_entrada_carga.addItem(f'{carga}')
            self.comboBox_carga.addItem(f'{carga}')
            self.comboBox_carga_2.addItem(f'{carga}')

    def clientes_comboBox(self):
        clientes = models.list_clientes()

        self.comboBox_cliente.clear()
        self.comboBox_cliente.addItem('Nenhum')

        self.comboBox_cliente_2.clear()
        self.comboBox_cliente_2.addItem('Nenhum')

        self.comboBox_avulsas_cliente.clear()
        self.comboBox_avulsas_cliente.addItem('Nenhum')

        self.comboBox_entrada_cliente.clear()
        self.comboBox_entrada_cliente.addItem('Nenhum')

        for cliente in clientes:
            self.comboBox_cliente.addItem(f'{cliente}')
            self.comboBox_cliente_2.addItem(f'{cliente}')
            self.comboBox_avulsas_cliente.addItem(f'{cliente}')
            self.comboBox_entrada_cliente.addItem(f'{cliente}')

    def veiculos_comboBox(self):
        veiculos = models.list_veiculos()

        self.comboBox_veiculo.clear()
        self.comboBox_veiculo.addItem('Nenhum')

        self.comboBox_veiculo_2.clear()
        self.comboBox_veiculo_2.addItem('Nenhum')

        self.comboBox_avulsas_veiculo.clear()
        self.comboBox_avulsas_veiculo.addItem('Nenhum')

        self.comboBox_entrada_veiculo.clear()
        self.comboBox_entrada_veiculo.addItem('Nenhum')

        for veiculo in veiculos:
            self.comboBox_veiculo.addItem(f'{veiculo}')
            self.comboBox_veiculo_2.addItem(f'{veiculo}')
            self.comboBox_avulsas_veiculo.addItem(f'{veiculo}')
            self.comboBox_entrada_veiculo.addItem(f'{veiculo}')

    def cargas(self):
        cargas = models.list_cargas()

        for carga in cargas:
            linha = self.tableWidget.rowCount()
            self.tableWidget.insertRow(linha)
            check = QTableWidgetItem()
            check.setCheckState(Qt.Unchecked)
            self.tableWidget.setItem(linha, 0, check)
            self.tableWidget.setItem(linha, 1, QTableWidgetItem(carga.nome))
            self.tableWidget.setItem(linha, 2, QTableWidgetItem(carga.preco))
            self.tableWidget.setItem(
                linha, 3, QTableWidgetItem(carga.densidade))
            self.tableWidget.setItem(
                linha, 4, QTableWidgetItem(carga.embalagem))
            self.tableWidget.setItem(
                linha, 5, QTableWidgetItem(carga.desconto))

    def clientes(self):
        clientes = models.list_clientes()

        for cliente in clientes:
            linha = self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(linha)
            check = QTableWidgetItem()
            check.setCheckState(Qt.Unchecked)
            self.tableWidget_2.setItem(linha, 0, check)
            self.tableWidget_2.setItem(
                linha, 1, QTableWidgetItem(cliente.nome))
            self.tableWidget_2.setItem(
                linha, 2, QTableWidgetItem(cliente.cpf_cnpj))
            self.tableWidget_2.setItem(linha, 3, QTableWidgetItem(cliente.rg))
            self.tableWidget_2.setItem(
                linha, 4, QTableWidgetItem(cliente.telefone))
            self.tableWidget_2.setItem(linha, 5, QTableWidgetItem(cliente.cep))
            self.tableWidget_2.setItem(
                linha, 6, QTableWidgetItem(cliente.endereço))

    def veiculos(self):
        veiculos = models.list_veiculos()

        for veiculo in veiculos:
            linha = self.tableWidget_3.rowCount()
            self.tableWidget_3.insertRow(linha)
            check = QTableWidgetItem()
            check.setCheckState(Qt.Unchecked)
            self.tableWidget_3.setItem(linha, 0, check)
            self.tableWidget_3.setItem(
                linha, 1, QTableWidgetItem(veiculo.placa))
            self.tableWidget_3.setItem(
                linha, 2, QTableWidgetItem(veiculo.proprietario))
            self.tableWidget_3.setItem(
                linha, 3, QTableWidgetItem(veiculo.nome))
            self.tableWidget_3.setItem(
                linha, 4, QTableWidgetItem(f'{veiculo.carga}'))

    def relatorio_avulsa(self):
        pesagens = models.list_pesagens_avulsa()

        for pesagem in pesagens:
            linha = self.tableWidget_4.rowCount()
            self.tableWidget_4.insertRow(linha)
            check = QTableWidgetItem()
            check.setCheckState(Qt.Unchecked)
            self.tableWidget_4.setItem(linha, 0, check)
            self.tableWidget_4.setItem(linha, 1, QTableWidgetItem(pesagem.motorista))
            self.tableWidget_4.setItem(linha, 2, QTableWidgetItem(pesagem.produto))
            self.tableWidget_4.setItem(linha, 3, QTableWidgetItem(pesagem.cliente))
            self.tableWidget_4.setItem(linha, 4, QTableWidgetItem(pesagem.peso_bruto))
            self.tableWidget_4.setItem(linha, 5, QTableWidgetItem(pesagem.data))
            self.tableWidget_4.setItem(linha, 6, QTableWidgetItem(pesagem.placa))

    # Pegando dados
    def get_dados_carga(self):
        nome = self.input_produtos_nome.text()
        densidade = self.input_produtos_densidade.text()
        embalagem = self.input_produtos_embalagemKG.text()
        preco = self.input_produtos_estoqueKG.text().replace(',', '.')
        desconto = self.input_produtos_desconto.text()
        saida = None
        self.ss15 = 30

        if nome:
            saida = True
            if densidade:
                if not self.is_num(densidade):
                    saida = False
            else:
                densidade = '0'

            if embalagem:
                if not self.is_num(embalagem):
                    saida = False
            else:
                embalagem = '0'

            if preco:
                if not self.is_num(preco):
                    saida = False
            else:
                preco = '0'

            if desconto:
                if not self.is_num(desconto):
                    saida = False
            else:
                desconto = '0'
        else:
            self.frame_saida.show()
            self.hide_segundos()
            self.label_realizada_ou_erro.setText('Campo obrigatório')
            self.label_realizada_ou_erro.setStyleSheet(
                'color:rgb(255, 32, 32);')
            self.label_veja_no_relatorio.setText(
                'O campo NOME não pode estar vazio.')
            self.label_logo_saida.setPixmap(
                QPixmap(u":/icons/circle-info-solidr.svg"))

        if saida == True:
            self.frame_saida.show()
            self.hide_segundos()
            self.label_realizada_ou_erro.setText(f'Carga "{nome}" adicionada')
            self.label_realizada_ou_erro.setStyleSheet(
                'color:rgb(6, 180, 20);')
            self.label_veja_no_relatorio.setText('')
            self.label_logo_saida.setPixmap(
                QPixmap(u":/icons/check-solid_green.svg"))

            # add db
            db = database.DBLocal()
            id_user = db.list_user_local()[0][0]
            models.add_carga(id_user, nome, preco,
                             densidade, embalagem, desconto)

            # add table
            linha = self.tableWidget.rowCount()
            self.tableWidget.insertRow(linha)
            check = QTableWidgetItem()
            check.setCheckState(Qt.Unchecked)
            self.tableWidget.setItem(linha, 0, check)
            self.tableWidget.setItem(linha, 1, QTableWidgetItem(nome))
            self.tableWidget.setItem(linha, 2, QTableWidgetItem(preco))
            self.tableWidget.setItem(linha, 3, QTableWidgetItem(densidade))
            self.tableWidget.setItem(linha, 4, QTableWidgetItem(embalagem))
            self.tableWidget.setItem(linha, 5, QTableWidgetItem(desconto))
            self.cargas_comboBox()

            # limpando campos
            nome = self.input_produtos_nome.setText('')
            densidade = self.input_produtos_densidade.setText('')
            embalagem = self.input_produtos_embalagemKG.setText('')
            preco = self.input_produtos_estoqueKG.setText('')
            desconto = self.input_produtos_desconto.setText('')

        elif saida == False:
            self.frame_saida.show()
            self.hide_segundos()
            self.label_realizada_ou_erro.setText('Campo incorreto')
            self.label_realizada_ou_erro.setStyleSheet(
                'color:rgb(255, 32, 32);')
            self.label_veja_no_relatorio.setText(
                'Apenas o campo NOME deve conter letras e espaços.')
            self.label_logo_saida.setPixmap(
                QPixmap(u":/icons/circle-info-solidr.svg"))

    def get_dados_cliente(self):
        nome = self.input_clientes_nome.text()
        cpf = self.input_clientes_cpf.text()
        rg = self.input_clientes_rg.text()
        cep = self.input_clientes_cep.text()
        endereco = self.input_clientes_endereco.text()
        telefone = self.input_clientes_telefone.text().replace(' ', '')
        detalhe_saida = ''
        saida = None
        self.ss15 = 30

        if nome and telefone:
            saida = True

            if not self.is_num(telefone):
                saida = False
                detalhe_saida = 'Telefone inválido.'

            if cep:
                if len(cep.replace('-', '').replace(' ', '')) != 8 and self.is_num(cep.replace('-', '').replace(' ', '')):
                    saida = False
                    detalhe_saida = 'Código postal (CEP) inválido.'
            else:
                cep = 'n/a'

            if rg:
                if len(rg.replace('-', '').replace('.', '').replace(' ', '')) != 9 and self.is_num(rg.replace('-', '').replace(' ', '').replace('.', '')):
                    saida = False
                    detalhe_saida = 'Registro geral (RG) inválido.'
            else:
                rg = 'n/a'

            if cpf:
                if not utils.validador(cpf):
                    saida = False
                    detalhe_saida = 'Certificação de pessoa física (CPF) inválida'
            else:
                cpf = 'n/a'

            if not endereco:
                endereco = 'n/a'
        else:
            self.frame_saida.show()
            self.hide_segundos()
            self.label_realizada_ou_erro.setText('Campo obrigatório')
            self.label_realizada_ou_erro.setStyleSheet(
                'color:rgb(255, 32, 32);')
            self.label_veja_no_relatorio.setText(
                'NOME e TELEFONE são obrigatórios.')
            self.label_logo_saida.setPixmap(
                QPixmap(u":/icons/circle-info-solidr.svg"))

        if saida == True:
            self.frame_saida.show()
            self.hide_segundos()
            self.label_realizada_ou_erro.setText(f'Cliente "{nome}" adicionado')
            self.label_realizada_ou_erro.setStyleSheet(
                'color:rgb(6, 180, 20);')
            self.label_veja_no_relatorio.setText('')
            self.label_logo_saida.setPixmap(
                QPixmap(u":/icons/check-solid_green.svg"))

            # add a db
            db = database.DBLocal()
            id_user = db.list_user_local()[0][0]
            models.add_cliente(id_user, nome, cpf, rg, telefone, cep, endereco)

            # add table
            linha = self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(linha)
            check = QTableWidgetItem()
            check.setCheckState(Qt.Unchecked)
            self.tableWidget_2.setItem(linha, 0, check)
            self.tableWidget_2.setItem(linha, 1, QTableWidgetItem(nome))
            self.tableWidget_2.setItem(linha, 2, QTableWidgetItem(cpf))
            self.tableWidget_2.setItem(linha, 3, QTableWidgetItem(rg))
            self.tableWidget_2.setItem(linha, 4, QTableWidgetItem(telefone))
            self.tableWidget_2.setItem(linha, 5, QTableWidgetItem(cep))
            self.tableWidget_2.setItem(linha, 6, QTableWidgetItem(endereco))
            self.clientes_comboBox()

            # limpando campos
            self.input_clientes_nome.setText('')
            self.input_clientes_cpf.setText('')
            self.input_clientes_rg.setText('')
            self.input_clientes_cep.setText('')
            self.input_clientes_endereco.setText('')
            self.input_clientes_telefone.setText('')

        elif saida == False:
            self.frame_saida.show()
            self.hide_segundos()
            self.label_realizada_ou_erro.setText('Campo incorreto')
            self.label_realizada_ou_erro.setStyleSheet(
                'color:rgb(255, 32, 32);')
            self.label_veja_no_relatorio.setText(detalhe_saida)
            self.label_logo_saida.setPixmap(
                QPixmap(u":/icons/circle-info-solidr.svg"))

    def get_dados_veiculos(self):
        nome = self.input_veiculos_nome.text()
        placa = self.input_veiculos_placa.text()
        proprietario = self.input_veiculos_valor_2.text()
        produto = self.comboBox_veiculos_produtos.currentText()
        id_produto = models.list_cargas(produto)
        self.ss15 = 30

        if nome and placa and proprietario and str(produto) != 'Nenhum':
            self.frame_saida.show()
            self.hide_segundos()
            self.label_realizada_ou_erro.setText('Veículo adicionado')
            self.label_realizada_ou_erro.setStyleSheet(
                'color:rgb(6, 180, 20);')
            self.label_veja_no_relatorio.setText('')
            self.label_logo_saida.setPixmap(
                QPixmap(u":/icons/check-solid_green.svg"))

            # add db
            db = database.DBLocal()
            id_user = db.list_user_local()[0][0]
            models.add_veiculo(id_user, proprietario, nome, placa, id_produto)

            # add table
            linha = self.tableWidget_3.rowCount()
            self.tableWidget_3.insertRow(linha)
            check = QTableWidgetItem()
            check.setCheckState(Qt.Unchecked)
            self.tableWidget_3.setItem(linha, 0, check)
            self.tableWidget_3.setItem(linha, 1, QTableWidgetItem(nome))
            self.tableWidget_3.setItem(linha, 2, QTableWidgetItem(placa))
            self.tableWidget_3.setItem(
                linha, 3, QTableWidgetItem(proprietario))
            self.tableWidget_3.setItem(linha, 4, QTableWidgetItem(produto))
            self.veiculos_comboBox()

            # limpando campos
            nome = self.input_veiculos_nome.setText('')
            placa = self.input_veiculos_placa.setText('')
            proprietario = self.input_veiculos_valor_2.setText('')
            produto = self.comboBox_veiculos_produtos.setCurrentIndex(0)

        else:
            self.frame_saida.show()
            self.hide_segundos()
            self.label_realizada_ou_erro.setText('Campo obrigatório')
            self.label_realizada_ou_erro.setStyleSheet(
                'color:rgb(255, 32, 32);')
            self.label_veja_no_relatorio.setText(
                'Todos os campos devem ser preenchidos.')
            self.label_logo_saida.setPixmap(
                QPixmap(u":/icons/circle-info-solidr.svg"))

    def delete_pesagem_avulsa(self):
        for i in range(self.tableWidget_4.rowCount()):
            if self.tableWidget_4.item(i, 0).checkState() == Qt.CheckState.Checked:
                indentificacao_data = self.tableWidget_4.item(i, 5).text()
                self.tableWidget_4.removeRow(i)
                models.del_pesagem_avulsa(indentificacao_data)

    def get_pesagem_avulsas(self):
        motorista = self.input_avulsas_motorista.text()
        veiculo = self.comboBox_avulsas_veiculo.currentText()
        cliente = self.comboBox_avulsas_cliente.currentText()
        carga = self.comboBox_avulsas_carga.currentText()
        obs = self.input_avulsas_obs.text()

        peso = self.lcdNumber_2.value()
        data = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        saida = None
        self.ss15 = 30

        if motorista and veiculo != 'Nenhum' and cliente != 'Nenhum' and carga != 'Nenhum':
            if not obs:
                obs = 'Sem observação'
            if int(self.lcdNumber_2.value()) == 0:
                saida = False
            # add db

            saida = True

        if saida == True:
            self.frame_saida.show()
            self.hide_segundos()
            self.label_realizada_ou_erro.setText('Pesagem Avulsa realizada')
            self.label_realizada_ou_erro.setStyleSheet(
                'color:rgb(6, 180, 20);')
            self.label_veja_no_relatorio.setText('Veja em relatório avulsas')
            self.label_logo_saida.setPixmap(
                QPixmap(u":/icons/check-solid_green.svg"))
        
            # add db
            db = database.DBLocal()
            id_user = db.list_user_local()[0][0]
            models.add_relatorio_avulsa(id_user, motorista, carga, cliente, peso, data, veiculo, obs)

            # add table
            linha = self.tableWidget_4.rowCount()
            self.tableWidget_4.insertRow(linha)
            check = QTableWidgetItem()
            check.setCheckState(Qt.Unchecked)
            self.tableWidget_4.setItem(linha, 0, check)
            self.tableWidget_4.setItem(linha, 1, QTableWidgetItem(motorista))
            self.tableWidget_4.setItem(linha, 2, QTableWidgetItem(carga))
            self.tableWidget_4.setItem(linha, 3, QTableWidgetItem(cliente))
            self.tableWidget_4.setItem(linha, 4, QTableWidgetItem(str(peso)))
            self.tableWidget_4.setItem(linha, 5, QTableWidgetItem(data))
            self.tableWidget_4.setItem(linha, 6, QTableWidgetItem(veiculo))

            # limpando campos
            self.input_avulsas_motorista.setText('')
            self.input_avulsas_obs.setText('')
            self.comboBox_avulsas_veiculo.setCurrentIndex(0)
            self.comboBox_avulsas_cliente.setCurrentIndex(0)
            self.comboBox_avulsas_carga.setCurrentIndex(0)
        
        elif saida == None:
            self.frame_saida.show()
            self.hide_segundos()
            self.label_realizada_ou_erro.setText(
                'Pesagem avulsa não realizada')
            self.label_realizada_ou_erro.setStyleSheet(
                'color:rgb(255, 32, 32);')
            self.label_veja_no_relatorio.setText(
                'Todos os campos devem ser preenchidos.')
            self.label_logo_saida.setPixmap(
                QPixmap(u":/icons/circle-info-solidr.svg"))

        else:
            self.frame_saida.show()
            self.hide_segundos()
            self.label_realizada_ou_erro.setText('Pesagem não realizada')
            self.label_realizada_ou_erro.setStyleSheet(
                'color:rgb(255, 32, 32);')
            self.label_veja_no_relatorio.setText(
                'Não foi possível coletar o peso com valor: 0')
            self.label_logo_saida.setPixmap(
                QPixmap(u":/icons/circle-info-solidr.svg"))

    # Entrada e Saida
    def get_pesagem_entrada(self):
        motorista = self.input_entrada_motorista.text()
        veiculo = self.comboBox_entrada_veiculo.currentText()
        cliente = self.comboBox_entrada_cliente.currentText()
        carga = self.comboBox_entrada_carga.currentText()
        obs = self.input_entrada_obs.text()
        saida = None
        self.ss15 = 30

        self.bindApply()

        if motorista and veiculo != 'Nenhum' and cliente != 'Nenhum' and carga != 'Nenhum':
            if not obs:
                obs = 'Sem observação'
            if int(self.lcdNumber.value()) == 0:
                saida = False
            # add db

            saida = True

        if saida == True:
            self.frame_saida.show()
            self.hide_segundos()
            self.label_realizada_ou_erro.setText(
                'Pesagem de entrada realizada')
            self.label_realizada_ou_erro.setStyleSheet(
                'color:rgb(6, 180, 20);')
            self.label_veja_no_relatorio.setText('realize a pesagem de saída')
            self.label_logo_saida.setPixmap(
                QPixmap(u":/icons/check-solid_green.svg"))

        elif saida == None:
            self.frame_saida.show()
            self.hide_segundos()
            self.label_realizada_ou_erro.setText(
                'Pesagem de entrada não realizada')
            self.label_realizada_ou_erro.setStyleSheet(
                'color:rgb(255, 32, 32);')
            self.label_veja_no_relatorio.setText(
                'Todos os campos devem ser preenchidos.')
            self.label_logo_saida.setPixmap(
                QPixmap(u":/icons/circle-info-solidr.svg"))

        else:
            self.frame_saida.show()
            self.hide_segundos()
            self.label_realizada_ou_erro.setText('Pesagem não realizada')
            self.label_realizada_ou_erro.setStyleSheet(
                'color:rgb(255, 32, 32);')
            self.label_veja_no_relatorio.setText(
                'Não foi possível coletar o peso com valor: 0')
            self.label_logo_saida.setPixmap(
                QPixmap(u":/icons/circle-info-solidr.svg"))

    def get_pesagem_saida(self):
        pesagem_entrada = self.comboBox_pesagem_entrada.currentText()
        saida = None
        self.ss15 = 30

        if pesagem_entrada != 'Nenhum':
            saida = True
            # add db

        else:
            saida = False

        if saida:
            self.frame_saida.show()
            self.hide_segundos()
            self.label_realizada_ou_erro.setText('Pesagem realizada')
            self.label_realizada_ou_erro.setStyleSheet(
                'color:rgb(6, 180, 20);')
            self.label_veja_no_relatorio.setText(
                'Veja em relatório entradas e saídas')
            self.label_logo_saida.setPixmap(
                QPixmap(u":/icons/check-solid_green.svg"))

        else:
            self.frame_saida.show()
            self.hide_segundos()
            self.label_realizada_ou_erro.setText(
                'Pesagem de saída não realizada')
            self.label_realizada_ou_erro.setStyleSheet(
                'color:rgb(255, 32, 32);')
            self.label_veja_no_relatorio.setText(
                'Escolha uma pesagem de entrada.')
            self.label_logo_saida.setPixmap(
                QPixmap(u":/icons/circle-info-solidr.svg"))

    def detalhes_saida(self):
        pesagem_entrada = self.comboBox_pesagem_entrada.currentText()

        height = self.frame_saida_detalhes.maximumHeight()

        if str(pesagem_entrada) != 'Nenhum':
            height_extend = 300
        else:
            height_extend = 0

        self.animation = QPropertyAnimation(
            self.frame_saida_detalhes, b'maximumHeight')
        self.animation.setDuration(400)
        self.animation.setStartValue(height)
        self.animation.setEndValue(height_extend)
        self.animation.start()

    # limitação
    def limit(self):
        self.ss15 = 30
        self.frame_saida.show()
        self.hide_segundos()
        self.label_realizada_ou_erro.setText(
            'Sem conexão')
        self.label_realizada_ou_erro.setStyleSheet(
            'color:rgb(255, 32, 32);')
        self.label_veja_no_relatorio.setText(
            'Conecte-se a uma balança')
        self.label_logo_saida.setPixmap(
            QPixmap(u":/icons/circle-info-solidr.svg"))


class LoginWindow(QWidget, Ui_Login_Widget, QRegion):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)

        self._senha_input.setEchoMode(self._senha_input.Password)
        self.entrar_button.setDisabled(True)
        self.email_input.textChanged.connect(self.disableButton)
        self._senha_input.textChanged.connect(self.disableButton)
        self.mais_servicos_button.clicked.connect(self.more_services)
        self.btn_close_windows.clicked.connect(lambda: self.close())
        self.btn_minimize_window.clicked.connect(lambda: self.showMinimized())
        self.entrar_button.clicked.connect(self.login)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.erro.hide()

        self.premium = PremiumWindow(self)
        self.main_window = MainWindow()

    def disableButton(self):
        if len(self.email_input.text()) > 0 and len(self._senha_input.text()) > 0:
            self.erro.hide()
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
            self.main_window.showFullScreen()
            sleep(1)
            user = database.DBLocal()
            user.add_user(email)
            self.premium.showFullScreen()
        else:
            self.erro.show()
            self._senha_input.setText('')

    def more_services(self):
        utils.open_link('https://www.caltecbalancas.com.br/servicos.html')


class PremiumWindow(QDialog, Ui_Dialog):
    def __init__(self, parent):
        super(PremiumWindow, self).__init__(parent)
        self.setupUi(self)
        self.btn_voltar.clicked.connect(self.voltar)
        self.btn_comprar.clicked.connect(self.comprar)
        self.btn_pular.clicked.connect(lambda: self.close())
        self.pushButton_2.clicked.connect(self.comprar)
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
    Window = MainWindow()
    Window.showFullScreen()
    app.exec_()
