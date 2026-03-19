from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)
driver.get('https://qavbox.github.io/demo/signup/')
driver.maximize_window()

wait = WebDriverWait(driver, 10)

first = wait.until(EC.presence_of_element_located((By.ID, 'username')))
first.send_keys('Nikhil')

email = wait.until(EC.presence_of_element_located((By.ID, 'email')))
email.send_keys('Temporary@gmail.com')

tel = wait.until(EC.presence_of_element_located((By.ID, 'tel')))
tel.send_keys('+91 324561799')


file = wait.until(EC.presence_of_element_located((By.NAME, 'datafile')))
file.send_keys(r"C:\Users\Niteesh Kumar\Downloads\image_53e153f4.png")

drop = wait.until(EC.presence_of_element_located((By.NAME,'sgender')))
value = Select(drop)
value.select_by_value('male')

radio = wait.until(EC.presence_of_element_located((By.XPATH,'//input[@value="one"]')))
radio.click()

checkbox = wait.until(EC.presence_of_element_located((By.XPATH,'//input[@value="manualtesting"]')))
checkbox.click()

drop1 = wait.until(EC.presence_of_element_located((By.ID, 'tools')))
value1 = Select(drop1)
value1.select_by_value('selenium')
value1.select_by_index(4)

submit = wait.until(EC.presence_of_element_located((By.ID,'submit')))
submit.click()

sleep(5)
driver.quit()







