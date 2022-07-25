import re


def is_valid_id(id_to_check: str) -> bool:
    """
    :param id_to_check:
    :return:true if valid else false
    """
    digit_lst = [str(num) for num in range(10)]
    for item in id_to_check:
        if item not in digit_lst or len(id_to_check) != 9:
            print(f"{id_to_check} worng id")
            return False
    return True


def is_valid_email(mail: str):
    """
    :return: true if email is valid else return false
    """
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(regex, mail):
        return True
    print(f"{mail} worng mail")
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
        print(f"{phone_number} worng phone_number")
        return False
    return True


def percentile(N :list, P: float) -> float:
    """
    Find the percentile of a list of values

    parameter N - A list of values.  N must be sorted.
    parameter P - A float value from 0.0 to 1.0

    return - The percentile of the values.
    """
    n = int(round(P * len(N) + 0.5))
    return N[n - 1]
