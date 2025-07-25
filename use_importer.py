import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

import importer

rows = importer.import_json("import_data.json")
importer.save_to_db(rows)
