from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from time import sleep

navegador = webdriver.Chrome()
navegador.get('https://www.google.com.br')

sleep(1)

elemento = navegador.find_element(by='name', value='q').send_keys('q' + Keys.RETURN)

sleep(2)

page_content = navegador.page_source

site = BeautifulSoup(page_content, 'html.parser')

print(site.prettify())
