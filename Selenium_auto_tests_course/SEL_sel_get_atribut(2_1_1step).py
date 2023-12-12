import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = 'http://suninjuly.github.io/get_attribute.html'

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def test_witch_get_att():
    browser = webdriver.Chrome()
    browser.get(link)

    chest = browser.find_element(By.ID, 'treasure')
    x = chest.get_attribute('valuex')
    answer = calc(x)

    browser.find_element(By.ID, 'answer').send_keys(answer)
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()

    browser.find_element(By.CLASS_NAME, 'btn').click()

    time.sleep(10)
    browser.quit()
