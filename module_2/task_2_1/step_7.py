from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager


def calc(value: str) -> str:
    return str(math.log(abs(12 * math.sin(int(value)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser: webdriver.Chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    browser.get(link)

    treasure_img: WebElement = browser.find_element(By.CSS_SELECTOR, '#treasure')
    x: str = treasure_img.get_attribute('valuex')
    y: str = calc(x)

    answer_field: WebElement = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer_field.send_keys(y)

    i_am_the_robot_checkbox: WebElement = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    i_am_the_robot_checkbox.click()

    robots_rule_radiobutton: WebElement = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    robots_rule_radiobutton.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn-default")
    submit_button.click()

    time.sleep(5)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()