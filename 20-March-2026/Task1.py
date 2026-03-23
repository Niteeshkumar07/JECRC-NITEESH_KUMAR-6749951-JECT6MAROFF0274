from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support.select import Select

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

driver.get(r'C:\Users\Niteesh Kumar\OneDrive\Desktop\seleniumPractice\20-March-2026\playlist.html')
driver.maximize_window()

song_list = driver.find_element(By.ID,'songs')
select = Select(song_list)

if select.is_multiple:
    for i in select.options:
        if "Love" in i.text or "Girl" in i.text:
            select.select_by_visible_text(i.text)

print([i.text for i in select.all_selected_options])
driver.find_element(By.XPATH,'//button[text()="Add to Playlist"]').click()
print([i.text for i in select.options])
sleep(5)

driver.quit()
