class SimpleReport:
    @classmethod
    def generate(cls, products):
        oldest_fabrication = cls.get_oldest_fabrication_date(products)
        closest_expiration_date = cls.get_closest_expiration_date(products)
        company_with_most_products = cls.company_with_most_products(products)

        return (
            f"Data de fabricação mais antiga: {oldest_fabrication}\n"
            f"Data de validade mais próxima: {closest_expiration_date}\n"
            f"Empresa com mais produtos: {company_with_most_products}"
        )

    @classmethod
    def get_oldest_fabrication_date(cls, products):
        return min([item["data_de_fabricacao"] for item in products])

    @classmethod
    def get_closest_expiration_date(cls, products):
        return min([item["data_de_validade"] for item in products])

    @classmethod
    def company_with_most_products(cls, products):
        return max(
            [item["nome_da_empresa"] for item in products],
            key=[item["nome_da_empresa"] for item in products].count,
        )

    @classmethod
    def count_product_per_company(cls, products):
        companies_products = dict()
        for product in products:
            if product["nome_da_empresa"] in companies_products.keys():
                companies_products[product["nome_da_empresa"]] += 1
            else:
                companies_products[product["nome_da_empresa"]] = 1
        return companies_products
