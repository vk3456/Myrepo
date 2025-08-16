# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# import time
#
# # Setup WebDriver options (optional)
# options = Options()
# options.add_argument("--start-maximized")  # Start browser maximized
#
# # Initialize the Chrome driver
# driver = webdriver.Chrome(options=options)
#
# # Open the target website
# driver.get("https://demo.opencart.com/")
#
# # Optional: Wait for the page to load
# time.sleep(2)
#
# # Create ActionChains object
# actions = ActionChains(driver)
#
# # Step 1: Locate the "Components" top menu item
# components_menu = driver.find_element(By.LINK_TEXT, "Components")
#
# # Step 2: Hover over the "Components" menu to reveal the dropdown
# actions.move_to_element(components_menu).perform()
# time.sleep(1)  # Wait a moment for the dropdown to appear
#
# # Step 3: Click the "Monitors" submenu item
# monitors_item = driver.find_element(By.LINK_TEXT, "Monitors (2)")
# monitors_item.click()
#
# # Step 4: Wait and verify the result
# time.sleep(3)
# print("Page Title after clicking Monitors:", driver.title)
#
# # Close the browser
# driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# import time
#
# # Setup WebDriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://jqueryui.com/droppable/")
#
# # Wait for the page to load
# time.sleep(2)
#
# # Step 1: Switch to the iframe that contains the drag and drop elements
# iframe = driver.find_element(By.CLASS_NAME, "demo-frame")
# driver.switch_to.frame(iframe)
#
# # Step 2: Locate the source and target elements
# source = driver.find_element(By.ID, "draggable")
# target = driver.find_element(By.ID, "droppable")
#
# # Step 3: Perform drag and drop
# actions = ActionChains(driver)
# actions.drag_and_drop(source, target).perform()
#
# # Optional: Wait and observe the result
# time.sleep(3)
#
# # Verify result (the text should change to "Dropped!")
# print("Result after drop:", target.text)
#
# # Quit the browser
# driver.quit()


# ActionChains(driver)	To perform mouse hover
# move_to_element()	To simulate hover
# WebDriverWait + expected_conditions	To wait for dropdowns and links to load
# time.sleep()	For basic timing (for dropdown animation delay)
# driver.quit()	Closes the browser cleanly

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup Chrome options
options = Options()
options.add_argument("--start-maximized")

# Launch WebDriver
driver = webdriver.Chrome(options=options)

try:
    # Open Amazon
    driver.maximize_window()
    driver.get("https://www.amazon.com")
    driver.find_element(By.XPATH, "/html/body/div/div[1]/div[3]/div/div/form/div/div/span").click()
    time.sleep(2)


    # Wait for the menu to load
    wait = WebDriverWait(driver, 10)

    # Step 1: Locate the "Account & Lists" menu
    account_lists = wait.until(
        EC.presence_of_element_located((By.ID, "nav-link-accountList"))
    )

    # Step 2: Hover over it to reveal dropdown
    actions = ActionChains(driver)
    actions.move_to_element(account_lists).perform()

    time.sleep(2)  # Allow dropdown to appear

    # Step 3: Click on "Your Orders"
    your_orders = wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Your Orders"))
    )
    your_orders.click()

    # Step 4: Wait for the redirection to either sign-in or orders page
    time.sleep(3)

    # Step 5: Output page title
    print("Page title after clicking 'Your Orders':", driver.title)

except Exception as e:
    print("Error:", e)

finally:
    # Clean up
    time.sleep(3)
    driver.quit()


