# savings_account.py

from bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, owner_name: str, account_number: str, routing_number: str,
                 initial_balance: float = 0.0, interest_rate: float = 0.02):
        super().__init__(owner_name, account_number, routing_number, initial_balance)
        self.interest_rate = float(interest_rate)

    def apply_interest(self) -> float:
        """
        Adds interest to the current balance and returns the interest amount added.
        """
        if self.interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")

        interest = self._balance * self.interest_rate
        self._balance += interest
        return interest
