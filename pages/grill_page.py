# *- coding: utf-8 -*-
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage
from locators.grill_page_locatiors import GrillPageLocators as Locators


class GrillPage(BasePage):

    def fill_fields_and_submit(self):
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

    def buttons_click(self):
        self.remove_thermometer()
        count = self.buttons_count()
        buttons = self.elements_are_located(Locators.BUTTONS_ADD)
        for i in range(count):
            ActionChains(self.driver).move_to_element(buttons[i]).click(buttons[i]).perform()

    def print_els(self):
        pass

    def print_menu(self):
        # dishes_list = self.elements_are_visible(Locators.DISHES)
        # print(dishes_list)
        self.elements_are_visible(Locators.ELEMENTS)
        # self.elements_are_visible(Locators.BUTTONS_ADD)

        # for i in range(len(elements_list)):
        #     print(f"{i+1}) {elements_list[i].text} rub.")

