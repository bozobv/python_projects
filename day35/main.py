import requests

API = ""
LAT = 47.501423
LNG = 19.071974

parameters = {
    "lat" : LAT,
    "lon" : LNG,
    "appid" : API,
    "cnt" : 4
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast?", params=parameters)
response.raise_for_status()
weather_data = response.json()["list"]

for data_chunk in weather_data:
    weather_code = data_chunk["weather"][0]["id"]
    if weather_code < 700:
        print("teso, vigyél esernyőt")
    print(weather_code)

#print(weather_data)
