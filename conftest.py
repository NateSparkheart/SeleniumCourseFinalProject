import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose your browser: Chrome or Firefox")

    parser.addoption('--language', action='store', default="en",
                     help="Choose language: en, ru ... (etc)")


@pytest.fixture(scope="function")
def browser(request):

    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    if browser_name == "chrome":
        print("\nЗапускаем Хром для теста..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        print("\nЗапускаем Лисичку для теста..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)

    yield browser

    print("\nВыходим из браузера")

    browser.quit()
