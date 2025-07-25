import csv

from pilotlog.models import Aircraft, Flight


def export_csv(rows):
    with open("export_data.csv", "w", newline="") as csvfile:
        aircraft_fieldnames = rows[0]
        writer = csv.DictWriter(csvfile, fieldnames=aircraft_fieldnames)

        writer.writeheader()
        writer.writerows(rows)
