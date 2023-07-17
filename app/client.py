import requests

endpoint = "http://127.0.0.1:8000/users/register"
get_user = "http://127.0.0.1:8000/users/1"
get_all_posts = "http://127.0.0.1:8000/sqlalchemy"
login_endpoint = "http://127.0.0.1:8000/login"

login_data = {
    "username": "unknown@gmail.com",
    "password":"test123"
}

data = {
    "email":"unknown@gmail.com",
    "password":"test123",
    "username":"Unknnown user"
}

response = requests.post(login_endpoint, data=login_data)
print(response.json())