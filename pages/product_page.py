from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_cart(self):
        busket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        busket_button.click()

    def product_name_in_added_message_control(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADDED_MESSAGE), "Message is not presented"
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_msg = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_MESSAGE).text
        assert product_name == product_name_in_msg, "Incorrect product name in message"

    def cart_value_control(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_MESSAGE), "Price message is not presented"
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_price_in_msg = self.browser.find_element(*ProductPageLocators.PRICE_MESSAGE).text
        assert product_price in product_price_in_msg, "Incorrect product price in message"


