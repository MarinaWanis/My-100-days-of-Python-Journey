import requests
import datetime as dt
import os

APP_ID = os.environ["APP_ID"]
API_KEY= os.environ["API_KEY"]
GENDER = "YOUR GENDER"
WEIGHT_KG = YOUR WEIGHT
HEIGHT_CM = YOUR HEIGHT
AGE = YOUR AGE


todays_date= dt.datetime.now()
formated_date= todays_date.strftime("%d/%m/%Y")
formated_time = todays_date.strftime("%H:%M:%S")

exercise_endpoint= "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_header= {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

exercise_parameters= {
 "query":input("What exercise have you done?: "),
 "gender":GENDER,
 "weight_kg":WEIGHT_KG,
 "height_cm":HEIGHT_CM,
 "age": AGE
}

nutitionix_response = requests.post(url=exercise_endpoint, headers=exercise_header, json= exercise_parameters)
nutitionix_data = nutitionix_response.json()

print(nutitionix_response)
calories = nutitionix_data["exercises"][0]["nf_calories"]
duration_min= nutitionix_data["exercises"][0]["duration_min"]
exercise = str.title((nutitionix_data["exercises"][0]["name"]))

print(calories, duration_min, exercise)

#--------------------------------Add a row in Google sheets--------------------------------#
sheety_endpoint = os.environ["SHEETY_ENDPOINT"]

sheety_header={
    "Authorization": os.environ["AUTHORIZATION"]
}

sheety_parameters={
    "workout": {
        "date": formated_date,
        "time": formated_time,
        "exercise": exercise,
        "duration": duration_min,
        "calories": calories,
    }
}
sheety_response= requests.post(url=sheety_endpoint, headers=sheety_header, json=sheety_parameters)
print(sheety_response.text)
