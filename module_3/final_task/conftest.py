import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="spanish")


@pytest.fixture()
def chrome_options(request) -> Options:
    language: str = request.config.getoption('language')
    options: Options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})

    return options


@pytest.fixture()
def browser(chrome_options: Options) -> None:
    service = Service(executable_path=ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=chrome_options)
    yield browser

    time.sleep(10)
    browser.quit()