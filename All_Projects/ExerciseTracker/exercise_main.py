import requests
import datetime

time = datetime.datetime.now()
today = time.strftime("%d/%m/%Y")

today_time = time.strftime("%H:%M:%S")

ask_user = input("Tell me which exercises you did: ")

nutritionix_key = "3eea825fe21ff12d039f071891dc7413"
nutritionix_id = "d7825e81"
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_api = "https://api.sheety.co/d042c69e7014b566880a618c3d9e7e4f/copyOfMyWorkouts/workouts"

params = {
 "query": ask_user,
 "gender": "male",
 "weight_kg": 50,
 "height_cm": 164,
 "age": 30
}

headers = {
    "x-app-id": nutritionix_id,
    "x-app-key": nutritionix_key,

}

my_response = requests.post(url=nutritionix_endpoint, json=params, headers=headers)
data = my_response.json()
print(my_response.status_code)

for exercise in data["exercises"]:
    params = {
        "workout": {
            "date": today,
            "time": today_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    bearer = {
        "Authorization": "Basic bnVsbDpudWxs"

    }
    response = requests.post(url=sheety_api, json=params, headers=bearer)



# fuck = requests.get(url="https://api.sheety.co/d042c69e7014b566880a618c3d9e7e4f/copyOfMyWorkouts/workouts")
# data = response.json()
# print(data)