# Achando elementos por texto

# Neste caso, vamos utilizar o Xpath

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

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
driver.get('https://cursoautomacao.netlify.app/')

texto_somente = driver.find_element(By.XPATH, "//*[text()='ZONA DE TESTES']")


if texto_somente:
    print('Texto encontrado')
    


# Achando todos por uma tag: //*[h4]
# Qualquer tag que contenha a propriedade texto com a palavra igual a 'exemplo: //*[contains(text(),'exemplo')]
# Conforme acima, porém, usando 'or' para mais uma condicional: //*[contains(text(),'exemplo') or contains(text(),'Dropdown')]
# Achar um elemento que tenha duas palavras diferentes é só usar o 'and' //*[contains(text(),'exemplo') and contains(text(),'Dropdown')]
# Achar um elemento somente com o começo do texto usando 'starts-with': //*[starts-with(@class,'btn')]

# é melhor usar a tag no lugar do * pois a busca fica mais apurada:  //h4[text()='Exemplo Checkbox']
# Outro exemplo: //button[@aria-label='Toggle navigation']

# Encontrando um elemento dentro de outro elemento: //div[@id='select-class-example']//fieldset/h4
# Acima a div é a primeira tag ou tag mãe, depois vem //fieldset e por ultimo vem //h4 onde se localizar o id procurado.

# Achando por indice: //thead//tr//th[3]  

input('')

