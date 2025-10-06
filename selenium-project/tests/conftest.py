import pytest
from utils.driver_factory import create_driver
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.sign_up_step_2 import SignUpStep2
from pages.account_created_page import AccountCreatedPage
from pages.contact_form_page import ContactFormPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.product_details_page import ProductDetailsPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage
from pages.order_placed_page import OrderPlacedPage

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
        "account_created_page": AccountCreatedPage(driver),
        "contact_form": ContactFormPage(driver),
        "products_page": ProductsPage(driver),
        "cart": CartPage(driver),
        "product_details": ProductDetailsPage(driver),
        "checkout": CheckoutPage(driver),
        "payment_page": PaymentPage(driver),
        "order_placed_page": OrderPlacedPage(driver)
    }