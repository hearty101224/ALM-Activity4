from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service  # Import Service class
import time

# Set up Chrome WebDriver service
chrome_service = Service("C:/xampp/htdocs/ALM-WebApp/chromedriver.exe")

# Initialize WebDriver
driver = webdriver.Chrome(service=chrome_service)

# Open the web application
driver.get("http://localhost/ALM-WebApp/")

# Enter username and password
driver.find_element(By.NAME, "username").send_keys("admin")
driver.find_element(By.NAME, "password").send_keys("password1")

# Click login button
driver.find_element(By.TAG_NAME, "button").click()

# Wait for 3 seconds and close the browser
time.sleep(3)
driver.quit()
