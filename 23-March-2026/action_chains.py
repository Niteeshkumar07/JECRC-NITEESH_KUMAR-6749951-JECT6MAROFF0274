from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# drag and drop

# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/drag_and_drop")
# driver.maximize_window()
# sleep(3)
#
#
# actions = ActionChains(driver)
# origin = driver.find_element(By.ID,'column-a')
# target = driver.find_element(By.ID,'column-b')
#
# actions.drag_and_drop(origin,target).perform()
# sleep(5)

# Mouse Hover

# driver = webdriver.Chrome()
# driver.get("https://supertails.com/")
# driver.maximize_window()
#
# action = ActionChains(driver)
# dog = driver.find_element(By.XPATH,'(//span[contains(text(),"Dogs")])')
# action.move_to_element(dog).perform()
# sleep(5)

#Scrolling Element and amount
# driver = webdriver.Chrome()
# driver.get('https://supertails.com/')
# driver.maximize_window()
#
# # cat = driver.find_element(By.XPATH,'//div[@data-ganame="Breed 5"]')
# action = ActionChains(driver)
# action.scroll_to_element(cat).perform()
# sleep(5)
#
# action.scroll_by_amount(0,-1500).perform()
# sleep(10)
# action.click()

#KeyBoard Actions
# driver = webdriver.Chrome()
# driver.get('https://supertails.com/')
# driver.maximize_window()
# action = ActionChains(driver)

# action.send_keys(Keys.PAGE_DOWN).perform()
# sleep(5)
# action.send_keys(Keys.PAGE_UP).perform()
# sleep(5)
# action.key_down(Keys.CONTROL).send_keys('a').perform()
# sleep(5)
# action.key_up(Keys.CONTROL).perform()
# sleep(2)


# copying and pasting for address fields
# driver = webdriver.Chrome()
# driver.get(r'C:\Users\Niteesh Kumar\OneDrive\Desktop\seleniumPractice\23-March-2026\action.html')
# driver.maximize_window()
# action = ActionChains(driver)
# present = driver.find_element(By.ID,'presentAddress')
# permanent = driver.find_element(By.ID,'permanentAddress')
# present.send_keys("Jecrc, Jaipur")
# sleep(2)
# present.click()
# action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
# sleep(1)
# action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
# permanent.click()
# action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
# sleep(5)

#password visibility

driver = webdriver.Chrome()
driver.get(r'C:\Users\Niteesh Kumar\OneDrive\Desktop\seleniumPractice\23-March-2026\index1.html')
driver.maximize_window()
driver.find_element(By.ID,'password').send_keys('nik')
sleep(3)
show_pwd = driver.find_element(By.ID,'eyeBtn')
action = ActionChains(driver)
action.click_and_hold(show_pwd).perform()
sleep(3)
action.release().perform()
sleep(2)
driver.quit()

