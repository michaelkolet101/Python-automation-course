from validation import *


class PersonalInfo:

    def __init__(self, name, _id, phone_number, email_address):
        """
        init method to the PersonalInfo class
        :param Name: name of person
        :param Id: id of person
        :param Phone_number: phone
        :param Email_address: mail
        """
      #  if is_valid_email(email_address) and is_valid_id(_id) and \
          #      is_valid_phone_number(phone_number):

        self._name = name
        self._id = _id
        self._phone_number = phone_number
        self._email_address = email_address


def main():
    user = PersonalInfo('michael', '301583174', '0507344462', 'michael@gmail.com')

    is_valid_phone_number('050-7344452')


if __name__ == '__main__':
    main()
