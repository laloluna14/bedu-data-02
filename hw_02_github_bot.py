'''
- Ask for a list of github usernames and download their avatar images

input('Users:')
galileoguzman, frasgado, laloluna14, ....
'''

import requests

# Importing function from another file
from github_user_function import get_user

# Modified function
def download_file(url_file, username):
    '''
    Name: download_file
    Params: url_file -> String
    Returns: None or image file
    '''
    response = requests.get(url_file)
    if response.status_code != 200:
        return None
    response_content = response.content # Store response content to be save later
    filename = f'tmp/{username}.png'
    with open(filename, 'wb') as image:
        image.write(response_content)
        return image

usernames = []
users = []
cycle = True

# Getting the usernames
while(cycle):
    username = input('Give me an username: ')
    usernames.append(username)

    add = input('Do you want to add more users? (y/n): ')

    if(add == 'n'):
        cycle = False

# Getting the records of the users
for username in usernames:
    users.append(get_user(username))

# Getting and downloading the avatar image of the user
for user in users:
    url_file = user['avatar_url']
    download_file(url_file, user['login'])
