# from .const import initialize_driver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException, NoSuchElementException
# import time, datetime, re
# from datetime import datetime, timedelta
# from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from openpyxl import Workbook
# from selenium import webdriver

# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(options=options)
# class LATimes:
#     def __init__(self, teardown=False):
#         self.driver = initialize_driver()
#         self.teardown = teardown
#     def __enter__(self):
#         return self

#     def load_first_page(self):
#         self.driver.get('https://www.latimes.com/')
        
#         try:
#             WebDriverWait(self.driver, 200).until(EC.presence_of_element_located((By.XPATH, "/html/body/ps-header/header/div[2]/button")))
#             print("Body loaded successfully")
#         except TimeoutException:
#             print("Timeout: Failed to load LA Times within 10 seconds.")


#     def search(self, search_word):
#         magnify_icon = self.driver.find_element(By.XPATH, '/html/body/ps-header/header/div[2]/button')
#         time.sleep(2)

#         magnify_icon.click()
#         WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/ps-header/header/div[2]/div[2]/form/label/input')))
#         search_bar = self.driver.find_element(By.XPATH, '/html/body/ps-header/header/div[2]/div[2]/form/label/input')
#         time.sleep(2)
#         search_bar.send_keys(f'{search_word}')
#         time.sleep(1)
#         search_bar.send_keys(Keys.ENTER)


#     def filter(self, selected_items):

#         try:
#             WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/ps-search-results-module/form/div[2]/ps-search-filters/div/aside/div/div[3]/div[1]/ps-toggler/ps-toggler/button")))
#             see_more_btn = self.driver.find_element(By.XPATH, "/html/body/div[2]/ps-search-results-module/form/div[2]/ps-search-filters/div/aside/div/div[3]/div[1]/ps-toggler/ps-toggler/button")

#             see_more_btn.click()
#         except TimeoutException:
#             print("Timeout: Failed to delete the pop up within 10 seconds.")

#         list_items = self.driver.find_elements(By.XPATH, "/html/body/div[2]/ps-search-results-module/form/div[2]/ps-search-filters/div/aside/div/div[3]/div[1]/ps-toggler/ps-toggler/div/ul")


#     def sort_newest(self):
        

        
#         politics = self.driver.find_element(By.XPATH, "/html/body/div[2]/ps-search-results-module/form/div[2]/ps-search-filters/div/aside/div/div[3]/div[1]/ps-toggler/ps-toggler/div/ul/li[3]/div/div[1]/label/input")
#         actions = ActionChains(self.driver)
#         actions.move_to_element(politics).perform()
        
#         try:
#             WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "metering-bottompanel")))
#             print('popup found')
#             element = self.driver.find_element(By.NAME,"metering-bottompanel")
#             self.driver.execute_script("""var element = arguments[0]; element.parentNode.removeChild(element);""", element)
#             print("Pop up deleted successfully")
#         except TimeoutException:
#             print("Timeout: Failed to delete the pop up within 10 seconds.")
#         politics.click()

#         print('topic chosen')
        


#         WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/ps-search-results-module/form/div[2]/ps-search-filters/div/main/div[1]/div[2]/div/label/select")))
#         sort_dropdown = self.driver.find_element(By.XPATH, "/html/body/div[2]/ps-search-results-module/form/div[2]/ps-search-filters/div/main/div[1]/div[2]/div/label/select")
#         actions = ActionChains(self.driver)
#         actions.move_to_element(sort_dropdown).perform()
        
#         sort_dropdown.click()

#         print('dropdown menu clicked')

        

#         newest_option = self.driver.find_element(By.CSS_SELECTOR, "[value='1']")
        
#         newest_option.click()

#         print("Sorted by Newest")

        

#     class Article :
#         def __init__(self, title,date,description,image,count,contains_money):
#             self.title = title
#             self.date = date
#             self.description = description
#             self.image = image
#             self.count = count
#             self.contains_money = contains_money

#     def delete_banner(self,time=10):
#         try:
#             WebDriverWait(self.driver, time).until(EC.presence_of_element_located((By.NAME, "metering-bottompanel")))
#             print('popup found')
#             element = self.driver.find_element(By.NAME,"metering-bottompanel")
#             self.driver.execute_script("""var element = arguments[0]; element.parentNode.removeChild(element);""", element)
#             print("Pop up deleted successfully")
#         except TimeoutException:
#             print("Timeout: Failed to delete the pop up within " +str(time)+" seconds.")
#         except:
#             pass

#     def pull_data(self):

#         all_data = []
#         search_word = "education"

#         while True:
#             WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.page-content > ps-search-results-module > form > div.search-results-module-ajax > ps-search-filters > div > main > ul")))
#             posts = self.driver.find_element(By.CSS_SELECTOR, "body > div.page-content > ps-search-results-module > form > div.search-results-module-ajax > ps-search-filters > div > main > ul")   
#             articles = posts.find_elements(By.TAG_NAME, "li")
#             for article in articles:
#                 title = article.find_element(By.CLASS_NAME, "promo-title")
#                 word_count = title.text.lower().count(search_word.lower())
#                 desc = article.find_element(By.CLASS_NAME,"promo-description")
#                 img = article.find_element(By.CLASS_NAME,"promo-media")
#                 image = img.find_element(By.TAG_NAME, "img")
#                 image_src = image.get_attribute("src")
#                 pub_date = article.find_element(By.CLASS_NAME, "promo-timestamp")
#                 pub_date_str = pub_date.text

#                 article_data = self.Article(title,pub_date,desc,image,0,0)
#                 all_data.append(article_data)
#                 current_date = datetime.now()
#                 three_months_ago = current_date - timedelta(days=3*30)  # Assuming 30 days per month

#                 # Define formats outside the if block
#                 formats = ['%B %d, %Y', '%b. %d, %Y', '%b %d, %Y']  # Possible date formats

            

#                 print(f"The title: '{title.text}'")

#                 print(f"The word '{search_word}' appears {word_count} times in the title.")              
#                 print(f"The word '{search_word}' appears {word_count} times in the description.")

#                 print(f"The description: '{desc.text}'")
#                 print(f"Image source: {image_src}")
#                 print('-='*90)
#                 self.delete_banner(0.1)



#                 pub_date = None
#                 for fmt in formats:
#                     try:
#                         pub_date = datetime.strptime(pub_date_str, fmt)
#                         print("Correct Date" ,pub_date, "stored three months ago is",three_months_ago)
#                         break  # Exit loop after successful parsing
#                     except ValueError as e:
#                         print(f"Error parsing date '{pub_date_str}' with format '{fmt}': {e}")
#                         continue  # Move on to the next format

#                 if pub_date is not None and pub_date < three_months_ago:
#                     print("Closing because time is more than 3 months")
#                     return all_data
#             print('Clicking next')
#             self.delete_banner(1)
#             self.driver.find_element(By.CSS_SELECTOR, "div > .search-results-module-next-page").click()
#             self.delete_banner(1)
        
        


#     def export(self):
#         title, desc, pub_date, image_src = self.pull_data()
#         news_data = []
#         news_data.append([title, desc, pub_date, image_src])
#         wb = Workbook()
#         ws = wb.active
#         wb.save("news_data.xlsx")

#     def __exit__(self, exc_type, exc_value, traceback):
#         if self.teardown:
#             self.driver.quit()

