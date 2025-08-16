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

#relative xpath using for extration
username_input = driver.find_element(By.XPATH, "//input[@ID='user-name']")
username_input.send_keys("standard_user")
time.sleep(1)
# password
password_input = driver.find_element(By.XPATH, "//input[@NAME='password']")
password_input.send_keys("secret_sauce")
time.sleep(1)
# login button
submit_button = driver.find_element(By.XPATH, "//input[@ID='login-button']")
submit_button.click()
time.sleep(2)

# want to click on add to card

#WebElement = driver.find_element(By.XPATH, "//button[contains(@id,'sauce-labs-backpack')]")
#WebElement.click()
#time.sleep(5)

#click = driver.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']")
#click.click()
#time.sleep(5)

click = driver.find_element(By.XPATH, "//div[contains(text(),'Sauce Labs Backpack')]")
click.click()
time.sleep(5)


WebElement = driver.find_element(By.XPATH, "//button[@name='add-to-cart']")
WebElement.click()
time.sleep(5)

# close browser
driver.quit()






