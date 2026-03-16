from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=opts)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()


name3 = driver.find_elements(By.XPATH,'//div[@class="form-group"]/child::div[@class="form-check form-check-inline"]/child::input[@type="checkbox"]')
print(len(name3))

for i in name3:
    i.click()
    label = i.find_element(By.XPATH, './following-sibling::label')
    print(label.text)
    sleep(2)

for i in reversed(name3):
    i.click()
    sleep(2)

sleep(5)
driver.quit()

