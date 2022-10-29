from abc import ABC
import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

REPORT = {"simples": SimpleReport, "completo": CompleteReport}


class Inventory(ABC):
    @classmethod
    def import_data(self, path, report_type):
        product_list = Inventory.read_file(path)

        return REPORT[report_type].generate(product_list)

    @classmethod
    def read_csv_file(self, path):
        with open(path) as file:
            reader = csv.reader(file)
            header, *data = reader

        product_list = [dict(zip(header, row)) for row in data]

        return product_list

    @classmethod
    def read_json_file(self, path):
        with open(path) as file:
            product_list = json.load(file)

        return product_list

    @classmethod
    def read_file(self, path):
        file_type = path.split(".")[-1]

        readers = {
            "csv": Inventory.read_csv_file,
            "json": Inventory.read_json_file,
        }

        return readers[file_type](path)
