import csv
import json

with open("tmp.json", "r") as file:
    contents = json.load(file)

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

# print(contents)
# print(len(contents))
# print(type(contents))
# print(type(contents[0]))
