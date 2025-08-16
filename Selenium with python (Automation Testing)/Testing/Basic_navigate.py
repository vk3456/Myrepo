from selenium import webdriver
import time

driver = webdriver.Chrome()  # webdriver will be open on chrome

driver.get("https://www.pexels.com/search/sexy/") # navigate to python page on url
time.sleep(4) # wait for a second to let on the page load

driver.get("https://www.youtube.com/") # navigate to the youtube -- open URL
time.sleep(4) # wait for a second to let on the page load

# go back to google page
driver.back()
time.sleep(4) # wait for a second to let on the page load
# go forward to youtube page
driver.forward()
time.sleep(4) # wait for a second to let on the page load
# And refresh the page
driver.refresh()

driver.close()  # close the open window




