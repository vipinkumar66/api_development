import requests

endpoint = "http://127.0.0.1:8000/users/register"

data = {
    "email":"vipin@gmail.com",
    "password":"test123",
    "username":"vipin"
}

response = requests.post(endpoint, json=data)
print(response.json())