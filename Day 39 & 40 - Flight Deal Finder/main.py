# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import datetime as dt
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager

tomorrows_date = dt.datetime.now() + dt.timedelta(days=1)
todays_date_plus60 = dt.datetime.now() + dt.timedelta(days=60)

read_sheet = DataManager()
flight_search = FlightSearch()

for key, value in read_sheet.get_data().items():
    city_code = f"{flight_search.get_city_code(read_sheet.get_data()[key]['cityTo'])}"
    print(f"{key}: {read_sheet.get_data()[key]['cityTo']}, {city_code}, {read_sheet.get_data()[key]['lowestPrice']}")

    flight_search.cityFrom = "city:DXB"
    flight_search.cityTo = f"city:{city_code}"
    flight_search.dateFrom = tomorrows_date.strftime("%d/%m/%Y")
    flight_search.dateTo = todays_date_plus60.strftime("%d/%m/%Y")
    flight_search.adults = 1

    try:
        flight_search.get_flight_details()
        current_lowest_price = int(flight_search.get_cheapest_flight_price())
        my_lowest_price = int(read_sheet.get_data()[key]['lowestPrice'])

    except IndexError:
        print(f"No flights found for this destination:{city_code}")
        continue

    if current_lowest_price < my_lowest_price:
        message = f"Low price alert! Only AED {flight_search.get_cheapest_flight_price()} to fly from {flight_search.get_cheapest_flight_cityFrom()} to {flight_search.get_cheapest_flight_cityTo()}, from {flight_search.dateFrom} to {flight_search.dateTo}"
        update_google_sheets = FlightData(object_id=key, code=f"{flight_search.get_cheapest_flight_cityFrom()} to {flight_search.get_cheapest_flight_cityTo()}", lowest_price= current_lowest_price )
        print(message)
        send_message = NotificationManager(message)
        for user_index in range(len(read_sheet.get_users_details()["users"])):
            print(read_sheet.get_users_details()["users"][user_index]["email"])
            send_message.sendEmail(to_email=read_sheet.get_users_details()["users"][user_index]["email"], message=f"Subject:Low Price Flight Alert!\n\n{message}")
