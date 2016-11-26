import pytest
import time
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome('C:\Tools\chromedriver.exe')
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://www.youtube.com/")
    driver.find_element_by_name('search_query').send_keys('котики')
    driver.find_element_by_id('search-btn').click()
    time.sleep(3)
