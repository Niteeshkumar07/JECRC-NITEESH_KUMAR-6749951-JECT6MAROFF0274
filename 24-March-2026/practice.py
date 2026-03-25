from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://demoqa.com/alerts")
driver.maximize_window()
sleep(2)

wait = WebDriverWait(driver, 10)
driver.find_element(By.XPATH,'//button[@id="timerAlertButton"]').click()
alert = wait.until(EC.alert_is_present())
sleep(2)
alert.accept()
sleep(2)

driver.quit()