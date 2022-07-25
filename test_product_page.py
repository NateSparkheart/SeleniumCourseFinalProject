from .pages.product_page import ProductPage
import pytest

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-girl-who-played-with-non-fire_203/"
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




