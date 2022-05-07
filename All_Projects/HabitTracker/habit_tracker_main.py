import requests
import datetime

time = datetime.datetime.now()
today = time.strftime("%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "sgsgv154g5f1vf5g1vfdg4"
USERNAME = "devesh1113"
GRAPH_ID = "graph2"

pixela_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}

# response = requests.post(url=pixela_endpoint, json=pixela_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "kilogram",
    "type": "int",
    "color": "sora",
}

header = {
    "X-USER-TOKEN": TOKEN,
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)

# Posting a pixel
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_params = {
    "date": today,
    "quantity": "5",
}

response = requests.post(url=pixel_endpoint, json=pixel_params, headers=header)
print(response.text)

# updating a pixel

put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

put_params = {
    "quantity": "15"
}
# response = requests.put(url=put_endpoint, json=put_params, headers=header)
# print(response.text)

# response = requests.delete(url=put_endpoint, headers=header)
# print(response.text)