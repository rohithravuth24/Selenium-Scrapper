from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time

# Set different options for the browser
service_obj = Service(r"C:\drivers\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(service=service_obj)

driver.get("https://www.imdb.com/title/tt11821912/reviews/?ref_=tt_urv_sm")
driver.maximize_window()  #maximize the browswer
time.sleep(10)

#TAG NAME
# links=driver.find_elements(By.TAG_NAME, 'a')
# print(len(links)) #Gives the Total no of links on the webpage
BTN = driver.find_element(By.XPATH, "//*[@id='load-more-trigger']")

while BTN:
    BTN.click()
    time.sleep(10)
    BTN = driver.find_element(By.XPATH, "//*[@id='load-more-trigger']")

#driver.close()

# 1: //*[@id="load-more-trigger"]
# //*[@id="load-more-trigger"]