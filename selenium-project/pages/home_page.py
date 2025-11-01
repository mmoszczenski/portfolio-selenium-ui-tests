from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    
    URL = "https://automationexercise.com/"
    
    _ACCEPT_COOKIES_BUTTON = (By.CSS_SELECTOR, "button.fc-cta-consent")
    _LOGOUT_BUTTON = (By.CSS_SELECTOR, "a[href='/logout']")
    
    _LOGIN_BUTTON = (By.CSS_SELECTOR, "a[href='/login']")
    _CONTACT_FORM_BUTTON = (By.CSS_SELECTOR, "a[href='/contact_us']")
    _PRODUCTS_PAGE_BUTTON = (By.CSS_SELECTOR, "a[href='/products']")
    
    def open_homepage(self) -> None:
        self.open(self.URL)
        self.accept_cookies()
    
    def is_on_homepage(self) -> bool:
        return self.driver.current_url == self.URL
       
    def accept_cookies(self) -> None:
        self.click(self._ACCEPT_COOKIES_BUTTON)

    def click_logout_button(self) -> None:
        self.click(self._LOGOUT_BUTTON)

    def is_logged_in(self) -> bool:
        return self.is_visible(self._LOGOUT_BUTTON)
    
    def go_to_login_page(self) -> None:
        self.click(self._LOGIN_BUTTON)
        
    def go_to_contact_form_page(self) -> None:
        self.click(self._CONTACT_FORM_BUTTON)
        
    def go_to_products_page(self) -> None:
        self.click(self._PRODUCTS_PAGE_BUTTON)
        