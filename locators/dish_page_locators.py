# *- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class DishPageLocators:
    DISHES = (By.XPATH, "//div[@class='products-list']")
    PRICES = (By.XPATH, "//div[@class='product-tile__price']")
    BUTTONS_ADD = (By.CSS_SELECTOR, ".bttn.product-tile__add-btn")
    ELEMENTS = (By.XPATH, "//div[@class='product-tile__name']")
    DISHES_COUNTER = (By.CSS_SELECTOR, ".cart-informer__counter")
    ORDER_SUM = (By.CSS_SELECTOR, ".cart-informer__total")
    THERMOMETER = (By.CSS_SELECTOR, ".thermometer-container")
    COSTS = (By.CSS_SELECTOR, ".product-tile__price")
    THERMOMETER_GIFT_VALUE = (By.CSS_SELECTOR, ".thermometer-scale-container__mark")
    GIFT_BUTTON = (By.CSS_SELECTOR, ".thermometer-button-container__gifts-popup-button")
    DISH_DETAIL_BUTTON = (By.CSS_SELECTOR, ".bttn.product-detail__add-btn.bttn_bigger")
    GIFTS = (By.CSS_SELECTOR, ".product-tile_small:not(.product-tile_placeholder)")
    GIFT_ADD_BUTTON = (By.CSS_SELECTOR, ".bttn.product-detail__add-btn.bttn_bigger")
    CLOSE_GIFTS_MENU = (By.CSS_SELECTOR, ".button.modal__close")
    CART_BUTTON = (By.CSS_SELECTOR, ".cart-informer__button.bttn")
    MOBILE_BLOCK = (By.CSS_SELECTOR, ".main-header__content_mobile")
