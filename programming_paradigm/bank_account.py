class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance


    def deposit(self, amount):
        self.account_balance += amount
    

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return self.account_balance
        else:
            return  None 
        
    def display_balance(self):
        amount = float(self.account_balance)
        print(f"Current Balance: ${amount:.2f}")
         

