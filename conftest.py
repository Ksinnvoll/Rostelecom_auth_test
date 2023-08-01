import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(autouse=True)
def driver():
    driver = Service('Selenium/driver/')
    driver = webdriver.Chrome(service=driver)
    driver.maximize_window()
    return driver

@pytest.fixture
def web_browser(request, driver):
    browser = driver
    browser.set_window_size(1400, 1000)

    yield browser

