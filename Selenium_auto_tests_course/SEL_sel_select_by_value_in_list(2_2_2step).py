from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time


link = 'http://suninjuly.github.io/selects1.html'


def test_select_in_list():
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = int(browser.find_element(By.ID, 'num1').text)
    num2 = int(browser.find_element(By.ID, 'num2').text)
    print(num1, num2)
    answer = str(num1 + num2)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(answer)

    browser.find_element(By.CLASS_NAME, 'btn').click()


    time.sleep(10)
    browser.quit()
