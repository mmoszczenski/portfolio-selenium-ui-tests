from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CheckoutPage(BasePage):
    _PLACE_ORDER_BUTTON = (By.CSS_SELECTOR, ".check_out")
    