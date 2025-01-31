class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance


    def deposit(self, amount):
        self.account_balance += amount
        pass

    def withdraw(self, amount):
        # self.account_balance -= amount
        if amount <= self.account_balance:
            self.account_balance -= amount
            return self.account_balance
        else:
            return  None 
        # if amount > self.account_balance:
        #     return self.account_balance
        # else:
        #     self.account_balance -= amount
        #     # print(f"Withdrew: ${amount:.2f}")
        # pass

    def display_balance(self):
        amount = float(self.account_balance)
        print(f"Current Balance: ${amount:.2f}")
        # self.account_balance = 

