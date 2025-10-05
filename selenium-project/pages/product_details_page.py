from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductDetailsPage(BasePage):
    
    _QUANTITY_FIELD = (By.ID, "quantity")
    _ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn.cart")
    
    def change_quantity(self, quantity: int):
        quantity_input= self.find(self._QUANTITY_FIELD)
        quantity_input.clear()
        quantity_input.send_keys(quantity)
        
    def add_product_to_cart(self):
        self.click(self._ADD_TO_CART_BUTTON)