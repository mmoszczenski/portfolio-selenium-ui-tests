from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CheckoutPage(BasePage):
    _PLACE_ORDER_BUTTON = (By.CSS_SELECTOR, ".check_out")
    
    
    def is_checkout_page_displayed(self) -> bool:
        return self.is_visible(self._PLACE_ORDER_BUTTON)
    
    def click_place_order_button(self) -> None:
        self.click(self._PLACE_ORDER_BUTTON)
        