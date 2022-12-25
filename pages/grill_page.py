# *- coding: utf-8 -*-
from typing import List

from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage
from locators.grill_page_locatiors import GrillPageLocators as Locators


class GrillPage(BasePage):

    def check_visible(self):
        self.elements_are_visible(Locators.DISHES)
        self.elements_are_visible(Locators.PRICES)
        self.elements_are_visible(Locators.BUTTONS_ADD)
        self.elements_are_visible(Locators.ELEMENTS)
        self.element_is_visible(Locators.DISHES_COUNTER)

    def dishes_counter(self) -> int:
        e = self.element_is_located(Locators.DISHES_COUNTER)
        return int(e.get_attribute('textContent').split(' ')[0])

    def buttons_count(self):
        return self.elements_count(Locators.BUTTONS_ADD)

    def remove_thermometer(self):
        self.remove_element("thermometer-container")

    def order_sum(self) -> int:
        return self.get_element_cost(self.element_is_located(Locators.ORDER_SUM))

    def dishes_costs(self) -> List[int]:
        return [self.get_element_cost(e) for e in self.elements_are_located(Locators.COSTS)]

    def min_gift_cost(self) -> int:
        return self.get_element_cost(self.element_is_located(Locators.THERMOMETER_GIFT_VALUE))

    def clicked_button(self, index: int, clicks: int):
        buttons = self.elements_are_located(Locators.BUTTONS_ADD)
        action = ActionChains(self.driver)
        action = action.move_to_element(buttons[index])
        for i in range(clicks):
            action = action.click(buttons[index])
        action = action.perform()

    def buttons_click(self):
        self.remove_thermometer()
        count = self.buttons_count()
        buttons = self.elements_are_located(Locators.BUTTONS_ADD)
        for i in range(count):
            ActionChains(self.driver).move_to_element(buttons[i]).click(buttons[i]).perform()
