from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def cart_should_be_empty(self):
        rows = self.browser.find_elements(*BasketPageLocators.BASKET_LIST)
        assert len(rows) == 1, "Cart is not empty"

    def empty_cart_text_control(self):
        language = self.browser.execute_script(
            "return window.navigator.userLanguage || window.navigator.language")
        languages = {
            "ar": "سلة التسوق فارغة",
            "ca": "La seva cistella està buida.",
            "cs": "Váš košík je prázdný.",
            "da": "Din indkøbskurv er tom.",
            "de": "Ihr Warenkorb ist leer.",
            "en": "Your basket is empty.",
            "el": "Το καλάθι σας είναι άδειο.",
            "es": "Tu carrito esta vacío.",
            "fi": "Korisi on tyhjä",
            "fr": "Votre panier est vide.",
            "it": "Il tuo carrello è vuoto.",
            "ko": "장바구니가 비었습니다.",
            "nl": "Je winkelmand is leeg",
            "pl": "Twój koszyk jest pusty.",
            "pt": "O carrinho está vazio.",
            "pt-br": "Sua cesta está vazia.",
            "ro": "Cosul tau este gol.",
            "ru": "Ваша корзина пуста",
            "sk": "Váš košík je prázdny",
            "uk": "Ваш кошик пустий.",
            "zh-cn": "Your basket is empty.",
        }

        assert languages.get(language) in self.browser.find_element(*BasketPageLocators.BASKET_LIST).text , \
             "Incorrect empty cart message"

    def should_not_be_product_added(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_THUMBNAIL), \
                "Product was added unintentionally"

