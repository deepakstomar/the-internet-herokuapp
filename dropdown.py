import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

CHROME_PATH = '/home/my/Downloads/chromedriver-linux64/chromedriver'
TARGET_WEB_PAGE = 'https://the-internet.herokuapp.com/'

service = Service(CHROME_PATH)

option = Options()
option.add_argument('--headless')

driver = webdriver.Chrome(service=service)
action = ActionChains(driver)
driver.get(TARGET_WEB_PAGE)

drag_and_drop_link = driver.find_element(By.XPATH, "//a[normalize-space()='Dropdown']")
drag_and_drop_link.click()

select = Select(driver.find_element(By.ID, "dropdown"))
select.select_by_visible_text("Option 2")
time.sleep(2)

driver.quit()

