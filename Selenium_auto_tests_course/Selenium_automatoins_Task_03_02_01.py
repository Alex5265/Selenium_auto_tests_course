import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys('Ivan')
        browser.find_element(By.CSS_SELECTOR, '.first_block .second').send_keys("Ivanov")
        browser.find_element(By.CSS_SELECTOR, '.first_block .third').send_keys('test@test.com')

        browser.find_element(By.CSS_SELECTOR, '.second_block .first').send_keys('+79876543210')
        browser.find_element(By.CSS_SELECTOR, '.second_block .second').send_keys("Backer st 228")

        browser.find_element(By.CSS_SELECTOR, '.btn').click()
        text_ends = browser.find_element(By.CSS_SELECTOR, 'h1').text

        self.assertEqual(text_ends, 'Congratulations! You have successfully registered!', "Should be end text congrats")


    def test_abs2(self):
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys('Ivan')
        browser.find_element(By.CSS_SELECTOR, '.first_block .second').send_keys("Ivanov")
        browser.find_element(By.CSS_SELECTOR, '.first_block .third').send_keys('test@test.com')

        browser.find_element(By.CSS_SELECTOR, '.second_block .first').send_keys('+79876543210')
        browser.find_element(By.CSS_SELECTOR, '.second_block .second').send_keys("Backer st 228")

        browser.find_element(By.CSS_SELECTOR, '.btn').click()
        text_ends = browser.find_element(By.CSS_SELECTOR, 'h1').text

        self.assertEqual(text_ends, 'Congratulations! You have successfully registered!', "Should be end text congrats")


if __name__ == "__main__":
    unittest.main()