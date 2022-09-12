import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    def import_data(path):
        if path.endswith(".csv"):
            with open(path) as file:
                dict_list = list(csv.DictReader(file))
            return dict_list
        else:
            raise ValueError("Arquivo inválido")
