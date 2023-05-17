from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.keys import Keys

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

driver.get('https://www.facebook.com/')
sleep(3)

# Campo email
email = driver.find_element(By.ID, 'email')
email.send_keys('davidinrock@hotmail.com')
sleep(2)

# Campo senha
senha = driver.find_element(By.ID, 'pass')
senha.send_keys('davidaline')
sleep(2)

# Botão 'Entrar'
entrar = driver.find_element(By.XPATH, "//button[@name='login']")
entrar.click()
sleep(4)

# Campo 'No que você está pensando'
postar = driver.find_element(By.XPATH, "//div[@class='xi81zsa x1lkfr7t xkjl1po x1mzt3pk xh8yej3 x13faqbe']")
postar.click()
sleep(2)


# Campo 'No que você está pensando?'
publicar = driver.find_element(By.XPATH, "//p[@class='xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8']")
publicar.click()
sleep(1)


publicar.send_keys('testando auto')
sleep(2)


# Clicar no botão publicar
publicando = driver.find_element(By.XPATH, "//*[text()='Publicar']")
publicando.click()



input('')
driver.close()