import csv


def export_csv(contents):
    with open("tmp.csv", "w", newline="") as csvfile:
        # fieldnames = [
        #     "AircraftID",
        #     "EquipmentType",
        #     "TypeCode",
        #     "Year",
        #     "Make",
        #     "Model",
        #     "Category",
        #     "Class",
        #     "GearType",
        #     "EngineType",
        #     "Complex",
        #     "HighPerformance",
        #     "Pressurized",
        #     "TAA",
        # ]
        fieldnames = [
            "user_id",
            "table",
            "guid",
            "meta",
            "platform",
            "_modified",
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(contents)
