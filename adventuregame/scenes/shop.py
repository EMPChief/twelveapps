from utils.printing import typewriter_print, clear_screen
from router import go_to_town, register_shop_function
from player import player, health_gold_name
import time


def shop():
    shop_items = {
        "1": {"name": "Health Potion", "inventory": 71, "price": 10},
        "2": {"name": "Gold Bar", "inventory": 82, "price": 100},
        "3": {"name": "Space Suit", "inventory": 92, "price": 50},
        "4": {"name": "Fuel", "inventory": 107, "price": 5},
    }

    while True:
        health_gold_name()
        typewriter_print("Welcome to the space shop!")
        typewriter_print(
            "Yes, the prices are ridiculous. No, we don't take coupons.")
        for key, item in shop_items.items():
            typewriter_print(
                f"{key}. {item['name']} (Price: {item['price']}, In stock: {item['inventory']})")

        choice = input(
            "Enter the number of the item you want to buy (or 'q' to quit): ")

        if choice.lower() == 'q':
            typewriter_print(
                "Fine, leave. The shopkeeper didn't like you anyway.")
            go_to_town()
            return

        if choice in shop_items:
            item = shop_items[choice]

            try:
                quantity = int(
                    input(f"How many {item['name']}s do you want to buy? "))
            except ValueError:
                typewriter_print("That doesn't look like a number. Try again.")
                continue

            total_price = item["price"] * quantity

            if quantity > item["inventory"]:
                typewriter_print(
                    f"Sorry, we only have {item['inventory']} in stock.")
            elif player["gold"] < total_price:
                typewriter_print(
                    "Aww... not enough gold. Maybe sell a kidney?")
            else:
                player["gold"] -= total_price
                player["inventory"].extend([item["name"]] * quantity)
                item["inventory"] -= quantity
                typewriter_print(
                    f"You bought {quantity} x {item['name']}! Big spender, huh?")
                time.sleep(1)
                clear_screen()
        else:
            typewriter_print(
                "Bold strategy. Picked an option that doesn't exist.")


register_shop_function(shop)
