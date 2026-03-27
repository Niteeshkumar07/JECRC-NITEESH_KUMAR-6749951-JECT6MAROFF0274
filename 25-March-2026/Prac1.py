from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(2)
wait = WebDriverWait(driver, 15)

assert "Amazon" in driver.title, "Failed"
sleep(2)
assert "amazon.in" in driver.current_url, "Failed"
sleep(2)

search = driver.find_element(By.ID,'twotabsearchtextbox')
search.send_keys('Headphones')
search.send_keys(Keys.ENTER)
sleep(2)

brand = driver.find_element(By.XPATH,'(//i[@class="a-icon a-icon-checkbox"])[5]')
brand.click()
sleep(5)

driver.find_element(By.XPATH,'//li[@id="p_36/dynamic-picker-0"]/child::span/a').click()
sleep(5)

driver.find_element(By.XPATH,'(//span[@class="rush-component"])[4]').click()
sleep(5)

product_title = driver.find_element(By.XPATH,'//a[@class="a-link-normal s-line-clamp-2 puis-line-clamp-3-for-col-4-and-8 s-link-style a-text-normal"]/child::h2/span')
print(product_title.text)

product_price = driver.find_element(By.XPATH,'(//span[@class="a-price-whole"])[1]')
print(product_price.text)

all = driver.window_handles
driver.switch_to.window(all[1])

product_Title_after = driver.find_element(By.XPATH,'//span[@id="productTitle"]')
print(product_Title_after.text)

product_price_after = driver.find_element(By.XPATH,'(//span[@class="a-price-whole"])[1]')
print(product_price_after.text)

driver.find_element(By.ID,'add-to-cart-button').click()
driver.find_element(By.XPATH,'//a[contains(text(),"Go to Cart")]').click()

cart_product_title = driver.find_element(By.XPATH,'//span[@class="a-truncate-cut"]')
print(cart_product_title.text)

cart_price = driver.find_element(By.XPATH,'//span[@class="a-price a-text-price sc-product-price sc-white-space-nowrap a-size-medium"]')
print(cart_price.text)

sleep(5)
driver.quit()