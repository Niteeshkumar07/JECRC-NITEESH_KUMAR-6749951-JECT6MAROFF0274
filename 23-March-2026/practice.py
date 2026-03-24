from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.get('https://demoqa.com/droppable')
driver.maximize_window()

actions = ActionChains(driver)
sleep(5)
origin = driver.find_element(By.ID,'draggable')
target = driver.find_element(By.ID,'droppable')

actions.drag_and_drop(origin,target).perform()

assert "Dropped!" == target.text,'Failed'

sleep(5)
driver.quit()