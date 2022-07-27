from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_TEXTFIELD = (By.CSS_SELECTOR, '#register_form [type="email"]')
    PASSWORD_TEXTFIELD = (By.CSS_SELECTOR, '#register_form [name="registration-password1"]')
    PASSWORD_CONFIRMATION_TEXTFIELD = (By.CSS_SELECTOR, '#register_form [name="registration-password2"]')
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form button")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    PRODUCT_ADDED_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(3)")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main p")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")

class BasketPageLocators():
    BASKET_LIST = (By.CSS_SELECTOR, "#content_inner p")
    PRODUCT_THUMBNAIL = (By.CSS_SELECTOR, ".thumbnail")