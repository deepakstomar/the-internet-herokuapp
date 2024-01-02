import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

CHROME_PATH = '/home/my/Downloads/chromedriver-linux64/chromedriver'
TARGET_WEB_PAGE = 'https://the-internet.herokuapp.com/'

service = Service(CHROME_PATH)

options = Options()
options.add_argument('--headless')

driver = webdriver.Chrome(service=service)
driver.get(TARGET_WEB_PAGE)

checkbox_link = driver.find_element(By.XPATH, "//a[normalize-space()='Context Menu']")
checkbox_link.click()

box = driver.find_element(By.ID, 'hot-spot')
action = ActionChains(driver)
action.context_click(box)
action.perform()

# time.sleep(2)

# Switching to alert window
alert_window = driver.switch_to.alert

# Perform click operation on alert window
alert_window.accept()

# time.sleep(2)

driver.quit()
