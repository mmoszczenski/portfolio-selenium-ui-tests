import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver

class BasePage():
    
    def __init__(self, driver: WebDriver, timeout = 10):
        self.driver = driver
        self.timeout = timeout
        
    def open(self, url):
        self.driver.get(url)    
        
    def find(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
    
    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)
        
    def get_text(self, locator):
        return self.find(locator).text
    
    def click(self, locator):
        element = WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator))
        element.click()
        
    def is_visible(self, locator):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
            return element
        except TimeoutError:
            return None