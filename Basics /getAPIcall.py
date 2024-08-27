import requests

url = "https://fakerestapi.azurewebsites.net/api/v1/Activities"
header = { 'accept':'text/plain' }
response = requests.get(url)

for res in response.json():
    print(f"Id - {res['id']} Title - {res['title']}\n")

assert response.status_code==200
