from selenium.common.exceptions import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

# Set you own email and password
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

# Open a specific profile
# option.add_argument(r"--user-data-dir=C:\Users\ASUS\AppData\Local\Google\Chrome\User Data")
# option.add_argument(r"--profile-directory=Default")

driver = webdriver.Chrome(options=option)

driver.get(
    "https://www.linkedin.com/jobs/search/?currentJobId=3743337474&f_AL=true&f_E=2&geoId=102713980&keywords=Software%20Engineer&location=India&origin=JOB_SEARCH_PAGE_KEYWORD_AUTOCOMPLETE&refresh=true")

time.sleep(2)
try:
    moveto_signin = driver.find_element(By.LINK_TEXT, "Sign in")
    moveto_signin.click()

    time.sleep(1)

    try:
        input_email = driver.find_element(By.ID, "username")
        input_email.send_keys(EMAIL)
    except NoSuchElementException:
        print("Account was found\n")

    input_pass = driver.find_element(By.ID, "password")
    input_pass.send_keys(PASSWORD)
    input_pass.send_keys(Keys.ENTER)
except NoSuchElementException:
    print("Some Error Occurred! Please Run Again")
    exit(-1)

time.sleep(6)
lists_to_scroll = driver.find_element(By.CSS_SELECTOR, ".jobs-search-results-list")
scroll_var = 500

time.sleep(4)
job_lists = driver.find_elements(By.CSS_SELECTOR, ".jobs-search-results__list-item")
print(f"Number of Jobs Found: {len(job_lists)}\n")

index = 1
for li in job_lists:
    driver.execute_script(f"arguments[0].scrollTop = {scroll_var};", lists_to_scroll)
    print(f"{index}. {li.text}")
    print("\n")
    scroll_var += 500
    index += 1

    driver.execute_script('arguments[0].click()', li)
    time.sleep(2)

    try:
        save = driver.find_element(By.CSS_SELECTOR, ".jobs-save-button")
        driver.execute_script('arguments[0].click()', save)
        print("\nJob saved")
    except NoSuchElementException:
        print("\nUnable to Save Job!")
    except StaleElementReferenceException:
        print("\nUnable to Save Job!")

    time.sleep(1)

    try:
        follow = driver.find_element(By.CSS_SELECTOR, ".follow")
        driver.execute_script('arguments[0].click()', follow)
        print("Company followed\n")
    except NoSuchElementException:
        print("Unable To Follow The Company!")
    except StaleElementReferenceException:
        print("Unable To Follow The Company!")
