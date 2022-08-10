from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_is_add_btn_on_page(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')

    assert WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.btn-add-to-basket')))