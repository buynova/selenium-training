import pytest
from selenium import webdriver, common
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_cart(driver):
    wait = WebDriverWait(driver, 5)
    quantity = 0
    # Добавление трех товаров в корзину
    while quantity < 3:
        driver.get('http://localhost/litecart/')
        driver.find_element_by_css_selector('div.content a.link').click()

        # Обработка исключения, если у товара нельзя выбрать размер
        try:
            select_size = driver.find_element_by_xpath("//select[@name='options[Size]']")
            driver.execute_script("arguments[0].selectedIndex = 1; arguments[0].dispatchEvent(new Event('change'))",
                                  select_size)
        except common.exceptions.NoSuchElementException:
            pass

        driver.find_element_by_xpath('//button[@name="add_cart_product"]').click()
        quantity += 1
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div#cart span.quantity'), str(quantity)))
    # Переход в корзину
    driver.find_element_by_partial_link_text('Checkout').click()

    # Считаем количество строк в корзине (их можеь быть меньше трех, если товары повторяются)
    items = driver.find_elements_by_css_selector('table td.item')
    while len(items) > 0:
        if len(items) > 1:  # Выбор первого товара (если всего один - выбора нет)
            driver.find_element_by_css_selector('ul.shortcuts li.shortcut').click()
        item_name = driver.find_element_by_css_selector('li.item p a').text  # Получаем наименование товара
        item = driver.find_element_by_xpath('//td[contains(.,"{}")]'.format(item_name))  # Находим товар в таблице
        driver.find_element_by_xpath('//button[@name="remove_cart_item"]').click()
        driver.refresh()
        wait.until(EC.staleness_of(item))
        items = driver.find_elements_by_css_selector('table td.item')
