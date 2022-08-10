import time
import math

from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


def calc(value: str) -> str:
    return str(math.log(abs(12 * math.sin(int(value)))))


try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser: webdriver.Chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    browser.get(link)

    x: str = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    y: str = calc(x)

    answer_field: WebElement = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer_field.send_keys(y)

    i_am_the_robot_checkbox: WebElement = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true);", i_am_the_robot_checkbox)
    i_am_the_robot_checkbox.click()

    robots_rule_radiobutton: WebElement = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", robots_rule_radiobutton)
    robots_rule_radiobutton.click()

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


    time.sleep(5)

finally:
    time.sleep(10)
    browser.quit()