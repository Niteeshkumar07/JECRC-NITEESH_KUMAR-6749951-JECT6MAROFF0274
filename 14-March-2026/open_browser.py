from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)
driver.get("https://testautomationpractice.blogspot.com/")
# driver.implicitly_wait(10)
sleep(10)
# name1 = driver.find_element(By.XPATH,'//span[@id="nav-search-label-id"]/ancestor::div[@class="nav-left"]')
# # name1.click()
# print(name1)
# name2 = driver.find_element(By.XPATH,'//span[contains(text(),"All")]/ancestor::div[@id="nav-main"]')
# print(name2)
#
# # //div[@id="nav-main"]/descendant::span[text()="All"]
# name3 = driver.find_element(By.XPATH,'//div[@id="nav-main"]/descendant::span[text()="All"]')
# print(name3)

# parent,child,siblings

# preceding-sibling -> middle-to elder
# following-sibling -> middle to younger

# v = driver.find_element(By.XPATH,'//a[text()="Fresh"]/ancestor::li/following-sibling::li[4]')
# print(v)

# siblings = driver.find_element(By.XPATH, '//a[@class="nav-a  "]/ancestor::li/following-sibling::li[2]')
# print(siblings)

# name4 = driver.find_element(By.LINK_TEXT,"Fresh")
# print(name4)

# name4 = driver.find_element(By.PARTIAL_LINK_TEXT, "Fre")
# name4.click()
# print(name4)

# //td[text()="Learn Java"]/following-sibling::td[3]
# name4 = driver.find_elements(By.XPATH,'//td[text()="300"]/preceding-sibling::td[3]')
# print(name4)
# print(len(name4))

name5 = driver.find_elements(By.XPATH,'//tbody[@id="rows"]/child::tr/child::td[1]')
print(len(name5))

driver.quit()






