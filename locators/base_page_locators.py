from selenium.webdriver.common.by import By


class BasePageLocators:
    BACK_TO_TOP = (By.XPATH, "//div[@class='back-top']")
    CART_COUNT = (By.XPATH, "cart-informer__counter")
    CART_TOTAL = (By.XPATH, "cart-informer__total")
    CART_BUTTON = (By.XPATH, "cart-informer__button")
