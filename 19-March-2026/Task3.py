from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)
driver.get('https://www.amazon.in/')
driver.maximize_window()

wait = WebDriverWait(driver, 10)

search = wait.until(EC.presence_of_element_located((By.ID,'twotabsearchtextbox')))
search.send_keys('mobiles')

bar = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="left-pane-results-container"]/div[4]')))
bar.click()

wait.until(EC.presence_of_element_located((By.XPATH, '//span[@data-action="a-dropdown-button"]'))).click()
wait.until(EC.presence_of_element_located((By.ID,'s-result-sort-select_4'))).click()

wait.until(EC.presence_of_element_located((By.XPATH, '(//i[@class="a-icon a-icon-checkbox"])[3]'))).click()

product = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="a-section a-spacing-small a-spacing-top-small"]//h2')))
print(product.get_attribute('aria-label'))

price = wait.until(EC.presence_of_element_located((By.XPATH, '//span[@class="a-price"]/child::span')))
print(price.get_attribute('innerHTML'))

sleep(10)
driver.quit()


