import pytest

from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


@pytest.fixture
def products():
    return [
        {
            "id": 1,
            "nome_do_produto": "Chocolate",
            "nome_da_empresa": "Sol",
            "data_de_fabricacao": "2021-07-10",
            "data_de_validade": "2024-07-10",
        }
    ]


def test_decorar_relatorio(products):
    red = "\033[31m"
    green = "\033[32m"
    blue = "\033[36m"
    color = "\033[0m"

    report = ColoredReport(SimpleReport).generate(products)

    assert f"{green}Data de fabricação mais antiga:{color}" in report
    assert f"{blue}2021-07-10{color}" in report

    assert f"{green}Data de validade mais próxima:{color}" in report
    assert f"{blue}2024-07-10{color}" in report

    assert f"{green}Empresa com mais produtos:{color}" in report
    assert f"{red}Sol{color}" in report
