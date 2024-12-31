from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time

# Set up the Edge WebDriver
service = Service(r"C:\Users\haley\Downloads\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(service=service)

# Base URL for your Flask app
base_url = "http://localhost:5000" 

# Test Registration
driver.get(f"{base_url}/register")

# Fill in the registration form
username_field = driver.find_element(By.NAME, "username")
password_field = driver.find_element(By.NAME, "password")

username_field.send_keys("testuser")
password_field.send_keys("testpassword")
password_field.send_keys(Keys.RETURN) 

# Wait for the response
time.sleep(5)

# Check for registration success
assert "Registration successful" in driver.page_source 

# Test Login
driver.get(f"{base_url}/login")

# Fill in the login form
username_field = driver.find_element(By.NAME, "username")
password_field = driver.find_element(By.NAME, "password")

username_field.send_keys("testuser")
password_field.send_keys("testpassword")
password_field.send_keys(Keys.RETURN)  # Submit the form

# Wait for the response
time.sleep(5)

# Check for login success
assert "Login successful" in driver.page_source

# Clean up
driver.quit()
