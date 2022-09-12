import sys
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter

from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main():
    if len(sys.argv) < 3:
        return sys.stderr.write('Verifique os argumentos\n')

    if sys.argv[1].endswith(".csv"):
        inventory_refactor = InventoryRefactor(CsvImporter)
        report = inventory_refactor.import_data(sys.argv[1], sys.argv[2])
        print(report, end="")
    elif sys.argv[1].endswith(".json"):
        inventory_refactor = InventoryRefactor(JsonImporter)
        report = inventory_refactor.import_data(sys.argv[1], sys.argv[2])
        print(report, end="")
    elif sys.argv[1].endswith(".xml"):
        inventory_refactor = InventoryRefactor(XmlImporter)
        report = inventory_refactor.import_data(sys.argv[1], sys.argv[2])
        print(report, end="")
    else:
        raise ValueError("Arquivo inválido")
