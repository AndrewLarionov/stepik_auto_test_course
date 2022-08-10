import time

from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


def calc(num_1: str, num_2: str) -> str:
    return str(int(num_1) + int(num_2))


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser: webdriver.Chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    browser.get(link)

    num1: str = browser.find_element(By.CSS_SELECTOR, '#num1').text
    num2: str = browser.find_element(By.CSS_SELECTOR, '#num2').text

    answer: str = calc(num_1=num1, num_2=num2)
    print(answer)

    num_select = Select(browser.find_element(By.CSS_SELECTOR, ".custom-select"))
    num_select.select_by_value(answer)

    submit_btn: WebElement = browser.find_element(By.CSS_SELECTOR, '.btn-default.btn')
    submit_btn.click()

    time.sleep(5)

finally:
    time.sleep(10)
    browser.quit()
