'''
Ask for a username and download his/her avatar image
'''

# Importing functions from another file
from github_user_function import get_user, download_file

# Getting the username
username = input('Give me an username: ')

# Getting the records of the user
user = get_user(username)

# Getting the avatar image of the user
url_file = user['avatar_url']

# Downloading the avatar image of the user
download_file(url_file)