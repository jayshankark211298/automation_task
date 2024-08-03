from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the Cowin website
driver.get("https://www.cowin.gov.in/")

try:
    # Click on the "FAQ" anchor tag and open a new window
    faq_link = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "FAQ")))
    faq_link.click()

    # Click on the "Partners" anchor tag and open a new window
    partners_link = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Partners")))
    partners_link.click()
except Exception as e:
    print("Error:", e)
    print(driver.page_source)
finally:
    # Fetch the opened Windows / Frame ID and display the same on the console
    window_handles = driver.window_handles
    print("Opened windows:")
    for handle in window_handles:
        print(handle)

    # Close the two new windows and come back to the Home page
    for handle in window_handles[1:]:
        driver.switch_to.window(handle)
        driver.close()

    driver.switch_to.window(window_handles[0])
    print("Back to the Home page")

driver.quit()