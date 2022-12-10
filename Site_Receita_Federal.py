"""
pip install requests #Instalar a biblioteca


"""


import requests
#import pandas as pd
from urllib.request import urlopen, urlretrieve, Request
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
from selenium import webdriver
from time import * # Da um tempo p\ carregar


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#Essa biblioteca nativamente te opriga a baixar o Webdriver do Navegadir
#Chrome---> chromedriver Firefox--->geckodriver
#Linhas de codigos PAD. para não da erro e atualizar sozinho de cada navegador, sempre igaul p\ usar Selenium
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
servico = Service(ChromeDriverManager().install())
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
navegador = webdriver.Chrome(service=servico)  #Rodando o  WebDriver do codigo, ñ algum que esteja instalado no computador
#Entrar no Navegador
link = 'https://servicos.receita.fazenda.gov.br/servicos/cpf/consultasituacao/consultapublica.asp'
navegador.get(url=link)
sleep(1)
#passo2
navegador.maximize_window()
navegador.find_element('xpath', '//*[@id="txtCPF"]').send_keys("05693833151")
navegador.find_element('xpath', '//*[@id="txtDataNascimento"]').send_keys("24062003")
sleep(25)
navegador.find_element('xpath', '//*[@id="id_submit"]').click()
#\\\\\\\\\\\\\\\\\\\\\\\\\ Fazer um request da Pagina ////////////////////////////////
res = requests.get('https://servicos.receita.fazenda.gov.br/Servicos/CPF/ConsultaSituacao/ConsultaPublicaExibir.asp')
res.enconding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')
dados = soup.find_all('div', attrs={'class": "clConteudoDados'})
#PARA SABER SE O SITE PERMITE QUE VOCÊ MEXA COM ROBO COLOQUE
#           AO FINAL DO LIIIIIINK /robots.txt



print(soup)

pass