import pytest
from utils.driver_factory import create_driver
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.sign_up_step_2 import SignUpStep2
from pages.main_page_logged_in import MainPageLoggedIn
from pages.account_created_page import AccountCreatedPage

@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()
    
@pytest.fixture
def pages(driver):
    return {
        "home": HomePage(driver),
        "login": LoginPage(driver),
        "sign_up_step2": SignUpStep2(driver),
        "main_page_logged_in": MainPageLoggedIn(driver),
        "account_created_page": AccountCreatedPage(driver)
    }