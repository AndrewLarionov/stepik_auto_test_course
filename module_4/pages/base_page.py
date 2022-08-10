from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class BasePage:

    def __init__(self, browser: webdriver.Chrome, url: str, timeout: int = 10) -> None:
        self.browser: webdriver.Chrome = browser
        self.url: str = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False

        return True