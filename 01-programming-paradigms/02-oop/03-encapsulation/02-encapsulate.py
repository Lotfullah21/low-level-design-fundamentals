class BankAccount:
    def __init__(self, balance):
        # private attribute
        self.__balance = balance

    def deposit(self, amount):
        if amount<0:
            raise ValueError("Amount cannot be negative")
        self.__balance+=amount
    
    def withdraw(self, amount):
        if self.__balance<amount:
            raise ValueError("Not enough money in the bank.")
        self.__balance-=amount
    
    def get_balance(self):
        return self.__balance

sbi = BankAccount(10000)
sbi.deposit(2000)
# print(sbi.__balance) # Cannot access it directly
print("Balance =",sbi.get_balance())

# Benefits: Data is protected, all modifications go through validation.
