from inventory_report.inventory.product import Product
import pytest


@pytest.fixture
def product_mock():
    return {
        "id": "1",
        "nome_do_produto": "Nicotine Polacrilex",
        "nome_da_empresa": "Target Corporation",
        "data_de_fabricacao": "2021-02-18",
        "data_de_validade": "2023-09-17",
        "numero_de_serie": "CR25 1551 4467 2549 4402 1",
        "instrucoes_de_armazenamento": "instrucao 1",
    }


def test_relatorio_produto(product_mock):
    product = Product(
        product_mock["id"],
        product_mock["nome_do_produto"],
        product_mock["nome_da_empresa"],
        product_mock["data_de_fabricacao"],
        product_mock["data_de_validade"],
        product_mock["numero_de_serie"],
        product_mock["instrucoes_de_armazenamento"],
    )

    expected = (
        "O produto {}".format(product_mock['nome_do_produto']) +
        " fabricado em {}".format(product_mock['data_de_fabricacao']) +
        " por {} com validade".format(product_mock['nome_da_empresa']) +
        " até {}".format(product_mock['data_de_validade']) +
        " precisa ser armazenado {}.".format(
            product_mock["instrucoes_de_armazenamento"]
        )
    )

    assert repr(product) == expected
