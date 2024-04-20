import yaml
from pprint import pprint

with open('data/playbook.yaml', 'r') as file:
    data = yaml.safe_load(file)
    pprint(data)