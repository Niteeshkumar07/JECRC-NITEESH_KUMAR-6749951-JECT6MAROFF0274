from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.royalchallengers.com/')
driver.maximize_window()

actions = ActionChains(driver)
photo = driver.find_element(By.XPATH, '//img[@alt="Devdutt Padikkal"]')
actions.move_to_element(photo).perform()
sleep(5)

i=5
while i > 0:
    actions.send_keys(Keys.PAGE_UP).perform()
    sleep(5)
    i=i-1

sleep(5)

driver.quit()