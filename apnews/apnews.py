from .const import initialize_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Apnews:
    def __init__(self):
        self.driver = initialize_driver()

    def land_first_page(self):
        self.driver.get('https://apnews.com/')
        time.sleep(2)

    def quit(self):
        self.driver.quit()