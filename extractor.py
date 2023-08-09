from selenium import webdriver
from os import environ

def start_driver():
    print("Starting remote driver")

    driver_url = environ.get("DRIVER_URL") or "http://localhost:4444"

    chrome_options = webdriver.ChromeOptions()

    return webdriver.Remote(
        command_executor=driver_url,
        options=chrome_options
    )

def open_site(driver):
    tob_site = "http://www.labes.icmc.usp.br/~tob-stt/admin/"
    driver.get(tob_site)

def login(driver):
    print("Login")

def navigate_to_logs(driver):
    print("Navigating")

def display_all_logs(driver):
    print("Displaying all logs")

def extract_logs(driver):
    print("Extracting logs")

if __name__ == "__main__":
   
    driver = start_driver()
    
    open_site(driver)

    login(driver)

    navigate_to_logs(driver)

    display_all_logs(driver)

    extract_logs(driver)

    driver.quit()
