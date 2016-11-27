import pytest
import time
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_admin_check_sections(driver):
    driver.get('http://localhost/litecart/admin')
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').click()
    # time.sleep(2)
    sections = driver.find_elements_by_css_selector('#box-apps-menu li')
    i = 0
    while i < len(sections):
        menu_apps = driver.find_element_by_css_selector('#box-apps-menu')
        app = menu_apps.find_elements_by_xpath("//li[@id='app-']/a")
        app[i].click()
        time.sleep(1)
        ul = driver.find_elements_by_css_selector('li#app- ul')
        if ul:
            # print(ul[0])
            j = 0
            print(len(driver.find_elements_by_css_selector('#app- li')))
            print(driver.find_elements_by_css_selector('#app- li'))
            while j < len(driver.find_elements_by_css_selector('#app- li')):
                ul1 = driver.find_element_by_css_selector('li#app-')
                ul1.find_elements_by_xpath("./ul/li/a")[j].click()
                time.sleep(2)
                j += 1
        i += 1

    # only main elements
    # sections = driver.find_elements_by_css_selector('#box-apps-menu li')
    # i = 0
    # while i < len(sections):
    #     menu_apps = driver.find_element_by_css_selector('#box-apps-menu')
    #     menu_apps.find_elements_by_xpath("//li[@id='app-']/a")[i].click()
    #     time.sleep(1)
    #     i += 1
