import requests
from bs4 import BeautifulSoup

resposta = requests.get('https://g1.globo.com')

conteudo = resposta.content

site = BeautifulSoup(conteudo, 'html.parser')

noticias = site.findAll('div', attrs={'class': 'feed-post-body'})

for noticia in noticias:

    titulo = noticia.find('a', attrs={'class': 'feed-post-link'})

    print(titulo['href'])


print()
