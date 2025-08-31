from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.sign_up_step_2 import SignUpStep2
from data.test_data import SIGNUP_DATA
import time

class TestRegister():
    
    def test_register_valid_user(self, pages):
        
        valid_user= SIGNUP_DATA["valid_user"]
        
        home_page: HomePage = pages["home"]
        login_page: LoginPage = pages["login"]
        sign_up_step2_page: SignUpStep2 = pages["sign_up_step2"]
        
        home_page.open(home_page.URL)
        home_page.accept_cookies()
        assert home_page.is_on_homepage()
        home_page.go_to_login_page()
        
        assert login_page.is_on_login_page()
        login_page.sign_up(valid_user["username"], valid_user["email"])
        
        assert sign_up_step2_page.is_on_sign_up_step2_page()

        sign_up_step2_page.fill_account_information_form("Mr", valid_user["password"], valid_user["day"], valid_user["month"])

        time.sleep(2)

       

        
    