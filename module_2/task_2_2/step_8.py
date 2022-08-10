import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


link: str = 'http://suninjuly.github.io/file_input.html'
browser: webdriver.Chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())

try:

    browser.get(link)

    first_name_field = browser.find_element(By.NAME, 'firstname')
    first_name_field.send_keys('Andrey')

    last_name_field = browser.find_element(By.NAME, 'lastname')
    last_name_field.send_keys('Larionov')

    email_field = browser.find_element(By.NAME, 'email')
    email_field.send_keys('Email')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    print(current_dir)
    file_path = os.path.join(current_dir, 'file.txt')
    print(file_path)

    file_field = browser.find_element(By.NAME, 'file')
    file_field.send_keys(file_path)

    submit_btn = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    submit_btn.click()

finally:

    time.sleep(10)
    browser.quit()
