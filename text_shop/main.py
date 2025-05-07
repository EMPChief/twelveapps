class TextShop:
    def __init__(self):
        """Initialize the shop with a predefined inventory, starting money, and an empty purchase history."""
        self.inventory = {
            "orange": {"price": 1.00, "quantity": 3},
            "lemon": {"price": 0.50, "quantity": 7},
            "lime": {"price": 0.50, "quantity": 207},
            "beef": {"price": 3.00, "quantity": 501},
            "pork": {"price": 3.00, "quantity": 501},
            "chicken": {"price": 2.00, "quantity": 501},
            "fish": {"price": 2.00, "quantity": 501},
            "tuna": {"price": 2.00, "quantity": 501}
        }
        self.balance = 299.17
        self.purchase_history = []

    def display_inventory(self):
        """Display the current inventory and available balance."""
        print("\n" + "=" * 40)
        print("🛒 Inventory".center(40))
        print("=" * 40)
        for item_name, item_details in self.inventory.items():
            print(
                f"{item_name.title():<10} ${item_details['price']:<5.2f}  x{item_details['quantity']}")
        print("-" * 40)
        print(f"💰 Available Balance: ${self.balance:.2f}")
        print("=" * 40)

    def buy_item(self, item_name, quantity_to_buy):
        """
        Attempt to buy a specified quantity of an item.

        Parameters:
        - item_name (str): Name of the item to buy.
        - quantity_to_buy (int): Number of units to purchase.
        """
        if item_name not in self.inventory:
            print("❌ Item not found.\n")
            return

        if quantity_to_buy > self.inventory[item_name]["quantity"]:
            print("⚠️ Not enough in stock.\n")
            return

        total_cost = self.inventory[item_name]["price"] * quantity_to_buy
        if self.balance >= total_cost:
            self.balance -= total_cost
            self.inventory[item_name]["quantity"] -= quantity_to_buy
            self.purchase_history.append((item_name, quantity_to_buy))
            print(f"✅ Bought {quantity_to_buy} x {item_name}.")
        else:
            print("❌ You don't have enough balance to buy that.")

        print(f"💰 You have ${self.balance:.2f} left.\n")

    def view_purchase_history(self):
        """Display the list of items the user has purchased so far."""
        print("\n📦 Items You've Bought So Far:")
        if not self.purchase_history:
            print("You haven't bought anything yet.\n")
            return
        item_totals = {}
        for item_name, quantity in self.purchase_history:
            item_totals[item_name] = item_totals.get(item_name, 0) + quantity
        for item_name, quantity in item_totals.items():
            print(f"• {quantity} x {item_name}")
        print()

    def run_program(self):
        """Run the shop program, allowing users to interact with the inventory."""
        try:
            while True:
                self.display_inventory()
                item_name = input(
                    "What would you like to buy? (type 'exit' to quit, 'lis' to view purchases): ").lower().strip()
                if item_name == "exit":
                    print("\n👋 Exiting shop. Thank you for visiting!\n")
                    break
                if item_name == "lis":
                    self.view_purchase_history()
                    continue
                if item_name not in self.inventory:
                    print("❌ Item not found. Try again.\n")
                    continue
                try:
                    quantity_to_buy = int(
                        input(f"How many {item_name}s would you like to buy? ").strip())
                    self.buy_item(item_name, quantity_to_buy)
                except ValueError:
                    print("❌ Please enter a valid number.\n")
        except KeyboardInterrupt:
            print("\n\n👋 Program interrupted. Goodbye!\n")


if __name__ == "__main__":
    print("🛒 Welcome to the Text Shop! 🛒")
    text_shop = TextShop()
    text_shop.run_program()
