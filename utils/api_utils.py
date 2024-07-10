import requests
import json
import datetime
import os


def print_github_api_limit(response):
    print('### Github API limit information ###')
    print(f'x-ratelimit-limit: {response.headers.get("x-ratelimit-limit")}')
    print(
        f'x-ratelimit-remaining: {response.headers.get("x-ratelimit-remaining")}')
    print(
        f'x-ratelimit-reset: {datetime.datetime.fromtimestamp(int(response.headers.get("x-ratelimit-reset")))}')


def get_issues():
    # set page information
    page = 1
    per_page = 100        # this is max value
    response_json_list = []

    # set url
    url = f'https://api.github.com/repos/{os.getenv("owner")}/{os.getenv("repo")}/issues'
    print(f'Now accessing to {url}')

    # for i in range(1):      # for debug
    while True:
        print(
            f'Now getting {page} page issues... (Each page contains {per_page} issues.)')
        # set url, headers and params
        headers = {
            'Authorization': f'token {os.getenv("access_token")}',
        }
        params = {
            'labels': os.getenv('bug_label'),
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
    print_github_api_limit(response)

    # write json to file
    output_dir = f'./output/{os.getenv("owner")}_{os.getenv("repo")}'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(f'{output_dir}/response.json', mode='w') as f:
        pretty_json_string = json.dumps(response_json_list, indent=4)
        f.write(pretty_json_string)

    return response_json_list
