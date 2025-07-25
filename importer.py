import json

from pilotlog.models import Aircraft, Flight


def import_json(json_file):
    with open(json_file, "r") as file:
        rows = json.load(file)

    return rows


def get_db_fields_to_data(row):
    verbose_to_fields = Aircraft.get_verbose_names_to_fields()
    db_fields_to_data = {}

    for key in row.meta.keys():
        db_field = verbose_to_fields[key]
        db_fields_to_data[db_field] = row.meta[key]


def save_aircraft(row):
    db_fields_to_data = get_db_fields_to_data(row)
    aircraft = Aircraft(**db_fields_to_data)
    aircraft.save()


def save_flight(row):
    db_fields_to_data = get_db_fields_to_data(row)
    flight = Flight(**db_fields_to_data)
    flight.save()


def save_to_db(rows):
    for row in rows:
        if row["table"] == "Aircraft":
            save_aircraft(row)

        # if row["table"] == "Flight":
        #     save_flight(row)
