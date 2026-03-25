import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

folder = os.path.join(os.getcwd(), 'screenshots')
os.makedirs(folder,exist_ok=True)

driver = webdriver.Chrome()
driver.get("https://in.pinterest.com/")
driver.maximize_window()
actions = ActionChains(driver)

sleep(5)

driver.save_screenshot(os.path.join(f'{folder}/full_page.png'))
sleep(5)

ele = driver.find_element(By.XPATH,'//img[contains(@alt, "Photo of a woman in a cherry-patterned sweater vest, white")]')
actions.scroll_to_element(ele).perform()
sleep(3)

ele.screenshot(f'{folder}/image.png')
sleep(3)

driver.quit()

