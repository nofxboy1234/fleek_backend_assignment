import json
import re

from pilotlog.models import Aircraft, Flight


def camel_to_snake(name):
    s1 = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def rename_keys_to_snake_case(data):
    """
    Recursively renames all camelCase keys in a dictionary (or list of dicts)
    to snake_case.
    """
    if isinstance(data, dict):
        new_dict = {}
        for key, value in data.items():
            new_key = camel_to_snake(key)
            new_dict[new_key] = rename_keys_to_snake_case(value)  # Recurse for value
        return new_dict
    elif isinstance(data, list):
        return [
            rename_keys_to_snake_case(elem) for elem in data
        ]  # Recurse for list elements
    else:
        return data  # Return non-dict/list types as is


def import_json():
    with open("tmp.json", "r") as file:
        contents = json.load(file)

    # put into db
    for row in contents:
        row_clean = rename_keys_to_snake_case(row)

        if row_clean["table"] == "Aircraft":
            aircraft = Aircraft(**row.meta)
            aircraft.save()

        if row_clean["table"] == "Flight":
            flight = Flight(**row.meta)
            flight.save()
