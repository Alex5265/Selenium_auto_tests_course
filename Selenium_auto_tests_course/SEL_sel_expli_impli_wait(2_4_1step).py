from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link = 'http://suninjuly.github.io/explicit_wait2.html'

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def test_wait_100_dolars():
    browser = webdriver.Chrome()
    browser.get(link)

    price_house = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))

    book_btn = browser.find_element(By.ID, 'book').click()

    browser.find_element(By.CLASS_NAME, 'btn').click()

    find_x = browser.find_element(By.ID, 'input_value').text
    answer = calc(find_x)

    browser.find_element(By.ID, 'answer').send_keys(answer)
    browser.find_element(By.ID, 'solve').click()

    time.sleep(20)
    browser.quit()