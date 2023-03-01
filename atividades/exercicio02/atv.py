import tempfile, os, hashlib, json,datetime, requests, unicodedata
from bs4 import BeautifulSoup
import pandas as pd
import re

class CacheRequest():

    def __init__(self, life=1, cache=True):
        self.cache = cache
        self.life = life
        self.VERSION = "1"
        self.text = None
    
    def get(self, url):
        PATH_TO_CACHE_FILE = os.path.join(tempfile.gettempdir(), hashlib.md5(url.encode()).hexdigest() + self.VERSION)

        if(self.cache):
            if os.path.exists(PATH_TO_CACHE_FILE):
                buffer = json.loads(open(PATH_TO_CACHE_FILE, "r").read())

                if(datetime.datetime.utcnow() < datetime.datetime.strptime(buffer["data"], '%Y-%m-%d %H:%M:%S')):
                    self.text = buffer["html"]
                    print("\033[92m[+]\033[0m Proveniente do Cache. ]]")
                    return True
        
        page = requests.get(url)
        page.encoding = "utf-8"
        self.text = unicodedata.normalize(u'NFKD', page.text).encode('ascii', 'ignore').decode('utf-8')
        print("\033[92m[+]\033[0m Proveniente do Request. ]]")

        if (self.cache):
            with open(PATH_TO_CACHE_FILE, 'w') as f:
                f.write(json.dumps({"data": (datetime.datetime.utcnow() + datetime.timedelta(minutes=self.life)).strftime('%Y-%m-%d %H:%M:%S'), "html": self.text}))
                f.close()
                print("\033[92m[*]\033[0m Cache criado. ]]")
        return True
    

c = CacheRequest (life=60)
lista_prod = []
url = 'https://lista.mercadolivre.com.br/'
produto_nome = 'Musica'
if c.get(url + produto_nome):
        
        for page in range(1,3):
            site =  site = BeautifulSoup(c.text, 'html.parser')
            produtos = site.find_all('div', {'class': 'andes-card andes-card--flat andes-card--default ui-search-result shops__cardStyles ui-search-result--core ui-search-result--advertisement andes-card--padding-default'})

            for produto in produtos:
                titulo = produto.find('h2', attrs={'class': 'ui-search-item__title shops__item-title'})
                real = produto.find('span', attrs={'class': 'price-tag-fraction'})
                cent = produto.find('span', attrs={'class': 'price-tag-cents'})
                link = produto.find('a', attrs={'class': 'ui-search-link'})

                #print(produto.prettify())
                #print('Titulo: ', titulo.text)
                #print('Link: ', link['href'])

                
                texto = site.find(produto_nome in titulo).get_text().strip()
                print('\20',texto, '\20')
                    

                if(cent):
                    #print('Preço: ', real.text + ',' + cent.text)
                    lista_prod.append([titulo.text, link['href'], real.text,cent.text])
                else:
                    #print('Preço: ', real.text)
                    lista_prod.append([titulo.text, link['href'], real.text, ''])

                print('\n\n')

            next_li_element = site.find('li', class_='next')

            while(next_li_element is not None):
                next_page = next_li_element.find('a', href=True)['href']
                page = requests.get(url + next_page)
                site = BeautifulSoup(page.text, 'html.parser')


total = pd.DataFrame(lista_prod, columns=['Titulo','Link','Real','Centavos'])
total.to_excel('produtos.xlsx', index=False)
print(total)
