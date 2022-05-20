import pytest
from selenium import webdriver
from Config.config import TestData


@pytest.fixture(params=["chrome"], scope='class')
def browser():
    driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
    driver.set_window_size(1400, 1000)
    yield driver
    driver.quit()
