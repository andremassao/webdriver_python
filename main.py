import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


def test1():
    service = Service(executable_path='/Users/asuzumura/Downloads/chromedriver-mac-arm64/chromedriver')
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(service=service, options=options)
    browser.get('https://python.org')
    print(browser.title)

    actions = ActionChains(browser)
    wait = WebDriverWait(browser, 5)
    menu_downloads = browser.find_element(By.ID, 'downloads')
    actions.move_to_element(menu_downloads).perform()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="downloads"]/ul/li[3]/a'))).click()

    text_box = browser.find_element(By.ID, 'id-search-field')
    text_box.send_keys('test 123')
    # text_box.send_keys(Keys.RETURN)
    text_box.submit()

    result_message = browser.find_element(By.XPATH, '//*[@id="content"]/div/section/form/ul/p')
    assert result_message.text == 'No results found.'

    time.sleep(3)

    browser.save_screenshot('printscreen.png')

    browser.quit()


def test2():
    assert 1 == 0

