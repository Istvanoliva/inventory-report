import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.importer.json_importer import JsonImporter


def get_importer_type(path):
    if path.endswith("csv"):
        return CsvImporter
    if path.endswith("xml"):
        return XmlImporter
    if path.endswith("json"):
        return JsonImporter

def main():
    try:
        path, report_type = sys.argv[1:]
    except ValueError:
        print("Verifique os argumentos", file=sys.stderr)
        return

    importer = get_importer_type(path)
    inventory = InventoryRefactor(importer)

    print(inventory.import_data(path, report_type), end="")
