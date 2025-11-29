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
        """
        Print the current balance in a stable format:
        - If balance is integer (100.0 or 100), print as "100"
        - Otherwise print the float normally (no extra formatting rules required by task)
        Output line must exactly match:
        Current Balance: $<amount>
        """
        bal = self.account_balance
        # If it's a float that is mathematically an integer, show as integer
        if isinstance(bal, float) and bal.is_integer():
            bal_str = str(int(bal))
        else:
            bal_str = str(bal)
        print(f"Current Balance: ${bal_str}")
