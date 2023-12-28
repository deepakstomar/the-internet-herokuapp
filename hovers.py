import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

CHROME_PATH = '/home/my/Downloads/chromedriver-linux64/chromedriver'
TARGET_WEB_PAGE = 'https://the-internet.herokuapp.com/'

service = Service(CHROME_PATH)
options = Options()
options.add_argument('--headless')  # Comment this if you want to see browser

driver = webdriver.Chrome(service=service, options=options)
action = ActionChains(driver)

driver.get(TARGET_WEB_PAGE)

hover_link = driver.find_element(By.CSS_SELECTOR, 'a[href="/hovers"]')
hover_link.click()

username = list()

figures = driver.find_elements(By.XPATH, '//div[@class="figure"]')

for figure in figures:
    action.move_to_element(figure)
    action.perform()
    name = figure.find_element(By.TAG_NAME, 'h5')
    link = figure.find_element(By.TAG_NAME, 'a')
    username.append((name.text[len('name: '):], link.get_attribute('href')))

print(username)
# time.sleep(5)

driver.quit()
