from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.sign_up_step_2 import SignUpStep2
from data.test_data import SIGNUP_DATA
import time

class TestRegisterPositive():
    
    def test_register_with_valid_data_minimal(self, pages):
        
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

        sign_up_step2_page.fill_account_information_form(
            valid_user["title"],
            valid_user["password"], 
            valid_user["day"], 
            valid_user["month"], 
            valid_user["year"],
            valid_user["country"],
            valid_user["first_name"],
            valid_user["last_name"],
            valid_user["address"],
            valid_user["state"],
            valid_user["city"],
            valid_user["zipcode"],
            valid_user["mobile_number"],
        )
        
        assert sign_up_step2_page.is_account_created()


    def test_register_with_valid_data_all_fields():
        pass


class TestRegisterNegative():
            
    def test_register_with_invalid_email():
        pass
        
    def test_register_with_empty_password():
        pass

    def test_register_with_empty_fields():
        pass

    def test_register_with_taken_email():
        pass

    def test_register_with_special_characters():
        pass

       

        
    