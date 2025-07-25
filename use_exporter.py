import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

import exporter
from pilotlog.models import Aircraft, Flight

# [{}, {}]
# [{}, {}]
# {"Aircraft": [{}, {}], "Flight": [{}, {}]}

tables = {}

tables["Aircraft"] = Aircraft.objects.all()
tables["Flight"] = Flight.objects.all()

exporter.save_to_csv(tables)
