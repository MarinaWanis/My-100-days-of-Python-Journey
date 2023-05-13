from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

header= {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
}
zillow_website= "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56825484228516%2C%22east%22%3A-122.29840315771484%2C%22south%22%3A37.731316620609356%2C%22north%22%3A37.819240145441945%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"

form_link = "https://forms.gle/CDNZ3bbs1exb7rz88"

html_response = requests.get(zillow_website, headers=header).text

soup = BeautifulSoup(html_response, 'html.parser')
# print(soup.prettify())

# print(soup.find_all(class_="property-card-link"))
anchor_tags= soup.find_all(class_="property-card-link")

all_links=[]
for tag in anchor_tags:
    link = tag.get("href")
    link_starting_with = link[:5]
    if link_starting_with != "https":
        link= "https://www.zillow.com"+link
    if link in all_links:
        pass
    else:
        all_links.append(link)

# print(all_links)

all_addresses=[]
address_tags = soup.select("article div div a address")

# print(address_tags_tags)
for address in address_tags:
    all_addresses.append(address.getText())
# print(all_addresses)

all_price_tags = soup.select("article div div div span")
# print(price_tags)
all_prices=[]
for price_tag in all_price_tags:
    price= price_tag.getText()
    first_char= price[:1]
    if first_char =="$":
        split_price_string= price.split("+")
        all_prices.append(split_price_string[0])
# print(all_prices)

# print(len(all_prices))


driver = webdriver.Chrome()
driver.get(form_link)
time.sleep(2)


for i in range(0,len(all_prices)-1):
    type_address = driver.find_element(By.XPATH,"/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    type_address.send_keys(all_addresses[i])
    time.sleep(1)

    type_price=driver.find_element(By.XPATH,"/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    type_price.send_keys(all_prices[i])
    time.sleep(1)

    type_link = driver.find_element(By.XPATH,"/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    type_link.send_keys(all_links[i])
    time.sleep(1)

    submit= driver.find_element(By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div')
    submit.click()

    re_submit = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    re_submit.click()


