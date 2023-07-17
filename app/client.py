import requests

endpoint = "http://127.0.0.1:8000/users/register"
get_user = "http://127.0.0.1:8000/users/1"
get_all_posts = "http://127.0.0.1:8000/sqlalchemy"
login_endpoint = "http://127.0.0.1:8000/login"
create_endpoint = "http://127.0.0.1:8000/sqlalchemy/createpost"

login_data = {
    "username": "unknown@gmail.com",
    "password":"test123"
}

data = {
    "email":"unknown@gmail.com",
    "password":"test123",
    "username":"Unknnown user"
}

post_data = {
  "title":"JWT TOKEN",
  "Content":"This is a third party package that is used with the fastapi and some other frameworks like DRF for the authentication purpose as the server is stateless",
  "published": "true"
}

response = requests.post(create_endpoint, json=post_data)
print(response.json())