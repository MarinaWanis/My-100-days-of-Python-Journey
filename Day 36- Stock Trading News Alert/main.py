import datetime as dt
import requests
from html import unescape
from twilio.rest import Client

account_sid = '*******************************'
auth_token = '********************************'
client = Client(account_sid, auth_token)

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_market_parameters= {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": "***************"
}

yesterdays_date= str(dt.datetime.today() - dt.timedelta(days=3)).split(" ")[0]
before_yesterdays_date = str(dt.datetime.today() - dt.timedelta(days=4)).split(" ")[0]

stock_response= requests.get(url="https://www.alphavantage.co/query", params= stock_market_parameters)
stock_response.raise_for_status()
yesterdays_closed_rate = float(stock_response.json()["Time Series (Daily)"][yesterdays_date]["4. close"])
before_yesterdays_closed_rate = float(stock_response.json()["Time Series (Daily)"][before_yesterdays_date]["4. close"])
print(f"{yesterdays_date}: {yesterdays_closed_rate}")
print(f"{before_yesterdays_date}: {before_yesterdays_closed_rate}")

percentage_rate = round((yesterdays_closed_rate/before_yesterdays_closed_rate)*100 - 100)

print(f"{percentage_rate}%")

if abs(percentage_rate) >= 5:
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_parameters = {
        "q": COMPANY_NAME,
        "from": yesterdays_date,
        "sortBy":"publishedAt",
        "apiKey": "************************"
    }

    news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
    news_response.raise_for_status()
    for index in range(0,3):
        news_title= unescape(news_response.json()["articles"][index]["title"])
        news_details= unescape(news_response.json()["articles"][index]["description"])
        news_url = news_response.json()["articles"][index]["url"]
        # print(f"{news_title}:\n{news_details}\n{news_url}\n\n")

## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
    if percentage_rate < 0:
        sign = "🔻"
    else:
        sign = "🔺"


    message = client.messages.create(
        body=f"{STOCK}:{sign}{percentage_rate}%\nHeadline: {news_title}\nBrief: {news_details}",
        from_='whatsapp:*********',
        to='whatsapp:**********'
    )

    print(message.status)

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

