import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption('--language', action='store', help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    chrome_options = ChromeOptions()
    chrome_options.add_argument(f"--lang={language}")
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)

    yield browser

    print("\nquit browser..")
    browser.quit()
