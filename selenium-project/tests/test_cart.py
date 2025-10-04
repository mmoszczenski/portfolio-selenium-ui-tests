import time
from pages.products_page import ProductsPage
from pages.home_page import HomePage


class TestCartPositive:
    
    def test_add_single_item_to_cart(self, pages):
        product_page: ProductsPage = pages["products_page"] 
        home_page: HomePage = pages["home"]
        
        home_page.open(home_page.URL)
        home_page.accept_cookies()
        home_page.go_to_products_page()
        
        time.sleep(2)
        product_page.remove_ads_banner_if_visible()
        product_page.add_to_cart_by_id(8)
        product_page.click_view_cart_btn()
        time.sleep(5)
        
    
    def test_add_multiple_items_to_cart(self):
        pass
    
    def test_remove_item_from_cart(self):
        pass
    
    def test_cart_state_after_page_reload(self):
        pass









class TestCartNegative:
    
    def test_add_negative_quantity_item(self):
        pass

