from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    browser.get(link)

    first_name_field = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
    first_name_field.send_keys("Имя")
    last_name_field = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
    last_name_field.send_keys("Фамилия")
    email_field = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
    email_field.send_keys("Мыло")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()