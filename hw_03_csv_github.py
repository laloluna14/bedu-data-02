'''
- Given a github username extrac all his/her folowers and store them into a CSV File

https://api.github.com/users/{user}/followers
'''

import requests, csv

COLUMNS = ['login', 'id', 'node_id', 'avatar_url', 'gravatar_id', 'url', 'html_url', 'followers_url', 'following_url', 'gists_url', 'starred_url', 'subscriptions_url', 'organizations_url', 'repos_url', 'events_url', 'received_events_url', 'type', 'site_admin']
FILENAME = 'tmp/followers_github.csv'
BASE_URL = 'https://api.github.com/'

# Modified functions from another file
def get_user_endpoint(username):
    '''
    Name: get_user_endpoint
    Params: username -> String
    Returns: The endpoint url to fetch user information from Github API
    '''
    return f'{BASE_URL}users/{username}/followers'

def get_user(username):
    '''
    Name: get_user
    Params: username -> String
    Returns: Dictionary with user information
    '''
    url = get_user_endpoint(username)
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

# Getting the username
username = input('Give me an username: ')

# Getting the followers of the user
followers = get_user(username)

# Opening file in writable mode
with open(FILENAME, mode='w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=COLUMNS)

    # Writing the columns
    writer.writeheader()

    # Writing the rows
    for follower in followers:
        writer.writerow(follower)
