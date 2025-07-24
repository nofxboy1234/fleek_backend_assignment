import csv


def export_csv(contents):
    with open("tmp.csv", "w", newline="") as csvfile:
        # aircraft_id = models.CharField(max_length=50)
        # equipment_type = models.CharField(max_length=50)
        # type_code = models.CharField(max_length=50)
        # year = models.CharField(max_length=50)
        # make = models.CharField(max_length=50)
        # model = models.CharField(max_length=50)
        # category = models.CharField(max_length=50)
        # _class = models.CharField(max_length=50)
        # gear_type = models.CharField(max_length=50)
        # engine_type = models.CharField(max_length=50)
        # _complex = models.CharField(max_length=50)
        # high_performance = models.CharField(max_length=50)
        # pressurized = models.CharField(max_length=50)
        # taa = models.CharField(max_length=50)

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
