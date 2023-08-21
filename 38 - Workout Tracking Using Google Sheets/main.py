import requests
import os
from datetime import datetime

APP_ID = os.environ['APP_ID']
API_KEY = os.environ['API_KEY']
SHEETY_ENDPOINT = os.environ['SHEETY_ENDPOINT']
TOKEN = os.environ['TOKEN']

USERNAME = os.environ['USERNAME']
PASSWORD = os.environ['PASSWORD']

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

GENDER = "male"
WEIGHT_KG = 69.85
HEIGHT_CM = 175
AGE = 24
exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
            "distance": exercise["met"]
        }
    }
  
    #sheet_response = requests.post(SHEETY_ENDPOINT, json=sheet_inputs)
   
    # Basic Authentication
    """
    sheet_response = requests.post(
        SHEETY_ENDPOINT,
        json=sheet_inputs,
        auth=("brian", "afawfaf32"))
    print(sheet_response.text)
    """
    # Bearer Token Authentication
    """
    bearer_headers = {
        "Authorization": TOKEN
    }
    sheet_response = requests.post(
        SHEETY_ENDPOINT,
        json=sheet_inputs,
        headers=bearer_headers
    )
    """
