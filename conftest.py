import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()  
    yield driver  
    driver.quit()

@pytest.fixture(params=[True, False])
def button_top(request):
    return request.param
