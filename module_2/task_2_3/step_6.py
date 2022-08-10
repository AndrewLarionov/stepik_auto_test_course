import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager


def calc(value: str) -> str:
    return str(math.log(abs(12 * math.sin(int(value)))))


link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())

try:
    browser.get(link)

    i_want_to_go_to_a_magical_journey_btn: WebElement = browser.find_element(
        By.CSS_SELECTOR, '.trollface.btn.btn-primary'
    )
    i_want_to_go_to_a_magical_journey_btn.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element: WebElement = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x: str = x_element.text
    y: str = calc(x)

    answer_field: WebElement = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer_field.send_keys(y)

    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()
