import json

def act_on_file(path, func):
    with open(path, 'r') as file:
        return func(file)

def load_json_from_file(path):
    return act_on_file(path, json.load)