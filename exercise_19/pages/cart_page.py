from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_quantity_of_products(self):
        return self.driver.find_elements_by_css_selector('table td.item')

    def choose_first_item(self):
        return self.driver.find_element_by_css_selector('ul.shortcuts li.shortcut')

    def find_item_in_datatable(self):
        product_name = self.driver.find_element_by_css_selector('li.item p a').text
        return self.driver.find_element_by_xpath('//td[contains(.,"{}")]'.format(product_name))

    def remove_item_from_cart(self):
        self.driver.find_element_by_xpath('//button[@name="remove_cart_item"]').click()
        return self

    def wait_for_datatable_to_refresh(self, deleted_item):
        self.driver.refresh()
        self.wait.until(EC.staleness_of(deleted_item))
        return self
