from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
# driver.get('https://testautomationpractice.blogspot.com/')
driver.get('https://www.lenskart.com/sunglasses.html')
driver.maximize_window()

# country_dropdown = driver.find_element(By.ID,'country')
# dropdown = Select(country_dropdown)
# dropdown.select_by_value('australia')
# sleep(4)
# dropdown.select_by_index(3)
# sleep(5)
# dropdown.select_by_visible_text('Japan')
# sleep(5)

drop = driver.find_element(By.ID,'sortByDropdown')
value = Select(drop)
sleep(3)
value.select_by_value('created')

name = driver.find_element(By.XPATH,'//div[@class="sc-23b7d3eb-6 hYdmOJ"]/child::p')
print(name.text)

sleep(5)
driver.quit()

