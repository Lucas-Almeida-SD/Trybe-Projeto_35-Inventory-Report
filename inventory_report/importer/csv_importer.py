from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(self, path):
        file_type = path.split(".")[-1]
        if file_type != "csv":
            raise ValueError("Arquivo inválido")

        product_list = CsvImporter.read_file(path)

        return product_list

    @classmethod
    def read_file(self, path):
        with open(path) as file:
            reader = csv.reader(file)
            header, *data = reader

        product_list = [dict(zip(header, row)) for row in data]

        return product_list
