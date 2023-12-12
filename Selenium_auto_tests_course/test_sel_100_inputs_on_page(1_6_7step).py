from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_find_and_input_100_elements():
    link = "http://suninjuly.github.io/huge_form.html"
    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("единообразное заполнение")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()


test_find_and_input_100_elements()