#This class is responsible for structuring the flight data into Google sheets.
import requests

class FlightData:
    def __init__(self, object_id, code, lowest_price ):
        edit_sheety_endpoint = f"https://api.sheety.co/539d02384dbdfa979ec8d677e3ec7a66/flightDeals/prices/{object_id}"
        edit_row = {
            "price": {
                "iataCode": code,
                "lowestPrice": lowest_price
            }
        }
        header = {
            "Authorization": "Basic TWFyaW5hOkphVGIqQjApNVB4Uk4="
        }
        edit_sheety_response = requests.put(url=edit_sheety_endpoint, headers=header, json= edit_row)
        edit_sheety_response.text


