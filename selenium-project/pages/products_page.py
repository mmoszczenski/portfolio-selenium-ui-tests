from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductsPage(BasePage):

    _ADD_TO_CART_BUTTON = "a.add-to-cart" 
    _VIEW_PRODUCT_BUTTON = (By.CSS_SELECTOR, ".choose a[href^='/product_details/']")
    
    _CONTINUE_SHOPPING_BUTTON = (By.CSS_SELECTOR, "button[data-dismiss='modal']")
    _VIEW_CART_BUTTON = (By.CSS_SELECTOR, "a[href='/view_cart']")
    _MODAL = (By.CLASS_NAME, "modal-content")

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