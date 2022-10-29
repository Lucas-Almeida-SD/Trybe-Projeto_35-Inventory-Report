from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(self, dict_list):
        oldest_manufacturing_date = SimpleReport.get_oldest_manufacturing_date(
            dict_list)
        closest_expiration_date = SimpleReport.get_closest_expiration_date(
            dict_list)
        company_with_more_products = (
            SimpleReport.get_company_with_more_products(dict_list))

        return (
            f"Data de fabricação mais antiga: {oldest_manufacturing_date}\n"
            f"Data de validade mais próxima: {closest_expiration_date}\n"
            f"Empresa com mais produtos: {company_with_more_products}"
        )

    @classmethod
    def get_oldest_manufacturing_date(self, product_list):
        manufacturing_date_in_seconds_list = [
            SimpleReport.convert_date_to_seconds(
                product["data_de_fabricacao"])
            for product in product_list
        ]

        oldest_date_in_seconds = min(manufacturing_date_in_seconds_list)

        return SimpleReport.convert_seconds_to_date(oldest_date_in_seconds)

    @classmethod
    def is_closest_expiration_date(self, seconds, closest_expiration_date):
        diff_now = seconds - datetime.now().timestamp()
        return (
            seconds < closest_expiration_date and
            diff_now > 0
        )

    @classmethod
    def get_closest_expiration_date(self, product_list):
        expiration_date_in_seconds_list = [
            SimpleReport.convert_date_to_seconds(
                product["data_de_validade"]
            )
            for product in product_list
        ]

        closest_expiration_date = max(expiration_date_in_seconds_list)
        for seconds in expiration_date_in_seconds_list:
            if SimpleReport.is_closest_expiration_date(
                seconds, closest_expiration_date
            ):
                closest_expiration_date = seconds

        return SimpleReport.convert_seconds_to_date(closest_expiration_date)

    @classmethod
    def products_stocked_by_company(self, product_list):
        stock_by_company = dict()

        for product in product_list:
            if product['nome_da_empresa'] in stock_by_company:
                stock_by_company[product['nome_da_empresa']] += 1
            else:
                stock_by_company[product['nome_da_empresa']] = 1

        return stock_by_company

    @classmethod
    def get_company_with_more_products(self, product_list):
        companies = SimpleReport.products_stocked_by_company(product_list)

        companies_items = list(companies.items())
        companies_values = list(companies.values())
        index = companies_values.index(max(companies_values))
        return companies_items[index][0]

    @classmethod
    def convert_date_to_seconds(self, date):
        seconds = datetime.fromisoformat(date).timestamp()

        return seconds

    @classmethod
    def convert_seconds_to_date(self, seconds):
        date = datetime.fromtimestamp(seconds).strftime("%Y-%m-%d")

        return date
