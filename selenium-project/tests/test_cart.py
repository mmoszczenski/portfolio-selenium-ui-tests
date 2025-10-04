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
        
        product_page.remove_ads_banner_if_visible()
        product_page.add_to_cart_by_id(product_id)
        product_page.click_view_cart_btn()

        actual_name = cart_page.product_name(product_id)
        actual_total = cart_page.product_total(product_id)
        
        assert cart_page.is_cart_page_displayed(), "Cart page not displayed"
        assert expected_name == actual_name, "Product name differs"
        assert expected_total == actual_total, "Total value is incorrect"
        
    
    def test_add_multiple_items_to_cart(self, pages):
        
        product_page: ProductsPage = pages["products_page"] 
        home_page: HomePage = pages["home"]
        cart_page: CartPage = pages["cart"]
    
        product_ids = [1, 6]
        product_1 = PRODUCTS[product_ids[0]]
        product_2 = PRODUCTS[product_ids[1]]
        
        expected_total = product_1["price"] + product_2["price"]
        
        home_page.open(home_page.URL)
        home_page.accept_cookies()
        home_page.go_to_products_page()
        
        product_page.remove_ads_banner_if_visible()
        product_page.add_to_cart_by_id(product_ids[0])
        product_page.click_continue_shopping_btn()
        product_page.add_to_cart_by_id(product_ids[1])
        product_page.click_view_cart_btn()
        
        actual_total = cart_page.product_total(product_ids[0]) + cart_page.product_total(product_ids[1])

        assert cart_page.is_cart_page_displayed(), "Cart page not displayed"
        assert expected_total == actual_total, "Expected total is differen than actual total"        
        
    
    
    def test_remove_item_from_cart(self):
        pass
    
    def test_add_to_cart_from_various_pages(self):
        pass






class TestCartNegative:
    
    def test_add_negative_quantity_item(self):
        pass

