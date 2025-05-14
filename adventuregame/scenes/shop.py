from utils.printing import typewriter_print, clear_screen
from router import go_to_town, register_shop_function
from player import player, health_gold_name
import time
import random

def shop():
    item_names = [
        "Health Potion", "Gold Bar", "Space Suit", "Fuel", "Laser Gun",
        "Teleportation Device", "Shield Generator", "Energy Drink", "Stamina Pills",
        "Jetpack", "Anti-Gravity Boots", "Space Helmet", "Quantum Chip", "Warp Drive",
        "Star Map", "Moon Rock", "Plasma Rifle", "Energy Shield", "Rocket Fuel",
        "Ion Blaster", "Exosuit Upgrade"
    ]
    shop_items = {}
    for i in range(1, 15):
        name = random.choice(item_names)
        price = random.randint(5, 150)
        inventory = random.randint(5, 100)
        shop_items[str(i)] = {
            "name": name,
            "inventory": inventory,
            "price": price
        }

    while True:
        health_gold_name()
        typewriter_print(
            "Welcome to the Space Shop™ – where dreams go to die and wallets come to cry.")
        typewriter_print(
            "Yes, the prices are ridiculous. No, we don't take coupons. Or common sense.")

        for key, item in shop_items.items():
            typewriter_print(
                f"{key}. {item['name']} (Price: {item['price']} credits, In stock: {item['inventory']})"
            )

        try:
            choice = input(
                "Pick an item number to buy, or 'q' to quit and spare yourself: ").strip()

            if choice.lower() == 'q':
                typewriter_print(
                    "Fine, leave. The shopkeeper didn't like your vibe anyway.")
                time.sleep(1)
                clear_screen()
                go_to_town()
                return

            if choice not in shop_items:
                typewriter_print(
                    "Bold move picking an item that doesn’t exist. Try again, space cadet.")
                continue

            item = shop_items[choice]

            try:
                quantity = int(
                    input(f"How many {item['name']}s do you want to overpay for? "))
            except ValueError:
                typewriter_print(
                    "You call that a number? Try again with actual digits.")
                continue

            if quantity <= 0:
                typewriter_print(
                    "Very funny. Come back when you're serious about spending money.")
                continue

            total_price = item["price"] * quantity

            if quantity > item["inventory"]:
                typewriter_print(
                    f"Wow, ambitious. We only have {item['inventory']} in stock.")
            elif player["gold"] < total_price:
                typewriter_print(
                    "Not enough gold? Maybe go shake down some space pirates first.")
            else:
                player["gold"] -= total_price
                player["inventory"].extend([item["name"]] * quantity)
                item["inventory"] -= quantity
                typewriter_print(
                    f"Look at you, buying {quantity} x {item['name']} like it’s payday in the asteroid mines.")
                time.sleep(1)
                clear_screen()

        except (EOFError, KeyboardInterrupt):
            typewriter_print(
                "\nTrying to rage-quit the shop? Respectable. Returning to town...")
            time.sleep(1)
            clear_screen()
            go_to_town()
            return


register_shop_function(shop)
