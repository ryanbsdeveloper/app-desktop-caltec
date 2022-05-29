import psycopg2
import webbrowser

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


def open_link(url):
    webbrowser.open(url)