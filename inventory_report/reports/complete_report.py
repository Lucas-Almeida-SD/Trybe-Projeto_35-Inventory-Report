from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, dict_list):
        oldest_manufacturing_date = SimpleReport.get_oldest_manufacturing_date(
            dict_list)
        closest_expiration_date = SimpleReport.get_closest_expiration_date(
            dict_list)
        company_with_more_products = (
            SimpleReport.get_company_with_more_products(dict_list))
        companies = CompleteReport.products_stocked_by_company(dict_list)
        stock_info = ''

        for companie, qtty_product in list(companies.items()):
            stock_info += f"- {companie}: {qtty_product}\n"

        return (
            f"Data de fabricação mais antiga: {oldest_manufacturing_date}\n"
            f"Data de validade mais próxima: {closest_expiration_date}\n"
            f"Empresa com mais produtos: {company_with_more_products}\n"
            "Produtos estocados por empresa:\n"
            f"{stock_info}"
        )
