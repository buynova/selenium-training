import pytest
import time
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_check_sort_countries(driver):
    driver.get('http://localhost/litecart/admin/?app=countries&doc=countries')
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').click()
    time.sleep(2)

    rows = driver.find_elements_by_css_selector('tr.row td')
    countries = []
    for row in rows:
        if row.get_attribute('cellIndex') == '4':
            countries.append(row.get_attribute('textContent'))
        if row.get_attribute('cellIndex') == '5' and row.text != '0':
            row.find_element_by_css_selector('a').click()
            time.sleep(10)
    if countries != sorted(countries):
        print('Countries on the page is not sorted')
        assert False
    # rows1 = driver.find_elements_by_css_selector('tr.row td')
    # for row1 in rows1:
    #     if row1.get_attribute('cellIndex') == '5' and row1.text != '0':
    #         print('wow')
