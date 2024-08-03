import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import os
import time

# Create a folder to store the images
folder_path = "C:\\Users\\User\\Desktop\\workspace\\PAT-25\\images_1"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Configure Chrome options to set the download directory
chrome_options = webdriver.ChromeOptions()
prefs = {"download.default_directory": folder_path}
chrome_options.add_experimental_option("prefs", prefs)

# Initialize the Chrome driver with options
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the webpage
driver.get("https://labour.gov.in/gallery/112th-session-ilc")
time.sleep(3)

# Find all image elements on the page
images = driver.find_elements(By.XPATH, "//img[@typeof='foaf:Image']")

# Save the first 10 images
for i, image in enumerate(images[:10]):
    # Move to the image element and context click
    ActionChains(driver).move_to_element(image).context_click().perform()
    time.sleep(1)

    # Use pyautogui to click on "Save image as"
    pyautogui.typewrite(['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])  # navigate to save image
    time.sleep(1)

    # Enter the file name and save
    file_name = f"image_{i + 1}.jpg"
    pyautogui.typewrite(file_name)
    pyautogui.press('enter')
    time.sleep(1)

# Close the browser
driver.quit()