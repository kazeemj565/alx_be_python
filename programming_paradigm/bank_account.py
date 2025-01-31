class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance


    def deposit(self, amount):
        self.account_balance += amount
        pass

    def withdraw(self, amount):
        self.account_balance -= amount

        # if amount > self.account_balance:
        #     print("Insufficient funds.")
        # else:
        #     self.account_balance -= amount
        #     # print(f"Withdrew: ${amount:.2f}")
        # pass

    def display_balance(self):
        amount = float(self.account_balance)
        print(f"Current Balance: ${amount}")
        # self.account_balance = 

