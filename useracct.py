class User:
    def __init__(self, name, email):
        self.name = name 
        self.email =  email 
        self.account = 100000

    def make_deposit(self, amount):
        self.account += amount
        return self

    def make_withdrawal(self, amount):
        self.account -= amount
        return self
    
    def display_user_balance(self):
        self.name, self.account
        return self

class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        self.int_rate = 0.01

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        self.int_rate
        return self

checking = BankAccount(0.01, 5000 )
saving = BankAccount(0.08, 25000 )

prince = User("prince", "piwejuo@gmail.com")
collins = User("collins", "cebozue@gmail.com")
arinze = User("arinze", "aobiora@gmail.com")

collins.account = 10000
arinze.account = 7000

prince.make_deposit(10000).make_deposit(1000).make_deposit(500)
print(prince.account)

prince.make_withdrawal(11500).display_user_balance()
print(prince.account)
print(prince.name, prince.account)

collins.make_deposit(500).make_deposit(500).make_withdrawal(1000).make_withdrawal(500).display_user_balance()
print(collins.name, collins.account)

arinze.make_deposit(4000).make_withdrawal(1000).make_withdrawal(500).make_withdrawal(2000).display_user_balance()
print(arinze.name, arinze.account)