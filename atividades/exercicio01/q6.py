import requests
import pandas as pd
from bs4 import BeautifulSoup

req = requests.get('https://www.uol.com.br/esporte/futebol/campeonatos/brasileirao/')

conteudo = req.content

site = BeautifulSoup(conteudo, 'html.parser')

tabela = site.find(name='table')

tabela_str = str(tabela)

df = pd.read_html(tabela_str)

print(df)
