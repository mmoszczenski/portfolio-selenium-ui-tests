from pages.home_page import HomePage
from pages.login_page import LoginPage
import pytest

class TestRegister():
    
    def test_register_valid_user(self, pages):
        
        home_page: HomePage = pages["home"]
        
        home_page.open(home_page.URL)
        home_page.is_on_homepage
    
        
    