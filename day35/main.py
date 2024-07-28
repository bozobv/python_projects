import requests
import os
from twilio.rest import Client

API = ""
LAT = 47.501423
LNG = 19.071974
TEST_LAT = 47.281280
TEST_LNG = 15.969010

def ask_12hours_code():

    parameters = {
        "lat" : TEST_LAT,
        "lon" : TEST_LNG,
        "appid" : API,
        "cnt" : 4
    }

    response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast?", params=parameters)
    response.raise_for_status()
    weather_data = response.json()["list"]

    will_rain = False

    for data_chunk in weather_data:
        weather_code = data_chunk["weather"][0]["id"]
        if weather_code < 700:
            will_rain = True
        #print(weather_code)
    
    return will_rain


def test_send_sms():
    account_sid = ""
    auth_token = ""
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Ma esni fog az eső, tesó. Vigyél esernyőt!",
        from_="",
        to="",
    )

    print(message.body)

if ask_12hours_code():
    test_send_sms()