from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)
driver.get("https://www.wikipedia.org/")
sleep(4)
#
# logo = driver.find_element(By.ID,'js-link-box-en')
# print(logo)
# bar = driver.find_element(By.ID,'search-form')
# print(bar)
# inp = driver.find_element(By.ID,'searchInput')
# print(inp)
# toggle = driver.find_element(By.ID,'searchLanguage')
# print(toggle)
#
# # CLASS NAME
# head = driver.find_elements(By.CLASS_NAME,'jsl10n-visible')
# print(head)
# head1 = driver.find_elements(By.CLASS_NAME,'central-textlogo')
# print(head1)
# head3 = driver.find_elements(By.CLASS_NAME,'footer')
# print(head3)
# head4 = driver.find_elements(By.CLASS_NAME,'footer-sidebar-icon')
# print(head4)
# head5 = driver.find_elements(By.CLASS_NAME,'svg-language-icon')
# print(head5)
#
# # NAME
# name1 = driver.find_element(By.NAME,'search')
# print(name1)
# name3 = driver.find_element(By.NAME,'go')
# print(name3)
# name4 = driver.find_element(By.NAME,'language')
# print(name4)
# name5 = driver.find_element(By.NAME,'search')
# print(name5)
# # TAG NAME
#
# tag1 = driver.find_element(By.TAG_NAME,'a')
# print(tag1)
# tag2 = driver.find_element(By.TAG_NAME,'div')
# print(tag2)
# tag3 = driver.find_element(By.TAG_NAME,'span')
# print(tag3)
# tag4 = driver.find_element(By.TAG_NAME,'form')
# print(tag4)
# tag5 = driver.find_element(By.TAG_NAME,'input')
# print(tag5)

x1 = driver.find_element(By.XPATH,'//input[@id="searchInput"]')
print(x1)
x2 = driver.find_element(By.XPATH,'//span[@class="lang-list-button-text jsl10n"]')
print(x2)
x3 = driver.find_element(By.XPATH,'//div[@class="footer-sidebar-icon sprite svg-wikipedia_app_tile"]')
print(x3)
x4 = driver.find_element(By.XPATH,'(//div[@class="other-project"])[3]')
print(x4)
x5 = driver.find_element(By.XPATH,'//p[@class="site-license"]')
print(x5)

name1 = driver.find_element(By.XPATH,'//div[@class="central-textlogo"]')
print(name1)
name2 = driver.find_element(By.XPATH,'//span[contains(text(),"Read Wikipedia")]')
print(name2)


