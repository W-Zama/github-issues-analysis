import json
import os


def generate_csv(json_list):
    # generate csv file about bug detection time
    output_dir = f'./output/{os.getenv("owner")}_{os.getenv("repo")}'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(f'./output/{os.getenv("owner")}_{os.getenv("repo")}/time_series_data.csv', 'w') as f:
        f.write('number, created_at, updated_at, closed_at\n')
        for d in json_list:
            f.write(
                f'{d["number"]}, {d["created_at"]}, {d["updated_at"]}, {d["closed_at"]}' + '\n')
