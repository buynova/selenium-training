import pytest
import time
from selenium import webdriver


@pytest.fixture
def driver(request):
    # options = webdriver.ChromeOptions()
    # options.add_argument('start-fullscreen')
    # wd = webdriver.Chrome(chrome_options=options)
    wd = webdriver.Firefox(firefox_binary='C:\\Program Files\\Nightly\\firefox.exe')
    # wd = webdriver.Ie()
    # wd = webdriver.Edge()
    # print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://www.youtube.com/")
    driver.find_element_by_name('search_query').send_keys('котики')
    driver.find_element_by_id('search-btn').click()
    time.sleep(1)
