from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.sign_up_step_2 import SignUpStep2
import pytest
import time

class TestRegister():
    
    def test_register_valid_user(self, pages):
        
        home_page: HomePage = pages["home"]
        login_page: LoginPage = pages["login"]
        sign_up_step2_page: SignUpStep2 = pages["sign_up_step2"]
        
        home_page.open(home_page.URL)
        home_page.accept_cookies()
        assert home_page.is_on_homepage()
        home_page.go_to_login_page()
        
        assert login_page.is_on_login_page()
        login_page.sign_up()
        
        assert sign_up_step2_page.is_on_sign_up_step2_page()
