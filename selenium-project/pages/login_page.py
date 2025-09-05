from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    
    _HEADER = (By.XPATH, "//h2[text()='New User Signup!']")
    _SIGN_UP_USERNAME_INPUT_FIELD = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
    _SIGN_UP_EMAIL_INPUT_FIELD = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    _SIGN_UP_BUTTON = (By.CSS_SELECTOR, "button[data-qa='signup-button']")
    
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

    def get_email_validation_error(self):
        email_input = self.find(self._SIGN_UP_EMAIL_INPUT_FIELD)
        return email_input.get_attribute("validationMessage")
