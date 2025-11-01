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
    _COMPANY_INPUT = (By.CSS_SELECTOR, "input[data-qa='company']")
    _ADDRESS_INPUT = (By.CSS_SELECTOR, "input[data-qa='address']")
    _ADDRESS2_INPUT = (By.CSS_SELECTOR, "input[data-qa='address2']")
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
        select.select_by_visible_text(str(day))

    def select_month(self, month: str):
        dropdown = self.find(self._MONTHS_DROPDOWN)
        select = Select(dropdown)
        select.select_by_visible_text(str(month))

    def select_year(self, year: str):
        dropdown = self.find(self._YEARS_DROPDOWN)
        select = Select(dropdown)
        select.select_by_visible_text(str(year))

    def select_country(self, country: str):
        dropdown = self.find(self._COUNTRY_DROPDOWN)
        select = Select(dropdown)
        select.select_by_visible_text(country)

    def mark_newsletter_checkbox(self):
        self.click(self._NEWSLETTER_CHECKBOX)
        
    def mark_special_offers_checkbox(self):
        self.click(self._SPECIAL_OFFERS_CHECKBOX)

    def fill_password(self, text: str):
        self.type(self._PASSWORD_FIELD_INPUT, text)

    def fill_first_name(self, text: str):
        self.type(self._FIRST_NAME_INPUT, text)

    def fill_last_name(self, text: str):
        self.type(self._LAST_NAME_INPUT, text)
        
    def fill_company(self, text: str):
        self.type(self._COMPANY_INPUT, text)

    def fill_address(self, text: str):
        self.type(self._ADDRESS_INPUT, text)
        
    def fill_address2(self, text: str):
        self.type(self._ADDRESS2_INPUT, text)

    def fill_state(self, text: str):
        self.type(self._STATE_INPUT, text)

    def fill_city(self, text: str):
        self.type(self._CITY_INPUT, text)

    def fill_zipcode(self, text: str):
        self.type(self._ZIPCODE_INPUT, text)

    def fill_mobile_number(self, text: str):
        self.type(self._MOBILE_NUMBER_INPUT, text)

    def click_create_account_button(self):
        self.click(self._CREATE_ACCOUNT_BUTTON)

    def fill_account_information_form(
        self, country, first_name, last_name, address, state, city, zipcode, mobile_number, password=None, **kwargs
        ):
        
        if "title" in kwargs:
            self.select_title(kwargs["title"])
        if password is not None:
            self.fill_password(password)
        if "day" in kwargs:    
            self.select_days(kwargs["day"])
        if "month" in kwargs:
            self.select_month(kwargs["month"])
        if "year" in kwargs:
            self.select_year(kwargs["year"])
        if country:
            self.select_country(country)
        if first_name:
            self.fill_first_name(first_name)
        if last_name:
            self.fill_last_name(last_name)
        if "company" in kwargs:
            self.fill_company(kwargs["company"])
        if address:    
            self.fill_address(address)
        if "address2" in kwargs:
            self.fill_address2(kwargs["address2"])
        if state:    
            self.fill_state(state)
        if city:
            self.fill_city(city)
        if zipcode:    
            self.fill_zipcode(zipcode)
        if mobile_number:
            self.fill_mobile_number(mobile_number)
        if kwargs.get("newsletter", False):
            self.mark_newsletter_checkbox()
        if kwargs.get("special_offers", False):
            self.mark_special_offers_checkbox()

        self.remove_ads_banner_if_visible()
        self.click_create_account_button()

    def is_account_created(self):
        return self.is_visible(self._ACCOUNT_CREATED_HEADER)
    
    def is_password_valid(self):
        password_input = self.find(self._PASSWORD_FIELD_INPUT)
        return self.is_valid(password_input)
    
    def is_password_error_type_value_missing(self):
        password_input = self.find(self._PASSWORD_FIELD_INPUT)
        return self.get_validity_property(password_input, "valueMissing")    
    