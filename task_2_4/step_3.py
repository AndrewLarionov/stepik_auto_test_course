import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager


service: Service = Service(executable_path=ChromeDriverManager().install())
browser: webdriver.Chrome = webdriver.Chrome(service=service)

try:
    browser.get("http://suninjuly.github.io/cats.html")
    button: WebElement = browser.find_element(By.ID, "button")
finally:
    browser.quit()