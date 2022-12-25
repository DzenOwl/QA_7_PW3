# *- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class GrillPageLocators:
    DISHES = (By.XPATH, "//div[@class='products-list']")
    PRICES = (By.XPATH, "//div[@class='product-tile__price']")
    BUTTONS_ADD = (By.XPATH, "//div[@class='bttn product-tile__add-btn bttn_primary']")
    ELEMENTS = (By.XPATH, "//div[@class='product-tile__name']")
    COUNT_DISHES = (By.XPATH, ".cart-informer__counter")
