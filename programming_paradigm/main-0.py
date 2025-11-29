import sys
from bank_account import BankAccount
import os

BALANCE_FILE = "balance.txt"


def load_balance():
    if not os.path.exists(BALANCE_FILE):
        return 100   # default initial balance for task
    with open(BALANCE_FILE, "r") as f:
        return float(f.read().strip())


def save_balance(balance):
    with open(BALANCE_FILE, "w") as f:
        f.write(str(balance))


def main():
    balance = load_balance()
    account = BankAccount(balance)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        save_balance(account.account_balance)
        print(f"Deposited: ${amount}")

    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            save_balance(account.account_balance)
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")

    elif command == "display":
        account.display_balance()

    else:
        print("Invalid command.")


if __name__ == "__main__":
    main()
