# Import required libraries
import dr
from selenium import webdriver  # To interact with the browser
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By  # To locate elements on the webpage
import time  # To add delays (for demonstration purposes)

# Initialize WebDriver and launch chrome browser
driver = webdriver.Chrome()
print("Browser opened")

#maximise browser window
driver.maximize_window()
print("Browser maximised")


#add wait for 10 sec
driver.implicitly_wait(10)

#open url
# Open the Web Elements page
driver.get("https://duckduckgo.com/")
print("url opened")

# wait a second
driver.implicitly_wait(10)

#time.sleep(5) #wait for 5 sec. for page load

#find search box web element
search_input = driver.find_element(By.NAME, "q")
search_input.send_keys("Selenium")
driver.implicitly_wait(10)


# # print the all dext
# for x in search_input:
#     print("Search all relevent : " , x.text)
#range
# for _ in range(10):
#     search_input.send_keys(Keys.RETURN)
# return send keys
search_input.send_keys(Keys.RETURN)

driver.implicitly_wait(10)
# close the open windows
driver.close()

