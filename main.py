# main.py

from savings_account import SavingsAccount
from checking_account import CheckingAccount

def run_demo():
    print("=== Creating accounts (2 savings, 2 checking) ===")

    # Two Savings accounts
    savings1 = SavingsAccount("Yama", "SAV-1001", "021000021", 500.00, interest_rate=0.05)
    savings2 = SavingsAccount("Alex", "SAV-2002", "021000021", 1000.00, interest_rate=0.03)

    # Two Checking accounts
    checking1 = CheckingAccount("Yama", "CHK-3003", "021000021", 300.00, transfer_limit=2)
    checking2 = CheckingAccount("Jamie", "CHK-4004", "021000021", 150.00, transfer_limit=1)

    print("\n=== Scenario: User opens a checking account and withdraws $50 ===")
    print("Before withdrawal:")
    checking1.display_info()

    checking1.withdraw(50)
    print("\nAfter withdrawal of $50:")
    checking1.display_info()

    print("\n=== Savings interest scenario ===")
    print("Before interest:")
    savings1.display_info()

    interest_added = savings1.apply_interest()
    print(f"\nInterest added: ${interest_added:.2f}")
    print("After interest:")
    savings1.display_info()

    print("\n=== Transfer limitation scenario (Checking transfers) ===")
    print(f"Checking1 remaining transfers: {checking1.remaining_transfers()}")
    checking1.transfer_to(savings2, 25)
    print("Transferred $25 from Checking1 to Savings2")
    print(f"Checking1 remaining transfers: {checking1.remaining_transfers()}")

    checking1.transfer_to(savings2, 25)
    print("Transferred another $25 from Checking1 to Savings2")
    print(f"Checking1 remaining transfers: {checking1.remaining_transfers()}")

    print("\nTrying one more transfer (should fail due to limit):")
    try:
        checking1.transfer_to(savings2, 10)
    except ValueError as e:
        print("Transfer blocked:", e)

    print("\n=== Final balances ===")
    print("\nChecking1:")
    checking1.display_info()
    print("\nSavings2:")
    savings2.display_info()

    print("\n=== Second checking account test (limit=1) ===")
    print(f"Checking2 remaining transfers: {checking2.remaining_transfers()}")
    checking2.transfer_to(savings1, 10)
    print("Transferred $10 from Checking2 to Savings1")
    print(f"Checking2 remaining transfers: {checking2.remaining_transfers()}")
    try:
        checking2.transfer_to(savings1, 5)
    except ValueError as e:
        print("Transfer blocked:", e)

if __name__ == "__main__":
    run_demo()
