from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)

driver.get("https://www.flipkart.com/")
driver.maximize_window()
sleep(2)
driver.find_element(By.CLASS_NAME,"b3wTlE").click()
search = driver.find_element(By.NAME,"q")
search.send_keys("mobile")
print(search.get_attribute("value"))

search.send_keys(Keys.ENTER)

driver.find_element(By.CLASS_NAME,"ybaCDx").click()
name4 = driver.find_element(By.CLASS_NAME,"buvtMR")
print(name4.text)

name5 = driver.find_element(By.XPATH,'//div[@class="lWX0_T"]/child::img')
print(name5.get_attribute("src"))

sleep(5)
driver.quit()
