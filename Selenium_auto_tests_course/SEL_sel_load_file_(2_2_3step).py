from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = 'http://suninjuly.github.io/file_input.html'

def test_load_file_ount_form():
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.NAME, 'firstname').send_keys('Ivan')
    browser.find_element(By.NAME, 'lastname').send_keys('Ivanov')
    browser.find_element(By.NAME, 'email').send_keys('test@test.com')

    btn_path_file = browser.find_element(By.ID, 'file')
    curret_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(curret_dir, 'file.txt')
    btn_path_file.send_keys(file_path)

    browser.find_element(By.CLASS_NAME, 'btn').click()

    time.sleep(10)
    browser.quit()