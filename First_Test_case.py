from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.service import  Service
import time

# Set different options for the browser
# options = Options()
# options.add_experimental_option("detach", True)

service_obj = Service(r"C:\drivers\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(service=service_obj)
driver.get(r"https://opensource-demo.orangehrmlive.com/auth/login")
time.sleep(5)

driver.find_element(By.NAME, "username").send_keys('Admin')
driver.find_element(By.NAME, "password").send_keys('admin123')
driver.find_element(By.XPATH, "//button[@type='submit']").click()  # Updated locator for the login button
time.sleep(5)

act_title = driver.title
exp_title = "OrangeHRM"
if act_title == exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")
driver.close()
