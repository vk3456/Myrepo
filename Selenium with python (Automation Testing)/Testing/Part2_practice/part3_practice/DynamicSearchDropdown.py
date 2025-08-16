# Import required libraries
from selenium import webdriver  # To interact with the browser
from selenium.webdriver.common.by import By  # To locate elements on the webpage
import time  # To add delays (for demonstration purposes)

# Initialize WebDriver
driver = webdriver.Chrome()

#maximise browser window
driver.maximize_window()

# Open Google
driver.get("https://www.google.com")
print("Google opened.")

# Locate the search box and type 'Selenium'
search_box = driver.find_element(By.CLASS_NAME, "gLFyf")
search_box.send_keys("Selenium")
print("Typed 'Selenium' in the search box.")

# Pause for suggestions to load (simple time.sleep for now)
time.sleep(8)

# Find all suggestions
suggestions = driver.find_elements(By.XPATH,"//ul[@role='listbox']//li")

# Print all suggestions
print("Search suggestions:")
for suggestion in suggestions:
    print("This is search element :", suggestion.text)


# Wait for result page to load
time.sleep(3)

# Close browser
driver.quit()