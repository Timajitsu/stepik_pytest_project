from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):

    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)
        self.current_url = browser.current_url

    def add_item_into_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
            return alert_text
        except NoAlertPresentException:
            print("No second alert presented")
            return None

    def get_item_name(self):
        return self.browser.find_element(*ProductPageLocators.CURRENT_ITEM).text

    def get_item_price(self):
        return self.browser.find_element(*ProductPageLocators.CURRENT_ITEM_PRICE).text

    def item_should_be_added_into_cart(self, current_item):
        item_in_the_cart = self.browser.find_element(*ProductPageLocators.ITEM_IN_THE_CART).text
        assert item_in_the_cart == current_item

    def item_price_should_be_valid(self, current_item_price):
        item_in_the_cart_price = self.browser.find_element(*ProductPageLocators.ITEM_IN_THE_CART_PRICE).text
        assert item_in_the_cart_price == current_item_price
