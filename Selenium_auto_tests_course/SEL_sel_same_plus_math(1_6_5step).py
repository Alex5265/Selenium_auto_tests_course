from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = "http://suninjuly.github.io/find_link_text"


browser = webdriver.Chrome()
browser.get(link)

try:
    # math calculates the value and clicks
    find_x = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000))).click()

    # find and send name
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    # find and send last name
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    # find and send city
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    # find and send country
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    # find button and click
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    #switch to alert/ take text/ split and print last value
    alert = browser.switch_to.alert
    alert_text = alert.text
    # validate the alert text
    alert.accept()

    print(alert_text.split()[-1])

finally:

    browser.quit()

