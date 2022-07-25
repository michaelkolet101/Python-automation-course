import sys
import xml.etree.ElementTree as ET

try:
    xml_file = sys.argv[1]
except:
    xml_file = 'init.xml'

tree = ET.parse(xml_file)
root = tree.getroot()


def convert():
    ret_lst = []

    for item in root:

        dict_of_items = {}
        dict_of_items.update(item.attrib)

        for elem in item:
            for sub in elem:
                dict_of_items[sub.tag] = sub.text

        ret_lst.append(dict_of_items)

    return ret_lst


def main():
    print(convert())


if __name__ == '__main__':
    main()
