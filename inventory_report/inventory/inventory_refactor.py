from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class InventoryRefactor(Importer):
    def __init__(self, importer: Importer):
        self.importer = importer
        self.data = list()

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, path, report_type):
        self.data.extend(self.importer.import_data(path))

        if report_type == "simples":
            return SimpleReport.generate(self.data)

        return CompleteReport.generate(self.data)