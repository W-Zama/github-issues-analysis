import requests
import json

owner = 'facebook'
repo = 'react'

url = f'https://api.github.com/repos/{owner}/{repo}/issues?labels=type: bug'

response = requests.get(url)

with open('./response.txt', mode='w') as f:
    if response.status_code == 200:
        print('ok')
        json_string = response.text
        json_data = json.loads(json_string)
        pretty_json_string = json.dumps(json_data, indent=4)
        f.write(pretty_json_string)
    else:
        print(f"Failed to retrieve issues: {response.status_code}")