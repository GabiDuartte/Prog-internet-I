import requests
from flask import Flask

print('CEP: ')
cep_cliente = input(str())

cep_cliente = cep_cliente.strip()

if len(cep_cliente) == 9:
    cep_cliente = cep_cliente.replace('-', "")

resposta = requests.get(f'https://viacep.com.br/ws/{cep_cliente}/json/')

resposta = resposta.json()

app = Flask(__name__)

@app.get('/')
def return_cep():
    return resposta
