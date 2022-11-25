import csv
import json
import xmltodict

from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:

    @classmethod
    def import_data(cls, path, type):
        products = []

        if path.endswith('csv'):
            products = cls.read_csv(path)
        if path.endswith('json'):
            products = cls.read_json(path)
        if path.endswith('xml'):
            products = cls.read_xml(path)

        if (type == 'simples'):
            return SimpleReport.generate(products)
            
        return CompleteReport.generate(products)


    @classmethod
    def read_csv(cls, path):
        with open(path) as csv_file:
            return list(csv.DictReader(csv_file))

    @classmethod
    def read_json(cls, path):
        with open(path) as json_file:
            return json.loads(json_file.read())

    @classmethod
    def read_xml(cls, path):
        with open(path) as xml_file:
            return xmltodict.parse(xml_file.read())["dataset"]["record"]
