from rich.console import Console
from bankaccount.cripto import *


def main():
    console = Console()

    account_id = int(input("Account ID: "))
    account_name = input("Account Holder: ")
    initial_balance = float(input("Initial Balance: "))

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