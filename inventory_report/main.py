import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter

IMPORTER = {
    'csv': CsvImporter,
    'json': JsonImporter,
    'xml': XmlImporter,
}


def main():
    if len(sys.argv) < 3:
        sys.stderr.write('Verifique os argumentos\n')
    else:
        _, path, report_type = sys.argv
        file_type = path.split('.')[-1]
        invetory = InventoryRefactor(IMPORTER[file_type])
        print(invetory.import_data(path, report_type), end='')
