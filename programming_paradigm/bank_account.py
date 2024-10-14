class BankAccount:
    def __init__(self, account_balance=0):
        self.__account_balance = account_balance
    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited: ${amount}"
    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
             return f"Withdrew: ${amount}"
            return True
        else:
            return False
    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance}")
