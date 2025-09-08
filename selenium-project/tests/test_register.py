from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.sign_up_step_2 import SignUpStep2
from data.test_data import SIGNUP_DATA
import time

class TestRegisterPositive():
    
    def test_register_with_valid_data_minimal(self, pages):
        
        user= SIGNUP_DATA["valid_user"]
        home_page: HomePage = pages["home"]
        login_page: LoginPage = pages["login"]
        sign_up_step2_page: SignUpStep2 = pages["sign_up_step2"]
        
        home_page.open(home_page.URL)
        home_page.accept_cookies()
        assert home_page.is_on_homepage()
        home_page.go_to_login_page()
        
        assert login_page.is_on_login_page()
        login_page.sign_up(user["username"], user["email"])
        
        assert sign_up_step2_page.is_on_sign_up_step2_page()

        sign_up_step2_page.fill_account_information_form(
            password = user["password"], 
            country = user["country"],
            first_name = user["first_name"],
            last_name = user["last_name"],
            address = user["address"],
            state = user["state"],
            city = user["city"],
            zipcode = user["zipcode"],
            mobile_number = user["mobile_number"]
        )
        
        assert sign_up_step2_page.is_account_created()


    def test_register_with_valid_data_all_fields(self, pages):
        
        user= SIGNUP_DATA["valid_user"]
        home_page: HomePage = pages["home"]
        login_page: LoginPage = pages["login"]
        sign_up_step2_page: SignUpStep2 = pages["sign_up_step2"]
        
        home_page.open(home_page.URL)
        home_page.accept_cookies()
        assert home_page.is_on_homepage()
        home_page.go_to_login_page()
        
        assert login_page.is_on_login_page()
        login_page.sign_up(user["username"], user["email"])
        
        assert sign_up_step2_page.is_on_sign_up_step2_page()

        sign_up_step2_page.fill_account_information_form(
            title = user["title"],
            password = user["password"], 
            day = user["day"], 
            month = user["month"], 
            year = user["year"],
            country = user["country"],
            first_name = user["first_name"],
            last_name = user["last_name"],
            address = user["address"],
            state = user["state"],
            city = user["city"],
            zipcode = user["zipcode"],
            mobile_number = user["mobile_number"],
            newsletter= True,
            special_offers=True
        )
        
        assert sign_up_step2_page.is_account_created()
        
class TestRegisterNegative():
            
    def test_register_with_invalid_email(self, pages):
        
        user = SIGNUP_DATA["valid_user"]
        home_page: HomePage = pages["home"]
        login_page: LoginPage = pages["login"]

        home_page.open(home_page.URL)
        home_page.accept_cookies()
        home_page.go_to_login_page()

        login_page.sign_up(user["username"], "invalidemail.com")

        assert login_page.is_email_valid() is False
        assert login_page.is_email_type_mismatch() is True
 
    def test_register_with_empty_password(self, pages):
        
        user = SIGNUP_DATA["valid_user"]
        home_page: HomePage = pages["home"]
        login_page: LoginPage = pages["login"]
        sign_up_step2_page: SignUpStep2 = pages["sign_up_step2"]
        
        home_page.open(home_page.URL)
        home_page.accept_cookies()
        home_page.go_to_login_page()
        
        login_page.sign_up(user["username"], user["email"])
        
        sign_up_step2_page.fill_account_information_form(
            country = user["country"],
            first_name = user["first_name"],
            last_name = user["last_name"],
            address = user["address"],
            state = user["state"],
            city = user["city"],
            zipcode = user["zipcode"],
            mobile_number = user["mobile_number"]            
        )
        
        assert sign_up_step2_page.is_password_valid() is False
        assert sign_up_step2_page.is_password_type_valueMissing() is True
        
        time.sleep(2)
       
    #def test_register_with_empty_fields():
       
    #def test_register_with_special_characters():
    
    #def test_register_with_taken_email():
      

       

        
    