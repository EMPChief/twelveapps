class TextShop:
    def __init__(self):
        self.shop = {
            "orange": {"price": 1.00, "quantity": 3},
            "lemon": {"price": 0.50, "quantity": 7},
            "lime": {"price": 0.50, "quantity": 207},
            "beef": {"price": 3.00, "quantity": 501},
            "pork": {"price": 3.00, "quantity": 501},
            "chicken": {"price": 2.00, "quantity": 501},
            "fish": {"price": 2.00, "quantity": 501},
            "tuna": {"price": 2.00, "quantity": 501}
        }
        self.money = 299.17
        self.user_buy = []

    def display_inventory(self):
        print("\n" + "=" * 40)
        print("🛒 Inventory".center(40))
        print("=" * 40)
        for item, details in self.shop.items():
            print(
                f"{item.title():<10} ${details['price']:<5.2f}  x{details['quantity']}")
        print("-" * 40)
        print(f"💰 Available Money: ${self.money:.2f}")
        print("=" * 40)

    def buy_item(self, item, quantity):
        if item not in self.shop:
            print("❌ Item not found.\n")
            return

        if quantity > self.shop[item]["quantity"]:
            print("⚠️ Not enough in stock.\n")
            return

        total_cost = self.shop[item]["price"] * quantity
        if self.money >= total_cost:
            self.money -= total_cost
            self.shop[item]["quantity"] -= quantity
            self.user_buy.append((item, quantity))
            print(f"✅ Bought {quantity} x {item}.")
        else:
            print("❌ You don't have enough money to buy that.")

        print(f"💰 You have ${self.money:.2f} left.\n")

    def user_bought_so_far(self):
        print("\n📦 Items You've Bought So Far:")
        if not self.user_buy:
            print("You haven't bought anything yet.\n")
            return
        totals = {}
        for item, quantity in self.user_buy:
            totals[item] = totals.get(item, 0) + quantity
        for item, quantity in totals.items():
            print(f"• {quantity} x {item}")
        print()

    def run_program(self):
        try:
            while True:
                self.display_inventory()
                item = input(
                    "What would you like to buy? (type 'exit' to quit, 'lis' to view purchases): ").lower().strip()
                if item == "exit":
                    print("\n👋 Exiting shop. Thank you for visiting!\n")
                    break
                if item == "lis":
                    self.user_bought_so_far()
                    continue
                if item not in self.shop:
                    print("❌ Item not found. Try again.\n")
                    continue
                try:
                    quant = int(
                        input(f"How many {item}s would you like to buy? ").strip())
                    self.buy_item(item, quant)
                except ValueError:
                    print("❌ Please enter a valid number.\n")
        except KeyboardInterrupt:
            print("\n\n👋 Program interrupted. Goodbye!\n")


if __name__ == "__main__":
    print("🛒 Welcome to the Text Shop! 🛒")
    text_shop = TextShop()
    text_shop.run_program()
