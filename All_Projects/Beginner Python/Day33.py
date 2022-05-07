import requests
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# print(response.status_code)
#
# data = response.json()
# print(data["iss_position"])
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
# print(iss_position)

para = {
    "lat": 28.626230,
    "lng": 77.394096,
    "formatted": 0,
    "date": "2003-06-11",
}

response = requests.get(url="http://api.sunrise-sunset.org/json", params=para)

data = response.json()
print(data["results"]["sunrise"].split("T")[1].split(":")[0])
print(data["results"]["sunset"].split("T")[1].split(":")[0])
