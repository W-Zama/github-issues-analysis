import json
from dotenv import load_dotenv
import os

def generate_csv(json_list):
    # load .env content
    load_dotenv()
    owner = os.getenv('OWNER')
    repo = os.getenv('REPO')

    # generate csv file about bug detection time
    with open(f'./output/time_data_{owner}_{repo}.csv', 'w') as f:
        f.write('created_at, updated_at, closed_at\n')
        for d in json_list:
            f.write(f'{d["created_at"]}, {d["updated_at"]}, {d["closed_at"]}' + '\n')
