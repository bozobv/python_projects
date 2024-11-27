import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USER_NAME = ""
TOKEN = ""
GRAPH_ID = "mygraph"
HEADERS = {
    "X-USER-TOKEN": TOKEN
}

def registration():

    user_params= {
            "token": TOKEN,
            "username": USER_NAME,
            "agreeTermsOfService": "yes",
            "notMinor": "yes"
        }

    response = requests.post(url=pixela_endpoint, json=user_params)

    print(response.text)

def create_graph():
    graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

    graph_config = {
        "id": GRAPH_ID,
        "name": "Learning Graph",
        "unit": "minute",
        "type": "float",
        "color": "ajisai"
    }

    response = requests.post(url=graph_endpoint, json=graph_config, headers=HEADERS)
    print(response.text)

def post_pixel():
    pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"
    today = datetime.now()
    #today = datetime(year=2024, month=8, day=19)
    print(today.strftime("%Y%m%d"))

    pixel_data = {
        "date": today.strftime("%Y%m%d"),
        "quantity": input("hány percet tanultál a mai napon, tanárbástyázatom?    ")
    }

    response = requests.post(url=pixel_endpoint, json=pixel_data, headers=HEADERS)
    print(response.text)

def put_pixel():
    pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
    today = datetime.now()

    pixel_data = {
        "quantity": "10.12"
    }

    response = requests.put(url=pixel_endpoint, json=pixel_data, headers=HEADERS)
    print(response.text)

def delete_pixel():
    today = datetime(year=2024, month=8, day=19)
    pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

    response = requests.delete(pixel_endpoint, headers=HEADERS)
    print(response.text)

post_pixel()


