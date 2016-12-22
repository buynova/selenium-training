from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_to_cart(self):
        self.driver.find_element_by_xpath('//button[@name="add_cart_product"]').click()
        return self

    def wait_for_cart_to_refresh(self, quantity):
        quantity += 1
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div#cart span.quantity'), str(quantity)))
        return quantity

    def choose_size(self):
        select_size = self.driver.find_element_by_xpath("//select[@name='options[Size]']")
        self.driver.execute_script(
            "arguments[0].selectedIndex = 1; arguments[0].dispatchEvent(new Event('change'))", select_size)
        return self

    def go_to_the_cart(self):
        self.driver.find_element_by_partial_link_text('Checkout').click()
        return self
