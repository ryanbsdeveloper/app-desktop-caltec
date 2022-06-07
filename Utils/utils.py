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


import requests

url = "https://sandbox.api.pagseguro.com/charges"

payload = {
    "amount": {
        "value": 1000,
        "currency": "BRL"
    },
    "payment_method": {
        "card": {
            "holder": {"name": "Jose da Silva"},
            "number": "4111111111111111",
            "exp_month": "03",
            "exp_year": "2026",
            "security_code": "123"
        },
        "type": "CREDIT_CARD",
        "installments": 1,
        "capture": True
    },
    "reference_id": "ex-00001",
    "description": "Motivo da cobrança"
}
headers = {
    "Accept": "application/json",
    "Content-type": "application/json"
    ""
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)