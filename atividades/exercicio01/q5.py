from selenium import webdriver
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Chrome()

navegador.get('http://www.google.com/search.')

elemento = navegador.find_element(by='tag_name', value='input')

elemento.send_keys('q')
