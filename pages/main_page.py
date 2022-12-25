from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators as Locators


class MainPage(BasePage):

    def print_els(self):
        pass

    def print_menu(self):
        # dishes_list = self.elements_are_visible(Locators.DISHES)
        # print(dishes_list)
        self.elements_are_visible(Locators.ELEMENTS)
        # self.elements_are_visible(Locators.BUTTONS_ADD)

        # for i in range(len(elements_list)):
        #     print(f"{i+1}) {elements_list[i].text} rub.")
