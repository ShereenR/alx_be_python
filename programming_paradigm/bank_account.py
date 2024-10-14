class BankAccount:
    def __init__(self, account_balance=0):
        self.__account_balance = account_balance
    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew: ${amount}")
            return True
        else:
            print("Insufficient balance.")
            return False
    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance}")
account = BankAccount()
account.deposit(67) 
account.display_balance() 
