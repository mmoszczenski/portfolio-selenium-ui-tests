from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AccountCreatedPage(BasePage):

    _CONTINUE_BUTTON = (By.CSS_SELECTOR, "a[data-qa='continue-button']")

    def click_continue_button(self):
        self.find(self._CONTINUE_BUTTON).click()