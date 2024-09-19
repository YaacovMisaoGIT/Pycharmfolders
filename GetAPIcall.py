import requests

def test_get_api_call():
    response = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Books/3")
    print(response.status_code)
    print(response.json())

