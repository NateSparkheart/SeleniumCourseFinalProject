from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def cart_should_be_empty(self):
        assert "basket is empty" in self.browser.find_element(*BasketPageLocators.BASKET_LIST).text , \
             "Cart is not empty"
