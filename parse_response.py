import json

with open('./response.txt', 'r') as f:
    json_text = f.read()

# print(json_text)

json_data = json.loads(json_text)

with open('./time_data.csv', 'w') as f:
    f.write('created_at, updated_at\n')
    for d in json_data:
        f.write(f'{d["created_at"]}, {d["updated_at"]}' + '\n')
