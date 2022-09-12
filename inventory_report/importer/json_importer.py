import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    def import_data(path):
        if path.endswith(".json"):
            with open(path) as file:
                dict_list = json.loads(file.read())
            return dict_list
        else:
            raise ValueError("Arquivo inválido")
