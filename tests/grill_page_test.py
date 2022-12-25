# *- coding: utf-8 -*-
from pages.grill_page import GrillPage


class TestGrillPage:

    def test_grill_page(self, driver):
        page = GrillPage(driver, "https://baranbellini.ru/grill")
        page.open()
        buttons = page.buttons_click()
        dishes_count = page.dishes_count()
        assert dishes_count == len(buttons)

    def test_select_gift(self, driver):
        page = GrillPage(driver, "https://baranbellini.ru/grill")
        page.open()
        dishes_costs = page.dishes_costs()
        min_gift_cost = page.min_gift_cost()

        max_cost = max(dishes_costs)
        index = dishes_costs.index(max_cost)
        clicks = min_gift_cost // max_cost + 1
        page.clicked_button(index, clicks)

        total_sum = page.order_sum()
        assert total_sum >= min_gift_cost

