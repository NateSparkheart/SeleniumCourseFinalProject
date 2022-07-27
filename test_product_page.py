from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

import pytest

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.parametrize('offer_num', [*range(7), pytest.param(7, marks=pytest.mark.xfail
    (reason="Некорректное название в сообщении о добавлении в корзину, не чиним")), *range(8,10)])
def test_guest_can_add_product_to_basket(browser, offer_num):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_num}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.product_name_in_added_message_control()
    page.cart_value_control()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.cart_should_be_empty()
    page.empty_cart_text_control()
    page.should_not_be_product_added()


class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/accounts/login/")
        page.open()
        page.register_new_user()
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart()
        page.product_name_in_added_message_control()
        page.cart_value_control()




