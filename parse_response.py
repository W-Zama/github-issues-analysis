import json

with open('./output/response.txt', 'r') as f:
    json_text = f.read()

json_data = json.loads(json_text)

# generate csv file about bug detection time
with open('./output/time_data.csv', 'w') as f:
    f.write('created_at, updated_at\n')
    for d in json_data:
        f.write(f'{d["created_at"]}, {d["updated_at"]}' + '\n')
