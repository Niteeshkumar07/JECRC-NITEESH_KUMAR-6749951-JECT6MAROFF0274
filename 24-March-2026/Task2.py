from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://demoqa.com/alerts")
driver.maximize_window()

sleep(2)

wait = WebDriverWait(driver, 10)
driver.find_element(By.ID,'alertButton').click()
alert = wait.until(EC.alert_is_present())
sleep(2)
alert.accept()
sleep(2)

driver.find_element(By.ID,'timerAlertButton').click()
alert = wait.until(EC.alert_is_present())
sleep(2)
alert.accept()
sleep(2)


driver.find_element(By.ID,'confirmButton').click()
alert = wait.until(EC.alert_is_present())
sleep(2)
alert.accept()
sleep(2)

result = driver.find_element(By.ID, "confirmResult")
assert "Ok" in result.text,'Failed'

driver.find_element(By.ID, "promtButton").click()
alert = wait.until(EC.alert_is_present())
sleep(2)
alert.send_keys("Hello")
alert.accept()
sleep(2)

result = driver.find_element(By.ID, "promptResult")
assert "Hello" in result.text,'Failed'


sleep(3)
driver.quit()