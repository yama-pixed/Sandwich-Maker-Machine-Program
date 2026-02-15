class Cashier:
    """Handles coin processing and payment validation."""

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01,
    }

    def process_coins(self) -> float:
        """Prompt for coin counts and return total payment."""
        print("Please insert coins.")
        total = 0.0
        for coin_name, value in self.COIN_VALUES.items():
            count = self._read_nonnegative_int(f"How many {coin_name}? ")
            total += count * value
        return round(total, 2)

    def transaction_result(self, payment: float, cost: float) -> bool:
        """Return True if enough money, else refund and False."""
        if payment < cost:
            print(f"Sorry, that's not enough money. ${payment:.2f} refunded.")
            return False

        change = round(payment - cost, 2)
        if change > 0:
            print(f"Here is ${change:.2f} in change.")
        print("Payment accepted.")
        return True

    @staticmethod
    def _read_nonnegative_int(prompt: str) -> int:
        """Read a non-negative integer from input."""
        while True:
            raw = input(prompt).strip()
            try:
                value = int(raw)
                if value < 0:
                    print("Please enter a non-negative number.")
                    continue
                return value
            except ValueError:
                print("Please enter a whole number (0, 1, 2, ...).")
