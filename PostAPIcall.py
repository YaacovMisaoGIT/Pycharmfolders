import requests


header = {
        "accept: */*",
        "Content-Type: application/json"
          }

request_payload = {
            "id": 12,
            "title": "stringsss",
            "description": "strinssg",
            "pageCount": 10,
            "excerpt": "string",
            "publishDate": "2024-08-31T18:47:32.725Z",
            "completed": True
        }


response = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Books",
                         headers = header,
                         json = request_payload)

print(response.status_code)
print(response.json())
