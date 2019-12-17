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
        return "Customer: {0} {1} {2}".format(self.customer_id,self.first_name,self.last_name)

# defining our own exception
class BankException(Exception):
    pass

class Account:
    last_id = 0
    interest_rate = 0.02
    history = []

    def __init__(self, customer):
        Account.last_id += 1
        self.account_id = Account.last_id
        self.customer = customer
        self._balance = 0

    def deposit(self, amount):
        if amount < 0:
            print("Not a valid amount!")
        else:
            self._balance += amount
            Account.history.append(str(datetime.now()) + " Added " + str(amount))

    def charge(self, amount):
        if amount > self._balance:
            raise BankException("Not enough money")
        else:
            self._balance -= amount
            Account.history.append(str(datetime.now()) + " Withdrawal " + str(amount))

    @classmethod
    def calc_interest_value(cls, amount):
        return cls.interest_rate*amount

    def calc_interest(self):
        interest = self.calc_interest_value(self._balance)
        self._balance = self._balance + interest
        Account.history.append(str(datetime.now()) + " Interest of " + str(interest))

    def get_balance(self):
        return self._balance



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
print(s_acc.get_balance())

print(acc.history)

