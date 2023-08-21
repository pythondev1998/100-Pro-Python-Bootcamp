import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 18.472019
MY_LONG = -69.902031
MY_EMAIL = ""
MY_PASSWORD = ""
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(3600)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Look Up :) \n\n The ISS is above you in the sky"
        )
