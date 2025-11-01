from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductDetailsPage(BasePage):
    
    _QUANTITY_FIELD = (By.ID, "quantity")
    _ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn.cart")
    
    _MODAL = (By.CLASS_NAME, "modal-content")
    _VIEW_CART_BUTTON = (By.CSS_SELECTOR, "a[href='/view_cart']")
    
    def change_quantity(self, quantity: int) -> None:
        quantity_input = self.find(self._QUANTITY_FIELD)
        quantity_input.clear()
        quantity_input.send_keys(quantity)
        
    def add_product_to_cart(self) -> None:
        self.click(self._ADD_TO_CART_BUTTON)
        
    def is_success_modal_displayed(self) -> bool:
        return self.is_visible(self._MODAL)
    
    def click_view_cart_button(self) -> None:
        self.find(self._MODAL)
        self.click(self._VIEW_CART_BUTTON)
        self.reload_page()
        