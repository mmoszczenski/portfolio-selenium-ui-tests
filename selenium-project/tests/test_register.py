from pages.home_page import HomePage
from pages.login_page import LoginPage
import pytest
import time

class TestRegister():
    
    def test_register_valid_user(self, pages):
        
        home_page: HomePage = pages["home"]
        login_page: LoginPage = pages["login"]
        
        home_page.open(home_page.URL)
       
        time.sleep(2)
         
        home_page.accept_cookies()
        
        time.sleep(2)
        
        assert home_page.is_on_homepage()
        
        home_page.go_to_login_page()
        
        assert login_page.is_on_login_page()
    
    
        
    