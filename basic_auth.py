import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
    
CHROME_PATH = '/home/my/Downloads/chromedriver-linux64/chromedriver'
# TARGET_WEB_PAGE = 'https://the-internet.herokuapp.com/'
TARGET_WEB_PAGE = 'http://admin:admin@the-internet.herokuapp.com/basic_auth'

service = Service(CHROME_PATH)

options = Options()
options.add_argument('--headless')

driver = webdriver.Chrome(service=service)
driver.get(TARGET_WEB_PAGE)

# basic_auth_link = driver.find_element(By.XPATH, "//a[normalize-space()='Basic Auth']")
# basic_auth_link.click()

time.sleep(5)

# alert = driver.switch_to.alert
# print(alert.text)

driver.quit()
