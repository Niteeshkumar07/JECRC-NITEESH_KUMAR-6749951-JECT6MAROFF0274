from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=opts)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()



# name3 = driver.find_elements(By.NAME,'gender')
# value = input('Enter gender: ')
# for i in name3:
#     if i.get_attribute("value") == value:
#         i.click()
#         sleep(5)
#         break
#
# sleep(5)




