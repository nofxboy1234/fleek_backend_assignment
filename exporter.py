import csv

from django.forms.models import model_to_dict

from pilotlog.models import Aircraft


def get_rows_with_verbose_fields(model_instances):
    fields_to_verbose = Aircraft.get_fields_to_verbose_names()

    rows_with_verbose_fields = []

    for model_instance in model_instances:
        print(model_instance)
        verbose_fields_to_data = {}
        model_instance_dict = model_to_dict(model_instance)

        for key in model_instance_dict.keys():
            verbose_key = fields_to_verbose[key]
            verbose_fields_to_data[verbose_key] = model_instance_dict[key]

        rows_with_verbose_fields.append(verbose_fields_to_data)

    return rows_with_verbose_fields


def export_csv(rows):
    with open("export_data.csv", "w", newline="") as csvfile:
        aircraft_fieldnames = Aircraft.get_verbose_names_to_fields().keys()
        writer = csv.DictWriter(csvfile, fieldnames=aircraft_fieldnames)

        writer.writeheader()
        writer.writerows(rows)


def save_to_csv(rows):
    verbose_rows = get_rows_with_verbose_fields(rows)
    export_csv(verbose_rows)
