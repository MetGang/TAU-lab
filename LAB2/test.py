from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from msedge.selenium_tools import Edge, EdgeOptions
import logging
import time

# ----------------------------------------------------------------

logging.basicConfig(
    encoding = 'utf-8',
    filemode = 'w',
    filename = 'test.log',
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
    time.sleep(2)
    return WebDriverWait(driver, 16).until(expected_conditions.presence_of_element_located((by, data)))

def get_elements(driver, by, data):
    time.sleep(2)
    return WebDriverWait(driver, 16).until(expected_conditions.presence_of_all_elements_located((by, data)))

# ----------------------------------------------------------------

def test_1a(driver):
    logger.info('Test 1. scenariusz 1.')

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

def test_1b(driver):
    logger.info('Test 1. scenariusz 2.')

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
        get_elements(driver, By.TAG_NAME, 'input')[0].send_keys('vimeo')
    except:
        logger.error('Brak pola wprowadzania')
        return False

    logger.info('Klikam przycisk wyszukiwania')
    try:
        get_elements(driver, By.TAG_NAME, 'button')[1].click()
    except:
        logger.error('Brak przycisku wyszukiwania')
        return False

    logger.info('Klikam kategorię filmów animowanych')
    try:
        get_element(driver, By.CSS_SELECTOR, '[data-value="animation"').click()
    except:
        logger.error('Brak kategorii filmów animowanych')
        return False

    logger.info('Klikam miniaturkę filmu')
    try:
        get_elements(driver, By.CSS_SELECTOR, 'a[class*=iris_video-vital__overlay]')[2].click()
    except:
        logger.error('Brak miniaturek filmu')
        return False

    time.sleep(5)

    return True

# ---------------------------------------------------------------

def test_2a(driver):
    logger.info('Test 2. scenariusz 1.')

    logger.info('Przechodzę na stronę Allegro')
    driver.get('https://allegro.pl/')
    logger.info('Jestem na stronie "' + driver.title + '"')

    logger.info('Zamykam powiedomienie o ciasteczkach')
    try:
        get_element(driver, By.CSS_SELECTOR, 'button[data-role="close-and-accept-consent"]').click()
    except:
        logger.warn('Brak powiadomienia o ciasteczkach')

    logger.info('Wprowadzam frazę do szukania')
    try:
        get_element(driver, By.CSS_SELECTOR, 'input[data-role="search-input"]').send_keys('kostka rubika')
    except:
        logger.error('Brak pola wprowadzania')
        return False

    logger.info('Klikam przycisk wyszukiwania')
    try:
        get_element(driver, By.CSS_SELECTOR, 'button[data-role="search-button"]').click()
    except:
        logger.error('Brak przycisku wyszukiwania')
        return False

    logger.info('Wybieram pierwszą promowaną ofertę')
    try:
        get_elements(driver, By.CSS_SELECTOR, 'a[href*="https://allegro.pl/oferta"][class]')[0].click()
    except:
        logger.error('Brak oferty do wyboru')
        return False

    logger.info('Dodaję wybrany produkt do koszyka')
    try:
        get_element(driver, By.ID, 'add-to-cart-button').click()
    except:
        logger.error('Brak przycisku dodania do koszyka')
        return False

    logger.info('Przechodzę do koszyka')
    try:
        get_element(driver, By.CSS_SELECTOR, 'a[data-analytics-click-label="goToCart"]').click()
    except:
        logger.error('Brak przycisku przejścia do koszyka')
        return False

    logger.info('Klikam przycisk wyboru płatności')
    try:
        get_elements(driver, By.TAG_NAME, 'submit-button')[0].click()
    except:
        logger.error('Brak przycisku wyboru płatności')
        return False

    time.sleep(5)

    return True

# ----------------------------------------------------------------

# https://stackoverflow.com/questions/63800954/i-am-using-microsoft-edge-chromium-with-selenium-and-i-keep-on-getting-the-msedg
# https://docs.microsoft.com/en-us/microsoft-edge/webdriver-chromium?tabs=python

edgeOptions = EdgeOptions()
edgeOptions.use_chromium = True
edgeOptions.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
edgeOptions.add_argument('--headless')
edgeOptions.add_experimental_option('excludeSwitches', [ 'enable-logging' ])

with Edge(options = edgeOptions) as driver:
    driver.maximize_window()
    logger.info('Testowanie w Microsoft Edge')
    logger.info('Test 1. scenariusz 1. zakończony ' + ('sukcesem' if test_1a(driver) else 'porażką'))
    logger.info('Test 1. scenariusz 2. zakończony ' + ('sukcesem' if test_1b(driver) else 'porażką'))
    logger.info('Test 2. scenariusz 1. zakończony ' + ('sukcesem' if test_2a(driver) else 'porażką'))

# ----------------------------------------------------------------

logger.info('----------------------------------------------------------------')

# ----------------------------------------------------------------

with webdriver.Chrome(executable_path = 'chromedriver.exe') as driver:
    driver.maximize_window()
    logger.info('Testowanie w Google Chrome')
    logger.info('Test 1. scenariusz 1. zakończony ' + ('sukcesem' if test_1a(driver) else 'porażką'))
    logger.info('Test 1. scenariusz 2. zakończony ' + ('sukcesem' if test_1b(driver) else 'porażką'))
    logger.info('Test 2. scenariusz 1. zakończony ' + ('sukcesem' if test_2a(driver) else 'porażką'))

# ----------------------------------------------------------------

logger.info('----------------------------------------------------------------')

# ----------------------------------------------------------------

with webdriver.Firefox(executable_path = 'geckodriver.exe') as driver:
    driver.maximize_window()
    logger.info('Testowanie w Mozilla Firefox')
    logger.info('Test 1. scenariusz 1. zakończony ' + ('sukcesem' if test_1a(driver) else 'porażką'))
    logger.info('Test 1. scenariusz 2. zakończony ' + ('sukcesem' if test_1b(driver) else 'porażką'))
    logger.info('Test 2. scenariusz 1. zakończony ' + ('sukcesem' if test_2a(driver) else 'porażką'))
