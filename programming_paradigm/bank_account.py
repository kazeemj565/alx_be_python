class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance


    def deposit(self, amount):
        self.account_balance += amount
        print(f"Deposited: ${amount}")
        pass

    def withdraw(self, amount):
        if amount > self.account_balance:
            print("Insufficient funds.")
        else:
            self.account_balance -= amount
            print(f"Withdrew: ${amount}")
        pass

    def display_balance(self):
        return self.account_balance

        

d = BankAccount()
d.deposit(100)
d.withdraw(500)
# print(d.display_balance())
balance = d.display_balance()
print(f"The Balance is ${balance}")