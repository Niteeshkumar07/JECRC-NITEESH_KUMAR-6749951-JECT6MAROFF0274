from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)
driver.get("https://www.wikipedia.org/")

name = driver.find_element(By.NAME,'search')
name.send_keys("Encylopedia",Keys.ENTER)

# name2 = driver.find_element(By.XPATH,'//button[@type="submit"]')
# name2.click()

sleep(5)
driver.quit()