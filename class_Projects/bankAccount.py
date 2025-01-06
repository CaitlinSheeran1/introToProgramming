class BankAccount:
    #class variable
    interest_rate = 0.02

    def __init__(self, name, balance - 0):
        self._owner = name
        self._balance = balance

# Accessor methods
    def get_owner(self):
        return self._owner
    
    def check_balance(self):
        return self._balance
    
    def get_interest_rate(self):
        return self.interest_rate

#Mutator methods:
    def change_name(self, new_name):
        self._owner = new_name

    def make_deposit(self, amount):
        self._balance += amount

    def make_withdraw(self, amount):
        if amount > self._balance:
            print(f'insufficant funds')

    def add_account(self, an_account):
        self._account.append(an_account)

    def give_interest(self):
        for account in self.accounts:
            account.set_balance() = account.get_balance() + 10


account1 = BankAccount('matt')
account2 = BankAccount('ashley', 250)

wells_fargo = Bank('Wells Fargo')
wells_fargo.add_account(account)

account1.make_deposit(500)