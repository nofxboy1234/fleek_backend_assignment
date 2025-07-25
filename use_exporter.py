import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

import exporter
from pilotlog.models import Aircraft

# get rows from db
# [{row}, {row}]
rows = Aircraft.objects.all()

# send rows to exporter
exporter.save_to_csv(rows)
