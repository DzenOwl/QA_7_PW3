from pages.main_page import MainPage
import time


class TestMainPage:

    # def test_main_page_scroll(self, driver):
    #     main_page = MainPage(driver, "https://baranbellini.ru/main")
    #     main_page.open()
    #     main_page.scroll_to_bottom()
    #     time.sleep(2)
    #     main_page.scroll_to_top()
    #     time.sleep(1)

    def test_main_page_promos(self, driver):
        main_page = MainPage(driver, "https://baranbellini.ru/main")
        main_page.open()
        main_page.scroll_to_promos()
        time.sleep(2)
        main_page.click_promos()
        time.sleep(2)
