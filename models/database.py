import sqlite3
from typing import Tuple
import psycopg2
import os

import models

BASE_DIR = os.path.dirname(__file__)

#Database in cloud


class DB():
    def __init__(self) -> None:
        self.con = psycopg2.connect(host='caltec.c4qq48rdfit7.us-east-1.rds.amazonaws.com',
                                    database='ryanl',
                                    port='5433', 
                                    user='ryanl', 
                                    password='842684265')
        self.cur = self.con.cursor()

    def user_log(self, email, senha):
        self.cur.execute('SELECT * FROM public.logs_usersmodel')
        for v in self.cur.fetchall():
            if email in v:
                if senha in v:
                    return True
        return False

    def list_users(self):
        self.users = []
        self.cur.execute('SELECT * FROM public.logs_usersmodel')
        for v in self.cur.fetchall():
            self.users.append(v)

        return self.users


#Database in localhost
class DBLocal():
    def __init__(self) -> None:
        self.con = sqlite3.connect(f'{BASE_DIR}/database.db')
        self.cur = self.con.cursor()
        self.db_cloud = DB()

    def list_user_local(self):
        lista = []
        SQL = 'SELECT * from users'
        self.cur.execute(SQL)
        for c in self.cur.fetchall():
            lista.append(c)

        return lista

    def add_user(self, email) -> Tuple:
        for user in self.db_cloud.list_users():
            if email in user:
                if user not in self.list_users_local():
                    id_cloud = user[0]
                    nome_empresa = user[1]
                    e_mail = user[2]
                    whatsapp = user[3]
                    senha = user[4]
                    licenca = user[5]
                    max_pesagem = user[6]
                    models.add_user(id_cloud, nome_empresa, e_mail,
                                    whatsapp, senha, licenca, max_pesagem)

    def add_veiculo(self, id_user_local, proprietario, modelo, placa, produto):
        SQL = 'INSERT'



if __name__ == '__main__':
    db = DB()
    print(db.list_users())
