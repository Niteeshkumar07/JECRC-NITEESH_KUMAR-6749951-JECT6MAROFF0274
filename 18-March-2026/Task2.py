from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)
driver.get("https://demoqa.com/automation-practice-form")

driver.maximize_window()

first = driver.find_element(By.ID,'firstName')
first.send_keys("Niteesh")

last = driver.find_element(By.ID,'lastName')
last.send_keys("Kumar")

email = driver.find_element(By.ID,'userEmail')
email.send_keys("Temp@gmail.com")

male = driver.find_element(By.XPATH,'//label[text()="Male"]').click()

phone_no = driver.find_element(By.ID,'userNumber')
phone_no.send_keys("9090909090")

subject = driver.find_element(By.ID,'subjectsInput')
subject.send_keys("Maths")
subject.send_keys(Keys.ENTER)


driver.find_element(By.XPATH, "//label[text()='Sports']").click()
driver.find_element(By.XPATH, "//label[text()='Reading']").click()

upload = driver.find_element(By.ID, "uploadPicture")
upload.send_keys(r"C:\Users\Niteesh Kumar\Downloads\statue.webp")


driver.find_element(By.ID, "currentAddress").send_keys("Jaipur")
sleep(2)

driver.find_element(By.ID, "state").click()
driver.find_element(By.XPATH, "//div[text()='NCR']").click()

driver.find_element(By.ID, "city").click()
driver.find_element(By.XPATH, "//div[text()='Gurgaon']").click()

submit = driver.find_element(By.ID, "submit").click()




sleep(5)
driver.quit()