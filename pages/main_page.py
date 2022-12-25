from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators as Locators
import time


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

    def scroll_to_info(self):
        self.scroll_to_first_element_of_class(Locators.FOOTER_LINKS_STR)

    def click_content(self, locator, scroll=False):
        for el in self.elements_located(locator):
            el.click()
            time.sleep(1)
            if scroll:
                self.scroll_to_info()
            time.sleep(1)

    def check_footer_links(self):
        self.scroll_to_info()
        time.sleep(2)
        self.click_content(Locators.FOOTER_LINKS, scroll=True)

    def check_sections(self):
        sections = self.elements_located(Locators.MENU_SECTIONS)
        assert int(len(sections) / 2) == 11

        for i in range((int(len(sections) / 2))):
            el_name = self.driver.execute_script(f"document.getElementsByClassName('{Locators.MENU_SECTIONS_STR}')[{i}]")
            self.driver.execute_script(f"document.getElementsByClassName('{Locators.MENU_SECTIONS_STR}')[{i}].click()")
            header = self.driver.execute_script(f"document.querySelector('h1').innerText")
            assert el_name == header
            # self.driver.execute_script(f"document.getElementsByClassName('{Locators.MENU_SECTIONS_STR}')[{i}].click();")
            time.sleep(1)




