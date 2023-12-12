from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/alert_accept.html'

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def test_alert_brwsr_click():
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CLASS_NAME, 'btn').click()

    show_up_alert = browser.switch_to.alert
    show_up_alert.accept()

    find_x = browser.find_element(By.ID, 'input_value').text
    answer = calc(find_x)

    browser.find_element(By.ID, 'answer').send_keys(answer)
    browser.find_element(By.CLASS_NAME, 'btn').click()


    time.sleep(10)
    browser.quit()