class BankAccount:
    def __init__(self,account_balance=0):
        self.__account_balance =account_balance
    def deposit( self):
        amount=int(input("Enter your amount you want to deposit: "))
        self.__account_balance+= amount
        print(f"Deposited:${self.__account_balance}")
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
 python main-0.py deposit:50
 python main-0.py withdraw:20
  python main-0.py withdraw:150
 python main-0.py display
