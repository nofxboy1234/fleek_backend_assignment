import csv


def export_csv(rows):
    fieldname_map = {
        "aircraft_code": "AircraftID",
        "company": "EquipmentType",
        "fin": "TypeCode",
        "_": "Year",
        "make": "Make",
        "_model": "Model",
        "category": "Category",
        "_class": "Class",
        "ref_search": "GearType",
        "reference": "EngineType",
        "_complex": "Complex",
        "high_perf": "HighPerformance",
        "aerobatic": "Pressurized",
        "active": "TAA",
    }
    filtered_rows = filter(lambda row: row in fieldname_map.keys(), rows)

    with open("tmp.csv", "w", newline="") as csvfile:
        aircraft_fieldnames = [
            "AircraftID",
            "EquipmentType",
            "TypeCode",
            "Year",
            "Make",
            "Model",
            "Category",
            "Class",
            "GearType",
            "EngineType",
            "Complex",
            "HighPerformance",
            "Pressurized",
            "TAA",
        ]
        writer = csv.DictWriter(csvfile, fieldnames=aircraft_fieldnames)

        writer.writeheader()
        writer.writerows(rows)
