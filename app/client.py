import requests

endpoint = "http://127.0.0.1:8000/users/register"
get_user = "http://127.0.0.1:8000/users/1"
get_all_posts = "http://127.0.0.1:8000/sqlalchemy"
login_endpoint = "http://127.0.0.1:8000/login"
create_endpoint = "http://127.0.0.1:8000/sqlalchemy/createpost"
get_post = "http://127.0.0.1:8000/sqlalchemy/posts/7"


login_data = {
    "username": "unknown@gmail.com",
    "password":"test123"
}

create_user = {
    "email": "unknown@gmail.com",
    "username":"unknown",
    "password":"test123"
}

data = {
    "email":"unknown@gmail.com",
    "password":"test123",
    "username":"Unknnown user"
}

post_data = {
  'title': 'Django Rest Framework',
  'content': 'Python framework which helps in creating a strong backend',
}

post_header = {
  "Authorization":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE2ODk2NTA1Njd9.Tywf8d-CRGzPE5nO1UWvhowQZHRya8jpBpM6T59jG2k"
}
# json=post_data
# response = requests.post(login_endpoint, json=login_data)
response = requests.post(create_endpoint, json=post_data, headers=post_header)
# response = requests.post(login_endpoint, data=login_data)

print(response.json())
"""
[{'title': 'Django Rest Framework', 'content': 'Python framework which helps in creating a strong backend', 'published': True}, {'title': 'Reactue}, {'title': 'OOPS', 'content': 'Object orientation programming. Here we make use of objects and classes.', 'published': True}, {'title': 'JWT TOKEN', 'content': 'This is a third party package that is used with the fastapi and some other frameworks like DRF for the authentication purpose as the server is stateless', 'published': True}]"""