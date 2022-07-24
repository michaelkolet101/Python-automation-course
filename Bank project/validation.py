import re


def is_valid_id(id_to_check: str) -> bool:
    """
    :param id_to_check:
    :return:true if valid else false
    """
    digit_lst = [str(num) for num in range(10)]
    for item in id_to_check:
        if item not in digit_lst or len(id_to_check) != 9:
            return False
    return True


def is_valid_email(mail: str):
    """
    :return: true if email is valid else return false
    """
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(regex, mail):
        return True
    return False


def is_valid_phone_number(phone_number: str) -> bool:
    """
    :param phone_number:
    :return:true if valid else false
    """
    digit_lst = [str(num) for num in range(10)]

    if len(phone_number) > 11:
        return False

    lst = []
    for item in phone_number:
        if item in digit_lst:
            lst.append(item)

    if len(lst) != 10:
        return False
    return True
