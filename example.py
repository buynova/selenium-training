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
    time.sleep(3)
