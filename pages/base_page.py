from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

from locators.base_page_locators import BasePageLocators as Locators


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_top(self):
        self.element_is_visible(Locators.BACK_TO_TOP).click()

    def scroll_to_first_element_of_class(self, locator_class):
        self.driver.execute_script(f"document.getElementsByClassName('{locator_class}')[0].scrollIntoView();")

    def elements_located(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def elements_count(self, locator, timeout=5) -> int:
        return len(Wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator)))

