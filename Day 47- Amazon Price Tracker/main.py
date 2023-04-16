import os

import requests
from bs4 import BeautifulSoup
import smtplib

ENDPOINT="https://www.amazon.com/Ninja-NC501-Milkshakes-Programs-Containers/dp/B0B9CZ6XBQ/ref=sr_1_2?crid=H9UTN6OOCDBX&keywords=ice+cream+machine+ninja&qid=1681573530&sprefix=ice+cream+machine+nin%2Caps%2C265&sr=8-2"
HEADER= {
    "User-Agent" :"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "Accept-Language":"en-GB,en-US;q=0.9,en;q=0.8"
}
SENDER_EMAIL= os.environ.get("SENDER_EMAIL")
SENDER_PASSWORD= os.environ.get("SENDER_PASSWORD")
receiver_email= os.environ.get("RECEIVER_EMAIL")

response = requests.get(url=ENDPOINT, headers=HEADER)

soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())
product_title =soup.find(name="span", id="productTitle").getText().strip()
print(product_title)
total_price_withdollar =soup.find(name="span", class_="a-offscreen").getText()
current_price = float(total_price_withdollar.split("$")[1])

email_msg = f"Subject:Amazon Lower Price!!\n\n Price has went down to $100 or below!\n\n Product Name: {product_title}\n\n Current Price: ${current_price}  "

if current_price >= 100:
    print(f"Current price= {current_price}")
    gmail_smtp = smtplib.SMTP(host="smtp.gmail.com", port=587)
    gmail_smtp.starttls()
    gmail_smtp.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)
    gmail_smtp.sendmail(from_addr=SENDER_EMAIL, to_addrs=receiver_email, msg=email_msg)




