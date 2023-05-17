from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=800,1000', '--incognito']
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
driver.get('https://cursoautomacao.netlify.app')
sleep(1)
driver.execute_script('window.scrollTo(0,2000);')
# Encontrar campo escolher arquivo
botao_escolher_arquivo = driver.find_element(By.XPATH, "//input[@id='myFile']")
sleep(1)
# Enviar caminho completo para o arquivo dentro do meu computador
botao_escolher_arquivo.send_keys(
    'D:\\Storage\\Desktop\\projetos selenium\\logo.jpg')
sleep(1)
# Clicar em enviar
botao_enviar = driver.find_element(
    By.XPATH, "//input[@value='Enviar Arquivo']")
sleep(1)
botao_enviar.click()
input('')
driver.close()