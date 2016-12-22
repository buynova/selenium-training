from selenium import webdriver, common
from selenium.webdriver.support.wait import WebDriverWait
from exercise_19.pages.main_page import MainPage
from exercise_19.pages.product_page import ProductPage
from exercise_19.pages.cart_page import CartPage


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 5)
        self.main_page = MainPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.cart_page = CartPage(self.driver)

    def quit(self):
        self.driver.quit()

    def add_products_to_cart(self, number_of_products):
        quantity = 0
        while quantity < number_of_products:
            self.main_page.open()
            self.main_page.choose_product().click()
            # Обработка исключения, если у товара нельзя выбрать размер
            try:
                self.product_page.choose_size()
            except common.exceptions.NoSuchElementException:
                pass
            self.product_page.add_to_cart()
            self.product_page.wait_for_cart_to_refresh(quantity)

    def remove_products_from_cart(self):
        self.product_page.go_to_the_cart()
        items = self.cart_page.get_quantity_of_products()
        while len(items) > 0:
            if len(items) > 1:  # Выбор первого товара (если всего один - выбора нет)
                self.cart_page.choose_first_item().click()
            item = self.cart_page.find_item_in_datatable()
            self.cart_page.remove_item_from_cart()
            self.cart_page.wait_for_datatable_to_refresh(deleted_item=item)
            items = self.cart_page.get_quantity_of_products()
