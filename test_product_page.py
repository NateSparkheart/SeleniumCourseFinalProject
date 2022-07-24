from .pages.product_page import ProductPage
import pytest

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




