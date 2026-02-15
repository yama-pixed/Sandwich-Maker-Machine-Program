# checking_account.py

from bank_account import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, owner_name: str, account_number: str, routing_number: str,
                 initial_balance: float = 0.0, transfer_limit: int = 3):
        super().__init__(owner_name, account_number, routing_number, initial_balance)
        self.transfer_limit = int(transfer_limit)
        self.transfers_made = 0

    def transfer_to(self, other_account: BankAccount, amount: float) -> None:
        """
        Overrides parent transfer_to with a transfer limitation.
        """
        if self.transfers_made >= self.transfer_limit:
            raise ValueError("Transfer limit reached for this checking account.")

        super().transfer_to(other_account, amount)
        self.transfers_made += 1

    def remaining_transfers(self) -> int:
        return self.transfer_limit - self.transfers_made
