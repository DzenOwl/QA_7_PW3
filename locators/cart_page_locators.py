from selenium.webdriver.common.by import By


class CartPageLocators:
    EMPTY_STATE = (By.XPATH, '//p[text()="В корзине ничего нет."]')
    PROMOCODE = (By.XPATH, '//div[@class="coupon-control"]/a')
    PROMO_ENTRY = (By.CSS_SELECTOR, ".coupon-control input")
    PROMO_BUTTON = (By.CSS_SELECTOR, ".coupon-control button")
    PROMO_ERROR = (By.CSS_SELECTOR, ".tooltip-content")