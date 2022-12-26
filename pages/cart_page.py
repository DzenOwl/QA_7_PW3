from selenium.webdriver import ActionChains
from pages.base_page import BasePage
from locators.cart_page_locators import CartPageLocators as Locators
from random import randint

class CartPage(BasePage):
  def locate_empty_state(self):
    self.element_is_visible(Locators.EMPTY_STATE)

  def open_promo(self):
    button = self.element_is_visible(Locators.PROMOCODE)

    action = ActionChains(self.driver)
    action.move_to_element(button).perform()

    self.driver.execute_script(f'document.querySelector(".coupon-control > a").click()')

  def enter_promo(self, text):
    self.scroll_to_bottom()

    inp = self.element_is_located(Locators.PROMO_ENTRY)
    inp.send_keys(text)

    button = self.element_is_located(Locators.PROMO_BUTTON)

    action = ActionChains(self.driver)
    action.click(button).pause(1).perform()

  def locate_promo_error(self):
    self.element_is_visible(Locators.PROMO_ERROR)