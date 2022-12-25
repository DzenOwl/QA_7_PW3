from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


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

    def elements_are_located(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_located(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_count(self, locator, timeout=5) -> int:
        return len(Wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator)))

    def remove_element(self, css_class: str):
        self.driver.execute_script(
            f'e=document.getElementsByClassName("{css_class}")[0]; e.parentElement.removeChild(e);')

    def get_element_cost(self, element: WebElement) -> int:
        return int(element.get_attribute('textContent').replace(' ', '').replace(' ', '')[:-1])
