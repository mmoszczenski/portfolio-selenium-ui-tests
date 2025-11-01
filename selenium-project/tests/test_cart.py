import time
import pytest
from pages.products_page import ProductsPage
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.product_details_page import ProductDetailsPage
from test_data.product_data import PRODUCTS

class TestCartPositive:
    
    def test_add_single_item_to_cart(self, pages):
        
        products_page: ProductsPage = pages["products_page"] 
        home_page: HomePage = pages["home"]
        cart_page: CartPage = pages["cart"]
        
        product_id = 1
        product = PRODUCTS[product_id]
        
        expected_name = product["name"]
        expected_total = product["price"]       
         
        home_page.open_homepage()
        home_page.go_to_products_page()
        
        products_page.remove_ads_banner_if_visible()
        products_page.add_to_cart_by_id(product_id)
        products_page.click_view_cart_btn()

        actual_name = cart_page.product_name(product_id)
        actual_total = cart_page.product_total(product_id)
        
        assert cart_page.is_cart_page_displayed(), "Cart page not displayed"
        assert cart_page.products_count() == 1, "Product count is incorrect"
        assert expected_name == actual_name, "Product name differs"
        assert expected_total == actual_total, "Total value is incorrect"
        
    
    def test_add_multiple_items_to_cart(self, pages):
        
        products_page: ProductsPage = pages["products_page"] 
        home_page: HomePage = pages["home"]
        cart_page: CartPage = pages["cart"]
    
        product_ids = [1, 6]
        product_1 = PRODUCTS[product_ids[0]]
        product_2 = PRODUCTS[product_ids[1]]
        
        expected_total = product_1["price"] + product_2["price"]
        
        home_page.open_homepage()
        home_page.go_to_products_page()
        
        products_page.remove_ads_banner_if_visible()
        products_page.add_to_cart_by_id(product_ids[0])
        products_page.click_continue_shopping_btn()
        products_page.add_to_cart_by_id(product_ids[1])
        products_page.click_view_cart_btn()
        
        actual_total = cart_page.product_total(product_ids[0]) + cart_page.product_total(product_ids[1])

        assert cart_page.is_cart_page_displayed(), "Cart page not displayed"
        assert expected_total == actual_total, "Expected total is different than actual total"     
        assert cart_page.products_count() == 2, "Product count is incorrect"   
        

    def test_remove_item_from_cart(self, pages):
    
        products_page: ProductsPage = pages["products_page"] 
        home_page: HomePage = pages["home"]
        cart_page: CartPage = pages["cart"]
    
        product_ids = [1, 6]
        product_1 = PRODUCTS[product_ids[0]]
        product_2 = PRODUCTS[product_ids[1]]
        
        expected_total = product_1["price"]
        
        home_page.open_homepage()
        home_page.go_to_products_page()
        
        products_page.remove_ads_banner_if_visible()
        products_page.add_to_cart_by_id(product_ids[0])
        products_page.click_continue_shopping_btn()
        products_page.add_to_cart_by_id(product_ids[1])
        products_page.click_view_cart_btn()
        
        cart_page.remove_product(product_ids[1])
        cart_page.wait_for_cart_items_count_to_be(1)
        
        actual_total = cart_page.product_total(product_ids[0])
        
        assert expected_total == actual_total
        assert cart_page.products_count() == 1, "Product count is incorrect"
    
    
    def test_add_to_cart_from_various_pages(self):
        pass






class TestCartNegative:
    
    @pytest.mark.xfail(reason="This is a known bug in the app")
    def test_add_negative_quantity_item(self, pages):
        
        home_page: HomePage = pages["home"]
        product_details: ProductDetailsPage = pages ["product_details"]
        products_page: ProductsPage = pages["products_page"] 
        
        product_id = 1
        product = PRODUCTS[product_id]
        
        home_page.open_homepage()
        home_page.go_to_products_page()
        
        products_page.go_to_product_detail_page(product_id)
        
        product_details.change_quantity(-5)
        product_details.add_product_to_cart()

        assert not product_details.is_success_modal_displayed(), "Success modal is displayed despite negative product quantity"

