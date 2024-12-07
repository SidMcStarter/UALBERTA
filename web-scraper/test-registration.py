from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pywhatkit as w
import pyautogui
import keyboard as k
import os
from dotenv import load_dotenv


load_dotenv()

phone_number = os.getenv("PHONE_NUMBER")
message = "Hi! This is a message send from python"

# print(phone_number);


# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Open the specific Bear Tracks URL
    # change the url
    course = "CMPUT-229"
    url = f"https://register.beartracks.ualberta.ca/criteria.jsp?access=0&lang=en&tip=2&page=results&scratch=0&advice=0&legend=1&term=1900&sort=none&filters=liiiiiiiii&bbs=&ds=&cams=UOFABiOFF_UOFABiMAIN&locs=any&isrts=any&ses=any&pl=&pac=1&course_0_0={course}&va_0_0=1a72&sa_0_0=&cs_0_0=&cpn_0_0=&csn_0_0=&ca_0_0=&dropdown_0_0=al&ig_0_0=0&rq_0_0=&bg_0_0=0&cr_0_0=&ss_0_0=0&sbc_0_0=0"
    # Open the URL
    driver.get(url)
    
    # Give time for the page to load
    time.sleep(5)

    # Infinite loop to check every 30 seconds
    while True:
        try:
            # Wait for the page body to be loaded
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
            # Find the warning elements
            warning_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'cbox-warnings')]")
            
            found_text = False
            print("Warning elements found:", len(warning_elements))  # Print the number of found warning elements

            for warning in warning_elements:
                # Check if the warning text contains "All classes are full"
                if "All classes are full" in warning.text:
                    found_text = True
                    break  # Stop checking once the text is found

            # Output based on the text found
            if found_text:
                print("Classes are full")
            else:
                print("Classes are not full")
                w.sendwhatmsg_instantly(phone_number, message)
                k.press_and_release('enter')
                driver.quit()
                break;

        except Exception as e:

            print("An error occurred:", e)

        time.sleep(10)

        # Refresh the page
        driver.refresh()
        time.sleep(5)

except KeyboardInterrupt:
    print("Process interrupted by the user.")

finally:
    # Close the browser when the loop ends
    driver.quit()
