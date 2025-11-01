from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

def create_driver(headless: bool = False) -> WebDriver:
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