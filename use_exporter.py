import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

import exporter
from pilotlog.models import Aircraft, Flight

rows = Aircraft.objects.all()
exporter.save_to_csv(rows, "Aircraft")

rows = Flight.objects.all()
exporter.save_to_csv(rows, "Flight")
