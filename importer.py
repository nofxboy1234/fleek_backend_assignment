import json

from pilotlog.models import Aircraft, Flight


def import_json(json_file):
    with open(json_file, "r") as file:
        rows = json.load(file)

    return rows


def get_db_fields_to_data(row, model):
    if model == "Aircraft":
        verbose_to_fields = Aircraft.get_verbose_names_to_fields()
    elif model == "Flight":
        verbose_to_fields = Flight.get_verbose_names_to_fields()
    else:
        raise ValueError(f"Unknown model: {model}")

    db_fields_to_data = {}

    for key in row["meta"].keys():
        if key in verbose_to_fields:
            db_field = verbose_to_fields[key]
            db_fields_to_data[db_field] = row["meta"][key]

    return db_fields_to_data


def save_aircraft(row):
    db_fields_to_data = get_db_fields_to_data(row, "Aircraft")
    aircraft = Aircraft(**db_fields_to_data)
    aircraft.save()


def save_flight(row):
    db_fields_to_data = get_db_fields_to_data(row, "Flight")

    aircraft_code_str = db_fields_to_data.get("aircraft_code")

    if aircraft_code_str:
        try:
            aircraft_instance = Aircraft.objects.get(pk=aircraft_code_str)
            db_fields_to_data["aircraft_code"] = aircraft_instance
        except Aircraft.DoesNotExist:
            print(
                f"Warning: Aircraft with code '{aircraft_code_str}' not found for flight. Skipping flight creation or handling error."
            )
            return
    else:
        print(
            "Warning: 'aircraft_code' not found in flight data. Cannot link flight to aircraft."
        )
        return

    flight = Flight(**db_fields_to_data)
    flight.save()


def save_to_db(rows):
    aircraft_rows = filter(lambda row: row["table"] == "Aircraft", rows)
    for row in aircraft_rows:
        save_aircraft(row)

    flight_rows = filter(lambda row: row["table"] == "Flight", rows)
    for row in flight_rows:
        save_flight(row)
