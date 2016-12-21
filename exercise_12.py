import pytest
import os
import random
import string
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_add_catalog_item(driver):
    driver.get('http://localhost/litecart/admin/')
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').click()

    driver.find_elements_by_xpath("//li[@id='app-']/a")[1].click()
    buttons = driver.find_elements_by_css_selector("td#content a.button")
    for button in buttons:
        if button.text == 'Add New Product':
            button.click()

    tabs = driver.find_elements_by_css_selector('div.tabs li a')
    # Создаем рандомный номер, чтобы товары не повторялись
    item_number = ''.join(random.choice(string.digits) for i in range(3))
    item_name = 'Rubber Chick ' + item_number

    general_inputs = driver.find_elements_by_css_selector('div#tab-general input')
    general_inputs[0].click()
    general_inputs[2].send_keys(item_name)
    general_inputs[3].send_keys('rc' + item_number)
    general_inputs[9].click()
    general_inputs[10].clear()
    general_inputs[10].send_keys('5')
    general_inputs[11].send_keys(os.getcwd() + '\chicken.jpg')
    general_inputs[12].send_keys('22.12.2016')
    general_inputs[13].send_keys('22.12.2019')

    # Переход во вкладку Information
    tabs[1].click()

    select_man = driver.find_element_by_xpath("//select[@name='manufacturer_id']")
    driver.execute_script("arguments[0].selectedIndex = 1; arguments[0].dispatchEvent(new Event('change'))", select_man)
    info_inputs = driver.find_elements_by_css_selector('div#tab-information input')
    info_inputs[0].send_keys('chicken, toy, rubber')
    info_inputs[1].send_keys('Rubber chicken')
    info_inputs[2].send_keys(item_name)
    info_inputs[3].send_keys('Custom chicken')
    driver.find_element_by_css_selector('div.trumbowyg-editor')\
        .send_keys('This is a description of the amazing rubber chicken! Weee!')

    # Переход во вкладку Prices
    tabs[3].click()

    prices_inputs = driver.find_elements_by_css_selector('div#tab-prices input')
    prices_inputs[0].clear()
    prices_inputs[0].send_keys('5')
    prices_inputs[1].clear()
    prices_inputs[1].send_keys('5')
    select_currency = driver.find_element_by_xpath("//select[@name='purchase_price_currency_code']")
    driver.execute_script("arguments[0].selectedIndex = 1; arguments[0].dispatchEvent(new Event('change'))",
                          select_currency)

    button_set = driver.find_element_by_css_selector('p span.button-set')
    button_set.find_element_by_xpath('//button[@value="Save"]').click()

    # Проверка наличия товара: клик по элементу с нужным именем и проверка заголовка страницы
    catalog_links = driver.find_elements_by_css_selector('table.dataTable tr.row a')
    for link in catalog_links:
        if link.text == item_name:
            link.click()
            break
    if driver.find_element_by_tag_name('h1').text != 'Edit Product: {}'.format(item_name):
        print('Product page is not about {}'.format(item_name))
        assert False
