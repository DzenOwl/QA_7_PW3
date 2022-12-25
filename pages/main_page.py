from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators as Locators


class MainPage(BasePage):

    def fill_fields_and_submit(self):
        self.elements_are_visible(Locators.DISHES)
        self.elements_are_visible(Locators.PRICES)
        self.elements_are_visible(Locators.BUTTONS_ADD)
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

    def click_promos(self):
        self.elements_are_visible(Locators.FOOTER_LINKS)[0].click()

    def scroll_to_promos(self):
        self.scroll_to_first_element_of_class(Locators.FOOTER_LINKS_STR)
        self.print_all_elements(Locators.FOOTER_LINKS)
        # print(self.elements_are_visible(Locators.FOOTER_LINKS)[0].text)
        # print(f"SECTION_TITLE = {title}")



