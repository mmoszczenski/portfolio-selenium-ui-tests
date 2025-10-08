from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

class BasePage():
    
    def __init__(self, driver: WebDriver, timeout = 10):
        self.driver = driver
        self.timeout = timeout
        
    def open(self, url):
        self.driver.get(url)    
        
    def find(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
    
    def find_all(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_all_elements_located(locator))
    
    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)
        
    def get_text(self, locator):
        return self.find(locator).text
    
    def click(self, locator):
        element = WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator))
        element.click()
        
    def is_visible(self, locator) -> bool:
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
        
    def execute_js(self, script: str, *args):
        return self.driver.execute_script(script, *args)
    
    def get_validity_property(self, element, property_name: str):
        script = f"return arguments[0].validity.{property_name};"
        return self.execute_js(script, element)

    def is_valid(self, element) -> bool:
        return self.get_validity_property(element, "valid")
    
    def remove_ads_banner_if_visible(self):
        try:
            self.execute_js(f"document.querySelectorAll('ins.adsbygoogle').forEach(ad => ad.remove());")
        except Exception as e:
            print(f"Failed to remove banners: {e}")
            
    def confirm_alert(self, accept: bool = True):
        alert = WebDriverWait(self.driver, self.timeout).until(EC.alert_is_present())
        if accept:
            alert.accept()
        else:
            alert.dismiss()
            
    def hover_over(self, element):
        ActionChains(self.driver).move_to_element(element).perform()
        
    def scroll_to(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", 
            element
        )
    
    def reload_page(self):
        self.driver.refresh()

