from selenium.webdriver.common.by import By


class MainPageLocators:
    DISHES = (By.XPATH, "//div[@class='products-list']")
    PRICES = (By.XPATH, "//div[@class='product-tile__price']")
    BUTTONS_ADD = (By.XPATH, "//div[@class='bttn product-tile__add-btn']")
    ELEMENTS = (By.XPATH, "//div[@class='product-tile__name']")
    COUNT_DISHES = (By.XPATH, ".cart-informer__counter")
    FOOTER_LINKS_STR = "bottom-nav__item"
    FOOTER_LINKS = (By.XPATH, f"//a[@class='{FOOTER_LINKS_STR}']")
    SECTION_TITLE = (By.XPATH, ".content-title")
    MENU_SECTIONS_STR = "top-nav__item"
    MENU_SECTIONS = (By.CSS_SELECTOR, f".{MENU_SECTIONS_STR}")
