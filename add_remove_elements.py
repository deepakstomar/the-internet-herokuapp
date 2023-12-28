
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

TARGET_WEB_PAGE = 'https://the-internet.herokuapp.com/'
CHROME_PATH = '/home/my/Downloads/chromedriver-linux64/chromedriver'

service = Service(CHROME_PATH)

driver = webdriver.Chrome(service=service)
driver.get(TARGET_WEB_PAGE)
action = ActionChains(driver)

link = driver.find_element(By.XPATH, "//a[normalize-space()='Add/Remove Elements']")
link.click()

add_button = driver.find_element(By.XPATH, "//button[@onclick='addElement()']")
# add_button.click()
action.click(on_element=add_button)
action.click(on_element=add_button)
action.click(on_element=add_button)
action.click(on_element=add_button)
action.click(on_element=add_button)
action.perform()

# time.sleep(5)
delete_buttons = driver.find_elements(By.XPATH, "//button[@class='added-manually']")

for delete_button in delete_buttons:
    delete_button.click()

# time.sleep(5)

driver.quit()
