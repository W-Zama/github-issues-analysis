import requests
import json
import os
from dotenv import load_dotenv
import datetime

def get_issues():
    # load .env content
    load_dotenv()
    owner = os.getenv('OWNER')
    repo = os.getenv('REPO')
    bug_label = os.getenv('BUG_LABEL')
    access_token = os.getenv('ACCESS_TOKEN')

    # set page information
    page = 1
    per_page = 100        # this is max value
    response_json_list = []

    # while True:
    for i in range(1):      # for debug
        print(
            f'Now getting {page} page issues... (Each page contains {per_page} issues.)')
        # set url, headers and params
        url = f'https://api.github.com/repos/{owner}/{repo}/issues?labels={bug_label}&per_page=100'
        headers = {
            'Authorization': f'token {access_token}',
        }
        params = {
            'labels': bug_label,
            'page': page,
            'per_page': per_page,
            'state': 'all'
        }

        # get issues via github api
        response = requests.get(url, headers=headers, params=params)

        # check response status code
        if response.status_code == 200:
            if not response.json():         # this means that response list is empty
                break
            response_json_list += response.json()
            page += 1
        else:
            print(f"Failed to retrieve issues: {response.status_code}")
            break

    # show github api limit information
    print('### Github API limit information ###')
    print(f'x-ratelimit-limit: {response.headers.get("x-ratelimit-limit")}')
    print(
        f'x-ratelimit-remaining: {response.headers.get("x-ratelimit-remaining")}')
    print(f'x-ratelimit-reset: {datetime.datetime.fromtimestamp(int(response.headers.get("x-ratelimit-reset")))}')

    # write json to file
    jst_now = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S+09:00')   # current time in JST
    with open(f'./output/response_{owner}_{repo}_{jst_now}.json', mode='w') as f:
        pretty_json_string = json.dumps(response_json_list, indent=4)
        f.write(pretty_json_string)

    return response_json_list
