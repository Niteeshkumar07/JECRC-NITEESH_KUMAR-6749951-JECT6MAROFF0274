from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
# opts.add_argument("--headless")
driver = webdriver.Chrome(options=opts)
driver.get("https://testautomationpractice.blogspot.com/")
sleep(1)
# name = driver.find_element(By.ID,'name')
# phone_no = driver.find_element(By.ID,'phone')
# radio_button = driver.find_elements(By.CLASS_NAME,'form-check-input')
# inp = driver.find_elements(By.TAG_NAME,'input')
# # print(name)
# # print(phone_no)
# print(radio_button)
# print(len(radio_button))
# print('name textfield found')

# name = driver.find_element(By.CSS_SELECTOR,'select[id="animals"]')
# name = driver.find_element(By.CSS_SELECTOR,'#animals')

# <a href="http://testautomationpractice.blogspot.com/">Home</a>
# a[href*="testautomationpractice"]
# a[href^="http://"] ##starting with it
#a[href$=".com"] ## find particular by symbol

# name = driver.find_element(By.CSS_SELECTOR,'a[href$=".com"')
# # input[type="text"][class="rewrite"]
# print(name)

# XPATH
# //input[@id='name'] xpath relative
## div/input/[@id='name'] xpath absolute
##(//input[@id="name"])[1]
# driver.quit()

# x1 = driver.find_element(By.XPATH,'//input[@id="searchInput"]')
# print(x1)

# //a[text()="Home"]
## //a[contains(text(),"jpan")]