from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ContactForm(BasePage):

    _NAME_INPUT_FIELD = (By.CSS_SELECTOR, "input['data-qa=name']")
    _EMAIL_INPUT_FIELD = (By.CSS_SELECTOR, "input['data-qa=email']")
    _SUBJECT_INPUT_FIELD = (By.CSS_SELECTOR, "input['data-qa=subject']")
    _MESSAGE_INPUT_FIELD = (By.CSS_SELECTOR, "input['data-qa=message']")
    _SUBMIT_BUTTON = (By.CSS_SELECTOR, "input['data-qa=submit-button']")
    _UPLOAD_BUTTON = (By.CSS_SELECTOR, "input['name=upload_file']")
    
    