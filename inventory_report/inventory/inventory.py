import csv

from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:

    @classmethod
    def import_data(cls, path, type):
        products = cls.read_csv(path)
        
        if (type == 'simples'):
            return SimpleReport.generate(products)
        return CompleteReport.generate(products)


    @classmethod
    def read_csv(cls, path):
        with open(path) as csv_file:
            return list(csv.DictReader(csv_file))
