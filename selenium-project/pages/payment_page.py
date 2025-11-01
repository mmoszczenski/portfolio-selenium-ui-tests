from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class PaymentPage(BasePage):
    
    _NAME_FIELD = (By.CSS_SELECTOR, "input[data-qa='name-on-card']")
    _CARD_NUMBER_FIELD = (By.CSS_SELECTOR, "input[data-qa='card-number']")
    _CVC_FIELD = (By.CSS_SELECTOR, "input[data-qa='cvc']")
    _EXPIRATION_MONTH_FIELD = (By.CSS_SELECTOR, "input[data-qa='expiry-month']")
    _EXPIRATION_YEAR_FIELD = (By.CSS_SELECTOR, "input[data-qa='expiry-year']")
    
    _CONFIRM_ORDER_BUTTON = (By.CSS_SELECTOR, "button[data-qa='pay-button']")
    
    def fill_name(self, name: str):
        self.type(self._NAME_FIELD, name)
        
    def fill_card(self, card_number: int):
        self.type(self._CARD_NUMBER_FIELD, card_number)
        
    def fill_cvc(self, cvc_number: int):
        self.type(self._CVC_FIELD, cvc_number)
        
    def fill_expiration_month(self, month):
        self.type(self._EXPIRATION_MONTH_FIELD, month)
        
    def fill_expiration_year(self, year):
        self.type(self._EXPIRATION_YEAR_FIELD, year)
        
    def click_confirm_button(self):
        self.click(self._CONFIRM_ORDER_BUTTON)
        
    def provide_payment_form_data(self, name, card_number, cvc_number, month, year):
        self.fill_name(name)
        self.fill_card(card_number)
        self.fill_cvc(cvc_number)
        self.fill_expiration_month(month)
        self.fill_expiration_year(year)
        self.click_confirm_button()
        