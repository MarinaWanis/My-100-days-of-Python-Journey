#This class is responsible for talking to the Google Sheet.
import requests
import os

sheety_endpoint = f"https://api.sheety.co/{os.environ['SHEET_ID']}/flightDeals"

prices_sheet_endpoint=f"{sheety_endpoint}/prices"

user_sheet_endpoint= f"{sheety_endpoint}/users"

HEADER = {
    "Authorization": os.envrion["SHEETY_AUTH"]
}

class DataManager:
    def __init__(self):
        self.data = {
            2:{
                'cityTo': 'Paris',
                'iataCode': '',
                'lowestPrice': 5000000,
                'id': 2
            }
        }

    def get_data(self):
        sheety_response = requests.get(url=prices_sheet_endpoint, HEADERs=HEADER)
        sheety_response.raise_for_status()
        data_list ={item["id"]:{"cityTo": item["city"], "lowestPrice": item["lowestPrice"]} for item in sheety_response.json()["prices"]}
        return data_list


    def add_users(self, firstName, lastName, email):
        add_user_params = {
            "user":
                {
                    "firstName": firstName,
                    "lastName": lastName,
                    "email": email
                }
        }
        add_row_response = requests.post(url=user_sheet_endpoint, json=add_user_params, headers=HEADER)
        add_row_response.raise_for_status()
        add_row_response.json()

    def get_users_details(self):
        get_details = requests.get(url=user_sheet_endpoint, headers= HEADER)
        get_details.raise_for_status()
        return get_details.json()



