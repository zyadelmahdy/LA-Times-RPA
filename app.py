from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(excutable_path='chromedriver')
driver = webdriver.Chrome(service=service)

driver.get('https://google.com')
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)
element = driver.find_element(By.CLASS_NAME,"gLFyf")
element.send_keys("Zyad Elmahdy" + Keys.ENTER)

link = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,"Zyad Elmahdy - Software Quality Assurance Specialist"))
)
link.click()

time.sleep(5)

driver.quit()