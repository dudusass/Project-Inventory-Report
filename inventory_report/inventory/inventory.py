import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def read_csv(path):
        with open(path) as file:
            dict_list = csv.DictReader(file)
            return list(dict_list)

    @classmethod
    def import_data(cls, path, type):
        data = Inventory.read_csv(path)
        if type == "simples":
            return SimpleReport.generate(data)
        elif type == "completo":
            return CompleteReport.generate(data)
