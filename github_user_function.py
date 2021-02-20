import requests

BASE_URL = 'https://api.github.com/'

def get_user_endpoint(username):
    '''
    Name: get_user_endpoint
    Params: username -> String
    Returns: The endpoint url to fetch user information from Github API
    '''
    return f'{BASE_URL}users/{username}'

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

def download_file(url_file):
    '''
    Name: download_file
    Params: url_file -> String
    Returns: None or image file
    '''
    response = requests.get(url_file)
    if response.status_code != 200:
        return None
    response_content = response.content # Store response content to be save later
    filename = f'tmp/usuario.png'
    with open(filename, 'wb') as image:
        image.write(response_content)
        return image
