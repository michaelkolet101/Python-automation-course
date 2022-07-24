# from student_bank_account import StudentBankAccount
import xml.etree.ElementTree as ET
# import bank

tree = ET.parse('data.xml')
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