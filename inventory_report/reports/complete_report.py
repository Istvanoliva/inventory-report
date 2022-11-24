from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, product_list):
        simple_report = super().generate(product_list)
        companies_products = super().count_product_per_company(product_list)

        list = "Produtos estocados por empresa:\n"
        for name, quantity in companies_products.items():
            list += f"- {name}: {quantity}\n"

        return simple_report + "\n" + list