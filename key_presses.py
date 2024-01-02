# import time
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

CHROME_PATH = '/home/my/Downloads/chromedriver-linux64/chromedriver'
TARGET_WEB_PAGE = 'https://the-internet.herokuapp.com/'

service = Service(CHROME_PATH)

option = Options()
option.add_argument('--headless')

driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get(TARGET_WEB_PAGE)

multiple_window_link = driver.find_element(By.XPATH, "//a[normalize-space()='Key Presses']")
multiple_window_link.click()

seconds = 0.5

action = ActionChains(driver)
action.send_keys(Keys.CONTROL)
action.pause(seconds)
action.send_keys(Keys.SHIFT)
action.pause(seconds)
action.send_keys(Keys.ESCAPE)
action.pause(seconds)
action.send_keys(Keys.ENTER)
action.perform()

time.sleep(0.5)

driver.quit()
