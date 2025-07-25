import json

from pilotlog.models import Aircraft, Flight


def import_json(json_file):
    with open(json_file, "r") as file:
        rows = json.load(file)

    return rows


def get_db_fields_to_data(row, model):
    if model == "Aircraft":
        verbose_to_fields = Aircraft.get_verbose_names_to_fields()
    elif model == "Flight":  # Use elif here for clarity and efficiency
        verbose_to_fields = Flight.get_verbose_names_to_fields()
    else:
        # Handle cases where model is neither Aircraft nor Flight if necessary
        raise ValueError(f"Unknown model: {model}")

    db_fields_to_data = {}

    # print(row) # Keep this for debugging if needed, otherwise remove
    for key in row["meta"].keys():
        # Ensure the key exists in verbose_to_fields to avoid KeyError
        if key in verbose_to_fields:
            db_field = verbose_to_fields[key]
            db_fields_to_data[db_field] = row["meta"][key]
        # else:
        # print(f"Warning: Verbose name '{key}' not found for {model} model.")

    return db_fields_to_data


def save_aircraft(row):
    db_fields_to_data = get_db_fields_to_data(row, "Aircraft")
    # You might want to handle potential duplicates here if 'aircraft_code' is primary_key
    # For example: Aircraft.objects.update_or_create(primary_key_field=value, defaults={...})
    aircraft = Aircraft(**db_fields_to_data)
    aircraft.save()


def save_flight(row):
    db_fields_to_data = get_db_fields_to_data(row, "Flight")

    # --- THE FIX STARTS HERE ---
    # Get the aircraft_code string from the data
    aircraft_code_str = db_fields_to_data.get("aircraft_code")  # Use .get() for safety

    if aircraft_code_str:
        try:
            # Retrieve the actual Aircraft instance
            aircraft_instance = Aircraft.objects.get(pk=aircraft_code_str)
            # Replace the string primary key with the actual Aircraft instance
            db_fields_to_data["aircraft_code"] = aircraft_instance
        except Aircraft.DoesNotExist:
            print(
                f"Warning: Aircraft with code '{aircraft_code_str}' not found for flight. Skipping flight creation or handling error."
            )
            # Depending on your requirements, you might want to:
            # 1. Skip this flight
            # 2. Log the error and continue
            # 3. Raise an exception to stop the import
            return  # Skip the flight if aircraft doesn't exist
    else:
        print(
            "Warning: 'aircraft_code' not found in flight data. Cannot link flight to aircraft."
        )
        return  # Skip if no aircraft code is provided
    # --- THE FIX ENDS HERE ---

    # Handle the default for flight_code which is a primary_key
    # If the JSON might not provide a unique flight_code, let Django generate it
    # or ensure it's unique if provided.
    # If flight_code is a primary_key and you always get a default from the model,
    # you might remove it from db_fields_to_data if it's not present in your JSON,
    # or ensure your JSON provides a unique one.
    # For now, assuming your JSON provides a valid, unique flight_code.

    flight = Flight(**db_fields_to_data)
    flight.save()


def save_to_db(rows):
    # Process Aircraft first to ensure they exist for flights
    aircraft_rows = filter(lambda row: row["table"] == "Aircraft", rows)
    for row in aircraft_rows:
        save_aircraft(row)

    # Now process flights
    flight_rows = filter(lambda row: row["table"] == "Flight", rows)
    for row in flight_rows:
        save_flight(row)
