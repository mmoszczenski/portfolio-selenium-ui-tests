from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    
    _HEADER = (By.XPATH, "//h2[text()='New User Signup!']")
    
    def is_on_login_page(self):
        return self.is_visible(self._HEADER)