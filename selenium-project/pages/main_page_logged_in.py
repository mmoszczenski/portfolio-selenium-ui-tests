from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPageLoggedIn(BasePage):

    _LOGOUT_BUTTON = (By.LINK_TEXT, " Logout")

    def click_logout_button(self):
        self.find(self._LOGOUT_BUTTON).click()