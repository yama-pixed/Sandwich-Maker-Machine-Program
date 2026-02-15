# bank_account.py

class BankAccount:
    def __init__(self, owner_name: str, account_number: str, routing_number: str, initial_balance: float = 0.0):
        self.owner_name = owner_name
        self._account_number = account_number          # protected member
        self.__routing_number = routing_number         # private member
        self._balance = float(initial_balance)         # protected (so subclasses can access)

    # ----- getters (safe access) -----
    def get_account_number(self) -> str:
        return self._account_number

    def get_routing_number_masked(self) -> str:
        # show only last 4 digits
        last4 = str(self.__routing_number)[-4:]
        return f"****{last4}"

    def get_balance(self) -> float:
        return self._balance

    # ----- core behaviors -----
    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount

    def transfer_to(self, other_account: "BankAccount", amount: float) -> None:
        if not isinstance(other_account, BankAccount):
            raise TypeError("Transfers must be to another BankAccount.")
        self.withdraw(amount)
        other_account.deposit(amount)

    def display_info(self) -> None:
        print(f"Owner: {self.owner_name}")
        print(f"Account#: {self._account_number}")
        print(f"Routing#: {self.get_routing_number_masked()}")
        print(f"Balance: ${self._balance:.2f}")
