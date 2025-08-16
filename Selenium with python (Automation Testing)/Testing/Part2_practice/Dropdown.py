from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# luching  over the web page
driver = webdriver.Chrome()
driver.maximize_window()
# open url
driver.get("https://dmytro-ch21.github.io/html/web-elements.html")
time.sleep(3)
print("Thi is the Web : ", driver.title) # title
print("Thi is the URL : ", driver.current_url) # Current URL
time.sleep(3)

# DROP DONW check button
ford_radio = driver.find_element(By.XPATH, "//select[@id='carBrands']")
ford_radio.click()
# check condition
if ford_radio.is_selected:
    print("Thi is the Ford Radio : ", ford_radio.is_selected)
    time.sleep(3)
# searchble check button
drop_radio = driver.find_element(By.XPATH, "//input[@placeholder='Search Car Type...']")
drop_radio.click()
# check condition
if drop_radio.is_selected:
    print("Thi is the Ford Radio : ", drop_radio.is_selected)
    time.sleep(3)
# radio check button
# bmw_radio = driver.find_element(By.ID, "radio2")
# bmw_radio.click()
# # check condition
#
# if bmw_radio.is_selected:
#     print("Thi is the Ford Radio : ", bmw_radio.is_selected)
#     time.sleep(3)

driver.quit()