import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_name', action = 'store', default = "chrome",
                     help="Выберите браузер: Хром или Лисичка")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nЗапускаем Хром для теста..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nЗапускаем Лисичку для теста..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name либо 'chrome' либо 'firefox'")
    yield browser
    print("\nВыходим из браузера")
    browser.quit()


