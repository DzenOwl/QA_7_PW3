from pages.cart_page import CartPage
from pages.dish_page import DishPage


class TestCartPage:
  def test_empty_state(self, driver):
    page = CartPage(driver, "https://baranbellini.ru/cart")
    page.open()
    page.locate_empty_state()

  def test_promo(self, driver):
    page = DishPage(driver, "https://baranbellini.ru/grill")
    page.open()
    page.buttons_click(count=1)

    page = CartPage(driver, "https://baranbellini.ru/cart")
    page.open()
    page.open_promo()
    page.enter_promo("hello")
    page.locate_promo_error()
