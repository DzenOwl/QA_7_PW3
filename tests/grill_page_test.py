# *- coding: utf-8 -*-
from pages.grill_page import GrillPage


class TestGrillPage:

    def test_main_page(self, driver):
        page = GrillPage(driver, "https://baranbellini.ru/grill")
        page.open()
        # page.print_menu()
        page.fill_fields_and_submit()

