from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)

driver.get("https://www.lenskart.com/")
driver.maximize_window()
sleep(5)

# eye= driver.find_element(By.ID,'lrd1')
# # print(eye.text)
#
#
# # assert 'GLASSES' == eye.text,'did not find EYEGLASSES'
# assert 'EYEGLASSES' == eye.text,'did not find EYEGLASSES'
# print('success')


driver.quit()
