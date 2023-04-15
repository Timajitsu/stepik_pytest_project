from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)
        self.current_url = browser.current_url

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_presented(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Invalid page have been opened"

    def should_be_login_form(self):
        assert self.is_element_presented(*MainPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_presented(*MainPageLocators.REGISTERED_FORM), "Registered form is not presented"
