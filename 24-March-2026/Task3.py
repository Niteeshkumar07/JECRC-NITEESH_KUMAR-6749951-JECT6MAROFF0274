from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get('https://demoqa.com/browser-windows')
driver.maximize_window()

parent = driver.current_window_handle

driver.find_element(By.ID, 'tabButton').click()
sleep(2)
all_windows = driver.window_handles
driver.switch_to.window(all_windows[1])
sleep(1)
result = driver.find_element(By.XPATH, '//h1')
assert "sample page" in result.text.lower(), "Failed"
sleep(1)

driver.switch_to.window(parent)
driver.find_element(By.ID, 'windowButton').click()
sleep(2)
all_windows = driver.window_handles
driver.switch_to.window(all_windows[2])
result = driver.find_element(By.XPATH, '//h1')
sleep(1)
assert "sample page" in result.text.lower(), "Failed"


driver.switch_to.window(parent)
driver.find_element(By.ID, 'messageWindowButton').click()

all_windows = driver.window_handles
driver.switch_to.window(all_windows[3])
result = driver.find_element(By.TAG_NAME,'body')


driver.quit()