from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import pytest


class TestForm(unittest.TestCase):

    def setUp(self) -> None:
        self.correct_link = 'http://suninjuly.github.io/registration1.html'
        self.wrong_link = 'http://suninjuly.github.io/registration2.html'
        self.browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    def tearDown(self) -> None:
        self.browser.quit()

    def test_required_fields(self):

        self.browser.get(self.correct_link)

        first_name_field = self.browser.find_element(By.CSS_SELECTOR, '.first_block .first')
        first_name_field.send_keys("Имя")
        last_name_field = self.browser.find_element(By.CSS_SELECTOR, '.first_block .second')
        last_name_field.send_keys("Фамилия")
        email_field = self.browser.find_element(By.CSS_SELECTOR, '.first_block .third')
        email_field.send_keys("Мыло")

        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_required_fields_with_wrong_link(self):
        self.browser.get(self.wrong_link)

        first_name_field = self.browser.find_element(By.CSS_SELECTOR, '.first_block .first')
        first_name_field.send_keys("Имя")
        last_name_field = self.browser.find_element(By.CSS_SELECTOR, '.first_block .second')
        last_name_field.send_keys("Фамилия")
        email_field = self.browser.find_element(By.CSS_SELECTOR, '.first_block .third')
        email_field.send_keys("Мыло")

        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        print(welcome_text)

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == '__main__':
    pytest.main()
