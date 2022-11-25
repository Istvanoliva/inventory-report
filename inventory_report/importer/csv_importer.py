from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith("csv"):
            raise ValueError("Arquivo inválido")

        with open(path) as file:
            return list(csv.DictReader(file))
