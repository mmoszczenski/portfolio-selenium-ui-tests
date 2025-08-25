from pages.home_page import HomePage
from pages.login_page import LoginPage
import pytest
import time

class TestRegister():
    
    def test_register_valid_user(self, pages):
        
        home_page: HomePage = pages["home"]
        login_page: LoginPage = pages["login"]
        
        home_page.open(home_page.URL)
        home_page.is_on_homepage()

        login_page.is_on_login_page()
    
    
        
    