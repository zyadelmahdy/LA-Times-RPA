from .const import initialize_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class Yahoo:
    def __init__(self, teardown=False):
        self.driver = initialize_driver()
        self.teardown = teardown
    def __enter__(self):
        return self

    def load_first_page(self):
        self.driver.get('https://news.yahoo.com/')
        
        try:
            EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
        except TimeoutException:
            print("Timeout: Failed to load Yahoo News within 10 seconds.")

    def __exit__(self, exc_type, exc_value, traceback):
        if self.teardown:
            self.driver.quit()