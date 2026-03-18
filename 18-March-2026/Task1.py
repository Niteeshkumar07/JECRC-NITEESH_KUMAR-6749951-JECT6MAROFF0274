from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)
driver.get('https://the-internet.herokuapp.com/')
driver.maximize_window()

first = driver.find_element(By.LINK_TEXT,'Checkboxes')
print(first.text)

second = driver.find_element(By.PARTIAL_LINK_TEXT,'Drag')
print(second.text)

third = driver.find_elements(By.TAG_NAME,'li')
print(len(third))

driver.get('https://the-internet.herokuapp.com/tables')

fourth = driver.find_element(By.XPATH,'//td[text()="jdoe@hotmail.com"]/following-sibling::td[2]')
print(fourth.text)

fifth = driver.find_element(By.XPATH,'//td[text()="Bach"]/following-sibling::td[5]/a[2]')
print(fifth.text)

sixth = driver.find_element(By.XPATH,'//div[@class="example"]/table[2]')
print(sixth.text)

seventh = driver.find_element(By.XPATH,'//td[text()="$100.00"]')
print(seventh.text)

seventh_parent = driver.find_element(By.XPATH, '//td[text()="$100.00"]/parent::tr')
print(seventh_parent)





sleep(5)
driver.quit()