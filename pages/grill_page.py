# *- coding: utf-8 -*-
from typing import List

from selenium.webdriver import ActionChains
from pages.base_page import BasePage
from locators.grill_page_locatiors import GrillPageLocators as Locators
from random import randint

class GrillPage(BasePage):

    def check_visible(self):
        self.elements_are_visible(Locators.DISHES)
        self.elements_are_visible(Locators.PRICES)
        self.elements_are_visible(Locators.BUTTONS_ADD)
        self.elements_are_visible(Locators.ELEMENTS)
        self.element_is_visible(Locators.DISHES_COUNTER)

    def dishes_count(self) -> int:
        e = self.element_is_located(Locators.DISHES_COUNTER)
        return int(e.get_attribute('textContent').split(' ')[0])

    def order_sum(self) -> int:
        return self.get_element_cost(self.element_is_located(Locators.ORDER_SUM))

    def dishes_costs(self) -> List[int]:
        return [self.get_element_cost(e) for e in self.elements_are_located(Locators.COSTS)]

    def min_gift_cost(self) -> int:
        return self.get_element_cost(self.element_is_located(Locators.THERMOMETER_GIFT_VALUE))

    def open_gift_frame(self):
        self.remove_element("main-header__content_mobile")
        button = self.element_is_visible(Locators.GIFT_BUTTON)
        ActionChains(self.driver).click(button).perform()
        gifts = self.elements_are_visible(Locators.GIFTS)
        random_gift = gifts[randint(0, len(gifts))]
        gift_id = random_gift.get_attribute("data-product-id")
        ActionChains(self.driver).click(random_gift).perform()
        gift_add_button = self.element_is_visible(Locators.GIFT_ADD_BUTTON)
        ActionChains(self.driver).click(gift_add_button).perform()
        close_menu_button = self.element_is_visible(Locators.CLOSE_GIFTS_MENU)
        ActionChains(self.driver).click(close_menu_button).perform()
        cart_button = self.element_is_visible(Locators.CART_BUTTON)
        ActionChains(self.driver).click(cart_button).perform()
        cart_gifts = self.elements_are_visible(Locators.GIFTS)
        cart_gifts_state = [(g.get_attribute("data-product-id"), g.get_attribute("checked")) for g in cart_gifts]
        for id, check in cart_gifts_state:
            if id == gift_id and check:
                return True
        return False


    def clicked_button(self, index: int, clicks: int):
        buttons = self.elements_are_located(Locators.BUTTONS_ADD)
        action = ActionChains(self.driver)
        action = action.move_to_element(buttons[index])
        for i in range(clicks):
            action = action.click(buttons[index])
        action = action.perform()
        return buttons

    def buttons_click(self):
        self.remove_element("thermometer-container")
        buttons = self.elements_are_located(Locators.BUTTONS_ADD)
        count = len(buttons)
        for i in range(count):
            ActionChains(self.driver).move_to_element(buttons[i]).click(buttons[i]).perform()
        return buttons
