import json

import requests

header = {'accept': 'text/plain',
          'content-type': 'application/json'}

url = 'https://fakerestapi.azurewebsites.net/api/v1/Activities'

request_payload = {
  "id": 169,
  "title": "rishi upload 3",
  "dueDate": "2024-08-27T00:44:26.822Z",
  "completed": True
}

response = requests.post(url=url, headers=header, json=request_payload)
print(response.text)
for i in json.loads(response.text):
    print(f"key - {i} | value - {json.loads(response.text)[i]}")
assert response.status_code == 200
