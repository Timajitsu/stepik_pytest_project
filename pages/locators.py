from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTERED_FORM = (By.ID, 'register_form')


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    CURRENT_ITEM = (By.CSS_SELECTOR, 'div h1')
    CURRENT_ITEM_PRICE = (By.CSS_SELECTOR, 'div p.price_color')
    ITEM_IN_THE_CART = (By.CSS_SELECTOR, '#messages > div:nth-child(1) strong')
    ITEM_IN_THE_CART_PRICE = (By.CSS_SELECTOR, 'div.alert-info  strong')
