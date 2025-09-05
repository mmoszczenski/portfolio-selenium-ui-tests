from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        
    def execute_js(self, script: str, *args):
        return self.driver.execute_script(script, *args)
    
    def get_validity_propert(self, element, property_name: str):
        script = f"return arguments[0].validity.{property_name};"
        return self.execute_js(script, element)

    def is_valid(self, element):
        return self.get_validity_propert(element, "valid")