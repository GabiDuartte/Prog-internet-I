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
c = CacheRequest (life=60)
url = 'https://lista.mercadolivre.com.br/'
produto_nome = 'fone de ouvido'
productlink = []
for x in range(1,6):
    if c.get(url + produto_nome):
        site = BeautifulSoup(c.text,'html.parser')

        productlist = site.find_all('div', {'class': 'andes-card andes-card--flat andes-card--default ui-search-result shops__cardStyles ui-search-result--core ui-search-result--advertisement andes-card--padding-default'})

        for item in productlist:
            titulo = item.find('h2', attrs={'class': 'ui-search-item__title shops__item-title'})

            for link in item.find_all('a',href=True):
                productlink.append([titulo.text,link['href']])


prod = pd.DataFrame(productlink, columns=['Titulo', 'Link'])
prod.to_excel('prod.xlsx', index=False)
print(prod)
