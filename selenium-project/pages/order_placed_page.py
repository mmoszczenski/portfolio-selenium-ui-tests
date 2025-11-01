from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class OrderPlacedPage(BasePage):
    
    _CONFIRMATION_MESSAGE = (By.CSS_SELECTOR, "h2[data-qa='order-placed']")
    _CONTINUE_BUTTON = (By.CSS_SELECTOR, "a[data-qa='continue-button']")
    
    def is_order_placed_page_displayed(self) -> bool:
        return self.is_visible(self._CONFIRMATION_MESSAGE)
        
    def click_continue_button(self) -> None:
        self.click(self._CONTINUE_BUTTON)
        