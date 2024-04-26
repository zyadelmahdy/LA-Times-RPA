from .const import initialize_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time, datetime
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
# from xlwt import Workbook
from selenium import webdriver
import pandas as pd


options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
class LATimes:
    def __init__(self, teardown=False):
        self.driver = initialize_driver()
        self.teardown = teardown
    def __enter__(self):
        return self
    
    
    
    def delete_popup(self,time=10):
        try:
            WebDriverWait(self.driver, time).until(EC.presence_of_element_located((By.NAME, "metering-bottompanel")))
            print('popup found')
            element = self.driver.find_element(By.NAME,"metering-bottompanel")
            self.driver.execute_script("""var element = arguments[0]; element.parentNode.removeChild(element);""", element)
            print("Pop up deleted successfully")
        except TimeoutException:
            print("Timeout: Failed to delete the pop up within " +str(time)+" seconds.")
        except:
            pass
        
        

    def load_first_page(self):
        self.driver.get('https://www.latimes.com/')
        
        try:
            WebDriverWait(self.driver, 200).until(EC.presence_of_element_located((By.XPATH, "/html/body/ps-header/header/div[2]/button")))
            print("Body loaded successfully")
        except TimeoutException:
            print("Timeout: Failed to load LA Times within 10 seconds.")


    def search(self, search_word):
        magnify_icon = self.driver.find_element(By.XPATH, '/html/body/ps-header/header/div[2]/button')
        time.sleep(2)

        magnify_icon.click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/ps-header/header/div[2]/div[2]/form/label/input')))
        search_bar = self.driver.find_element(By.XPATH, '/html/body/ps-header/header/div[2]/div[2]/form/label/input')
        time.sleep(2)
        search_bar.send_keys(f'{search_word}')
        time.sleep(1)
        search_bar.send_keys(Keys.ENTER)


    def filter(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/ps-search-results-module/form/div[2]/ps-search-filters/div/aside/div/div[3]/div[1]/ps-toggler/ps-toggler/button")))
            see_more_btn = self.driver.find_element(By.XPATH, "/html/body/div[2]/ps-search-results-module/form/div[2]/ps-search-filters/div/aside/div/div[3]/div[1]/ps-toggler/ps-toggler/button")

            see_more_btn.click()
        except TimeoutException:
            print("Timeout: Failed to delete the pop up within 10 seconds.")

        list_of_topics = self.driver.find_elements(By.XPATH, "/html/body/div[2]/ps-search-results-module/form/div[2]/ps-search-filters/div/aside/div/div[3]/div[1]/ps-toggler/ps-toggler/div/ul")
        print(list_of_topics)


    def sort_newest(self):
        time.sleep(2)
        politics = self.driver.find_element(By.XPATH, "/html/body/div[2]/ps-search-results-module/form/div[2]/ps-search-filters/div/aside/div/div[3]/div[1]/ps-toggler/ps-toggler/div/ul/li[3]/div/div[1]/label/input")
        time.sleep(2)
        actions = ActionChains(self.driver)
        time.sleep(2)
        actions.move_to_element(politics).perform()
        
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "metering-bottompanel")))
            print('popup found')
            element = self.driver.find_element(By.NAME,"metering-bottompanel")
            self.driver.execute_script("""var element = arguments[0]; element.parentNode.removeChild(element);""", element)
            print("Pop up deleted successfully")
        except TimeoutException:
            print("Timeout: Failed to delete the pop up within 10 seconds.")
        politics.click()

        print('topic chosen')
        


        sort_dropdown = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/ps-search-results-module/form/div[2]/ps-search-filters/div/main/div[1]/div[2]/div/label/select")))
        # sort_dropdown = self.driver.find_element(By.CSS_SELECTOR, "/html/body/div[2]/ps-search-results-module/form/div[2]/ps-search-filters/div/main/div[1]/div[2]/div/label/select")
        print('sort menu found')
        actions = ActionChains(self.driver)
        actions.move_to_element(sort_dropdown).perform()
        try:
            sort_dropdown.click()
            print('dropdown menu clicked')

        except:
            print('sort dropdown cannot be clicked')

        

        newest_option = self.driver.find_element(By.CSS_SELECTOR, "[value='1']")
        
        newest_option.click()

        print("Sorted by Newest")

        

    class Article:
        def __init__(self, article_data):
            self.title = article_data.get('title')
            self.date = article_data.get('date')
            self.description = article_data.get('description')
            self.image = article_data.get('image')
            self.count = article_data.get('count')



    def check_pub_date(self, pub_date_str):
        formats = ['%B %d, %Y', '%b. %d, %Y', '%b %d, %Y']
        current_date = datetime.now()
        three_months_ago = current_date - timedelta(days=3*30)

        for fmt in formats:
            try:
                pub_date = datetime.strptime(pub_date_str, fmt)
                print("Correct Date", pub_date, "stored three months ago is", three_months_ago)
                return pub_date  # Return the parsed date if successful
            except ValueError as e:
                print(f"Error parsing date '{pub_date_str}' with format '{fmt}': {e}")
                continue
        
        return None  # Return None if all formats fail


    def pull_data(self):

        all_data = []
        search_word = "education"

        while True:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.page-content > ps-search-results-module > form > div.search-results-module-ajax > ps-search-filters > div > main > ul")))
            posts = self.driver.find_element(By.CSS_SELECTOR, "body > div.page-content > ps-search-results-module > form > div.search-results-module-ajax > ps-search-filters > div > main > ul")   
            articles = posts.find_elements(By.TAG_NAME, "li")
            time.sleep(2)

            for article in articles:
                title = None
                word_count_title = None
                desc = None
                word_count_desc = None
                img = None
                
                time.sleep(2)
                title = article.find_element(By.CLASS_NAME, "promo-title")
                word_count_title = title.text.lower().count(search_word.lower())
                desc = article.find_element(By.CLASS_NAME,"promo-description")
                word_count_desc = desc.text.lower().count(search_word.lower())
                img = article.find_element(By.CLASS_NAME,"promo-media")
                image = img.find_element(By.TAG_NAME, "img")
                image_src = image.get_attribute("src")
                pub_date_elem = article.find_element(By.CLASS_NAME, "promo-timestamp")
                pub_date_str = pub_date_elem.text
                pub_date = self.check_pub_date(pub_date_str)

                article_data = self.Article(title, pub_date, word_count_title, word_count_desc, desc, image_src)
                all_data.append(article_data)

                print(f"The title: '{title.text}'")
                print(f"The word '{search_word}' appears {word_count_title} times in the title.")              
                print(f"The word '{search_word}' appears {word_count_desc} times in the description.")
                print(f"The description: '{desc.text}'")
                print(f"Image source: {image_src}")
                print('-='*90)
                self.delete_popup(0.1)

            print('Clicking next')
            self.delete_popup(1)
            self.driver.find_element(By.CSS_SELECTOR, "div > .search-results-module-next-page").click()
            self.delete_popup(1)
            
            return all_data


        
        

    def export(self, all_data):
        scraped_data = []

        for data in all_data:
            # Extract data from each article
            title = data.title.text
            word_count = data.word_count
            desc = data.desc.text
            image_src = data.image.get_attribute("src")
            pub_date_str = data.pub_date.text

            # Append to scraped_data list
            scraped_data.append({
                "title": title,
                "word count": word_count,
                "description": desc,
                "Image source": image_src,
                "publish date": pub_date_str
            })

        df = pd.DataFrame(scraped_data)
        df.to_excel("scraped_data.xlsx", sheet_name="Scraped Data", index=False)
        print("Data exported successfully to scraped_data.xlsx!")



    def __exit__(self, exc_type, exc_value, traceback):
        if self.teardown:
            self.driver.quit()

