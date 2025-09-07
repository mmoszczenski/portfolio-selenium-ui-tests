from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class SignUpStep2(BasePage):
    
    #Headers
    _PAGE_HEADER = (By.XPATH, "//div[contains(@class,'login-form')]//h2[b[text()='Enter Account Information']]")
    _ACCOUNT_CREATED_HEADER = (By.CSS_SELECTOR, "h2[data-qa='account-created']")

    #Input Fields
    _PASSWORD_FIELD_INPUT = (By.CSS_SELECTOR, "input[data-qa='password']")
    _FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[data-qa='first_name']")
    _LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[data-qa='last_name']")
    _ADDRESS_INPUT = (By.CSS_SELECTOR, "input[data-qa='address']")
    _STATE_INPUT = (By.CSS_SELECTOR, "input[data-qa='state']")
    _CITY_INPUT = (By.CSS_SELECTOR, "input[data-qa='city']")
    _ZIPCODE_INPUT = (By.CSS_SELECTOR, "input[data-qa='zipcode']")
    _MOBILE_NUMBER_INPUT = (By.CSS_SELECTOR, "input[data-qa='mobile_number']")

    #Dropdowns
    _DAYS_DROPDOWN = (By.CSS_SELECTOR, "select[data-qa='days']")
    _MONTHS_DROPDOWN = (By.CSS_SELECTOR, "select[data-qa='months']")
    _YEARS_DROPDOWN = (By.CSS_SELECTOR, "select[data-qa='years']")
    _COUNTRY_DROPDOWN = (By.CSS_SELECTOR, "select[data-qa='country']")

    #Checkobxes
    _NEWSLETTER_CHECKBOX = (By.ID, "newsletter")
    _SPECIAL_OFFERS_CHECKBOX = (By.ID, "optin")

    #Action buttons
    _CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "button[data-qa='create-account']")

    #Multiple choices
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
        
    def mark_special_offers_checkbox(self):
        self.click(self._SPECIAL_OFFERS_CHECKBOX)

    def fill_password(self, text):
        self.type(self._PASSWORD_FIELD_INPUT, text)

    def fill_first_name(self, text):
        self.type(self._FIRST_NAME_INPUT, text)

    def fill_last_name(self, text):
        self.type(self._LAST_NAME_INPUT, text)

    def fill_address(self, text):
        self.type(self._ADDRESS_INPUT, text)

    def fill_state(self, text):
        self.type(self._STATE_INPUT, text)

    def fill_city(self, text):
        self.type(self._CITY_INPUT, text)

    def fill_zipcode(self, text):
        self.type(self._ZIPCODE_INPUT, text)

    def fill_mobile_number(self, text):
        self.type(self._MOBILE_NUMBER_INPUT, text)

    def click_create_account_button(self):
        self.click(self._CREATE_ACCOUNT_BUTTON)

    def fill_account_information_form(
        self, title, password, day, month, year, country, first_name, last_name, address, state, city, zipcode, mobile_number, newsletter = False, special_offers = False
        ):
        if title:
            self.select_title(title)
        if password:
            self.fill_password(password)
        if day:    
            self.select_days(day)
        if month:
            self.select_month(month)
        if year:
            self.select_year(year)
        if country:
            self.select_country(country)
        if first_name:
            self.fill_first_name(first_name)
        if last_name:
            self.fill_last_name(last_name)
        if address:    
            self.fill_address(address)
        if state:    
            self.fill_state(state)
        if city:
            self.fill_city(city)
        if zipcode:    
            self.fill_zipcode(zipcode)
        if mobile_number:
            self.fill_mobile_number(mobile_number)
        if newsletter:
            self.mark_newsletter_checkbox()
        if special_offers:
            self.mark_special_offers_checkbox()
        
        self.click_create_account_button()

    def is_account_created(self):
        return self.is_visible(self._ACCOUNT_CREATED_HEADER)