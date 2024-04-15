from selenium import webdriver

driver = webdriver.Chrome()

class Apnews(webdriver.Chrome):
    def __init__(self, driver=driver):
        self.driver_path = driver
        super(Apnews, self).__init__()

    def land_first_page(self):
        self.get('https://apnews.com/')
