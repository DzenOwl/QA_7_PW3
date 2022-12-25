# *- coding: utf-8 -*-
from pages.grill_page import GrillPage


class TestGrillPage:

    def test_grill_page(self, driver):
        page = GrillPage(driver, "https://baranbellini.ru/grill")
        page.open()
        page.buttons_click()
        dishes_count = page.dishes_counter()
        button_count = page.buttons_count()
        assert dishes_count == button_count
