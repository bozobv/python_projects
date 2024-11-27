import requests
from datetime import datetime


APP_ID = ""
API_KEY = ""
nutri_endpoint = "https://trackapi.nutritionix.com/v2/natural"
sheety_post_endpoint = "https://api.sheety.co/bf3695847498eb9921b1e7d8c48331f5/workoutTracking/workouts"


HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

HEADERS2 = {
    "Authorization": " "
}


def exercise_req():

    query = input("mit sportoltál, barátom?   ")

    message = {
        "query": query,
        "weight_kg": 83,
        "height_cm": 190,
        "age": 24
    }

    response = requests.post(url=f"{nutri_endpoint}/exercise", json=message, headers=HEADERS)
    #print(response.text)

    exercises = response.json()["exercises"]

    today = datetime.now()

    for excercise in exercises:
        message = {
                "workout": {
                    "date" : f"{today.strftime('%Y-%m-%d')}",
                    "time": f"{today.strftime('%H:%M:%S')}",
                    "exercise": excercise["name"],
                    "duration": excercise["duration_min"],
                    "calories": excercise["nf_calories"]
                }
        }
            
        response = requests.post(url=f"{sheety_post_endpoint}", json=message, headers=HEADERS2)
        print(response.text)
            
exercise_req()

