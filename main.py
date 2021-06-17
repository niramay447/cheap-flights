
from data_manager import DataManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

if sheet_data[0]["iatacode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iatacode"] = flight_search.get_destination_code()