from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


SIMILAR_ACCOUNT =account
USERNAME = YOUR USERNAME
PASSWORD = YOUR PASSWORD


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(4)
        self.driver.find_element(By.NAME, "username").send_keys(USERNAME)
        time.sleep(1)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(PASSWORD)
        time.sleep(1)
        password.send_keys(Keys.ENTER)
        time.sleep(3)


    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a")))
        followers = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a")
        followers.click()

    def follow(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "_aano")))
        time.sleep(2)

        for i in range(1,200):
            click_here = self.driver.find_element(By.XPATH, f"/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[{i}]/div")
            if i == 1:
                ActionChains(self.driver).move_to_element(click_here).click(click_here).perform()
            ActionChains(self.driver).move_to_element(click_here).send_keys(Keys.DOWN).perform()
            ActionChains(self.driver).move_to_element(click_here).send_keys(Keys.DOWN).perform()
            time.sleep(1)
            followers_list = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div")
            follower = followers_list.find_element(By.XPATH, f"/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[{i}]/div/div/div/div[3]/div/button")
            if follower.text == "Follow":
                ActionChains(self.driver).move_to_element(follower).click(follower).perform()
            else:
                pass



insta_follower = InstaFollower()
insta_follower.login()
insta_follower.find_followers()
insta_follower.follow()
