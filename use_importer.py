import importer

rows = importer.import_json("import_data.json")
importer.save_to_db(rows)
