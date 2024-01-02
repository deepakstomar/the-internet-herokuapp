import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

CHROME_PATH = '/home/my/Downloads/chromedriver-linux64/chromedriver'
TARGET_WEB_PAGE = 'https://the-internet.herokuapp.com/'

service = Service(CHROME_PATH)

options = Options()
options.add_argument('--headless')

driver = webdriver.Chrome(service=service)
driver.get(TARGET_WEB_PAGE)

checkbox_link = driver.find_element(By.XPATH, "//a[normalize-space()='Checkboxes']")
checkbox_link.click()

checkbox_1 = driver.find_element(By.XPATH, '//input[1]')
time.sleep(5)
checkbox_1.click()

checkbox_2 = driver.find_element(By.XPATH, '//input[2]')
checkbox_2.click()

driver.quit()
