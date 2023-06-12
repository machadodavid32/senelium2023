from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep
from selenium.webdriver.support import expected_conditions as condicao_esperada


# Documentação exceções selenium: https://selenium-python.readthedocs.io/api.html#module-selenium.common.exceptions

# Iniciar o webdriver


def iniciar_driver():
    chrome_options = Options()

    arguments = ['--lang=en-US', '--window-size=1300,1000',
                 '--incognito']

    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1

    })

    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)
    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException,
        ]
    )
    return driver, wait


driver, wait = iniciar_driver()
driver.get('https://google.com/flights')

sugestoes_de_voo = wait.until(condicao_esperada.visibility_of_all_elements_located(
    (By.XPATH, "//div[@class='wIuJz']")))

# sugestoes_de_voo = wait.until(condicao_esperada.visibility_of_any_elements_located(
#     (By.XPATH, "//div[@class='wIuJz']")))

sugestoes_de_voo[0].click()


sleep(5)

driver.get('https://cursoautomacao.netlify.app/login')

campo_email = wait.until(condicao_esperada.element_to_be_clickable(
    (By.XPATH, "//input[@id='email']")))

campo_email.send_keys('jhonatan@hotmail.com')

# sugestoes_de_voo = driver.find_elements(By.XPATH, "//div[@class='wIuJz]")

input('')
driver.close()