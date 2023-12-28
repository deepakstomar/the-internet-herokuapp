import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

TARGET_WEB_PAGE = 'https://the-internet.herokuapp.com/'
CHROME_PATH = '/home/my/Downloads/chromedriver-linux64/chromedriver'

service = Service(CHROME_PATH)

driver = webdriver.Chrome(service=service)
driver.get(TARGET_WEB_PAGE)

element = driver.find_element(By.XPATH, "//a[normalize-space()='A/B Testing']")
element.click()

header = driver.find_element(By.XPATH, "//div[@class='example']/h3")
header_text = header.text

assert header_text == 'A/B Test Variation 1', 'Header changed to A/B Test Control'

time.sleep(5)
driver.quit()
