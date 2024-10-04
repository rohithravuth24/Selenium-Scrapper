from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time

# Set different options for the browser
service_obj = Service(r"C:\drivers\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(service=service_obj)

try:
    driver.get("https://www.imdb.com/title/tt15354916/reviews/?ref_=tt_urv_sm")
    driver.maximize_window()  # Maximize the browser
    time.sleep(10)

    while True:
        try:
            BTN = driver.find_element(By.XPATH, "//*[@id='load-more-trigger']")
            BTN.click()
            time.sleep(10)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        except Exception as e:
            print("No more load buttons found or an error occurred:", e)
            break

    # Save the HTML content
    with open("page_source.html", "w", encoding="utf-8") as file:
        file.write(driver.page_source)

except Exception as e:
    print("An error occurred:", e)

finally:
    driver.quit()
