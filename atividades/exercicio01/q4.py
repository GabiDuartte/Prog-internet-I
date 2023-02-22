import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_img = []

resposta = requests.get('https://g1.globo.com')

conteudo = resposta.content

site = BeautifulSoup(conteudo, 'html.parser')

noticias = site.findAll('div', attrs={'class': 'feed-post-body'})

for noticia in noticias:

    img = noticia.find('picture', attrs={'class': 'bstn-fd-cover-picture'})

    if(img):
        lista_img.append([img.text])


news = pd.DataFrame(lista_img, columns=['Imagem'])

news.to_excel('Imagens-noticias.xlsx', index=False)

print(news)
