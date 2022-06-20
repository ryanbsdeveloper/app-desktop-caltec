import sqlite3
from typing import Tuple
import psycopg2
import os

from . import models

BASE_DIR = os.path.dirname(__file__)

#Database in cloud
class DB():
    def __init__(self) -> None:
        self.con = psycopg2.connect(host='localhost',
                                    database='caltecbalancas', user='postgres', password='842684265santos')
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

    def list_users_local(self):
        lista = []
        SQL = 'SELECT * from users'
        self.cur.execute(SQL)  
        for c in self.cur.fetchall():
            lista.append(c)

        return lista

    def add_user(self, email) -> Tuple:
        for user in self.db_cloud.list_users():
            if email in  user:
                if user not in self.list_users_local():
                    nome_empresa = user[1]
                    e_mail = user[2]
                    whatsapp = user[3]
                    senha = user[4]
                    licenca = user[5]
                    max_pesagem = user[6]
                    models.add_user(nome_empresa, e_mail,
                                    whatsapp, senha, licenca, max_pesagem)



if __name__ == '__main__':
    db = DBLocal()
    print(db.list_users_local())