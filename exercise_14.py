import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_work_with_windows(driver):
    driver.get('http://localhost/litecart/admin/?app=countries&doc=countries')
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').click()
    wait = WebDriverWait(driver, 5)

    driver.find_element_by_css_selector('table.dataTable tr.row a').click()
    main_window = driver.current_window_handle
    existing_windows = driver.window_handles
    table = driver.find_element_by_css_selector('td#content table')
    links = table.find_elements_by_xpath('//tbody/tr/td/a[@target="_blank"]')
    for link in links:
        link.click()
        wait.until(EC.number_of_windows_to_be, 2)  # Ждем, пока не появится второй handle
        new_windows = driver.window_handles
        new_window = list(set(new_windows) - set(existing_windows))[0]
        driver.switch_to_window(new_window)
        driver.close()
        driver.switch_to_window(main_window)
