from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
import time

# Load environment variables from .env file
load_dotenv()

# Retrieve CCID and password from environment variables
CCID = os.getenv("CCID")
PASSWORD = os.getenv("PASSWORD")

# Initialize the WebDriver
driver = webdriver.Chrome()

try:
    # Open the Bear Tracks website
    driver.get("https://www.beartracks.ualberta.ca/")

    # Wait for the page to load (optional)
    driver.implicitly_wait(10)

    # Locate and click the "Single Sign-On" button
    single_sign_on_button = driver.find_element(By.XPATH, '//img[@alt="Click for single sign-on"]')
    single_sign_on_button.click()

    print("Clicked 'Single Sign-On', waiting for the next page to load...")

    # Wait for the login form to load
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "username"))  # Wait for the username field
    )

    print("Login form loaded!")

    # Fill in the CCID and Password fields using the environment variables
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "user_pass")

    username_field.send_keys(CCID)  # Use the CCID from .env file
    password_field.send_keys(PASSWORD)  # Use the PASSWORD from .env file

    # Submit the form
    password_field.send_keys(Keys.RETURN)

    print("Submitted the login form!")

    # Wait for the "My Schedule Builder" tile to be visible
    try:
        schedule_builder_tile = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@id='PTNUI_LAND_REC_GROUPLET_LBL$0' and text()='My Schedule Builder']")
            )
        )
        print("Successfully logged in and the 'My Schedule Builder' tile is visible.")
    except Exception as e:
        print(f"Error locating 'My Schedule Builder' tile: {e}")

    # Click on the "My Schedule Builder" tile
    schedule_builder_tile_div = driver.find_element(By.XPATH, "//div[@id='win0divPTNUI_LAND_REC_GROUPLET$0']")
    schedule_builder_tile_div.click()
    print("Clicked 'My Schedule Builder' tile.")
    time.sleep(15)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
