from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://www.myntra.com/')
driver.maximize_window()
wait = WebDriverWait(driver, 10)
action = ActionChains(driver)

men = wait.until(EC.visibility_of_element_located((By.XPATH,'//a[@data-group="men"]')))
action.move_to_element(men).perform()

wait.until(EC.element_to_be_clickable((By.XPATH,'//ul[@class="desktop-navBlock"]/child::li[3]'))).click()
# item = driver.find_element(By.XPATH,'//ul[@class="desktop-navBlock"]/child::li[3]').click()
sleep(2)

photo = wait.until(EC.presence_of_element_located((By.XPATH,'(//h3[@class="product-brand"])[20]')))
action.move_to_element(photo).perform()
sleep(5)

driver.quit()

