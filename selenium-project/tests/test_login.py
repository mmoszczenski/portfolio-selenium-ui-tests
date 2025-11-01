from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.sign_up_step_2 import SignUpStep2
from pages.account_created_page import AccountCreatedPage
from utils.user_factory import make_user

class TestLoginPositive():

    def test_login_with_valid_credentials(self, pages):
        
        user = make_user()
        email = user.email
        home_page: HomePage = pages["home"]
        login_page: LoginPage = pages["login"]
        sign_up_step2_page: SignUpStep2 = pages["sign_up_step2"]
        account_created_page: AccountCreatedPage = pages["account_created_page"]
        
        home_page.open_homepage()
        home_page.go_to_login_page()
        login_page.sign_up(user.username, email)
        sign_up_step2_page.fill_account_information_form(
            password = user.password, 
            country = user.country,
            first_name = user.first_name,
            last_name = user.last_name,
            address = user.address,
            state = user.state,
            city = user.city,
            zipcode = user.zipcode,
            mobile_number = user.mobile_number
        )        
        account_created_page.click_continue_button()
        home_page.click_logout_button()
        login_page.login(user.email, user.password)

        assert home_page.is_logged_in()


class TestLoginNegative():

    def test_login_with_invalid_password(self, pages):

        user = make_user()
        home_page: HomePage = pages["home"]
        login_page: LoginPage = pages["login"]
        sign_up_step2_page: SignUpStep2 = pages["sign_up_step2"]
        account_created_page: AccountCreatedPage = pages["account_created_page"]
        
        home_page.open_homepage()
        home_page.go_to_login_page()
        login_page.sign_up(user.username, user.email)
        sign_up_step2_page.fill_account_information_form(
            password = user.password, 
            country = user.country,
            first_name = user.first_name,
            last_name = user.last_name,
            address = user.address,
            state = user.state,
            city = user.city,
            zipcode = user.zipcode,
            mobile_number = user.mobile_number
        )        
        account_created_page.click_continue_button()
        home_page.click_logout_button()
        login_page.login(user.email, "invalidpassword")

        assert login_page.is_login_validation_error_message_displayed()

    def test_login_with_non_existing_email(self, pages):

        home_page: HomePage = pages["home"]
        login_page: LoginPage = pages["login"]

        home_page.open_homepage()
        home_page.go_to_login_page()
        login_page.login("random_non_existing_email_1191919191@example.com", "random_password")

        assert login_page.is_login_validation_error_message_displayed()

    def test_submit_empty_form(self, pages):

        home_page: HomePage = pages["home"]
        login_page: LoginPage = pages["login"]

        home_page.open_homepage()
        home_page.go_to_login_page()
        login_page.login("", "")
        
        assert login_page.is_email_error_type_value_missing()
  

    def test_login_without_password(self, pages):

        user = make_user()
        home_page: HomePage = pages["home"]
        login_page: LoginPage = pages["login"]
        sign_up_step2_page: SignUpStep2 = pages["sign_up_step2"]
        account_created_page: AccountCreatedPage = pages["account_created_page"]

        home_page.open_homepage()
        home_page.go_to_login_page()
        login_page.sign_up(user.username, user.email)
        sign_up_step2_page.fill_account_information_form(
            password = user.password, 
            country = user.country,
            first_name = user.first_name,
            last_name = user.last_name,
            address = user.address,
            state = user.state,
            city = user.city,
            zipcode = user.zipcode,
            mobile_number = user.mobile_number
        )        
        account_created_page.click_continue_button()
        home_page.click_logout_button()
        login_page.login(user.email, "")

        assert login_page.is_password_error_type_value_missing()

        


