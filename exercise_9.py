import pytest
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

    countries = []
    i = 0
    while i < len(driver.find_elements_by_css_selector('tr.row')):
        cells = driver.find_elements_by_css_selector('tr.row')[i].find_elements_by_css_selector('tr.row td')
        countries.append(cells[4].get_attribute('textContent'))

        if cells[5].text != '0':
            country_name = cells[4].get_attribute('textContent')
            cells[4].find_element_by_css_selector('a').click()

            zones = []
            j = 1
            country_zones = driver.find_elements_by_css_selector('table#table-zones tr')
            while j < len(country_zones) - 1:
                zone_cells = country_zones[j].find_elements_by_css_selector('td')
                zones.append(zone_cells[2].get_attribute('textContent'))
                j += 1

            if zones != sorted(zones):
                print('Zones of ' + country_name + ' is not sorted')
                assert False

            driver.get('http://localhost/litecart/admin/?app=countries&doc=countries')
        i += 1

    if countries != sorted(countries):
        print('Countries on the page is not sorted')
        assert False


def test_check_sort_geo_zones(driver):
    driver.get('http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones')
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').click()

    i = 0
    while i < len(driver.find_elements_by_css_selector('tr.row')):
        driver.find_elements_by_css_selector('tr.row')[i].find_element_by_css_selector('tr.row td a').click()
        zones = []
        rows = driver.find_elements_by_xpath('//select[contains(@name,"zone_code")]')
        j = 0
        while j < len(rows):
            zones.append(rows[j].find_element_by_xpath('./option[@selected="selected"]').get_attribute('textContent'))
            j += 1

        if zones != sorted(zones):
            print('Geo zones is not sorted')
            assert False

        driver.get('http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones')
        i += 1
