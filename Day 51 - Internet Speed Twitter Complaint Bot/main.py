from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys
import time

PROMISED_DOWN = 120
PROMISED_UP = 50
CHROME_DRIVE_PATH = ""
TWITTER_EMAIL = YOUR TWITTER EMAIL
TWITTER_PASSWORD = YOUR TWITTER PASSWORD
USERNAME =YOUR TWITTER USERNAME


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME, "js-start-test").click()
        continue_loop= True

        while continue_loop:
            try:
                download_speed = self.driver.find_element(By.CLASS_NAME, "download-speed")
                upload_speed = self.driver.find_element(By.CLASS_NAME, "upload-speed")
            except NoSuchElementException:
                continue_loop = True
            else:
                if download_speed.get_attribute("data-download-status-value") == "NaN" or upload_speed.get_attribute("data-upload-status-value") == "NaN":
                    continue_loop= True
                else:
                    download_speed = self.driver.find_element(By.CLASS_NAME, "download-speed")
                    upload_speed = self.driver.find_element(By.CLASS_NAME, "upload-speed")
                    # print(self.driver.page_source)
                    continue_loop= False
                    self.down= float(download_speed.get_attribute("innerHTML"))
                    self.up = float(upload_speed.get_attribute("innerHTML"))
                    print(f"Download speed = {self.down} and Upload speed = {self.up}")
                   

    def tweet_internet_provider(self):
        if self.down < PROMISED_DOWN or self.up < PROMISED_UP:
            self.driver.get("https://twitter.com/home")
            time.sleep(2)
            email =self.driver.find_element(By.NAME,"text")
            email.send_keys(TWITTER_EMAIL)
            email.send_keys(Keys.ENTER)
            time.sleep(1)
            username = self.driver.find_element(By.NAME,"text")
            username.send_keys(USERNAME)
            username.send_keys(Keys.ENTER)
            time.sleep(1)
            password = self.driver.find_element(By.NAME, "password")
            password.send_keys(TWITTER_PASSWORD)
            password.send_keys(Keys.ENTER)
            time.sleep(5)
            post = self.driver.find_element(By.CLASS_NAME,"public-DraftStyleDefault-block")
            post.send_keys(f"My current download is {self.down}Mbps and current upload is {self.up}Mbps. I'm paying for {PROMISED_DOWN}Mpbs download and {PROMISED_UP}Mbps upload. Why am I not getting what I'm paying for ? ") #@Etisalat_Care
            click_Tweet = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]")
            click_Tweet.click()
            self.driver.quit()



internetspeed = InternetSpeedTwitterBot()
internetspeed.get_internet_speed()
internetspeed.tweet_internet_provider()
