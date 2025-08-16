from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.print_page_options import PrintOptions

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# Wait for the page to load
driver.get("https://dmytro-ch21.github.io/html/web-elements.html")
time.sleep(2)

# # Check with the actual URL
# print("This is the Actual title : ", driver.title)
# # actual URL
# print("URL : ", driver.current_url)
#
# # Locate and click the checkbox
# checkbox = driver.find_element(By.ID, "option1")  # Replace with correct ID or use other selector
# checkbox.click()
#
# if not checkbox.is_selected():
#     print("Checkbox is selected : ",checkbox.is_selected())
#     time.sleep(2)
#     checkbox.click()
# else:
#     print("Checkbox is not selected : ",checkbox.is_selected())
#     time.sleep(2)

# checkbox1 = driver.find_element(By.ID, "option2")  # Replace with correct ID or use other selector
# checkbox1.click()
#
# if checkbox1.is_selected():
#     print("Checkbox is selected : ",checkbox1.is_selected())
# else:
#     print("Checkbox is not selected : ",checkbox1.is_selected())
#     time.sleep(2)
# # Replace with correct ID or use other selector
# checkbox2 = driver.find_element(By.ID, "option3")  # Replace with correct ID or use other selector
# checkbox2.click()
#
# if checkbox2.is_selected():
#     print("Checkbox is selected : ",checkbox2.is_selected())
# else:
#     print("Checkbox is not selected : ",checkbox2.is_selected())
#     time.sleep(2)
#
# checkbox3 = driver.find_element(By.ID, "option4")  # Replace with correct ID or use other selector
# checkbox3.click()
#
# if checkbox3.is_selected():
#     print("Checkbox is selected : ",checkbox3.is_selected())
# else:
#     print("Checkbox is not selected : ",checkbox3.is_selected())
#     time.sleep(2)
#
# # Optional: check if it's selected
# Checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
# for checkbox in Checkboxes:
#     checkbox.click()
#     if not checkbox.is_selected():
#         print("All checked : ",checkbox.is_selected())
#     else:
#         print("Selected : ",checkbox.is_selected())

# check radio check box
# Cleanup
time.sleep(3)
driver.quit()
