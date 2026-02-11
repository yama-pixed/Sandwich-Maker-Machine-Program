import data
import sandwich_maker
import cashier


def main() -> None:
    resources = data.resources
    recipes = data.recipes

    maker = sandwich_maker.SandwichMaker(resources)
    register = cashier.Cashier()

    menu_items = ", ".join(recipes.keys())

    is_on = True
    while is_on:
        choice = input(
            f"What would you like? ({menu_items})\n"
            f"Type 'report' to view inventory or 'off' to quit: "
        ).strip().lower()

        if choice == "off":
            is_on = False
            print("Machine shutting down. Bye!")
            continue

        if choice == "report":
            maker.report()
            continue

        if choice not in recipes:
            print("Invalid selection. Try again.")
            continue

        recipe = recipes[choice]
        ingredients = recipe["ingredients"]
        cost = recipe["cost"]

        if not maker.check_resources(ingredients):
            continue

        print(f"The cost is ${cost:.2f}")
        payment = register.process_coins()

        if register.transaction_result(payment, cost):
            maker.make_sandwich(choice, ingredients)


if __name__ == "__main__":
    main()
