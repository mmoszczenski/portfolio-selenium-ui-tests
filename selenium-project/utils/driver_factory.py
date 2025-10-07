from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

def create_driver(headless: bool = False):
    options = Options()
    options.add_argument("--start-maximized")
    # options.add_argument("--incognito")
    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-gpu")
    service = ChromeService()
    driver = webdriver.Chrome(service=service, options=options)
    return driver