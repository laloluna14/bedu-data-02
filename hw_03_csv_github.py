'''
- Given a github username extrac all his/her folowers and store them into a CSV File

https://api.github.com/users/{user}/followers
'''

import requests, csv
page = 1
cycle = True

COLUMNS = ['login', 'id', 'node_id', 'avatar_url', 'gravatar_id', 'url', 'html_url', 'followers_url', 'following_url', 'gists_url', 'starred_url', 'subscriptions_url', 'organizations_url', 'repos_url', 'events_url', 'received_events_url', 'type', 'site_admin']
FILENAME = 'tmp/followers_github.csv'
BASE_URL = 'https://api.github.com/'

# Modified functions from another file
def get_user_endpoint(username, page):
    '''
    Name: get_user_endpoint
    Params: username -> String
    Returns: The endpoint url to fetch user information from Github API
    '''
    return f'{BASE_URL}users/{username}/followers?page={page}'

def get_user(username, page):
    '''
    Name: get_user
    Params: username -> String
    Returns: Dictionary with user information
    '''
    url = get_user_endpoint(username, page)
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

# Getting the username
username = input('Give me an username: ')

# Opening file in writable mode
with open(FILENAME, mode='w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=COLUMNS)

    # Writing the columns
    writer.writeheader()

    while cycle == True:
        # Getting the followers of the user from all the pages
        followers = get_user(username, page)

        if followers != None:
            # Writing the rows
            for follower in followers:
                writer.writerow(follower)
            
            page = page + 1
        
        else:
            cycle = False
