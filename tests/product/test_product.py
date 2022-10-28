from inventory_report.inventory.product import Product
import pytest


@pytest.fixture
def product_mock():
    return ({
        "id": "1",
        "nome_do_produto": "Nicotine Polacrilex",
        "nome_da_empresa": "Target Corporation",
        "data_de_fabricacao": "2021-02-18",
        "data_de_validade": "2023-09-17",
        "numero_de_serie": "CR25 1551 4467 2549 4402 1",
        "instrucoes_de_armazenamento": "instrucao 1",
    })


def test_cria_produto(product_mock):
    product = Product(
        product_mock['id'],
        product_mock['nome_do_produto'],
        product_mock['nome_da_empresa'],
        product_mock['data_de_fabricacao'],
        product_mock['data_de_validade'],
        product_mock['numero_de_serie'],
        product_mock['instrucoes_de_armazenamento'],
    )

    assert hasattr(product, 'id') is True
    assert type(product.id) is str
    assert product.id == product_mock['id']

    assert hasattr(product, 'nome_do_produto') is True
    assert type(product.nome_do_produto) is str
    assert product.nome_do_produto == product_mock['nome_do_produto']

    assert hasattr(product, 'nome_da_empresa') is True
    assert type(product.nome_da_empresa) is str
    assert product.nome_da_empresa == product_mock['nome_da_empresa']

    assert hasattr(product, 'data_de_fabricacao') is True
    assert type(product.data_de_fabricacao) is str
    assert product.data_de_fabricacao == product_mock['data_de_fabricacao']

    assert hasattr(product, 'data_de_validade') is True
    assert type(product.data_de_validade) is str
    assert product.data_de_validade == product_mock['data_de_validade']

    assert hasattr(product, 'numero_de_serie') is True
    assert type(product.numero_de_serie) is str
    assert product.numero_de_serie == product_mock['numero_de_serie']

    assert hasattr(product, 'instrucoes_de_armazenamento') is True
    assert type(product.instrucoes_de_armazenamento) is str
    assert product.instrucoes_de_armazenamento == (
        product_mock['instrucoes_de_armazenamento'])
