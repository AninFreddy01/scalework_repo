class BankAccount:
    def __init__(self,account_holder, balance=0):
        self.account_holder = account_holder #public attribute
        self.__balance = balance #private attribute

    def get_balance(self):
        return f"Your balance is: ${self.__balance}"
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"${amount} deposited, New balance: ${self.__balance}")
        else:
            print("Invalid input")
    
    def withdraw(self, amount):
        if amount > self.__balance:
            print(f"Insufficient amount to make withdraw, your balance is ${self.__balance}")
        else:
            self.__balance -= amount
            print(f"${amount} withdrawn, New balance: ${self.__balance}")