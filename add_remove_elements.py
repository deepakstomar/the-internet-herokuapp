from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

TARGET_WEB_PAGE = 'https://the-internet.herokuapp.com/'
CHROME_PATH = '/home/my/Downloads/chromedriver-linux64/chromedriver'

service = Service(CHROME_PATH)

driver = webdriver.Chrome(service=service)
driver.get(TARGET_WEB_PAGE)