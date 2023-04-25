from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import time

# -----------Open Window and maximize---------------------#
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.linkedin.com/jobs/")
wait = WebDriverWait(driver, 10)
# -----------------------Login ----------------------------#
username = driver.find_element(By.ID, 'session_key')
username.send_keys(USERNAME)

password = driver.find_element(By.ID, "session_password")
password.send_keys(PASSWORD)

driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form[1]/div[2]/button').send_keys(Keys.ENTER)

# ------------------------Type Job Title-----------------------#
time.sleep(5)
wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "jobs-search-box__text-input")))
job_title = driver.find_element(By.CLASS_NAME, "jobs-search-box__text-input")
job_title.click()
job_title.send_keys("Python Developer")
job_title.click()

# --------------------------------Type Location----------------------------#
location = driver.find_element(By.XPATH, "/html/body/div[5]/header/div/div/div/div[2]/div[3]/div/div/input[2]")
time.sleep(2)
ActionChains(driver).move_to_element(location).click(location).perform()
ActionChains(driver).move_to_element(location).send_keys("Dubai, United Arab Emirates").perform()
time.sleep(0.5)
# ActionChains(driver).move_to_element(location).send_keys(Keys.ENTER).perform()

# job_title = driver.find_element(By.CLASS_NAME,"jobs-search-box__text-input")
ActionChains(driver).move_to_element(job_title).click(job_title).perform()
ActionChains(driver).move_to_element(job_title).send_keys(Keys.ENTER).perform()

# create a WebDriverWait object with a timeout of 'timeout' seconds
time.sleep(3)

# -------------------------------Click Easy Apply Filter------------------------#
wait.until(EC.visibility_of_element_located(
    (By.XPATH, "/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[8]/div/button")))
wait.until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[8]/div/button")))

easy_apply = driver.find_element(By.XPATH,
                                 "/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[8]/div/button")

time.sleep(1)
ActionChains(driver).move_to_element(easy_apply).click(easy_apply).perform()

time.sleep(5)

# -----------------------------Finding out how many job openings----------------------------#
# search_result = driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[1]/header/div[1]/small/div")
# print(search_result.text)
#

# ---------------------------------Get all the job posting in a list-------------------------#
wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "jobs-search-results__list-item")))
all_listings = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")
for listing in all_listings:
    ActionChains(driver).move_to_element(listing).click(listing).perform()
    time.sleep(2)

    try:
    # ---------------------click Apply---------------------#
        apply = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
        ActionChains(driver).move_to_element(apply).click(apply).perform()
        time.sleep(2)
    # --------------------------Click Next---------------------------#
        next_address = driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button")
        ActionChains(driver).move_to_element(next_address).click(next_address).perform()
        time.sleep(2)
        # ------------------------Click Review---------------------------#
        next_or_review = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]")
        next_or_review_text = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]/span").text
        print(next_or_review_text)
        # ------------If button is not equal to review then it's a multi-level application--------#
        if next_or_review_text == "Review":
            time.sleep(1)
            ActionChains(driver).move_to_element(next_or_review).click(next_or_review).perform()
            submit_application = driver.find_element(By.CSS_SELECTOR,"footer button")
            time.sleep(1)
            ActionChains(driver).move_to_element(submit_application).click(submit_application).perform()
            time.sleep(1)
            driver.find_element(By.XPATH,"/html/body/div[3]/div/div/button/li-icon/svg").send_keys(Keys.ESCAPE)

        else:
            next_or_review.send_keys(Keys.ESCAPE)
            driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div[3]/button[1]").click()

    except NoSuchElementException:
        time.sleep(1)
        l = driver.find_element(By.TAG_NAME,"input")
        l.send_keys(Keys.ESCAPE)
        try:
            driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div[3]/button[1]").click()
        except NoSuchElementException:
            pass

