from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://in.pinterest.com/")
driver.maximize_window()
sleep(3)

# to the bottom of the page
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
sleep(5)

#to the origin of the page
driver.execute_script("window.scrollTo(0,0);")
sleep(3)

#using Scroll By
driver.execute_script("window.scrollBy(0,1000);")
sleep(2)
driver.execute_script("window.scrollTo(0,-500);")
sleep(2)

#scrolling to element
ele = driver.find_element(By.XPATH,'//img[contains(@alt, "Photo of a woman in a cherry-patterned sweater vest, white")]')

driver.execute_script('arguments[0].scrollIntoView();',ele)
sleep(2)

#clicking
ele1 = driver.find_element(By.XPATH,'(//div[@class="lIkAnG eMU5i5 o5UlW_ hL1e7w"])[2]')
driver.execute_script('arguments[0].click();',ele1)
sleep(5)


driver.quit()