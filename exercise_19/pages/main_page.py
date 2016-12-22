from selenium.webdriver.support.wait import WebDriverWait


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get('http://localhost/litecart/')
        return self

    def choose_product(self):
        return self.driver.find_element_by_css_selector('div.content a.link')
