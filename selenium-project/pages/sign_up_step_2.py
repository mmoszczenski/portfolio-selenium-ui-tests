from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SignUpStep2(BasePage):
    
    _PAGE_HEADER = (By.XPATH, "//div[contains(@class,'login-form')]//h2[b[text()='Enter Account Information']]")
    _title = {
        "Mr": (By.ID, "id_gender1"),
        "Mrs": (By.ID, "id_gender2")
    }
    
    def is_on_sign_up_step2_page(self):
        return self.is_visible(self._PAGE_HEADER)
    
    def select_title(self, title):
        self.click(self._title[title])