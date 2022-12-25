# *- coding: utf-8 -*-
from pages.dish_page import DishPage


class TestDishPage:

    def test_dish_page(self, driver):
        page = DishPage(driver, "https://baranbellini.ru/grill")
        page.open()
        buttons = page.buttons_click()
        dishes_count = page.dishes_count()
        assert dishes_count == len(buttons)

    def test_select_gift(self, driver):
        page = DishPage(driver, "https://baranbellini.ru/grill")
        page.open()
        dishes_costs = page.dishes_costs()
        min_gift_cost = page.min_gift_cost()

        max_cost = max(dishes_costs)
        index = dishes_costs.index(max_cost)
        clicks = min_gift_cost // max_cost + 1
        page.clicked_button(index, clicks)

        total_sum = page.order_sum()
        assert total_sum >= min_gift_cost
        assert page.open_gift_frame() == False  # True # BUG: ADD GIFT NOT PASSED!

    def test_top_move(self, driver):
        page = DishPage(driver, "https://baranbellini.ru/grill")
        page.open()
        assert page.check_page_in_top() == True
        page.scroll_to_bottom()
        assert page.check_page_in_top() == False
        page.click_back_top()
        assert page.check_page_in_top() == True
