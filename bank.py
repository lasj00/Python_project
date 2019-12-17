from datetime import datetime

class Customer:
    last_id = 0
    def __init__(self,first_name, last_name, email):
        Customer.last_id += 1
        self.customer_id = Customer.last_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __str__(self):
        return "Customer: {0} {1} {2}".format(self.customer_id, self.first_name, self.last_name)

# defining our own exception
class BankException(Exception):
    pass

class History:
    def __init__(self):
        self.history = []

    def add_to_history(self, operation, amount, balance):
        self.history.append(str(datetime.now()) + str(operation) + str(amount) + " Balance after transaction: " + str(balance))

    def __str__(self):
        full_history = ""
        for transaction in self.history:
            full_history += str(transaction) + "\n"
        return full_history

class Account:
    last_id = 0
    interest_rate = 0.02

    def __init__(self, customer):
        Account.last_id += 1
        self.account_id = Account.last_id
        self.customer = customer
        self._balance = 0
        self._history = History()

    def deposit(self, amount):
        if amount < 0:
            print("Not a valid amount!")
        else:
            self._balance += amount
            self._history.add_to_history(" Added ", amount, self._balance)

    def charge(self, amount):
        if amount > self._balance:
            raise BankException("Not enough money")
        else:
            self._balance -= amount
            self._history.add_to_history(" Withdrawal ", amount, self._balance)

    @classmethod
    def calc_interest_value(cls, amount):
        return cls.interest_rate*amount

    def calc_interest(self):
        interest = self.calc_interest_value(self._balance)
        self._balance = self._balance + interest
        self._history.add_to_history(" Interest ", interest, self._balance)

    def get_balance(self):
        return self._balance

    def get_history(self):
        return self._history


c = Customer('Anne', 'Smith', 'anne@smith.com')
print(c)
acc = Account(c)
acc.deposit(1000)
acc.calc_interest()
print(acc.get_balance())

try:
    acc.charge(1100)
except BankException as e:
    print(e)

print(acc.get_balance())

class SavingsAccount(Account):
    interest_rate = 0.03

class DebitAccount(Account):
    interest_rate = 0.001

s_acc = SavingsAccount(c)
s_acc.deposit(100)
s_acc.calc_interest()
s_acc.calc_interest()
print(s_acc.get_balance())

print(acc.get_history())
print(s_acc.get_history())





