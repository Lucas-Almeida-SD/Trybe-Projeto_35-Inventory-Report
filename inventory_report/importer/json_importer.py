from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(self, path):
        file_type = path.split(".")[-1]
        if file_type != "json":
            raise ValueError("Arquivo inválido")

        product_list = JsonImporter.read_file(path)

        return product_list

    @classmethod
    def read_file(self, path):
        with open(path) as file:
            product_list = json.load(file)

        return product_list
