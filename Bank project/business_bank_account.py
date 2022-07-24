from personal_Info import PersonalInfo
from bank_account import BankAccount
from business_info import BusinessInfo


class BusinessBankAccount(BankAccount):
    # 150% from commission of normal bank account
    commission = BankAccount.commission
    commission = commission * 1.5 + commission

    def __init__(self, name: str, _id: str, phone_number: str, email_address: str, balance: str = '0', \
                 bf: str = "BusinessInfo"):

        """
        init for BusinessBankAccount class
        :param Name:
        :param Id:
        :param Phone_number:
        :param Email_address:
        :param Balance:
        :param business_info:
        """
        super().__init__(name, _id, phone_number, email_address, balance)
        self._business_info = bf

        def Withdraw(self, money: int):
            """
            Withdrawal of money from the bank account
            :param money:
            :return: NAN
            """
            money = (money + money * self.commission)
            super().Withdraw(money)

        def Deposit(self, money: int):
            """
            Deposit of money in the bank account
            :param money:
            :return: NAN
            """
            money = (money - money * self.commission)
            super().Deposit(money)

def main():
    b = BusinessInfo('mmm', '1234')
    bb = BusinessBankAccount("michael", "301583175", '050-7344462', 'michael@gmail.com', '100', b)
    print(bb.get_balance())
    bb.Deposit(10000)
    print(bb.get_balance())
    bb.Withdraw(2000)
    print(bb.get_balance())
    print(bb)


if __name__ == '__main__':
    main()