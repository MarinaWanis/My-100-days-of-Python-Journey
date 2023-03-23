import requests

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_HEADER = {
    "apikey": "hZRR3BfXdraWXGISmB8HK_SMJJ0YRJWF"
}

# This class searches for the chepeast flight price using Tequila Flight Search API
class FlightSearch:
    def __init__(self):
        self.cityFrom = None
        self.cityTo = None
        self.dateFrom = None
        self.dateTo = None
        self.adults = None

    def get_city_code(self, cityname: str):
        tequila_location_url = f"{TEQUILA_ENDPOINT}/locations/query"
        tequila_location_params = {
            "term": cityname,
        }
        location_response = requests.get(url=tequila_location_url, headers=TEQUILA_HEADER,
                                         params=tequila_location_params)
        location_response.raise_for_status()
        return location_response.json()["locations"][0]["code"]

    def get_flight_details(self):
        tequila_search_url = f"{TEQUILA_ENDPOINT}/v2/search?"

        tequila_parameters = {
            "fly_from": self.cityFrom,
            "fly_to": self.cityTo,
            "date_from": self.dateFrom,
            "date_to": self.dateTo,
            "adults": self.adults,
            "curr": "AED",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0
        }

        tequila_response = requests.get(url=tequila_search_url, headers=TEQUILA_HEADER, params=tequila_parameters)
        tequila_response.raise_for_status()

        self.flight_prices_list = [{'price': f"{d['price']}", 'flyfrom': f"{d['cityFrom']}-{d['flyFrom']}",
                                    'flyto': f"{d['cityTo']}-{d['flyTo']}"} for d in tequila_response.json()["data"]]

        tequila_parameters = {
            "fly_from": self.cityFrom,
            "fly_to": self.cityTo,
            "date_from": self.dateFrom,
            "date_to": self.dateTo,
            "adults": self.adults,
            "curr": "AED",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 1
        }
        tequila_response = requests.get(url=tequila_search_url, headers=TEQUILA_HEADER, params=tequila_parameters)
        tequila_response.raise_for_status()

    def get_cheapest_flight_price(self):
        cheapest_flight_price = self.flight_prices_list[0]["price"]
        return cheapest_flight_price

    def get_cheapest_flight_cityFrom(self):
        cheapest_flight_cityFrom = self.flight_prices_list[0]["flyfrom"]
        return cheapest_flight_cityFrom

    def get_cheapest_flight_cityTo(self):
        cheapest_flight_cityTo = self.flight_prices_list[0]["flyto"]
        return cheapest_flight_cityTo
