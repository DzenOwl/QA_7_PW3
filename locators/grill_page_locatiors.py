# *- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class GrillPageLocators:
    DISHES = (By.XPATH, "//div[@class='products-list']")
    PRICES = (By.XPATH, "//div[@class='product-tile__price']")
    BUTTONS_ADD = (By.CSS_SELECTOR, ".bttn.product-tile__add-btn")
    ELEMENTS = (By.XPATH, "//div[@class='product-tile__name']")
    COUNT_DISHES = (By.CSS_SELECTOR, ".cart-informer__counter")
