from rich.console import Console
from cripto import *


def main():
    console = Console()

    while True:
        try:
            account_id = int(input("Account ID: "))
            break
        except ValueError:
            console.print("ERROR! Enter only integer numbers for the Account ID.")

        account_name = input("Account Holder: ")

    while True:
        try:
            initial_balance = float(input("Initial Balance: "))
            break
        except ValueError:
            console.print("ERROR! Enter only numeric values for the Initial Balance.")

    account = BankAccount(account_id, account_name, initial_balance)

    console.print()
    console.print(account)

    deposit_amount = float(input("\nDeposit Amount: "))
    console.print(account.deposit(deposit_amount))

    withdraw_amount = float(input("\nWithdraw Amount: "))
    console.print(account.withdraw(withdraw_amount))

    console.print()
    console.print(account)

    console.print()
    print("Changing the account holder")
    new_name = input("New Account Holder: ")

    account.name = new_name

    console.print()
    console.print(account)


if __name__ == "__main__":
    main()