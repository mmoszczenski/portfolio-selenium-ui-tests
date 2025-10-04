from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductsPage(BasePage):
    
    _PRODUCT_CONTAINER = ".single-products"
    _ADD_TO_CART_BUTTON = ".add-to-cart"
    
    def add_to_cart_by_id(self, product_id):
        selector = f"{self._PRODUCT_CONTAINER}[data-product-id='{product_id}'] {self._ADD_TO_CART_BUTTON}"
        add_btn = self.driver.find_element(By.CSS_SELECTOR, selector)
        add_btn.click()
        