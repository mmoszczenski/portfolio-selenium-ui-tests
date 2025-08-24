from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    
    URL = "https://automationexercise.com/"
    
    _LOGIN_BUTTON = (By.XPATH, "a[@href='/login']" )
            
    def is_on_homepage(self):
        return self.driver.current_url == self.URL
    
    def go_to_login_page(self):
        self.click(self._LOGIN_BUTTON)