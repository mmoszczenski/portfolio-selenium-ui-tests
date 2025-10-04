from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ContactFormPage(BasePage):

    _NAME_INPUT_FIELD = (By.CSS_SELECTOR, "input[data-qa='name']")
    _EMAIL_INPUT_FIELD = (By.CSS_SELECTOR, "input[data-qa='email']")
    _SUBJECT_INPUT_FIELD = (By.CSS_SELECTOR, "input[data-qa='subject']")
    _MESSAGE_INPUT_FIELD = (By.CSS_SELECTOR, "textarea[data-qa='message']")
    _SUBMIT_BUTTON = (By.CSS_SELECTOR, "input[data-qa='submit-button']")
    _UPLOAD_BUTTON = (By.CSS_SELECTOR, "input[type='file']")
    
    _SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".status.alert.alert-success")
    _CONFIRM_ALERT_WINDOW = ()
    
    def fill_name(self, text):
        self.type(self._NAME_INPUT_FIELD, text)
        
    def fill_email(self, text):
        self.type(self._EMAIL_INPUT_FIELD, text)
    
    def fill_subject(self, text):
        self.type(self._SUBJECT_INPUT_FIELD, text)
        
    def fill_message(self, text):
        self.type(self._MESSAGE_INPUT_FIELD, text)
        
    def upload_file(self, file):
        file_input = self.find(self._UPLOAD_BUTTON)
        file_input.send_keys(str(file))

    def click_submit_button(self):
        self.click(self._SUBMIT_BUTTON)
        
    def is_contact_form_submitted(self) -> bool:
        return self.is_visible(self._SUCCESS_MESSAGE)