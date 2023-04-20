from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException

import time

try:
    driver = webdriver.Chrome()
    driver.get("http://orteil.dashnet.org/experiments/cookie/")
    cookie = driver.find_element(By.ID, 'cookie')
    html_stores = driver.find_elements(By.CSS_SELECTOR, "#store div")
    html_ids = [each_id.get_attribute("id") for each_id in html_stores[:8]]
    print(html_ids)
    # stores = driver.find_elements(By.CSS_SELECTOR, "#store b")

    while True:
        affordable_store_price_list = []
        affordable_store_id_list =[]
        t_end = time.time() + 10
        while t_end >= time.time():
            cookie.click()
        earned_money = int(driver.find_element(By.ID,"money").text.replace(",",""))
        print(f"earned money: {earned_money}")
        count = 0
        for each_id in html_ids:
            print(driver.find_element(By.ID, f"{each_id}").text.split("-")[1].split("\n")[0])
            store_price = int(driver.find_element(By.ID, f"{each_id}").text.split("-")[1].split("\n")[0].replace(",",""))
            store_id = each_id
            if store_price <= earned_money:
                # print(f"store price:{store_price}")
                affordable_store_price_list.append(store_price)
                affordable_store_id_list.append(store_id)
        highest_affordable_store = affordable_store_price_list[-1]
        highest_affordable_store_id = affordable_store_id_list[-1]

        buy_store = driver.find_elements(By.CSS_SELECTOR, "#store b")
        print(f"highest affordable price: {highest_affordable_store}, ID: {highest_affordable_store_id}")
        click_on_store = driver.find_element(By.ID, f"{highest_affordable_store_id}")
        click_on_store.click()

except KeyboardInterrupt:
    driver.close()
