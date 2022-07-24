from .pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

def test_login_url_is_correct(browser):
    page = LoginPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.should_be_login_url()  # выполняем метод страницы

def test_guest_can_see_login_form(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()

def test_guest_can_see_register_form(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()
