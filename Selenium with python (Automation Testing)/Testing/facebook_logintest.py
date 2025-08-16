from unittest import expectedFailure

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait

from Testing.Firsttestingcode import element

# lucch in browser
driver = webdriver.Chrome()
#minimise
driver.maximize_window()

def forgetpassword():
    driver.get("https://www.facebook.com/")
    time.sleep(2)
    #driver.find_element(By.LINK_TEXT, "Forgotten password?").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Forgotten").click()
    time.sleep(2)
    expected_title = "Forgotten Password | Can't Log In | Facebook"
    actual_title = driver.title
    if expected_title == actual_title:
        print("Successful pass")
    else:
        print("Failed pass expected_title {}".format(expected_title))

    # enter the email id in facebook
    #driver.find_element(By.XPATH, "(//input)[1]").send_keys("exmaple@gmail.com")
    #time.sleep(2)
    #password
    #driver.find_element(By.XPATH, "(//input)[2]").send_keys("password")
    #time.sleep(2)
    #forgett email id
    driver.find_element(By.XPATH, "//input[@placeholder='Email address or mobile number' and @name ='email']").send_keys("rohit.kumar1995.rj@gmail.com")
    time.sleep(2)
    # search the email it is correct or not
    driver.find_element(By.XPATH,"//button[@type ='submit' or @name ='did_submit']").click()
    time.sleep(5)
#forgetpassword()

def css_selector():
    driver.get("https://practice.expandtesting.com/inputs")
    time.sleep(2)
    # fill the all required details
    driver.find_element(By.CSS_SELECTOR, "input#input-number").send_keys("726599745")
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, "input#input-text").send_keys("Vikash")
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, "input#input-password").send_keys("Password")
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, "input#input-date").send_keys("2020-07-21")
    time.sleep(2)

    button = driver.find_element(By.CSS_SELECTOR, "button#btn-display-inputs")
    button.click()
    time.sleep(5)

    driver.find_element(By.CSS_SELECTOR, "button#btn-clear-inputs").click()
    time.sleep(3)

    # scrolling the view
    #driver.execute_script("arguments[0].scrollIntoView(true);", button)
    #time.sleep(2)

css_selector()
time.sleep(2)
driver.quit()

