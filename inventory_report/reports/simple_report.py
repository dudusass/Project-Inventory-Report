
class SimpleReport:
    def generate(products):
        fabrication_date = min(
            product["data_de_fabricacao"] for product in products
            )

        expiration_date = min(
            product["data_de_validade"] for product in products
            )
        return (
            f"Data de fabricação mais antiga: {fabrication_date}\n"
            f"Data de validade mais próxima: {expiration_date}\n"
            f"Empresa com mais produtos: {SimpleReport.gen_products(products)}"
        )

    def generate_dict(products):
        count_company = dict()
        for product in products:
            if product['nome_da_empresa'] in count_company:
                count_company[product["nome_da_empresa"]] += 1
            else:
                count_company[product["nome_da_empresa"]] = 1
        return count_company

    def gen_products(products):
        count_company = SimpleReport.generate_dict(products)
        max_products = max(
            count_company, key=count_company.get
            )
        return max_products
        # max_products = max(count_company, key=lambda key:count_company[key])
