from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

def create_driver():
    options = Options()
    options.add_argument("--start-maximized")
    #options.add_argument("--incognito")
    #options.add_argument("--headless")
    service = ChromeService()
    driver = webdriver.Chrome(service=service, options=options)
    return driver