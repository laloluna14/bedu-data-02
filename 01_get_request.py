import requests

response = requests.get('https://galileoguzman.com')

print(response.content)
print(response.status_code)
