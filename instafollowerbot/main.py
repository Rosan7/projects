from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time
CHROME_DRIVER_PATH = "C:\Development\chromedriver_win32\chromedriver.exe"
SIMILAR_ACCOUNT = "chefsteps"
USERNAME = "rosan_sen7"
PASSWORD = "rosansen7#"
class Instafollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        self.driver.get("https://www.instagram.com/chefsteps/")
        time.sleep(2)
        followers = self.driver.find_element(By.CLASS_NAME,"/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]")
        followers.click()
        time.sleep(2)
        popup_followers = self.driver.find_elements(By.XPATH,"//*[@id='mount_0_0_xM']/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]")
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",popup_followers)
            time.sleep(2)


    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR,"button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH,"//*[@id='mount_0_0_Df']/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
                cancel_button.click()

obj = Instafollower()
obj.login()
time.sleep(8)
obj.find_followers()
obj.follow()
obj.driver.quit()





