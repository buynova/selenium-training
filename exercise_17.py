import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


class MyListener(AbstractEventListener):
    def before_find(self, by, value, driver):
        print(by, value)

    def after_find(self, by, value, driver):
        print(by, value, "found")

    def on_exception(self, exception, driver):
        print(exception)


@pytest.fixture
def driver(request):
    wd = EventFiringWebDriver(webdriver.Chrome(), MyListener())
    request.addfinalizer(wd.quit)
    return wd


def test_browser_logs(driver):
    driver.get('http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1')
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').click()
    wait = WebDriverWait(driver, 5)

    wait.until(EC.presence_of_element_located((By.XPATH, '//a[contains(.,"Duck")]')))
    ducks = driver.find_elements_by_xpath('//a[contains(.,"Duck")]')
    i = 1
    while i < len(ducks):
        ducks[i].click()
        driver.get('http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1')
        ducks = driver.find_elements_by_xpath('//a[contains(.,"Duck")]')
        i += 1

    for l in driver.get_log("browser"):
        print(l)
        if l is None:
            pass
        else:
            print('See browser logs in console')
            assert False
