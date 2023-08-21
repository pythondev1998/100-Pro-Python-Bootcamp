import requests
from datetime import datetime
USERNAME = "brianfortuna95"
TOKEN = ""
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"
nutri_endpoint = "https://trackapi.nutritionix.com/v2/locations"

def create_account():
    url = "https://pixe.la/v1/users"

    params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }

    #response = requests.post(url=url, json=params)
    #response.raise_for_status()
    #print(response.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
        "id": GRAPH_ID,
        "name": "Running Graph",
        "unit": "km",
        "type": "float",
        "color": "shibafu",

    }

headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year=2023, month=5, day=11)

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "80",
}

#response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
#print(response.text)


#UPDATE PIXEL
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "5.0",
}
#response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
#print(response.text)

#DELETE PIXEL

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
