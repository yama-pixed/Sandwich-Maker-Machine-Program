class SandwichMaker:
    

    def __init__(self, resources: dict[str, int]) -> None:
        self.resources = resources

    def report(self) -> None:
        """Print current resource levels."""
        print("\n--- Inventory Report ---")
        for item, amount in self.resources.items():
            print(f"{item.capitalize()}: {amount}")
        print("------------------------\n")

    def check_resources(self, ingredients: dict[str, int]) -> bool:
        """Return True if enough resources exist; otherwise False."""
        for item, required in ingredients.items():
            available = self.resources.get(item, 0)
            if required > available:
                print(f"Sorry, not enough {item}. (need {required}, have {available})")
                return False
        return True

    def make_sandwich(self, sandwich_name: str, ingredients: dict[str, int]) -> None:
        """Deduct ingredients and confirm sandwich made."""
        for item, required in ingredients.items():
            self.resources[item] -= required
        print(f"Here is your {sandwich_name.replace('_', ' ')}. Enjoy! 🥪")
