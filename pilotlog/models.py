from django.db import models


class Aircraft(models.Model):
    fin = models.CharField("Fin", max_length=50)
    sea = models.BooleanField("Sea", default=False)
    tmg = models.BooleanField("TMG", default=False)
    efis = models.BooleanField("Efis", default=False)
    fnpt = models.IntegerField("FNPT", default=0)
    make = models.CharField("Make", max_length=50)
    run2 = models.BooleanField("Run2", default=False)
    _class = models.IntegerField("Class", default=0)
    model = models.CharField("Model", max_length=50)
    power = models.IntegerField("Power", default=0)
    seats = models.IntegerField("Seats", default=0)
    active = models.BooleanField("Active", default=False)
    kg5700 = models.BooleanField("Kg5700", default=False)
    rating = models.CharField("Rating", max_length=50)
    company = models.CharField("Company", max_length=50)
    _complex = models.BooleanField("Complex", default=False)
    cond_log = models.IntegerField("CondLog", default=0)
    fav_list = models.BooleanField("FavList", default=False)
    category = models.IntegerField("Category", default=0)
    high_perf = models.BooleanField("HighPerf", default=False)
    sub_model = models.CharField("SubModel", max_length=50)
    aerobatic = models.BooleanField("Aerobatic", default=False)
    ref_search = models.CharField("RefSearch", max_length=50)
    reference = models.CharField("Reference", max_length=50)
    tailwheel = models.BooleanField("Tailwheel", default=False)
    default_app = models.IntegerField("DefaultApp", default=0)
    default_log = models.IntegerField("DefaultLog", default=0)
    default_ops = models.IntegerField("DefaultOps", default=0)
    device_code = models.IntegerField("DeviceCode", default=0)
    aircraft_code = models.CharField("AircraftCode", max_length=50)
    default_launch = models.IntegerField("DefaultLaunch", default=0)
    record_modified = models.IntegerField("Record_Modified", default=0)

    @classmethod
    def get_verbose_names_to_fields(cls):
        verbose_name_fields = {}
        for verbose_name, field_name in map(
            lambda field: [field.verbose_name, field.name], cls._meta.fields
        ):
            verbose_name_fields[verbose_name] = str(field_name)

        return verbose_name_fields

    @classmethod
    def get_fields_to_verbose_names(cls):
        field_verbose_names = {}
        for field in cls._meta.fields:
            field_verbose_names[field.name] = str(field.verbose_name)

        return field_verbose_names


class Flight(models.Model):
    pass
