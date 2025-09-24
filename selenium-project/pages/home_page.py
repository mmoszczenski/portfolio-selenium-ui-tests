from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    
    URL = "https://automationexercise.com/"
    
    _ACCEPT_COOKIES_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Zgadzam się']")
    _LOGOUT_BUTTON = (By.CSS_SELECTOR, "a[href='/logout']")
    
    _LOGIN_BUTTON = (By.CSS_SELECTOR, "a[href='/login']" )
    _CONTACT_FORM_BUTTON = (By.CSS_SELECTOR, "a[href='/contact_us']")
    
            
    def is_on_homepage(self) -> bool:
        return  self.driver.current_url == self.URL
       
    def go_to_login_page(self):
        self.click(self._LOGIN_BUTTON)
        
    def go_to_contact_form_page(self):
        self.click(self._CONTACT_FORM_BUTTON)
        
    def accept_cookies(self):
        self.click(self._ACCEPT_COOKIES_BUTTON)

    def click_logout_button(self):
        self.click(self._LOGOUT_BUTTON)

    def is_logged_in(self) -> bool:
        return self.is_visible(self._LOGOUT_BUTTON)