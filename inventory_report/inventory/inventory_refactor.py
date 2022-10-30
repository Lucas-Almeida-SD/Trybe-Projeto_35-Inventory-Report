from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


REPORT = {
            "simples": SimpleReport,
            "completo": CompleteReport
        }


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path, report_type):
        self.data.extend(self.importer.import_data(path))

        return REPORT[report_type].generate(self.data)

    def __iter__(self):
        print(len(self.data))
        return InventoryIterator(self.data)
