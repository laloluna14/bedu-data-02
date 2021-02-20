import csv
from github_user_function import get_user

COLUMNS = ['login', 'id', 'node_id', 'avatar_url', 'gravatar_id', 'url', 'html_url', 'followers_url', 'following_url', 'gists_url', 'starred_url', 'subscriptions_url', 'organizations_url', 'repos_url', 'events_url', 'received_events_url', 'type', 'site_admin', 'name', 'company', 'blog', 'location', 'email', 'hireable', 'bio', 'twitter_username', 'public_repos', 'public_gists', 'followers', 'following', 'created_at', 'updated_at',]
FILENAME = 'tmp/user_github.csv'

user = get_user('galileoguzman')

# Opening file in writable mode
with open(FILENAME, mode='w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=COLUMNS)

    # Write columns
    writer.writeheader()

    # Write at least one row
    writer.writerow(user)
    