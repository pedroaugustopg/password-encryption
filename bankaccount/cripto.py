from hashlib import sha256

from rich.table import Table

class BankAccount:

    def __init__(self, id:int, name:str = None, balance:float = 0, password:str = None):
        self._id = id
        self._name = name
        self.__balance = balance
        if password is None:
            password = self.create_password()
        self.__hash = sha256(password.encode()).hexdigest()
        print(f"Bank Account {self._id} created! Actual balance: R$ {self.__balance:,.2f}")

    def create_password(self) -> str:
        while True:
            code = str(input("Password: ")).strip()
            if len(code) >= 6:
                break
            print("Enter a password of at least 6 characters.")

        return code

    def validate_password(self, password:str) -> bool:
        user = sha256(password.encode()).hexdigest()
        if user == self.__hash:
            return True
        else:
            return False

    def __rich_console__(self, console, options):
        balance_color = "green" if self.__balance >= 0 else "red"

        table = Table(title="BANK ACCOUNT", show_header=True, header_style="bold cyan")
        table.add_column("Field", style="cyan")
        table.add_column("Value")

        table.add_row("Hash", self.__hash)
        table.add_row("ID", str(self._id))
        table.add_row("Name", self._name)
        table.add_row(
            "Balance",
            f"[{balance_color}]R$ {self.__balance:,.2f}[/{balance_color}]"
        )

        yield table

    def deposit(self, value):
        self.__balance += value

        table = Table(title="DEPOSIT RECEIPT", show_header=True, header_style="bold green")
        table.add_column("Description")
        table.add_column("Value", justify="right")

        table.add_row("Operation", "Deposit")
        table.add_row("Amount", f"[green]R$ {value:,.2f}[/green]")
        table.add_row(
            "Current Balance",
            f"[green]R$ {self.__balance:,.2f}[/green]"
        )

        return table

    def withdraw(self, value:float, password:str = None):
        value = abs(value)

        if password is None:
            password = self.create_password()

        if self.validate_password(password):
            if value > self.__balance:
                table = Table(title="WITHDRAW FAILED", show_header=True, header_style="bold red")
                table.add_column("Description")
                table.add_column("Value", justify="right")

                table.add_row("Requested", f"R$ {value:,.2f}")
                table.add_row("Available", f"[green]R$ {self.__balance:,.2f}[/green]")
                table.add_row("Status", "[bold red]INSUFFICIENT BALANCE[/bold red]")

                return table

            else:
                self.__balance -= value

                balance_color = "green" if self.__balance >= 0 else "red"

                table = Table(title="WITHDRAW RECEIPT", show_header=True, header_style="bold yellow")
                table.add_column("Description")
                table.add_column("Value", justify="right")

                table.add_row("Operation", "Withdraw")
                table.add_row("Amount", f"[yellow]R$ {value:,.2f}[/yellow]")
                table.add_row(
                    "Current Balance",
                    f"[{balance_color}]R$ {self.__balance:,.2f}[/{balance_color}]"
                )

                return table

        else:
            print(f"Incorrect password. Withdrawal not authorized.")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, newname:str = None):
        password = self.create_password()

        if self.validate_password(password):
            if len(newname) >= 1:
                self._name = newname
        else:
            print("ERROR! Incorrect password.")