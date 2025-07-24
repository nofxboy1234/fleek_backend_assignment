from django.db import models


class Aircraft(models.Model):
    fin = (models.CharField(max_length=50),)
    sea = models.BooleanField(default=False)
    tmg = models.BooleanField(default=False)
    efis = models.BooleanField(default=False)
    fnpt = (models.IntegerField(default=0),)
    make = (models.CharField(max_length=50),)
    run2 = models.BooleanField(default=False)
    _class = (models.IntegerField(default=0),)
    model = (models.CharField(max_length=50),)
    power = (models.IntegerField(default=0),)
    seats = (models.IntegerField(default=0),)
    active = models.BooleanField(default=False)
    kg5700 = models.BooleanField(default=False)
    rating = (models.CharField(max_length=50),)
    company = (models.CharField(max_length=50),)
    _complex = models.BooleanField(default=False)
    cond_log = (models.IntegerField(default=0),)
    fav_list = models.BooleanField(default=False)
    category = (models.IntegerField(default=0),)
    high_perf = models.BooleanField(default=False)
    sub_model = (models.CharField(max_length=50),)
    aerobatic = models.BooleanField(default=False)
    ref_search = (models.CharField(max_length=50),)
    reference = (models.CharField(max_length=50),)
    tailwheel = models.BooleanField(default=False)
    default_app = (models.IntegerField(default=0),)
    default_log = (models.IntegerField(default=0),)
    default_ops = (models.IntegerField(default=0),)
    device_code = (models.IntegerField(default=0),)
    aircraft_code = (models.CharField(max_length=50),)
    default_launch = (models.IntegerField(default=0),)
    record_modified = (models.IntegerField(default=0),)


class Flight(models.Model):
    pass
