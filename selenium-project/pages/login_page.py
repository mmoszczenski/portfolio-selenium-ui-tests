from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    
    _HEADER = (By.XPATH, "//h2[text()='New User Signup!']")
    _SIGN_UP_USERNAME_INPUT_FIELD = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
    _SIGN_UP_EMAIL_INPUT_FIELD = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    _SIGN_UP_BUTTON = (By.CSS_SELECTOR, "button[data-qa='signup-button']")
    _LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    _LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    _LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    
    _EMAIL_TAKEN_ERROR_MESSAGE = (By.XPATH, "//form[@action='/signup']//p")

    def is_on_login_page(self):
        return self.is_visible(self._HEADER)
    
    def fill_sign_up_form(self, username, email):
        self.type(self._SIGN_UP_USERNAME_INPUT_FIELD, username)
        self.type(self._SIGN_UP_EMAIL_INPUT_FIELD, email)
        
    def click_sign_up_button(self):
        self.click(self._SIGN_UP_BUTTON)
        
    def sign_up(self, username, email):
        self.fill_sign_up_form(username, email)
        self.click_sign_up_button()

    def fill_login_form(self, email, password):
        self.type(self._LOGIN_EMAIL_INPUT, email)
        self.type(self._LOGIN_PASSWORD_INPUT, password)

    def click_login_button(self):
        self.click(self._LOGIN_BUTTON)

    def login(self, email, password):
        self.fill_login_form(email, password)
        self.click_login_button()

    def is_email_valid(self):
        email_input = self.find(self._SIGN_UP_EMAIL_INPUT_FIELD)
        return self.is_valid(email_input)
    
    def is_email_error_type_mismatch(self):
        email_input = self.find(self._SIGN_UP_EMAIL_INPUT_FIELD)
        return self.get_validity_property(email_input, "typeMismatch")
    
    def is_email_taken_error_displayed(self):
        return self.is_visible(self._EMAIL_TAKEN_ERROR_MESSAGE)