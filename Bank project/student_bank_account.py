from personal_Info import PersonalInfo
from bank_account import BankAccount


class StudentBankAccount(BankAccount):

    def __init__(self, name: str, _id: str, phone_number: str, email_address: str, balance: str = "0",
                 college_name: str = ""):

        super().__init__(name, _id, phone_number, email_address, balance)
        self.college_name = college_name

    def __str__(self):
        return f"""{super().__str__()} 
            college_name :{self.college_name}"""

    def Withdraw(self, money: int):
        """
        Withdrawal of money from the bank account
        :param money:
        :return: NAN
        """

        if money >= (self._balance - self.commission):
            self._balance = 0
        else:
            super().Withdraw(money)


def main():
    b = StudentBankAccount("michael", "301583175", '0507344462', 'michael@gmail.com', '100', 'sela')
    print(b.get_id())
    print(b.get_balance())
    print(b.commission)
    b.Withdraw(50)
    print(b.get_balance())
    b.Deposit(2000)
    print(b.get_balance())
    print(b)


if __name__ == '__main__':
    main()