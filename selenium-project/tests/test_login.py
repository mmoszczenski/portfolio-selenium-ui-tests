from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.sign_up_step_2 import SignUpStep2
from pages.main_page_logged_in import MainPageLoggedIn
from pages.account_created_page import AccountCreatedPage
from data.test_data import SIGNUP_DATA
from utils.helpers import generate_random_email


class TestLoginPositive():

#Test Case 1 - User provides valid login and password and then user is redirected to the proper page

    def test_login_with_valid_credentials(self, pages):

        user= SIGNUP_DATA["valid_user"]
        home_page: HomePage = pages["home"]
        login_page: LoginPage = pages["login"]
        sign_up_step2_page: SignUpStep2 = pages["sign_up_step2"]
        account_created_page: AccountCreatedPage = pages["account_created_page"]
        
        #TODO - Refactor so I can use just a helper/fixture instead of copying the whole code from registration test
        home_page.open(home_page.URL)
        home_page.accept_cookies()
        home_page.go_to_login_page()
        login_page.sign_up(user["username"], user["email"])
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
        account_created_page.click_continue_button()










#Test Case 2 - User logins in and then logs out and no longer has acess to the logged in resources








class TestLoginPositive():
    pass


#Test Case 1 - User provides valid login and invalid password. There is proper error message


#Test Case 3 - User provides non-existing login and tries to submit the form. There is porper error message

#Test Case 4 - User doesn't provide any data what so ever and submits the form

#Test Case 5 - 