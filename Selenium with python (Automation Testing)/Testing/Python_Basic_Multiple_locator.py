from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
time.sleep(2)
# using the multiple web locater"

#username = driver.find_elements(By.TAG_NAME, "input")
products = driver.find_element(By.XPATH, "//div[@class='inventory_item_name ']")

print("Product list")

for product in products:
    print(product.text)

#print(username[0].get_attribute("id"))
#print(username[1].get_attribute("id"))
#print(username[2].get_attribute("id"))
#index =0
#for fields in username:
    #print(f"Index : {index} value: {fields.get_attribute('id')}")
    #index = index+1


#print(len(username))




driver.close()