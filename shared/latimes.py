from .const import initialize_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys

class LATimes:
    def __init__(self, teardown=False):
        self.driver = initialize_driver()
        self.teardown = teardown
    def __enter__(self):
        return self

    def load_first_page(self):
        self.driver.get('https://www.latimes.com/')
        
        try:
            EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
        except TimeoutException:
            print("Timeout: Failed to load Yahoo News within 10 seconds.")


    def search(self, search_word):
        magnify_icon = self.driver.find_element(By.CSS_SELECTOR, '[data-element="magnify-icon"]')
        magnify_icon.click()
        search_bar = self.driver.find_element(By.CSS_SELECTOR, '[data-element="search-form-input"]')
        search_bar.send_keys(f'{search_word}')
        search_bar.send_keys(Keys.ENTER)




    # def pull_titles(self, ):
        
    
    
    
    # def pull_date(self, ):
        
        
        
        
    # def pull_desc(self, ):
        
        
    
    
    
    
    
    
    
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.teardown:
            self.driver.quit()