from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductsPage(BasePage):
    
    _PRODUCT_CONTAINER = ".single-products"
    _ADD_TO_CART_BUTTON = ".add-to-cart"
    
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage(BasePage):

    _ADD_TO_CART_BUTTON = "a.add-to-cart"  # selektor przycisku

    def add_to_cart_by_id(self, product_id: int):
        
        selector = f"{self._ADD_TO_CART_BUTTON}[data-product-id='{product_id}']"
        self.find((By.CSS_SELECTOR, selector)).click()