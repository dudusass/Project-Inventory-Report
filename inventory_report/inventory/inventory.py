import csv
import json
from xml.etree import ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def read(path):
        if path.endswith(".csv"):
            with open(path) as file:
                dict_list = csv.DictReader(file)
                return list(dict_list)

        elif path.endswith(".json"):
            with open(path) as file:
                dict_list = json.loads(file.read())
            return dict_list

        elif path.endswith(".xml"):
            if path.endswith(".xml"):
                with open(path) as file:
                    tree = ET.parse(file)
                    root = tree.getroot()
                return list(
                    {item.tag: item.text for item in row} for row in root
                    )
        return list()

    @classmethod
    def import_data(cls, path, type):
        data = Inventory.read(path)
        if type == "simples":
            return SimpleReport.generate(data)
        elif type == "completo":
            return CompleteReport.generate(data)
