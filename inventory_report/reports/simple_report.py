
class SimpleReport:
    def generate(products):
        count_company = dict()

        fabrication_date = min(
            product["data_de_fabricacao"] for product in products
            )

        expiration_date = min(
            product["data_de_validade"] for product in products
            )

        for product in products:
            if product['nome_da_empresa'] in count_company:
                count_company[product["nome_da_empresa"]] += 1
            else:
                count_company[product["nome_da_empresa"]] = 1
        max_products = max(
            count_company, key=count_company.get
            )
        return (
            f"Data de fabricação mais antiga: {fabrication_date}\n"
            f"Data de validade mais próxima: {expiration_date}\n"
            f"Empresa com mais produtos: {max_products}"
        )
