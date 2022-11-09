from typing import Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestItems:

    BASE_PAGE: str = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    ADD_TO_BASKET_BTN: Tuple = (By.CLASS_NAME, "btn-add-to-basket")

    def test_items(self, my_browser):
        my_browser.get(self.BASE_PAGE)
        assert WebDriverWait(my_browser, 5).until(ec.element_to_be_clickable(self.ADD_TO_BASKET_BTN))
