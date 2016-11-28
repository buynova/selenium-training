import pytest
import time
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_admin_check_sections(driver):
    driver.get('http://localhost/litecart/')
    time.sleep(2)
    images = driver.find_elements_by_css_selector('li div.image-wrapper')
    i = 0
    while i < len(images):
        sticker = images[i].find_elements_by_css_selector('.sticker')
        if len(sticker) != 1:
            print('The item does not have only 1 sticker!')
            assert False
        i += 1
