import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

CHROME_PATH = '/home/my/Downloads/chromedriver-linux64/chromedriver'
TARGET_WEB_PAGE = 'https://the-internet.herokuapp.com/'

service = Service(CHROME_PATH)

option = Options()
option.add_argument('--headless')

driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get(TARGET_WEB_PAGE)

multiple_window_link = driver.find_element(By.XPATH, "//a[normalize-space()='JavaScript Alerts']")
multiple_window_link.click()

js_alert = driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
js_alert.click()

wait = WebDriverWait(driver, 5)
alert = wait.until(expected_conditions.alert_is_present())
time.sleep(1)
alert.accept()

js_confirm = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
js_confirm.click()
# wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.alert_is_present())

# Different approach to store alert
alert = driver.switch_to.alert

time.sleep(1)
alert.dismiss()

time.sleep(1)

js_prompt = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
js_prompt.click()

wait.until(expected_conditions.alert_is_present())
alert = Alert(driver)
alert.send_keys("Sending keys to this alert")
time.sleep(2)
alert.accept()

time.sleep(1)

driver.quit()
