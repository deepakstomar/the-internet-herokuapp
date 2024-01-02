# import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

CHROME_PATH = '/home/my/Downloads/chromedriver-linux64/chromedriver'
TARGET_WEB_PAGE = 'https://the-internet.herokuapp.com/'

service = Service(CHROME_PATH)

option = Options()
option.add_argument('--headless')

driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get(TARGET_WEB_PAGE)

multiple_window_link = driver.find_element(By.XPATH, "//a[normalize-space()='Multiple Windows']")
multiple_window_link.click()

click_here_link = driver.find_element(By.XPATH, "//a[normalize-space()='Click Here']")
click_here_link.click()

# time.sleep(2)

driver.switch_to.window(driver.window_handles[1])
driver.close()

# time.sleep(2)

driver.switch_to.window(driver.window_handles[0])
driver.quit()
