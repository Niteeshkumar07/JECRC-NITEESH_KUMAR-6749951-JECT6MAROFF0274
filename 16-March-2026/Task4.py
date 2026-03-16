from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://opensource-demo.orangehrmlive.com/")

print(driver.title)

sleep(3)

username = driver.find_element(By.NAME, "username")
username.send_keys("Admin")

password = driver.find_element(By.NAME, "password")
password.send_keys("admin123",Keys.ENTER)



sleep(5)
url = driver.current_url
print(driver.current_url)

if "dashboard" in url:
    print("successful login")

driver.quit()