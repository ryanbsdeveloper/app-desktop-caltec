from typing import Tuple
import psycopg2
import sqlite3
import json

import models

#Database in cloud
class DB():
    def __init__(self) -> None:
        self.con = psycopg2.connect(host='caltecbalancas.postgres.database.azure.com',
                                    database='caltecbalancas', user='ryanl', password='842684265@Ry')
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
        self.con = sqlite3.connect('database.db')
        self.cur = self.con.cursor()
        self.db_cloud = DB()

    def add_user(self, email) -> Tuple:
        id = 0
        dados = {}
        for user in self.db_cloud.list_users():
            if email in user:
                id = user[0]
                nome_empresa = user[1]
                e_mail = user[2]
                whatsapp = user[3]
                senha = user[4]
                licenca = user[5]
                max_pesagem = user[6]
                models.add_user(id, nome_empresa, e_mail, whatsapp, senha, licenca, max_pesagem)

# data = DBLocal()
# data.add_user('rybala63@gmail.com')