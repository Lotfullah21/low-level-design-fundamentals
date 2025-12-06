class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance+=amount

sbi = BankAccount(10000)
sbi.deposit(-100000)
print(sbi.balance) # -90000 which is wrong, no validation. 