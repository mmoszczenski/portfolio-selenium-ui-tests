import pytest
from utils.driver_factory import create_driver
from pages.home_page import HomePage

@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()
