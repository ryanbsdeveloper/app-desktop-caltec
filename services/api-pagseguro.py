import requests
import webbrowser
from xml.etree import ElementTree

email =  'rybala63@gmail.com'
token = '74C46796DFD944D886F8DC2FC0DCDB7E'

url = f'https://ws.sandbox.pagseguro.uol.com.br/v2/checkout?email={email}&token={token}'

payload = {
  'email': f'{email}',
  'token': f'{token}',
  'currency': 'BRL',
  'itemId1': '1',
  'itemDescription1': 'Licenca Anual',
  'itemAmount1': '119.99',
  'itemQuantity1': 1,
  'itemWeight1': 0,
  'reference': 'rbsservices',
  'senderName': '',
  'senderAreaCode': '11',
  'senderPhone': '952636545',
  'senderCPF': '66688604604',
  'senderEmail': 'ryan.lindo65@gmail.com',
  'shippingAddressRequired': 'FALSE',
  'receiverEmail': 'rybala63@gmail.com',
  'notificationURL': '',
  'maxUses': 3,
  'maxAge': 3000,
  'timeout': '30',
  'shippingCost': '0.00'
}

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
}

response = requests.post(url, data=payload, headers=headers)

code = (str(response.text)[76:-60])

url = f"https://sandbox.pagseguro.uol.com.br/v2/checkout/payment.html?code={code}"

webbrowser.open(url)

