import requests
import requests_cache
from bs4 import BeautifulSoup 

requests_cache.install_cache() 

paginas = [] 
paginas_palavra = [] 


def download(url):
	response = ''
	try:
		response = requests.get(url)
	except Exception as ex:
		response = None
	finally:
		return response

def _palavra_chave(keyword,pagina):
	texto = ''
	tamanho_keyword = len(keyword)

	soup = BeautifulSoup(pagina.text,'html.parser')
	page = soup.text

	palavra = page.find(keyword)

	if palavra < 0:
		texto = None
	elif palavra < 10:
		texto = page[0:palavra+tamanho_keyword+10:1]
	elif palavra > 10:
		texto = page[palavra-10:palavra+tamanho_keyword+10:1]

	return texto


def verif_link(url,url_original):
	if url != None:
		if url.startswith('http://') or url.startswith('https://'):
			return url
		elif url.startswith('/'):
			return url_original + url
		else:
			return url

def _links(pagina,url,deth,keyword):
	urls = [] 

	soup = BeautifulSoup(pagina.text,'html.parser')

	links = soup.find_all('a')
	
	for link in links:
		if verif_link(link.get('href'),url) != None:
			if deth > 0:
				urls.append(verif_link(link.get('href'),url))

				url = verif_link(link.get('href'),url)			
				paginas.append({'Url':url,'Nivel':deth})

	return urls

def scrape(keyword,url,deth):
	pagina = download(url)

	if pagina != None:

		if _palavra_chave(keyword,pagina) != None:
			print('Link: %s' % url)
			print('Trecho: %s' % _palavra_chave(keyword,pagina))
			paginas_palavra.append(url)	
		else:
			print('Link: %s' % url)
			print('Palavra não encontrada')

		if deth > 0 :
			urls = _links(pagina,url,deth,keyword)

			for url in urls:
				try:
					scrape(keyword,url,deth-1)
				except:
					continue	

	else:
		print('Erro')


def _paginas(keyword):
	if len(paginas_palavra) > 0:
		print('Paginas com a palavra %s' % keyword)
		for pagina in paginas_palavra:
			print(pagina)
			
	
def main():
	keyword = 'emprego'
	url = 'https://g1.globo.com/'
	deth = 1
	scrape(keyword,url,deth)
	_paginas(keyword)
	

if __name__ == '__main__':
	main()
