from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1, 'Chocolate', 'Sol', '10-10-22', '10-10-23', 12345, 'em local fresco'
    )

    assert (
        str(product) == "O produto Chocolate"
        " fabricado em 10-10-22"
        " por Sol com validade"
        " até 10-10-23"
        " precisa ser armazenado em local fresco."
    )