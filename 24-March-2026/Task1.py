from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.get('https://codepen.io/gdw96/pen/jOypoYL')
driver.maximize_window()

sleep(5)

iframe = driver.find_element(By.ID, 'result')
driver.switch_to.frame(iframe)

user = driver.find_element(By.ID, 'username')
user.clear()
user.send_keys('Mohan')

password = driver.find_element(By.ID, 'password')
password.clear()
password.send_keys('123456')

action = ActionChains(driver)
hold = driver.find_element(By.CLASS_NAME, "fa-eye")
action.click_and_hold(hold).perform()
sleep(2)
action.release().perform()

register = driver.find_element(By.CLASS_NAME, 'submit')
register.click()
sleep(2)

driver.back()

sleep(5)
iframe = driver.find_element(By.ID, 'result')
driver.switch_to.frame(iframe)

name = driver.find_element(By.XPATH, '//div[@class="container"]/h1')
assert "Registration" in name.text, "Registration not found"

sleep(5)
driver.quit()