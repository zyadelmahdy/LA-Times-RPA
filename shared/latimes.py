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

        print('topic chosen')
        time.sleep(70)


        iframe_locator = self.driver.switch_to.frame(0)
        iframe = self.driver.find_element(*iframe_locator)
        self.driver.switch_to.frame(iframe)
        print("Switched to iframe")

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "class=met-flyout-close"))).click()
            print("X btn clicked successfully")
        except TimeoutException:
            print("Timeout: Failed to click on the X btn within 10 seconds.")

        self.driver.switch_to.default_content()

        


        time.sleep(3)
        # x_button = self.driver.find_element(By.XPATH, "")
        # x_button.click()

        sort_dropdown = self.driver.find_element(By.XPATH, "/html/body/div[2]/ps-search-results-module/form/div[2]/ps-search-filters/div/main/div[1]/div[2]/div/label/select")
        actions = ActionChains(self.driver)
        actions.move_to_element(sort_dropdown).perform()
        time.sleep(3)
        sort_dropdown.click()

        print('dropdown menu clicked')

        time.sleep(3)

        newest_option = self.driver.find_element(By.CSS_SELECTOR, "[value='1']")
        time.sleep(3)
        newest_option.click()

        print("Sorted by Newest")

        time.sleep(3)



        

    # def pull_titles(self, ):
        
    
    
    
    # def pull_date(self, ):
        
        
        
        
    # def pull_desc(self, ):
        
        
    
    
    
    
    
    
    
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.teardown:
            self.driver.quit()