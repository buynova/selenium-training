import pytest
import time
import random
import string
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_registration(driver):
    driver.get('http://localhost/litecart/')
    driver.find_element_by_css_selector('div#box-account-login a').click()
    email = 'jack' + ''.join(random.choice(string.digits) for i in range(3)) + '@black.com'
    print(email)
    password = 'blackjack'

    form_fields = driver.find_elements_by_css_selector('.content table input')
    form_fields[0].send_keys('666')
    form_fields[1].send_keys('Tenacious D')
    form_fields[2].send_keys('Jack')
    form_fields[3].send_keys('Black')
    form_fields[4].send_keys('Los-Angeles')
    form_fields[6].send_keys('12345')
    form_fields[7].send_keys('Los-Angeles')
    select_country = driver.find_element_by_css_selector('select')
    driver.execute_script("arguments[0].selectedIndex = 224; arguments[0].dispatchEvent(new Event('change'))", select_country)
    form_fields[9].send_keys(email)
    form_fields[10].send_keys('+76661234567')
    form_fields[12].send_keys(password)
    form_fields[13].send_keys(password)

    driver.find_element_by_css_selector('button').click()

    select_zone = driver.find_element_by_xpath('//select[@name="zone_code"]')
    driver.execute_script("arguments[0].selectedIndex = 11; arguments[0].dispatchEvent(new Event('change'))", select_zone)
    driver.find_element_by_xpath('//input[@name="password"]').send_keys(password)
    driver.find_element_by_xpath('//input[@name="confirmed_password"]').send_keys(password)

    driver.find_element_by_css_selector('button').click()
    time.sleep(1)
    logout(driver)

    form_fields = driver.find_elements_by_css_selector('div#box-account-login table input')
    form_fields[0].send_keys(email)
    form_fields[1].send_keys(password)
    driver.find_element_by_xpath('//button[@name="login"]').click()
    time.sleep(1)

    logout(driver)
    time.sleep(1)


def logout(driver):
    links = driver.find_elements_by_css_selector('div#box-account .list-vertical a')
    for link in links:
        if link.text == 'Logout':
            link.click()
