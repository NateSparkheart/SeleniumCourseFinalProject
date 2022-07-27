from .base_page import BasePage
from .locators import LoginPageLocators
import faker


class LoginPage(BasePage):
    def should_be_login_url(self):
        assert "login" in self.url, "Login link is not presented"

    def should_be_login_form(self):
        assert self.browser.find_elements(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.browser.find_elements(*LoginPageLocators.REGISTER_FORM), "Registry form is not presented"

    def register_new_user(self):
        f = faker.Faker()
        email = f.email()
        password = f.password(length=9)
        self.browser.find_element(*LoginPageLocators.EMAIL_TEXTFIELD).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_TEXTFIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRMATION_TEXTFIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()


