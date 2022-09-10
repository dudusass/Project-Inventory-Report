from inventory_report.inventory.product import Product


def test_cria_produto():
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
    assert fogao.id == product_id
    assert fogao.nome_do_produto == product_name
    assert fogao.nome_da_empresa == company_name
    assert fogao.data_de_fabricacao == manufacturing_date
    assert fogao.data_de_validade == product_valid_date
    assert fogao.numero_de_serie == product_serie
    assert fogao.instrucoes_de_armazenamento == product_instructions
