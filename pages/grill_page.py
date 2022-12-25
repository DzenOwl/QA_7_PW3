# *- coding: utf-8 -*-

from pages.base_page import BasePage
from locators.grill_page_locatiors import GrillPageLocators as Locators


class GrillPage(BasePage):

    def fill_fields_and_submit(self):
        self.elements_are_visible(Locators.DISHES)
        self.elements_are_visible(Locators.PRICES)
        [btn.click() for btn in self.elements_are_visible(Locators.BUTTONS_ADD)]
        self.elements_are_visible(Locators.ELEMENTS)
        self.element_is_visible(Locators.COUNT_DISHES)

    def print_els(self):
        pass

    def print_menu(self):
        # dishes_list = self.elements_are_visible(Locators.DISHES)
        # print(dishes_list)
        self.elements_are_visible(Locators.ELEMENTS)
        # self.elements_are_visible(Locators.BUTTONS_ADD)

        # for i in range(len(elements_list)):
        #     print(f"{i+1}) {elements_list[i].text} rub.")

