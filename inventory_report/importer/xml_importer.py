from inventory_report.importer.importer import Importer
from xml.etree import ElementTree


class XmlImporter(Importer):
    def import_data(path):
        if path.endswith(".xml"):
            tree = ElementTree.parse(path)
            root = list(tree.getroot())

            dict_list = []
            info_dict = {}

            for index in range(len(root)):

                for info in root[index]:
                    info_dict[info.tag] = info.text

                dict_list.append(info_dict)
                info_dict = {}

            return dict_list
        else:
            raise ValueError("Arquivo inválido")
