from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(self, path):
        file_type = path.split(".")[-1]
        if file_type != "xml":
            raise ValueError("Arquivo inválido")

        product_list = XmlImporter.read_file(path)

        return product_list

    @classmethod
    def read_file(self, path):
        with open(path) as file:
            product_list = xmltodict.parse(file.read())['dataset']['record']

        return product_list
