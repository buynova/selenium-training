import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd


def test_check_duck_price(driver):
    driver.get('http://localhost/litecart/')
    duck = driver.find_element_by_css_selector('div#box-campaigns a')
    duck_name = duck.find_element_by_css_selector('div.name').text

    duck_old_price = duck.find_element_by_css_selector('div.price-wrapper .regular-price')
    # получение текста и стилей обычной цены
    duck_old_price_text = duck_old_price.text
    color_duck_old_price = duck_old_price.value_of_css_property('color')
    size_duck_old_price = duck_old_price.value_of_css_property('font-size')
    text_dec_duck_old_price = duck_old_price.value_of_css_property('text-decoration')
    # проверка правильности стилей обычной цены
    check_old_price_css_properties(color_duck_old_price, size_duck_old_price, text_dec_duck_old_price)

    duck_new_price = duck.find_element_by_css_selector('div.price-wrapper .campaign-price')
    # получение текста и стилей новой цены
    duck_new_price_text = duck_new_price.text
    color_duck_new_price = duck_new_price.value_of_css_property('color')
    size_duck_new_price = duck_new_price.value_of_css_property('font-size')
    weight_duck_new_price = duck_new_price.value_of_css_property('font-weight')
    # проверка правильности стилей новой цены
    check_new_price_css_properties(color_duck_new_price, size_duck_new_price, weight_duck_new_price)

    duck.click()
    driver.implicitly_wait(3)

    page_duck_name = driver.find_element_by_css_selector('h1.title')

    page_duck_old_price = driver.find_element_by_css_selector('.content div.price-wrapper .regular-price')
    # получение стилей обычной цены
    color_old_price = page_duck_old_price.value_of_css_property('color')
    size_old_price = page_duck_old_price.value_of_css_property('font-size')
    text_dec_old_price = page_duck_old_price.value_of_css_property('text-decoration')
    # проверка правильности стилей обычной цены
    check_old_price_css_properties(color_old_price, size_old_price, text_dec_old_price)

    page_duck_new_price = driver.find_element_by_css_selector('.content div.price-wrapper .campaign-price')
    # получение стилей новой цены
    color_new_price = page_duck_new_price.value_of_css_property('color')
    size_new_price = page_duck_new_price.value_of_css_property('font-size')
    weight_new_price = page_duck_new_price.value_of_css_property('font-weight')
    # проверка правильности стилей новой цены
    check_new_price_css_properties(color_new_price, size_new_price, weight_new_price)

    if duck_name != page_duck_name.text:
        print('Item name from main page is not equal item name from current page.')
        assert False
    elif duck_old_price_text != page_duck_old_price.text:
        print('Item price from main page is not equal item price from current page.')
        assert False
    elif duck_new_price_text != page_duck_new_price.text:
        print('Item campaign price from main page is not equal item campaign price from current page.')
        assert False


def check_old_price_css_properties(color, size, text_decoration):
    """Проверка свойств css для обычной (старой) цены.

    Args:
        color: цвет текста (проверка на отсутствие).
        size: размер текста.
        text_decoration: декорирование текста.
    """
    if color == '' or (size != '16px' and size != '14.4px') or text_decoration != 'line-through':
        print('Style properties of regular price is not correct')
        assert False


def check_new_price_css_properties(color, size, weight):
    """Проверка свойств css для новой цены.

    Args:
        color: цвет текста (проверка на отсутствие).
        size: размер текста.
        weight: "вес" текста.
    """
    if color == '' or (size != '22px' and size != '18px') or weight == '':
        print('Style properties of campaign price is not correct')
        assert False
