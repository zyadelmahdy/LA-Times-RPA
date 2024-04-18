from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def initialize_driver():
    options = Options()
    options.page_load_strategy = 'none'
    return webdriver.Chrome(options=options)