from bank_account import BankAccount
from business_bank_account import BusinessBankAccount
from student_bank_account import StudentBankAccount
import convert_data as cd
import statistics


class Bank:
    list_of_accounts = []

    def load_and_parse_init_data(self):

        list_of_data = cd.convert()

        for _item in list_of_data:
            self.add_new_account(_item)

    def add_new_account(self, dict_of_pram: dict):
        """
        add new account to the bank
        :param dict_of_pram: Name: str,
                 Id: str,
                 Phone_number: str,
                 Email_address: str,
                 Balance: str
                 extra
        """
        if dict_of_pram['type'] == 'BankAccount':
            self.list_of_accounts.append(BankAccount(dict_of_pram['name'],
                                                     dict_of_pram['id'],
                                                     dict_of_pram['phone'],
                                                     dict_of_pram['email'],
                                                     dict_of_pram['balance']
                                                     ))
        if dict_of_pram['type'] == 'StudentBankAccount':
            self.list_of_accounts.append(StudentBankAccount(dict_of_pram['name'],
                                                            dict_of_pram['id'],
                                                            dict_of_pram['phone'],
                                                            dict_of_pram['email'],
                                                            dict_of_pram['balance'],
                                                            dict_of_pram['college']
                                                            ))
        if dict_of_pram['type'] == 'BusinessBankAccount':
            self.list_of_accounts.append(BusinessBankAccount(dict_of_pram['name'],
                                                             dict_of_pram['id'],
                                                             dict_of_pram['phone'],
                                                             dict_of_pram['email'],
                                                             dict_of_pram['balance']
                                                             ))

    def delete_by_userID(self, _id: str):
        """
        delet item from list by id
        :param _id:
        :return:
        """

        for item in self.list_of_accounts:
            if item.get_id() == _id:
                self.list_of_accounts.remove(item)

    def Withdraw_by_user_id(self, _id: str, money: int):
        """
        finds the client account by id and updates the balance for this client
        :param money:
        :param _id:
        :return: NON
        """
        for elem in self.list_of_accounts:
            if _id == elem.get_id():
                elem.Withdraw(money)

    def Deposit_by_user_id(self, _id: str, money: int):
        """
        finds the client account by id and updates the balance for this client
        :param money:
        :param _id:
        :return: NAN
        """
        for elem in self.list_of_accounts:
            if _id == elem.get_id():
                elem.Deposit(money)

    def __str__(self):
        string = ''
        for item in self.list_of_accounts:
            string += '\n' + item.__str__()
        return string


    def calc_balance_statistics(self) -> tuple:
        """
        this function returns the average, the median,
        90th percentile
        and 10th percentile of balances of all already added
        clients of the bank
        :return:tuple of average, median,90th percentile, 10th percentile
        """

def main():
    b = Bank()
    b.load_and_parse_init_data()

    print(f"before delete_by_userID: {len(b.list_of_accounts)} accounts")
    b.delete_by_userID('485547485')
    print(f"after delete_by_userID: {len(b.list_of_accounts)} accounts")

    # dict to test with add account
    param = {'name': "michael",
             'id': "301583275 ",
             'phone': "050-7344552",
             'email': "michael@gmail.com",
             'balance': "5000",
             'college': " sela",
             'type': "StudentBankAccount"
             }

    print(f"before add account: {len(b.list_of_accounts)} accounts")
    b.add_new_account(param)

    print(f"after add account: {len(b.list_of_accounts)} accounts")

    user_id = b.list_of_accounts[2].get_id()
    print(user_id)
    some_bank_account = b.list_of_accounts[2]
    co = b.list_of_accounts[2].commission
    print(some_bank_account.get_balance(), user_id)
    b.Withdraw_by_user_id(user_id, 100)
    print(some_bank_account.get_balance(), some_bank_account.get_id())
    b.Deposit_by_user_id(user_id, 2000)
    print(some_bank_account.get_balance(), some_bank_account.get_id())
    print(b)


if __name__ == '__main__':
    main()