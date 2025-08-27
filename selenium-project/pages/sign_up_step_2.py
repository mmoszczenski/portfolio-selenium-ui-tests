from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class SignUpStep2(BasePage):
    
    _PAGE_HEADER = (By.XPATH, "//div[contains(@class,'login-form')]//h2[b[text()='Enter Account Information']]")
    _PASSWORD_FIELD = (By.CSS_SELECTOR, "input[data-qa='password']")
    _title = {
        "Mr": (By.ID, "id_gender1"),
        "Mrs": (By.ID, "id_gender2")
    }
    
    def is_on_sign_up_step2_page(self):
        return self.is_visible(self._PAGE_HEADER)
    
    def select_title(self, title):
        self.click(self._title[title])
        
    def fill_account_information_form(self, title, password):
        self.select_title(title)
        self.type(self._PASSWORD_FIELD, password)