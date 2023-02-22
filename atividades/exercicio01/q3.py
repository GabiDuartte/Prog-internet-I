import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = []

resposta = requests.get('https://g1.globo.com')

conteudo = resposta.content

site = BeautifulSoup(conteudo, 'html.parser')

noticias = site.findAll('div', attrs={'class': 'feed-post-body'})

for noticia in noticias:

    titulo = noticia.find('a', attrs={'class': 'feed-post-link'})

    # print(titulo.text)

    subtitulo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})

    if(subtitulo):
        lista_noticias.append([titulo.text, subtitulo.text])
    else:
        lista_noticias.append([titulo.text, ''])


news = pd.DataFrame(lista_noticias, columns=['Título', 'Subtítulo'])

print(news)

