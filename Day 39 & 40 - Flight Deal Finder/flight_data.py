#This class is responsible for structuring the flight data into Google sheets.
import requests
import os

class FlightData:
    def __init__(self, object_id, code, lowest_price ):
        edit_sheety_endpoint = f"https://api.sheety.co/{os.environ['SHEET_ID']}/flightDeals/prices/{object_id}"
        edit_row = {
            "price": {
                "iataCode": code,
                "lowestPrice": lowest_price
            }
        }
        header = {
            "Authorization": os.envrion["SHEETY_AUTH"]
        }
        edit_sheety_response = requests.put(url=edit_sheety_endpoint, headers=header, json= edit_row)
        edit_sheety_response.text


