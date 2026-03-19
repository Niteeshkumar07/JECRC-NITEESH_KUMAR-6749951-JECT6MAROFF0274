
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

# driver.get('https://abc.com/')
# driver.maximize_window()
# driver.implicitly_wait(1) ## it is only applicable for find element as element have to present in the dom structure
#
# name = driver.find_element(By.XPATH, '(//a[@class="AnchorLink"]/parent::li/descendant::img)[1]')
# print(name.get_attribute('src'))

wait_obj = WebDriverWait(driver, 10,poll_frequency=200)
submit_button = wait_obj.until(EC.element_to_be_clickable((By.ID,'button')))
submit_button.click()



driver.quit()