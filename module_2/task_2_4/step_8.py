import math
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(value: str) -> str:
    return str(math.log(abs(12 * math.sin(int(value)))))


service: Service = Service(executable_path=ChromeDriverManager().install())
browser: webdriver.Chrome = webdriver.Chrome(service=service)
link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser.get(link)

    price = WebDriverWait(browser, 12, 0.3).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))

    book_btn = browser.find_element(By.ID, 'book')
    book_btn.click()

    x_element: WebElement = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x: str = x_element.text
    y: str = calc(x)

    answer_field: WebElement = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer_field.send_keys(y)

    submit_button = browser.find_element(By.CSS_SELECTOR, "#solve")
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()
