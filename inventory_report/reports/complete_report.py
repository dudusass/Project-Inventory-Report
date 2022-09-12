from simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(products):
        simple_report = SimpleReport.generate(products)

        dict_report = SimpleReport.create_dict(products)

        dict_string = CompleteReport.format_dict(dict_report)

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{dict_string}"
        )

    def format_dict(products):
        string = str()
        for key, value in products.items():
            string += f"- {key}: {value}\n"
        return string
