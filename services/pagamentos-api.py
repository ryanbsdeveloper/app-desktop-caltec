import psycopg2
import requests
import xmltodict


con = psycopg2.connect(host='localhost', database='caltecbalancas',
                       user='postgres', password='842684265santos')
cur = con.cursor()
cur.execute('SELECT * FROM public."logs_notificaçõesmodel"')

# for l in cur.fetchall():
#     print(l)

email = 'rybala63@gmail.com'
token = '74C46796DFD944D886F8DC2FC0DCDB7E'

url = f'https://ws.sandbox.pagseguro.uol.com.br/v2/transactions?email={email}&token={token}&reference=rbsservices'

print(url)

headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.get(url, headers=headers)

response = xmltodict.parse(response.text)

print(response)
code_transition = response['transactionSearchResult']['transactions']['transaction']['code']

url = f'https://ws.sandbox.pagseguro.uol.com.br/v2/transactions/cancels?email={email}&token={token}'

headers = {
	'Content-Type': 'application/x-www-form-urlencoded'
}
payload = {
	'transactionCode': f'{code_transition}'
    }

response = requests.post(url, data=payload, headers=headers)

print(response.text)