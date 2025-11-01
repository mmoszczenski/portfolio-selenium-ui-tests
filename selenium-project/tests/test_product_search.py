from pages.home_page import HomePage
from pages.products_page import ProductsPage


class TestProductSearch:
    
    def test_correct_product_search(self, pages):
        
        home_page: HomePage = pages["home"]
        products_page: ProductsPage = pages["products_page"] 
    
    
        home_page.open_homepage()
        home_page.go_to_products_page()
        
        products_page.use_search_input("Blue top")