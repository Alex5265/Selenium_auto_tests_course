from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

# explicitly fixing the site for less hardcoding (явно фиксируем сайт для возможности изменить в любой момент)
link = "http://suninjuly.github.io/simple_form_find_task.html"
# give variable Chrome - brower
browser = webdriver.Chrome()

browser.get(link)

#try do tests things (пробуем сделать тестовые вещи)
try:

    #find name by TAG and send value
    name_find = browser.find_element(By.TAG_NAME, "input")
    name_find.send_keys("Ivan")
    #find last name and send value
    list_name_find = browser.find_element(By.NAME, "last_name")
    list_name_find.send_keys("Petrov")
    #find city and send value
    city_find = browser.find_element(By.CLASS_NAME, "city")
    city_find.send_keys("Smolensk")
    #find country and send value
    country_find = browser.find_element(By.ID, "country")
    country_find.send_keys("Russia")
    #find button and click
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # vait 30 seconds
    time.sleep(10)
    # clise browser
    browser.quit()

