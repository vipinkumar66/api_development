import requests

endpoint = "http://127.0.0.1:8000/users/register"
get_user = "http://127.0.0.1:8000/users/1"
get_all_posts = "http://127.0.0.1:8000/sqlalchemy?search=django"
login_endpoint = "http://127.0.0.1:8000/login"
create_endpoint = "http://127.0.0.1:8000/sqlalchemy/createpost"
get_post = "http://127.0.0.1:8000/sqlalchemy/posts/7"
vote_endpoint = "http://127.0.0.1:8000/votes/"
get_posts = "http://127.0.0.1:8000/sqlalchemy/"


vote_data = {
  "post_id" : 10,
  "dir" : 1
}

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
    "email":"Mahes@gmail.com",
    "password":"test123",
    "username":"Mahesh Kumar"
}

post_data = {
  'title': 'DS',
  'content': 'DS stands for the data structures and they are basically used to store the data.', 'published': 'true'}


post_header = {
  "Authorization":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE2ODk4MjA0OTN9.HXNxOKuSsAd6Pc0XQ_v32Voi9rt_SDS8J9nUkrXmX1g"
}
# json=post_data
# response = requests.post(endpoint, json=data)
# response = requests.post(create_endpoint, json=post_data, headers=post_header)
# response = requests.post(login_endpoint, data=login_data)
# response = requests.get(get_all_posts, headers=post_header)
response = requests.get(get_all_posts, headers=post_header)

# response = requests.post(vote_endpoint, json=vote_data, headers=post_header)


print(response.json())
