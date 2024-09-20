class BankAccount:
    def init(self, name, balance=0):
        self.balance = balance
        self.name = name


    def deposit(self, cash_amount):
        self.balance += cash_amount


    def cash(self, cash_amount):
        self.balance -= cash_amount


    def my_balance(self):
        return self.balance