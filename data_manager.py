import requests

SHEETY_ENDPOINT = "https://api.sheety.co/cf63aa3d1cb6c7ae5ecf49eb6a340d82/flightDeals/prices"

class DataManager:

    def __int__(self):
        self.destination_code = {}

    def get_destination_data(self):

        response = requests.get(SHEETY_ENDPOINT)
        data = response.json()
        self.destination_code = data["prices"]

        return self.destination_code