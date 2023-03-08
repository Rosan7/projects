from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#<button class="btn__primary--large from__button--floating" data-litms-control-urn="login-submit" type="submit" aria-label="Sign in">Sign in</button>
import time
EMAIL = "senrosan2002@gmail.com"
PASSWORD = "rosansen7"
chrome_driver_path = "C:\Development\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
sign_in_button = driver.find_element(By.LINK_TEXT,"Sign in")
sign_in_button.click()

time.sleep(5)

login_name = driver.find_element(By.ID,"username")
login_name.send_keys(EMAIL)
login_password = driver.find_element(By.ID,"password")

login_password.send_keys(PASSWORD)
login_password.send_keys(Keys.ENTER)
time.sleep(10)
all_jobs = driver.find_elements(By.CSS_SELECTOR,".job-card-container--clickable")

for job in all_jobs:
    print("called")
    job.click()
    time.sleep(5)
    try:
        apply_button = driver.find_element(By.CSS_SELECTOR,".jobs-s-apply button")
        apply_button.click()


driver.quit()

