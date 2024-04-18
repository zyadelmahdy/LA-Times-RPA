from .const import initialize_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class LATimes:
    def __init__(self, teardown=False):
        self.driver = initialize_driver()
        self.teardown = teardown
    def __enter__(self):
        return self

    def load_first_page(self):
        self.driver.get('https://www.latimes.com/')
        
        try:
            WebDriverWait(self.driver, 200).until(EC.presence_of_element_located((By.XPATH, "/html/body/ps-header/header/div[2]/button")))
            print("Body loaded successfully")
        except TimeoutException:
            print("Timeout: Failed to load LA Times within 10 seconds.")


    def search(self, search_word):
        magnify_icon = self.driver.find_element(By.XPATH, '/html/body/ps-header/header/div[2]/button')
        time.sleep(3)

        magnify_icon.click()
        time.sleep(3)

        search_bar = self.driver.find_element(By.XPATH, '/html/body/ps-header/header/div[2]/div[2]/form/label/input')
        time.sleep(3)
        search_bar.send_keys(f'{search_word}')
        search_bar.send_keys(Keys.ENTER)
        time.sleep(3)

    def filter(self, selected_items):
        see_more_btn = self.driver.find_element(By.XPATH, "/html/body/div[2]/ps-search-results-module/form/div[2]/ps-search-filters/div/aside/div/div[3]/div[1]/ps-toggler/ps-toggler/button")
        time.sleep(3)

        see_more_btn.click()
        time.sleep(3)
        list_items = self.driver.find_elements(By.XPATH, "/html/body/div[2]/ps-search-results-module/form/div[2]/ps-search-filters/div/aside/div/div[3]/div[1]/ps-toggler/ps-toggler/div/ul")
        print(list_items)

        for item in list_items:
            print(item.text)

    

    def sort_newest(self):
        time.sleep(3)

        
        climate_environment = self.driver.find_element(By.XPATH, "/html/body/div[2]/ps-search-results-module/form/div[2]/ps-search-filters/div/aside/div/div[3]/div[1]/ps-toggler/ps-toggler/div/ul/li[54]/div/div[1]/label/input")
        # element = self.driver.find_element(By.XPATH, "/html/body/div[2]/ps-search-results-module/form/div[2]/ps-search-filters/div/aside/div/div[3]/div[1]/ps-toggler/ps-toggler/div/ul/li[54]/div/div[1]/label/span")
        actions = ActionChains(self.driver)
        actions.move_to_element(climate_environment).perform()

        climate_environment.click()

        # x_button = self.driver.find_element(By.XPATH, "/html/body/modality-custom-element//div/div/div/div/a")
        # x_button.click()

        time.sleep(3)

        sort_dropdown = self.driver.find_element(By.CSS_SELECTOR, "[name='s']")
        sort_dropdown.click()

        time.sleep(3)

        newest_option = self.driver.find_element(By.CSS_SELECTOR, "[value='1']")
        newest_option.click()

        print("Sorted by Newest")

        time.sleep(3)



        

    # def pull_titles(self, ):
        
    
    
    
    # def pull_date(self, ):
        
        
        
        
    # def pull_desc(self, ):
        
        
    
    
    
    
    
    
    
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.teardown:
            self.driver.quit()