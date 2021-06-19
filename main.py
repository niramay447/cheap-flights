import datetime

from data_manager import DataManager
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

ORIGIN_CITY_IATA = "AMD"
if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + datetime.timedelta(days=1)
six_months_from_today = datetime.now() + datetime.timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time = tomorrow,
        to_time = six_months_from_today
    )