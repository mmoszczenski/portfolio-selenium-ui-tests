import time
from pages.products_page import ProductsPage
from pages.home_page import HomePage
from pages.cart_page import CartPage
from test_data.product_data import PRODUCTS

class TestCartPositive:
    
    def test_add_single_item_to_cart(self, pages):
        product_page: ProductsPage = pages["products_page"] 
        home_page: HomePage = pages["home"]
        cart_page: CartPage = pages["cart"]
        
        product_id = 1
        product = PRODUCTS[product_id]
        expected_name = product["name"]
        expected_total = product["price"]       
         
        home_page.open(home_page.URL)
        home_page.accept_cookies()
        home_page.go_to_products_page()
        
        time.sleep(2)
        product_page.remove_ads_banner_if_visible()
        product_page.add_to_cart_by_id(1)
        time.sleep(2)
        product_page.click_view_cart_btn()
        time.sleep(2)
        
        actual_name = cart_page.product_name(product_id)
        actual_total = cart_page.product_total(product_id)
        
        assert expected_name == actual_name, "Product name differs"
        assert expected_total == actual_total, "Total value is incorrect"
        
    
        
    
    def test_add_multiple_items_to_cart(self):
        pass
    
    def test_remove_item_from_cart(self):
        pass
    
    def test_cart_state_after_page_reload(self):
        pass









class TestCartNegative:
    
    def test_add_negative_quantity_item(self):
        pass

