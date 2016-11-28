import pytest
from selenium import webdriver, common


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

    menu_sections = driver.find_elements_by_css_selector('#box-apps-menu li')
    i = 0
    while i < len(menu_sections):
        driver.find_elements_by_xpath("//li[@id='app-']/a")[i].click()
        driver.find_element_by_css_selector('td#content h1')

        try:
            driver.find_element_by_css_selector('li#app- ul')
        except common.exceptions.NoSuchElementException:
            pass
        else:
            pass
            section_items = driver.find_elements_by_css_selector('#app- li')
            j = 0
            while j < len(section_items):
                driver.find_elements_by_css_selector('#app- li a')[j].click()
                driver.find_element_by_css_selector('td#content h1')
                j += 1
        i += 1
