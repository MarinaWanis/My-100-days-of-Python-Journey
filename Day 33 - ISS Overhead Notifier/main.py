import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 23.093652 # Your latitude
MY_LONG = 55.149418 # Your longitude
SENDER_EMAIL= "********@gmail.com"
SENDER_PASSWORD = "***************"
RECEIVER_EMAIL = "******@yahoo.com"

iss_latitude = None
iss_longitude = None

def is_iss_overhead():
    global iss_longitude, iss_latitude
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    print(f"lat:{iss_latitude} and lng:{iss_longitude}")

    #Your position is within +5 or -5 degrees of the ISS position.
    if abs(iss_latitude - MY_LAT) <= 5 and abs(iss_longitude - MY_LONG) <=5:
        # print(f"Close by: {abs(iss_latitude - MY_LAT)} and {abs(iss_longitude - MY_LONG)}")
        return True

    else:
        # print(f"Far away: {abs(iss_latitude - MY_LAT)} and {abs(iss_longitude - MY_LONG)}")
        return False

def is_nighttime():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.utcnow().hour
    # print(sunset, time_now)
    if time_now >= sunset or time_now <= sunrise:
        return True
    else:
        return False

while True: # this is to run the code at night and running this check every 60 seconds 
    time.sleep(60) 
    if is_nighttime() and is_iss_overhead():
        with smtplib.SMTP(host="smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL,password=SENDER_PASSWORD)
            connection.sendmail(from_addr=SENDER_EMAIL,to_addrs=RECEIVER_EMAIL,msg=f"Subject:LOOK UP 👆 \n\n"
                        f"The ISS is about you in the sky")


