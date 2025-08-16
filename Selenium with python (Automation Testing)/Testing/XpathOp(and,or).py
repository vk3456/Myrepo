import driver
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v136.fed_cm import click_dialog_button
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
driver.implicitly_wait(5)

"""

#relative xpath using for extration
#username_input = driver.find_element(By.XPATH, "//input[@type='text' and @name='user-name']")
#enter username

#username_input.send_keys("standard_user")
username = driver.find_element(By.XPATH, "(//input)[1]")
username.send_keys("standard_user")
username.click()
time.sleep(1)

# password
##password_input = driver.find_element(By.XPATH, "(//input[@id='password'])[1]")
#password_input.send_keys("secret_sauce")

username = driver.find_element(By.XPATH, "(//input)[2]")
username.send_keys("secret_sauce")
username.click()
time.sleep(1)

# login button
#submit_button = driver.find_element(By.XPATH, "//input[@class='submit-button btn_action' or @id='login-button']")
#submit_button.click()
username = driver.find_element(By.XPATH, "(//input)[3]")
username.click()
time.sleep(2)

# using link text path
productlink = driver.find_element(By.LINK_TEXT, "Sauce Labs Backpack")
productlink.click()
time.sleep(2)
# want to click on add to card
#WebElement = driver.find_element(By.XPATH, "//button[contains(@id,'sauce-labs-backpack')]")
#WebElement.click()
#time.sleep(5)

#click = driver.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']")
#click.click()
#time.sleep(5)

#click = driver.find_element(By.XPATH, "//div[contains(text(),'Sauce Labs Backpack')]")
#click.click()
#time.sleep(5)


#WebElement = driver.find_element(By.XPATH, "//button[@name='add-to-cart']")
#WebElement.click()
#time.sleep(5)

"""


# THIS IS THE PARTIAL LINK TEXT

#username = driver.find_element(By.XPATH, "(//input)[1]")
#username.send_keys("standard_user")
#username.click()
#time.sleep(1)

# THIS IS TAGNAME

#username = driver.find_element(By.TAG_NAME, "input")
#username.send_keys("standard_user")
#username.click()
#time.sleep(1)

"""
username = driver.find_element(By.TAG_NAME, "input")
username.send_keys("standard_user")
username.click()
time.sleep(1)



username = driver.find_element(By.XPATH, "(//input)[2]")
username.send_keys("secret_sauce")
username.click()
time.sleep(1)

# when multiple element have the same class and you want to locate the first one
username = driver.find_element(By.CLASS_NAME, "btn_action")
username.click()
time.sleep(2)

product = driver.find_element(By.PARTIAL_LINK_TEXT, "Labs Backpack")
product.click()
time.sleep(2)

"""

# using the css selector
#username = driver.find_element(By.CSS_SELECTOR, "input")
#sername = driver.find_element(By.CSS_SELECTOR, "#user-name")
#username = driver.find_element(By.CSS_SELECTOR, "div > input[type='text']")
username = driver.find_element(By.CSS_SELECTOR, "form input[type='text']")
username.send_keys("standard_user")
username.click()
time.sleep(1)

# using the xpath

#username = driver.find_element(By.XPATH, "(//input)[2]")
# using the CSS_SELECTOR
password = driver.find_element(By.CSS_SELECTOR, "[id='password']")
password.send_keys("secret_sauce")
time.sleep(3)

# when multiple element have the same class and you want to locate the first one
#username = driver.find_element(By.CLASS_NAME, "btn_action")
#login = driver.find_element(By.CSS_SELECTOR, ".btn_action")
#login = driver.find_element(By.CSS_SELECTOR, "input.btn_action")
login = driver.find_element(By.CSS_SELECTOR, "form > input[type='submit']")
login.click()
time.sleep(2)

product = driver.find_element(By.PARTIAL_LINK_TEXT, "Labs Backpack")
product.click()
time.sleep(2)


# close browser
driver.quit()




