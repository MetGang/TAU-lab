from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import logging
import time

# ----------------------------------------------------------------

logging.basicConfig(
    encoding = 'utf-8',
    filemode = 'w',
    filename = 'logger.txt',
    format = '%(asctime)s : %(name)s - %(message)s (%(levelname)s)'
)

# ----------------------------------------------------------------

stream = logging.StreamHandler()
stream.setLevel(logging.DEBUG)
stream.setFormatter(logging.Formatter('%(asctime)s : %(name)s - %(message)s (%(levelname)s)'))

# ----------------------------------------------------------------

logger = logging.getLogger('LAB2')
logger.setLevel(logging.INFO)
logger.addHandler(stream)

# ----------------------------------------------------------------

def get_element(driver, by, data):
    return WebDriverWait(driver, 16).until(expected_conditions.presence_of_element_located((by, data)))

def get_elements(driver, by, data):
    return WebDriverWait(driver, 16).until(expected_conditions.presence_of_all_elements_located((by, data)))

# ----------------------------------------------------------------

def test_1(driver):
    logger.info('Test pierwszy')

    driver.maximize_window()

    logger.info('Przechodzę na stronę Vimeo')
    driver.get('https://vimeo.com/')
    logger.info('Jestem na stronie "' + driver.title + '"')

    logger.info('Klikam przycisk otwarcia wyszukiwania')
    try:
        get_elements(driver, By.TAG_NAME, 'button')[0].click()
    except:
        logger.error('Brak przycisku otwarcia wyszukiwania')
        return False

    logger.info('Wprowadzam frazę do szukania')
    try:
        get_elements(driver, By.TAG_NAME, 'input')[0].send_keys('4K')
    except:
        logger.error('Brak pola wprowadzania')
        return False

    logger.info('Klikam przycisk wyszukiwania')
    try:
        get_elements(driver, By.TAG_NAME, 'button')[1].click()
    except:
        logger.error('Brak przycisku wyszukiwania')
        return False

    logger.info('Klikam miniaturkę filmu')
    try:
        get_elements(driver, By.CSS_SELECTOR, 'a[class*=iris_video-vital__overlay]')[0].click()
    except:
        logger.error('Brak miniaturek filmu')
        return False

    logger.info('Klikam przycisk ustawienia rozdzielczości')
    try:
        get_element(driver, By.CSS_SELECTOR, 'button[class*=vp-prefs]').click()
    except:
        logger.error('Brak ustawień rozdzielczości')
        return False

    logger.info('Klikam ikonkę rozdzielczości 4K')
    try:
        get_element(driver, By.CSS_SELECTOR, '[data-time="2160p"').click()
    except:
        logger.error('Brak rozdzielczości 4K')
        return False

    logger.info('Klikam przycisk przejścia w pełen ekran')
    try:
        get_element(driver, By.CSS_SELECTOR, 'button[class=fullscreen').click()
    except:
        logger.error('Brak przycisku pełnego ekranu')
        return False

    time.sleep(5)

    return True

# ---------------------------------------------------------------

def test_2(driver):
    logger.info('Test drugi')

    return True

# ----------------------------------------------------------------

with webdriver.Edge(executable_path = 'msedgedriver.exe') as driver:
    logger.info('Testowanie w Microsoft Edge')
    logger.info('Test 1. zakończony ' + ('sukcesem' if test_1(driver) else 'porażką'))
    logger.info('Test 2. zakończony ' + ('sukcesem' if test_2(driver) else 'porażką'))

# ----------------------------------------------------------------

logger.info('----------------------------------------------------------------')

# ----------------------------------------------------------------

with webdriver.Chrome(executable_path = 'chromedriver.exe') as driver:
    logger.info('Testowanie w Google Chrome')
    logger.info('Test 1. zakończony ' + ('sukcesem' if test_1(driver) else 'porażką'))
    logger.info('Test 2. zakończony ' + ('sukcesem' if test_2(driver) else 'porażką'))

# ----------------------------------------------------------------

logger.info('----------------------------------------------------------------')

# ----------------------------------------------------------------

with webdriver.Firefox(executable_path = 'geckodriver.exe') as driver:
    logger.info('Testowanie w Mozilla Firefox')
    logger.info('Test 1. zakończony ' + ('sukcesem' if test_1(driver) else 'porażką'))
    logger.info('Test 2. zakończony ' + ('sukcesem' if test_2(driver) else 'porażką'))
