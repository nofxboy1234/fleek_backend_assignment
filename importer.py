import json


def import_json():
    with open("tmp.json", "r") as file:
        contents = json.load(file)
    return contents
