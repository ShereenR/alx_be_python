class BankAccount:
    def __init__(self,account_balance=0):
        self.__account_balance =account_balance
    def deposit(self, amount):

    if amount > 0:
        amount=int(input("Enter your amount you want to deposit: "))
        self.__account_balance += amount
        print(f"Deposited: ${amount}")
    def withdraw(self):
        amount=float(input("Enter your amount you want to withdraw: "))
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew:${self.__account_balance}")
            return True
        else:
            return False
    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance}")
