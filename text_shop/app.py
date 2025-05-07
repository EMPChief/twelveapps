class GalacticMarket:
    """
    Welcome to the GalacticMarket™ — because survival should always come at a steep price.
    You're a lone pilot with 299.17 credits and a shopping list of questionable morality.
    """

    def __init__(self):
        """
        Initialize the cargo hold with pseudo-edible items and set the user's credit balance.
        Because what's space commerce without inflation and a mild existential crisis?
        """
        self.cargo_hold = {
            "oxygen_canister": {"price": 25.00, "quantity": 3},
            "hydration_gel": {"price": 5.00, "quantity": 7},
            "quantum_lime": {"price": 12.50, "quantity": 207},
            "synth_beef": {"price": 30.00, "quantity": 501},
            "lab_grown_pork": {"price": 30.00, "quantity": 501},
            "clone_chicken": {"price": 20.00, "quantity": 501},
            "space_fish": {"price": 22.00, "quantity": 501},
            "canned_tuna_alpha": {"price": 22.00, "quantity": 501}
        }
        self.credits = 299.17
        self.acquired_loot = []

    def display_manifest(self):
        """
        Print the current contents of the cargo hold and remaining credits.
        A transparent reminder of what you can’t afford and the weight of your choices.
        """
        print("\n" + "=" * 50)
        print("🚀 CARGO MANIFEST - U.S.S. CAPITALISM 🚀".center(50))
        print("=" * 50)
        for item, details in self.cargo_hold.items():
            print(
                f"{item.replace('_', ' ').title():<20} ⛽ {details['price']:<6.2f} ¢  x{details['quantity']}")
        print("-" * 50)
        print(f"💳 Remaining Galactic Credits: {self.credits:.2f}")
        print("=" * 50)

    def acquire_item(self, item, quantity):
        """
        Attempt to buy an item from the cargo hold.
        May fail if you’re broke, unlucky, or asking for too much — much like real life.
        """
        if item not in self.cargo_hold:
            print("🤖 ERROR 404: That item has been erased from the timeline.\n")
            return

        if quantity > self.cargo_hold[item]["quantity"]:
            print("🚨 Not enough in stock. Try asking the void for mercy.\n")
            return

        total_cost = self.cargo_hold[item]["price"] * quantity
        if self.credits >= total_cost:
            self.credits -= total_cost
            self.cargo_hold[item]["quantity"] -= quantity
            self.acquired_loot.append((item, quantity))
            print(
                f"🛰️ Transaction complete: {quantity} x {item.replace('_', ' ')} acquired.")
            print("📦 Your survival rate has increased by 0.0002%. Congratulations.")
        else:
            print(
                "💀 Not enough credits. You can always trade in a memory or two. Childhood ones sell well.")

        print(f"📉 Remaining credits: {self.credits:.2f}\n")

    def review_loot(self):
        """
        Display a summary of what the user has bought so far.
        A great way to reflect on your consumption before the void consumes you.
        """
        print("\n📦 Acquired Cargo So Far:")
        if not self.acquired_loot:
            print("Nothing. Just like your dreams, hopes, and stable income.\n")
            return
        manifest = {}
        for item, quantity in self.acquired_loot:
            manifest[item] = manifest.get(item, 0) + quantity
        for item, quantity in manifest.items():
            print(f"• {quantity} x {item.replace('_', ' ').title()}")
        print()

    def initiate_trade_protocol(self):
        """
        Main loop for galactic shopping.
        You can purchase, view your loot, or exit and await the heat death of the universe.
        """
        try:
            while True:
                self.display_manifest()
                item = input(
                    "\nWhat cargo would you like to acquire? (type 'eject' to exit, 'log' to view acquired cargo): "
                ).lower().strip()
                if item == "eject":
                    print(
                        "\n🪐 Exiting Galactic Market. Your fate is now in the hands of entropy.\n")
                    break
                if item == "log":
                    self.review_loot()
                    continue
                if item not in self.cargo_hold:
                    print(
                        "🛰️ INVALID REQUEST: That item doesn’t exist, kind of like job security.\n")
                    continue
                try:
                    quant = int(
                        input(f"How many units of {item.replace('_', ' ')}? ").strip())
                    self.acquire_item(item, quant)
                except ValueError:
                    print(
                        "🤖 INPUT ERROR: That wasn’t a number. Just like the love your creator gave you.\n")
        except KeyboardInterrupt:
            print(
                "\n\n💫 Protocol terminated. You may now return to screaming into the void.\n")


if __name__ == "__main__":
    """
    Initiate the GalacticMarket.
    This is your last chance to shop before capitalism collapses under cosmic radiation.
    """
    print("🪐 Welcome to the Galactic Market, pilot. Where dreams are sold... and sometimes refunded for store credit. 🪐")
    market = GalacticMarket()
    market.initiate_trade_protocol()
