import requests

SHEET_TOKEN = ''
url = "https://api.sheety.co/2cb1ee9bee71238329d813bc8334954d/flightDeals/users"


class ClubRegister:
    def __init__(self):
        pass

    def welcome(self):
        print("Welcome to Brian's Flight Club.")
        print("We find the best flight deals ad email you.")
        first_name_text = input("What is your first name? ")
        last_name_text = input("What is your last name? ")
        email_text = input("What is your email? ")
        re_email_text = input("Type your email again. ")

        headers = {
            "Authorization": f"Bearer {SHEET_TOKEN}",
            "Content-Type": "application/json"
        }

        if email_text == re_email_text:
            data = {
                "user": {
                    "firstName": first_name_text,
                    "lastName": last_name_text,
                    "email": email_text
                }
            }
            response = requests.post(url=url, json=data, headers=headers)
            if response.status_code == 200:
                print("You're in the club!")
            else:
                print("Error en la solicitud POST:", response.status_code)
