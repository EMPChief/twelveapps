"""Shop scene implementation."""
from utils.printing import typewriter_print, clear_screen
from router import go_to_town, register_shop_function
from player import player
from scenes.shop_inventory import get_available_items
import time
import random

def shop():
    """The shop scene where player can buy items."""
    while True:
        player.display_status()
        typewriter_print(
            "Welcome to the Space Shop™ – where dreams go to die and wallets come to cry.")
        typewriter_print(
            "Yes, the prices are ridiculous. No, we don't take coupons. Or common sense.")

        # Get available items based on shop tier
        available_items = get_available_items(player.get_shop_tier())
        
        # Create numbered menu of items
        shop_menu = {}
        for i, (name, item) in enumerate(available_items.items(), 1):
            price = item["base_price"] * (1 + random.uniform(-0.1, 0.1))
            inventory = random.randint(1, 5)
            shop_menu[str(i)] = {
                "name": name,
                "price": int(price),
                "inventory": inventory,
                "description": item["description"]
            }
            typewriter_print(
                f"{i}. {name} - {item['description']}\n   Price: {int(price)} credits, In stock: {inventory}"
            )

        try:
            choice = input(
                "\nPick an item number to buy, or 'q' to quit and spare yourself: ").strip()

            if choice.lower() == 'q':
                typewriter_print(
                    "Fine, leave. The shopkeeper didn't like your vibe anyway.")
                time.sleep(1)
                clear_screen()
                go_to_town()
                return

            if choice not in shop_menu:
                typewriter_print(
                    "Bold move picking an item that doesn't exist. Try again, space cadet.")
                continue

            item = shop_menu[choice]

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
            elif player.gold < total_price:
                typewriter_print(
                    "Not enough gold? Maybe go shake down some space pirates first.")
            else:
                player.gold -= total_price
                player.inventory.extend([item["name"]] * quantity)
                typewriter_print(
                    f"Look at you, buying {quantity} x {item['name']} like it's payday in the asteroid mines.")
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
