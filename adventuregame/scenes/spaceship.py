"""Spaceship scene implementation."""
from utils.printing import typewriter_print, clear_screen
from router import go_to_town, register_scene, router
from player import player
import time

def display_ship_status():
    """Display ship status and available upgrades."""
    typewriter_print("=== Ship Systems Status ===")
    typewriter_print("Hull Integrity: 100%")
    typewriter_print("Fuel Level: 87%")
    typewriter_print("Life Support: Optimal")
    typewriter_print("Navigation: Online")
    typewriter_print("=========================")

def view_missions():
    """Display available and completed missions."""
    typewriter_print("=== Mission Control ===")
    if not player.progress["quests_completed"]:
        typewriter_print("No missions completed yet.")
    else:
        typewriter_print("Completed Missions:")
        for quest in player.progress["quests_completed"]:
            typewriter_print(f"- {quest}")
    
    typewriter_print("\nActive Missions:")
    typewriter_print("- Collect mineral samples from the crystal caves")
    typewriter_print("- Investigate the mysterious signal in sector 7")
    typewriter_print("====================")

def check_inventory():
    """Display detailed inventory with item descriptions."""
    typewriter_print("=== Cargo Hold Contents ===")
    if not player.inventory:
        typewriter_print("The cargo hold is empty.")
        return
    
    from collections import Counter
    from scenes.shop_inventory import SHOP_ITEMS
    
    inventory_counts = Counter(player.inventory)
    for item, count in inventory_counts.items():
        if item in SHOP_ITEMS:
            description = SHOP_ITEMS[item]["description"]
            typewriter_print(f"- {item} (x{count})")
            typewriter_print(f"  {description}")
    typewriter_print("========================")

def spaceship():
    """The spaceship scene where player can check status, inventory, and missions."""
    while True:
        player.display_status()
        typewriter_print("\nWelcome aboard the S.S. Wanderlust!")
        typewriter_print("What would you like to do?")
        typewriter_print("1. Check Ship Status")
        typewriter_print("2. View Mission Log")
        typewriter_print("3. Check Cargo Hold")
        typewriter_print("4. Launch Adventure")
        typewriter_print("5. Exit to Surface")
        typewriter_print("6. Quit Game")

        try:
            choice = input("\nEnter your choice (1-6): ").strip()

            if choice == "1":
                clear_screen()
                display_ship_status()
                time.sleep(2)

            elif choice == "2":
                clear_screen()
                view_missions()
                time.sleep(2)

            elif choice == "3":
                clear_screen()
                check_inventory()
                time.sleep(2)

            elif choice == "4":
                typewriter_print("Accessing adventure control system...")
                time.sleep(1)
                clear_screen()
                router.go_to_scene("adventure")
                break

            elif choice == "5":
                typewriter_print("Exiting ship... Don't forget your space suit!")
                time.sleep(1)
                clear_screen()
                go_to_town()
                break

            elif choice == "6":
                typewriter_print("Shutting down ship systems...")
                typewriter_print("Thank you for playing!")
                time.sleep(1)
                clear_screen()
                exit()

            else:
                typewriter_print("Invalid command. Please select 1-6.")
                time.sleep(1)
                clear_screen()
                continue

        except (EOFError, KeyboardInterrupt):
            typewriter_print("\nEmergency exit initiated. Returning to surface...")
            time.sleep(1)
            clear_screen()
            go_to_town()
            break

# Register the spaceship scene
register_scene("spaceship", spaceship) 