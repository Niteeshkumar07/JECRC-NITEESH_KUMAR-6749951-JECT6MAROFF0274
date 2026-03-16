from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://demoqa.com/radio-button")

print(driver.title)
sleep(5)

name = driver.find_element(By.ID,'yesRadio')
name.click()
text = driver.find_element(By.CLASS_NAME,'text-success')
print(text.text)

print(name.get_attribute('class'))
print(name.get_attribute('id'))

print(driver.current_url)

sleep(3)



driver.quit()