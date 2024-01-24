import requests
from datetime import datetime
import os


GENDER = "female"
WEIGHT_KG = 84
HEIGHT_CM = 160
AGE = 20


APP_ID = os.environ.get("ba05f607")
API_KEY = os.environ.get("83687c185251c22a89d7c971cbd5d732")


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"


exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": "ba05f607",
    "x-app-key": "83687c185251c22a89d7c971cbd5d732",
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(f"Nutritionix API call: \n {result} \n")

# Adding date and time
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

GOOGLE_SHEET_NAME = "MyWorkouts"
sheet_endpoint = "https://api.sheety.co/93985b5f8ac73b3a167d8ad23cc79a90/myWorkouts/workouts"

# Sheety API Call & Authentication
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }


    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=headers)

    # sheet_response = requests.post(
    #     sheet_endpoint,
    #     json=sheet_inputs,
    #     auth=(
    #         os.environ["meltingClock"],
    #         os.environ["Ticker12Tocker21"],
    #     )
    # )

    print(f"Sheety Response: \n {sheet_response.text}")
    print(f"Sheety Response: \n {sheet_response.text}")

