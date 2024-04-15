from apnews.const import Apnews
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

apnews_instance = Apnews()

apnews_instance.land_first_page()

WebDriverWait(apnews_instance, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "AnClick-MainNav")))

element = apnews_instance.find_element(By.CLASS_NAME, "AnClick-MainNav")
element.click()

time.sleep(5)

apnews_instance.quit()
