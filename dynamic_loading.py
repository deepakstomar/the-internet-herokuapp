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

element = driver.find_element(By.XPATH, "//a[normalize-space()='Dynamic Loading']")
element.click()

first_example_link = driver.find_element(By.XPATH, "//div[@class='example']/a")
first_example_link.click()

start_button = driver.find_element(By.XPATH, "//div[@id='start']/button")
start_button.click()

content = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@id='finish']/h4"))
)

print(content.text)

driver.back()

second_example_link = driver.find_element(By.XPATH, '//div[@class="example"]/a[2]')
second_example_link.click()

start_button = driver.find_element(By.XPATH, "//div[@id='start']/button")
start_button.click()

second_example_content = content = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@id='finish']/h4"))
)

print(second_example_content.text)
driver.quit()
