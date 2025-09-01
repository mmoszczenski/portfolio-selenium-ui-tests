from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class SignUpStep2(BasePage):
    
    _PAGE_HEADER = (By.XPATH, "//div[contains(@class,'login-form')]//h2[b[text()='Enter Account Information']]")
    _PASSWORD_FIELD = (By.CSS_SELECTOR, "input[data-qa='password']")
    _DAYS_DROPDOWN = (By.CSS_SELECTOR, "select[data-qa='days']")
    _MONTHS_DROPDOWN = (By.CSS_SELECTOR, "select[data-qa='months']")
    _YEARS_DROPDOWN = (By.CSS_SELECTOR, "select[data-qa='years']")
    _COUNTRY_DROPDOWN = (By.CSS_SELECTOR, "select[data-qa='country']")
    _NEWSLETTER_CHECKBOX = (By.ID, "newsletter")
    _FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[data-qa='first_name']")
    _LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[data-qa='last_name']")
    _ADDRESS_INPUT = (By.CSS_SELECTOR, "input[data-qa='address']")
    _STATE_INPUT = (By.CSS_SELECTOR, "input[data-qa='state']")
    _CITY_INPUT = (By.CSS_SELECTOR, "input[data-qa='city']")
    _ZIPCODE_INPUT = (By.CSS_SELECTOR, "input[data-qa='zipcode']")
    _MOBILE_NUMBER_INPUT = (By.CSS_SELECTOR, "input[data-qa='mobile_number']")
    _CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "button[data-qa='create-account']")


    _title = {
        "Mr": (By.ID, "id_gender1"),
        "Mrs": (By.ID, "id_gender2")
    }
    
    def is_on_sign_up_step2_page(self):
        return self.is_visible(self._PAGE_HEADER)
    
    def select_title(self, title):
        self.click(self._title[title])

    def select_days(self, day: str):
        dropdown = self.find(self._DAYS_DROPDOWN)
        select = Select(dropdown)
        select.select_by_visible_text(day)

    def select_month(self, month: str):
        dropdown = self.find(self._MONTHS_DROPDOWN)
        select = Select(dropdown)
        select.select_by_visible_text(month)

    def select_year(self, year: str):
        dropdown = self.find(self._YEARS_DROPDOWN)
        select = Select(dropdown)
        select.select_by_visible_text(year)

    def select_country(self, country: str):
        dropdown = self.find(self._COUNTRY_DROPDOWN)
        select = Select(dropdown)
        select.select_by_visible_text(country)

    def mark_newsletter_checkbox(self):
        self.click(self._NEWSLETTER_CHECKBOX)

    def fill_first_name_input(self, text):
        self.type(self._FIRST_NAME_INPUT, text)

    def fill_last_name_input(self, text):
        self.type(self._LAST_NAME_INPUT, text)

    def fill_address_field_input(self, text):
        self.type(self._ADDRESS_INPUT, text)

    def fill_state_field_input(self, text):
        self.type(self._STATE_INPUT, text)

    def fill_city_field_input(self, text):
        self.type(self._CITY_INPUT, text)

    def fill_zipcode_field_input(self, text):
        self.type(self._ZIPCODE_INPUT, text)

    def fill_mobile_number_input(self, text):
        self.type(self._MOBILE_NUMBER_INPUT, text)

    def click_create_account_button(self):
        self.click(self._CREATE_ACCOUNT_BUTTON)

        
    def fill_account_information_form(self, title, password, day, month, year, first_name, last_name, address, state, city, zipcode, mobile_numer ):
        self.select_title(title)
        self.type(self._PASSWORD_FIELD, password)
        self.select_days(day)
        self.select_month(month)
        self.select_year(year)
        self.mark_newsletter_checkbox()
        self.fill_first_name_input(first_name)
        self.fill_last_name_input(last_name)
        self.fill_address_field_input(address)
        self.fill_state_field_input(state)
        self.fill_city_field_input(city)
        self.fill_zipcode_field_input(zipcode)
        self.fill_mobile_number_input(mobile_numer)
        self.click_create_account_button()