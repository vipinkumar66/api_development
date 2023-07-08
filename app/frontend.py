import requests

# endpoint = "http://127.0.0.1:8000/get_data"
# endpoint = "http://127.0.0.1:8000/posts/10"
# endpoint = "http://127.0.0.1:8000/retrieve/post/10"
# endpoint = "http://127.0.0.1:8000/delete/post/10"
# endpoint = "http://127.0.0.1:8000/update/post/1"
endpoint = "http://127.0.0.1:8000/sqlalchemy/createpost"


# response = requests.get(endpoint)
data = {
    "title":"React framework",
    "content":"It is a javascript framework for the frontend part",
    "published":"True"

}
response = requests.post(endpoint, data=data)
# print(response.json()) in case of delete there will be no data
# if response.status_code == 204:
#     print("Your Post has been deleted")
# else:
#     print(response.json())
print(response.json())
