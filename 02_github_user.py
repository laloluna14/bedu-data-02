import requests

BASE_URL = "https://api.github.com/"

username = input('Give me a github username:\t')
endpoint_url = BASE_URL + f'users/{username}'

response = requests.get(endpoint_url)
# print(response.status_code) # 200 means user exists
user = response.json() # From json to python Dict

# print(type(user))

print(user['avatar_url'])
