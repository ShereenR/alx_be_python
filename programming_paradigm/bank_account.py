class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance
    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited: ${amount}")
    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True  
        else:
            return False 
    def display_balance(self):
        print(f"Current balance: ${self.__account_balance}")
account = BankAccount()  
account.deposit(67)  
