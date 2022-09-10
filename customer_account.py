class CustomerAccount:
    pass

    def __init__(self, balance=0.0):
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def check_balance(self):
        return self.balance
