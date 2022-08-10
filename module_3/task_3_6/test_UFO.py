import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import math

answer: str = str(math.log(int(time.time())))


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    service = Service(executable_path=ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestUFO:

    msg = ''
    num_array = ["895", "896", '897', '898', '899', '903', '904', '905']

    @pytest.mark.parametrize('nums', num_array)
    def test_ufo_link(self, browser, nums):
        link = f"https://stepik.org/lesson/236{nums}/step/1"
        browser.get(link)
        browser.implicitly_wait(10)

        text_area = browser.find_element(By.TAG_NAME, "textarea")
        text_area.send_keys(str(math.log(int(time.time()))))

        submit_btn = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.submit-submission')))
        submit_btn.click()

        feedback_elem = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint')))
        feedback_msg = feedback_elem.text
        print(feedback_msg)

        if feedback_msg != 'Correct':
            self.msg += feedback_msg
            print(feedback_msg)