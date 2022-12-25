from pages.main_page import MainPage


class TestMainPage:

    def test_main_page(self, driver):
        main_page = MainPage(driver, "https://baranbellini.ru/main")
        main_page.open()
        main_page.print_menu()
