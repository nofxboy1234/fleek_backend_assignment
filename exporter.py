import csv

from django.forms.models import model_to_dict

from pilotlog.models import Aircraft, Flight


def get_tables_with_rows_with_verbose_fields(tables):
    tables_with_rows_with_verbose_fields = {}

    for table in tables:
        if table == "Aircraft":
            fields_to_verbose = Aircraft.get_fields_to_verbose_names()
        elif table == "Flight":
            fields_to_verbose = Flight.get_fields_to_verbose_names()
        else:
            raise ValueError(f"Unknown table: {table}")

        rows_with_verbose_fields = []
        rows = tables[table]

        for row in rows:
            verbose_fields_to_data = {}
            model_instance_dict = model_to_dict(row)

            for key in model_instance_dict.keys():
                verbose_key = fields_to_verbose[key]
                verbose_fields_to_data[verbose_key] = model_instance_dict[key]

            rows_with_verbose_fields.append(verbose_fields_to_data)

        tables_with_rows_with_verbose_fields[table] = rows_with_verbose_fields

    return tables_with_rows_with_verbose_fields


def export_csv(tables):
    with open("export_data.csv", "w", newline="") as csvfile:
        for table in tables:
            if table == "Aircraft":
                fieldnames = Aircraft.get_verbose_names_to_fields().keys()
            elif table == "Flight":
                fieldnames = Flight.get_verbose_names_to_fields().keys()
            else:
                raise ValueError(f"Unknown table: {table}")

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            rows = tables[table]
            writer.writerows(rows)


def save_to_csv(tables):
    tables_with_rows_with_verbose_fields = get_tables_with_rows_with_verbose_fields(
        tables
    )
    export_csv(tables_with_rows_with_verbose_fields)
