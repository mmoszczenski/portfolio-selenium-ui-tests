from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductsPage(BasePage):

    _ADD_TO_CART_BUTTON = "a.add-to-cart" 
    _VIEW_PRODUCT_BUTTON = (By.CSS_SELECTOR, ".choose a[href^='/product_details/']")
    
    _CONTINUE_SHOPPING_BUTTON = (By.CSS_SELECTOR, "button[data-dismiss='modal']")
    _VIEW_CART_BUTTON = (By.CSS_SELECTOR, "a[href='/view_cart']")
    _MODAL = (By.CLASS_NAME, "modal-content")
    
    _SEARCH_INPUT = (By.ID, "search_product")
    _SUBMIT_SEARCH_BUTTON = (By.ID, "submit_search")
    
    _PRODUCT_NAMES = (By.CSS_SELECTOR, ".single-products")
    
    def add_to_cart_by_id(self, product_id: int):
        selector = f"{self._ADD_TO_CART_BUTTON}[data-product-id='{product_id}']"
        add_button = self.find((By.CSS_SELECTOR, selector))
        add_button.click()
        
    def click_continue_shopping_btn(self):
        self.click(self._CONTINUE_SHOPPING_BUTTON)
        
    def click_view_cart_btn(self):
        self.find(self._MODAL)
        self.click(self._VIEW_CART_BUTTON)
        self.reload_page()
        
    def view_product_button(self, product_id: int):
        return (By.CSS_SELECTOR, f".choose a[href='/product_details/{product_id}']")
        
    def go_to_product_detail_page(self, product_id: int):
        self.remove_ads_banner_if_visible()
        self.click(self.view_product_button(product_id))
        
    def use_search(self, text):
        self.type(self._SEARCH_INPUT, text)
        self.click(self._SUBMIT_SEARCH_BUTTON)
    
    def get_products_name(self):
        products = self.find_all(self._PRODUCT_NAMES)
        return [product.text.strip() for product in products]
    
    def contains_product_with_text(self, text):
        names = self.get_products_name()
        return any(text.lower() in name.lower() for name in names)
        
        