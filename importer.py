import json
import re

from pilotlog.models import Aircraft, Flight


def camel_to_snake(name):
    """
    Converts a camelCase or PascalCase string to snake_case.
    Handles general cases but might not perfectly handle all acronyms
    (e.g., 'myAPIKey' might become 'my_a_pi_key' instead of 'my_api_key').
    """
    s1 = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    s2 = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s1).lower()
    return s2


# Define the set of keywords that need to be prefixed with an underscore
RESERVED_KEYWORDS_TO_PREFIX = {"class", "complex"}


def rename_keys_to_snake_case(data):
    """
    Recursively renames all camelCase/PascalCase keys in a dictionary
    (or list of dicts) to snake_case.
    If a snake_case key matches a reserved keyword, it gets prefixed with an underscore.
    """
    if isinstance(data, dict):
        new_dict = {}
        for key, value in data.items():
            # 1. Convert key to snake_case
            snake_case_key = camel_to_snake(key)

            # 2. Check if the snake_case key is in the reserved list
            final_key = snake_case_key
            if snake_case_key in RESERVED_KEYWORDS_TO_PREFIX:
                final_key = "_" + snake_case_key

            # 3. Recursively process the value and add to the new dictionary
            new_dict[final_key] = rename_keys_to_snake_case(value)
        return new_dict
    elif isinstance(data, list):
        # Recursively process each element in the list
        return [rename_keys_to_snake_case(elem) for elem in data]
    else:
        # Return non-dict/list types as is
        return data


def import_json():
    with open("tmp.json", "r") as file:
        rows = json.load(file)

    # put into db
    for row in rows:
        row_clean = rename_keys_to_snake_case(row)

        if row_clean["table"] == "Aircraft":
            aircraft = Aircraft(**row.meta)
            aircraft.save()

        if row_clean["table"] == "Flight":
            flight = Flight(**row.meta)
            flight.save()
