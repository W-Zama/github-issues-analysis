import requests
import json
import os
from dotenv import load_dotenv

# load .env content
load_dotenv()
owner = os.getenv('OWNER')
repo = os.getenv('REPO')
bug_label = os.getenv('BUG_LABEL')
access_token = os.getenv('ACCESS_TOKEN')

# set url, headers and params
url = f'https://api.github.com/repos/{owner}/{repo}/issues?labels={bug_label}&per_page=100'
headers = {
    'Authorization': f'token {access_token}',
}
params = {
    'labels': bug_label,
    'per_page': 100,
}

# get issues via github api
response = requests.get(url, headers=headers, params=params)

# print(response.request.url)
# print(response.headers.get('x-ratelimit-limit'))
# print(response.headers.get('x-ratelimit-remaining'))
# print(response.headers.get('x-ratelimit-reset'))

with open('./output/response.txt', mode='w') as f:
    if response.status_code == 200:
        print('OK')
        json_string = response.text
        json_data = json.loads(json_string)
        pretty_json_string = json.dumps(json_data, indent=4)
        f.write(pretty_json_string)
    else:
        print(f"Failed to retrieve issues: {response.status_code}")