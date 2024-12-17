from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

def capture_network_calls(city):
    # Enable Performance Logging
    caps = DesiredCapabilities.CHROME
    caps['goog:loggingPrefs'] = {'performance': 'ALL'}
    driver = webdriver.Chrome(desired_capabilities=caps)

    # Open the OpenWeatherMap homepage
    driver.get("https://openweathermap.org/")

    try:
        # Locate search input and search for city
        search_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search city']"))
        )
        search_input.send_keys(city)

        # Wait for the loader to disappear before clicking the button
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "owm-loader"))
        )

        # Locate and click the search button
        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        search_button.click()

        # Wait for network calls to complete
        time.sleep(5)

        # Capture logs
        logs = driver.get_log("performance")
        print("Network calls captured successfully.")

        return logs

    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()