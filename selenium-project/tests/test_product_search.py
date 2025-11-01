from pages.home_page import HomePage
from pages.products_page import ProductsPage


class TestProductSearch:
    
    def test_correct_product_search(self, pages):
        
        home_page: HomePage = pages["home"]
        products_page: ProductsPage = pages["products_page"] 
        
        search_phrase = "Blue top"
    
        home_page.open_homepage()
        home_page.go_to_products_page()
        
        products_page.use_search(search_phrase)
        home_page.remove_ads_banner_if_visible()
        
        assert products_page.contains_product_with_text(search_phrase), "No result with given search phrase were found"
        