from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")

# Switch to iframe if date picker is inside one
driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "demo-frame"))

# Click the date input to open the calendar
driver.find_element(By.XPATH, "//input[@id='datepicker']").send_keys("08/11/2025")

# Wait for calendar to load (add proper wait in real code)
time.sleep(1)

#yyy,mmm,ddd
Year = "2025"
month = "Aug"
date = "11"

driver.find_element(By.XPATH, "//*[@id='datepicker']").click()
time.sleep(1)
while True:
    #mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").test
    mon=driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yr=driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if mon ==month and yr==Year:
        break;
    else:
        driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[2]/span").click()
        driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[2]/span").click()
date=driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/table/tbody")

for ele in date:
    if ele.test==date:
        ele.click()
        break
    time.sleep(2)



driver.close()

