import json

def generate_csv(json_list):
    # generate csv file about bug detection time
    with open('./output/time_data.csv', 'w') as f:
        f.write('created_at, updated_at, closed_at\n')
        for d in json_list:
            f.write(f'{d["created_at"]}, {d["updated_at"]}, {d["closed_at"]}' + '\n')
