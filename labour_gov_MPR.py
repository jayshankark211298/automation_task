# Download
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


# initialize chrome
driver = webdriver.Chrome()

# get url
driver.get("https://labour.gov.in/monthly-progress-report")

# find download button
driver.find_element(By.LINK_TEXT, "Download(204.07 KB)").click()
time.sleep(5)

driver.quit()