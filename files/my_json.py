import json
from pprint import pprint

with open('data/data.json', 'r') as file:
    data = json.load(file)
    pprint(data)
    print('Version: ' + data['Version'])

with open('data/my_data.json', 'w') as file:
    data['a'] = 10
    data['b'] = 20
    text = json.dump(data, file)
