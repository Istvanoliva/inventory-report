from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1, 'Chocolate', 'Sol', '10/10/22', '10/10/23', 12345, 'em local fresco'
    )

    assert product.id == 1
    assert product.nome_do_produto == 'Chocolate'
    assert product.nome_da_empresa == 'Sol'
    assert product.data_de_fabricacao == '10/10/22'
    assert product.data_de_validade == '10/10/23'
    assert product.numero_de_serie == 12345
    assert product.instrucoes_de_armazenamento == 'em local fresco'
