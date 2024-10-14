class BankAccount:
    def __init__(self, account_balance=0):
        self.__account_balance = account_balance
    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited: ${amount}"
    def withdraw(self, amount):
        if amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return f"Withdrew: ${amount}"
            return True
    def display_balance(self):
         return f"Current Balance: ${self.__account_balance}"
