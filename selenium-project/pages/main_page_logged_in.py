from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPageLoggedIn(BasePage):

    _LOGOUT_BUTTON = (By.CSS_SELECTOR, " a[href='/logout']")

    def click_logout_button(self):
        self.click(self._LOGOUT_BUTTON)