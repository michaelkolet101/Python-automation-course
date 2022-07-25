from personal_Info import PersonalInfo


class BankAccount(PersonalInfo):
    # 1% from the deal
    commission = 0.01

    def __init__(self, name: str, _id: str, phone_number: str, email_address: str, balance: str='0'):
        """
        init to BankAccount class
        :param name:
        :param _id:
        :param phone_number:
        :param email_address:
        :param balance:
        """
        super().__init__(name, _id, phone_number, email_address)
        self._balance = int(balance)

    def get_id(self):
        """
        :return: id of person
        """
        return self._id

    def get_balance(self):
        """
        :return:the balance of the account
        """
        return self._balance

    def set_balance(self, money: int = 0):
        """
        add balance with money
        :return NON:
        """
        self._balance += money

    def Withdraw(self, money: int):
        """
        Withdrawal of money from the bank account
        :param money:
        :return: NAN
        """
        money = (money + money * self.commission)
        self.set_balance(-money)

    def Deposit(self, money: int):
        """
        Deposit of money in the bank account
        :param money:
        :return: NAN
        """
        money = (money - money * self.commission)
        self.set_balance(money)

    def __str__(self):
        return f"""BankAccount:
            Name: {self._name} 
            Id: {self._id} 
            Phone_number: {self._phone_number}
            Email_address: {self._email_address} 
            Balance: {self._balance}  
            commission: {self.commission}"""

#test for band account
def main():
    account = BankAccount("michael", "301583275", "050-7344552", "michael@gmail.com", "5000")

    print(account.get_id())
    print(account.get_balance())
    account.Withdraw(1000)
    print(account.get_balance())
    account.Deposit(1000)
    print(account.get_balance())
    print(account)


if __name__ == '__main__':
    main()