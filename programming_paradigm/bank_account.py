class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        bal = self.account_balance
        if isinstance(bal, float) and bal.is_integer():
            bal_str = str(int(bal))
        else:
            bal_str = str(bal)
        print(f"Current Balance: ${bal_str}")
