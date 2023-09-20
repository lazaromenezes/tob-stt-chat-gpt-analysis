from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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
    print("Opening site")
    tob_site = "http://www.labes.icmc.usp.br/~tob-stt/admin/"
    driver.get(tob_site)

def login(driver):
    print("Login")
    driver.find_element(By.ID, "user_name").send_keys("****")
    driver.find_element(By.ID, "pw").send_keys("****")
    driver.find_element(By.XPATH, "//input[@type='submit']").click()

def navigate_to_logs(driver):
    print("Navigating to logs")
    driver.find_element(By.PARTIAL_LINK_TEXT, "Conversation Logs").click()

def display_all_logs(driver):    
    print("Displaying all logs")
    select = Select(driver.find_element(By.ID, "showing"))
    select.select_by_value("all time")
    driver.find_element(By.ID, "submit").click()

def extract_logs(driver):
    print("Extracting logs")
    
    user_list = driver.find_elements(By.CSS_SELECTOR, ".userlist ul li a")

    user_ids = [user.get_attribute("name") for user in user_list]

    for user in user_ids:
        extract_log(driver, user)

def extract_log(driver, user):
    print(f"Extracting log {user}")
    
    driver.get(f"http://www.labes.icmc.usp.br/~tob-stt/admin/index.php?page=logs&showing=all%20time&id={user}#{user}")

    with open(f"/opt/logs/user_{user}_conversations", 'w') as log_file:
        conversation = driver.find_elements(By.CSS_SELECTOR, "div.convolist span")

        for message in conversation:
            log_file.write(message.text)
            log_file.write("\n")

        log_file.close()

if __name__ == "__main__":
   
    driver = start_driver()

    open_site(driver)
    login(driver)
    navigate_to_logs(driver)
    display_all_logs(driver)
    extract_logs(driver)

    driver.quit()
