from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Launch the browser.
driver = webdriver.Chrome()
# maximize the page
driver.maximize_window()
def successful_login():
    # Navigate to the login page URL.
    driver.get("https://practice.expandtesting.com/login")
    # wait a second
    time.sleep(2)
    # incorrect login
    username = driver.find_element(By.ID, "username")
    username.send_keys("practice")
    time.sleep(2)

    password = driver.find_element(By.NAME, "password")
    password.send_keys("SuperSecretPassword!")
    time.sleep(2)

    # login = driver.find_element(By.XPATH, "//button[@class='btn btn-bg btn-primary d-block w-100']")
    # login = driver.find_element(By.XPATH, "//button[text() ='Login']")
    login = driver.find_element(By.XPATH,
                                "//button[@type='submit' and contains(@class, 'btn btn-bg btn-primary d-block w-100')]")
    # login = driver.find_element(By.TAG_NAME, "input")
    login.click()
    time.sleep(2)
#Enter Username: practice.
#username = driver.find_element(By.ID, "username")
#username.send_keys("practice")
#time.sleep(2)
#Enter Password: SuperSecretPassword!.
#password = driver.find_element(By.ID, "password")
#password.send_keys("SuperSecretPassword!")
#time.sleep(2)
#Click the Login button.
#login = driver.find_element(By.XPATH, "//button[@type='submit']")
#login.click()
#time.sleep(2)
#Verify that a Logout button is displayed.
#logout = driver.find_element(By.XPATH, "//i[@class='icon-2x icon-signout']")
#logout.click()
#time.sleep(2)
# incorrect username
#username = driver.find_element(By.ID, "username")
##username.send_keys("practices")
#time.sleep(2)

#password = driver.find_element(By.ID, "password")
#password.send_keys("SuperSecretPassword!")
#time.sleep(2)

#login = driver.find_element(By.XPATH, "//button[@type='submit']")
#login.click()
#time.sleep(2)

# incorrect passwords

#close window
driver.close()

