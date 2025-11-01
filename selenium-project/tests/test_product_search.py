from pages.home_page import HomePage
from pages.products_page import ProductsPage

class TestProductSearchPositive:
    
    def test_correct_product_search(self, pages):
        
        home_page: HomePage = pages["home"]
        products_page: ProductsPage = pages["products_page"] 
        
        search_phrase = "Blue top"
    
        home_page.open_homepage()
        home_page.go_to_products_page()
        
        products_page.use_search(search_phrase)
        home_page.remove_ads_banner_if_visible()
        
        assert products_page.contains_product_with_text(search_phrase), "No result with given search phrase were found"
        
    def test_category_menu_filtering(self, pages):
        
        home_page: HomePage = pages["home"]
        products_page: ProductsPage = pages["products_page"]
        
        category = "Jeans"
        
        home_page.open_homepage()
        home_page.go_to_products_page()
        
        products_page.expand_men_section()
        products_page.click_jeans_category()
        products_page.get_products_name()
        
        assert products_page.contains_product_with_text(category), f"Results do not match {category} category"
        
        
class TestProductSearchNegative:
        
    def test_search_no_results(self, pages):
            
        home_page: HomePage = pages["home"]
        products_page: ProductsPage = pages["products_page"]
            
        search_phrase = "nonexistentproduct"
            
        home_page.open_homepage()
        home_page.go_to_products_page()
            
        products_page.use_search(search_phrase)
        home_page.remove_ads_banner_if_visible()
            
        assert not products_page.search_has_results(wait=False), "Results were found"