from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.importer.json_importer import JsonImporter


def test_decorar_relatorio():
    path = 'inventory_report/data/inventory.json'
    product_list = JsonImporter.import_data(path)
    coloredReport = ColoredReport(SimpleReport)
    report = coloredReport.generate(product_list)
    splited_report = report.split('\n')

    phrases = [
        "\033[32mData de fabricação mais antiga:\033[0m ",
        "\033[32mData de validade mais próxima:\033[0m ",
        "\033[32mEmpresa com mais produtos:\033[0m ",
    ]

    value_phrases = [
        "\033[36m2020-09-06\033[0m",
        "\033[36m2023-09-17\033[0m",
        "\033[31mTarget Corporation\033[0m"
    ]

    for index, row in enumerate(splited_report):
        assert row == phrases[index] + value_phrases[index]
