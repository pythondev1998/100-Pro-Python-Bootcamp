import requests
import os

SHEET_ENDPOINT = "https://api.sheety.co/2cb1ee9bee71238329d813bc8334954d/flightDeals/prices"
SHEET_TOKEN = ""
SHEET_USERS_ENDPOINT = "https://api.sheety.co/2cb1ee9bee71238329d813bc8334954d/flightDeals/users"
SHEETY_PRICES_ENDPOINT = SHEET_ENDPOINT


class DataManager:
    def __init__(self):
        self.customer_data = None
        self.destination_data = {}

    def get_destination_data(self):
        headers = {
            "Authorization": SHEET_TOKEN,
            "Content-Type": "application/json"
        }
        response = requests.get(SHEET_ENDPOINT, headers=headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data


    def update_destination_codes(self):
        headers = {
            "Authorization": SHEET_TOKEN,
            "Content-Type": "application/json"
        }
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=headers
            )
            print(response.text)

    def get_customer_emails(self):
        headers = {
            "Authorization": SHEET_TOKEN,
            "Content-Type": "application/json"
        }
        customers_endpoint = SHEET_USERS_ENDPOINT
        response = requests.get(customers_endpoint, headers=headers)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data