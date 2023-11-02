class AccountDB:
    def __init__(self):
        self.account_database = []

    def insert(self, account):
        index = self.__search_private(account.account_number)
        if index == -1:
            self.account_database.append(account)
        else:
            print(account, "Duplicated account; nothing to be insert")

    def delete_account(self, num):
        index = self.__search_private(num)
        if index != -1:
            delete_acc = self.account_database.pop(index)
            print("Deleting account:", delete_acc.account_number)
        else:
            print(num, "invalid account number; nothing to be deleted.")

    def __search_private(self, account_num):  # search each account in private attribute
        for i, account in enumerate(self.account_database):
            if self.account_database[i].account_number == account_num:
                return i
        return -1

    def search_public(self, account_num):  # search each account in public attribute
        for account in self.account_database:
            if account.account_number == account_num:
                return account
        return None

    def __str__(self):
        s = ''
        for account in self.account_database:
            s += str(account) + ", "
        return s

    def deposit_to_account(self, account_num, amount):
        account = self.search_public(account_num)
        if account:
            account.deposit(amount)
            print("Deposited", amount, "to account:", account_num)
        else:
            print(account_num, "invalid account number; nothing to be deposited.")


class Account:
    def __init__(self, num, type, account_name, balance):
        self.account_number = num
        self.type = type
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):  # add value to the amount
        self.balance += amount

    def withdraw(self, amount):  # increase value to the amount
        if self.balance >= amount:
            self.balance -= amount

    def __str__(self):
        return '{' + str(self.account_number) + ',' + str(self.type) + ',' + str(self.account_name) + ',' + str(
            self.balance) + '}'


# Create accounts and account DB
account1 = Account("0000", "saving", "David Patterson", 1000)
account2 = Account("0001", "checking", "John Hennessy", 2000)
account3 = Account("0003", "saving", "Mark Hill", 3000)
account4 = Account("0004", "saving", "David Wood", 4000)
account5 = Account("0005", "saving", "Alice Johnson", 5000)

my_account_DB = AccountDB()

# Insert accounts
my_account_DB.insert(account1)
my_account_DB.insert(account2)
my_account_DB.insert(account3)
my_account_DB.insert(account4)
my_account_DB.insert(account5)
print(my_account_DB)

# Deposit to account
my_account_DB.deposit_to_account("0010", 50)
print(my_account_DB)

# Delete an account
my_account_DB.delete_account("0003")
print(my_account_DB)
