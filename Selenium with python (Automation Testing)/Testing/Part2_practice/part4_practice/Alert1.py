# Import required libraries
from selenium import webdriver  # To interact with the browser
from selenium.webdriver.common.by import By  # To locate elements on the webpage
import time  # To add delays (for demonstration purposes)

# Initialize WebDriver and launch chrome browser
driver = webdriver.Chrome()
print("Browser opened")

#maximise browser window
driver.maximize_window()
print("Browser maximised")

#open url
# Open the Web Elements page
driver.get("https://demo.guru99.com/V4/index.php")
print("url opened")

#find login button
login_btn = driver.find_element(By.NAME,"btnLogin")
#click on login button
login_btn.click()
time.sleep(5)
#switch focus to alter window
alert = driver.switch_to.alert
print("Alert message:", alert.text)
time.sleep(5)
alert.accept()
time.sleep(3)

#close all browser window
driver.quit()