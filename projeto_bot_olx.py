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

def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=800,600', '--incognito']
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

# Localizar campo de busca
campo_busca = driver.find_element(By.ID,"searchtext-input")
campo_busca.click()
sleep(1)
campo_busca.send_keys('Yamaha mt-07')
sleep(1)
# Achar campo busca em buscar
botao_busca = driver.find_element(By.CLASS_NAME, 'search-button-submit')
botao_busca.click()

input('')
driver.close()