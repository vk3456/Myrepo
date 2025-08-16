from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import keys
import time

"""

# Start Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()
# Go to Swag Labs login page
driver.get("https://www.saucedemo.com/")
time.sleep(3)
# Fill in login details
username = driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")
password = driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")
login = driver.find_element(By.ID, "login-button")
login.click()
time.sleep(3)

# After login, collect product data
products = driver.find_elements(By.CLASS_NAME, "inventory_item")

# Prepare HTML content
html_content = "<html><head><title>Swag Labs Products</title></head><body>"
html_content += "<h1>Swag Labs Product List</h1><ul>"

for product in products:
    name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
    description = product.find_element(By.CLASS_NAME, "inventory_item_desc").text
    price = product.find_element(By.CLASS_NAME, "inventory_item_price").text
    ImgUrl = product.find_element(By.CLASS_NAME, "inventory_item_img").text
    html_content += f"<li><strong>{name}</strong><br>{description}<br><em>{price}</em><br>{ImgUrl}</br></li><hr>"

html_content += "</ul></body></html>"

# Save the data to an HTML file
with open("swag_labs_products.html", "w", encoding="utf-8") as file:
    file.write(html_content)

# Close browser
driver.quit()

print("✅ Data extracted and saved to 'swag_labs_products.html'")
"""

# Launch browser and go to Swag Labs
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
time.sleep(2)

# Log in
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

# Add first product to cart
driver.find_element(By.CLASS_NAME, "btn_inventory").click()
time.sleep(1)

# Go to cart
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
time.sleep(1)

# Proceed to checkout
driver.find_element(By.ID, "checkout").click()
time.sleep(1)

# Fill in checkout information
driver.find_element(By.ID, "first-name").send_keys("John")
driver.find_element(By.ID, "last-name").send_keys("Doe")
driver.find_element(By.ID, "postal-code").send_keys("12345")
driver.find_element(By.ID, "continue").click()
time.sleep(2)

# Get order summary details
summary_subtotal = driver.find_element(By.CLASS_NAME, "summary_subtotal_label").text
summary_tax = driver.find_element(By.CLASS_NAME, "summary_tax_label").text
summary_total = driver.find_element(By.CLASS_NAME, "summary_total_label").text

# Finish checkout
driver.find_element(By.ID, "finish").click()
time.sleep(2)

# Get confirmation message
thank_you_msg = driver.find_element(By.CLASS_NAME, "complete-header").text
order_msg = driver.find_element(By.CLASS_NAME, "complete-text").text

# Save order details in HTML
html_content = f"""
<html>
<head><title>Order Confirmation</title></head>
<body>
    <h1>Pls add in the query form: {thank_you_msg}</h1>
    <p>The thank you message: {order_msg}</p>
</body>
</html>
"""

with open("order_confirmation.html", "w", encoding="utf-8") as read:
    read.write(html_content)


# Close browser
driver.quit()

print("✅ Order details saved in 'order_confirmation.html'")




