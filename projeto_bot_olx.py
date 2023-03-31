'''
Projeto monitoramento de preços OLX
Passos:
1 - Entrar na pagina.
2 - Localizar campo de busca
3 - clicar em campo de busca
4 - digitar o alvo

'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import os

def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1920,1080', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    return driver


driver = iniciar_driver()
# Entrar na página
driver.get('https://www.olx.com.br/')
sleep(5)

# Localizar campo de busca
campo_busca = driver.find_element(By.ID,"searchtext-input")
# Clicando no campo de busca
campo_busca.click()
sleep(2)
#Digitando no campo de pesquisa
campo_busca.send_keys('Yamaha mt-07')
sleep(2)

# Achar campo busca em buscar
botao_busca = driver.find_element(By.CLASS_NAME, 'search-button-submit')
sleep(2)
# Clicando no botão de busca
botao_busca.click()
sleep(8)

# Xpath dos EStados:

acre = driver.find_element(By.XPATH, "//a[text()='Acre']") 
acre.click()

# Alagoas:  //a[text()='Alagoas']
# Amapá:  //a[text()='Amapá']
# Amazonas: //a[text()='Amazonas']
# Bahia:  //a[text()='Bahia']
# Ceara: //a[text()='Ceará']
# Distrito Federal:  //a[text()='Distrito Federal']
# espirito_santo: //a[text()='Espírito Santo']
# goias:  //a[text()='Goiás']
# maranhao:  //a[text()='Maranhão']
# mato_grosso:  //a[text()='Mato Grosso'] 
# mato_grosso_sul:  //a[text()='Mato Grosso do Sul']  
# minas:  //a[text()='Minas Gerais']
# para:  //a[text()='Pará']
# paraiba:  //a[text()='Paraíba']
# parana:  //a[text()='Paraná']
# pernanbuco:  //a[text()='Pernambuco']
# piaui:  //a[text()='Piauí']
# rio:  //a[text()='Rio de Janeiro']
# rio_grande_norte:  //a[text()='Rio Grande do Norte']
# rio_grand_sul:  //a[text()='Rio Grande do Sul']
# rondonia:  //a[text()='Rondônia']
# roraima:  //a[text()='Roraima']
# santa_catarina: //a[text()='Santa Catarina']
# sao_paulo: //a[text()='São Paulo']
# sergipe:  //a[text()='Sergipe']
# tocantins: // //a[text()='Tocantins']

espirito_santo = driver.find_element(By.XPATH, "//a[text()='Espírito Santo']") 
sleep(1)

espirito_santo.click()
sleep(5)

while True:



    # Não esquecer de mover até o final da pagina.
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    sleep(2)


    # Class anuncio normal: kgl1mq-0 eFXRHn sc-ifAKCX iUMNkO
    # Class anuncio destaque: kgl1mq-0 eFXRHn sc-ifAKCX ghBVzA   
    # São classes diferentes, preciso achar algo incomum
    # Achei esta: //div[@class='sc-12rk7z2-7 kDVQFY'] 
    # Como queremos os titulos pra jogar na tabela, é só ir na tag mãe h2 desta forma; //div[@class='sc-12rk7z2-7 kDVQFY']//h2

    titulos = driver.find_elements(By.XPATH,"//div[@class='sc-12rk7z2-7 kDVQFY']//h2")

    # Agora devemos pesquisar os preços:

    precos = driver.find_elements(By.XPATH, "//div[@class='sc-1kn4z61-1 dGMPPn']")

    links = driver.find_elements(By.XPATH, "//a[@data-lurker-detail='list_id']")

    # estados_todos = driver.find_elements(By.XPATH, '//a[@class="sc-1l6qrj6-0 hSmLZl sc-gzVnrw kGFTcZ"]') 


    # Guardar esses dados em arquivos CSV
    for titulo, preco, link in zip(titulos, precos, links):
        with open('precos1.csv', 'a', encoding='utf-8', newline='') as arquivo:
            link_processado = link.get_attribute('href')   # href é o atributo onde se encontra de fato o link
            arquivo.write(f'{titulo.text};{preco.text};{link_processado}{os.linesep}')  #os.linesep é uma quebra de linha para organizar as linhas
    try:        
        proxima_pagina = driver.find_element(By.XPATH, "//span[text()='Próxima pagina']")     
        proxima_pagina.click()
    except:
        print('Fim da extração')
        break      

input('')
driver.close()