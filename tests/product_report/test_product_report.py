from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product_id = 1
    product_name = "Fogão"
    company_name = "Casas Bahia"
    manufacturing_date = "10/09/2022"
    product_valid_date = "10/09/2032"
    product_serie = "123945029"
    product_instructions = "Não possui"

    fogao = Product(
        product_id,
        product_name,
        company_name,
        manufacturing_date,
        product_valid_date,
        product_serie,
        product_instructions,
    )
    assert fogao.__repr__() == (
        f"O produto {product_name}"
        f" fabricado em {manufacturing_date}"
        f" por {company_name} com validade"
        f" até {product_valid_date}"
        f" precisa ser armazenado {product_instructions}."
    )
