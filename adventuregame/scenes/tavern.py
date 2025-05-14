"""Tavern scene implementation."""
from utils.printing import typewriter_print, clear_screen
from router import go_to_town, register_tavern_function
from player import player
from config import (
    TAVERN_SLEEP_COST,
    TAVERN_STEW_COST,
    TAVERN_HEAL_AMOUNT,
    TAVERN_POISON_DAMAGE,
    TAVERN_POISON_DURATION
)
import time
import random


def tavern():
    """The tavern scene where player can rest, eat suspicious stew, or leave."""
    while True:
        player.display_status()
        typewriter_print(
            "You enter the tavern. It's... cozy? Or is that just the smell?")
        typewriter_print(
            f"1. Rest   - Get some sleep and heal (Cost: {TAVERN_SLEEP_COST} gold).")
        typewriter_print(
            f"2. Eat    - Try the suspicious stew (Cost: {TAVERN_STEW_COST} gold).")
        typewriter_print("3. Leave  - Get out while you can.")

        try:
            choice = input("What would you like to do? (1/2/3): ")

            if choice == '1':
                if player.gold < TAVERN_SLEEP_COST:
                    typewriter_print(
                        "You don't have enough gold to rest. Maybe you should've saved some?")
                    time.sleep(1)
                    clear_screen()
                    continue

                typewriter_print(
                    "You decide to take a nap. Sweet dreams, but it's gonna cost you.")
                time.sleep(1)
                clear_screen()

                player.gold -= TAVERN_SLEEP_COST
                player.heal(TAVERN_HEAL_AMOUNT)
                player.display_status()

                typewriter_print("You feel refreshed! Health restored.")
                time.sleep(1)
                clear_screen()
                go_to_town()
                break

            elif choice == '2':
                if player.gold < TAVERN_STEW_COST:
                    typewriter_print(
                        "You don't have enough gold to try the suspicious stew. Maybe try again later?")
                    time.sleep(1)
                    clear_screen()
                    continue

                typewriter_print(
                    "You eat the suspicious stew. It tastes... interesting.")
                player.gold -= TAVERN_STEW_COST
                effect = random.choice(["poison", "damage", "heal", "nothing"])
                time.sleep(1)
                clear_screen()

                if effect == "poison":
                    survived = player.poison_damage(TAVERN_POISON_DAMAGE, TAVERN_POISON_DURATION)
                    if survived:
                        typewriter_print(
                            "That stew was laced with something! You barely survived.")
                elif effect == "damage":
                    player.damage(TAVERN_POISON_DAMAGE)
                    typewriter_print(
                        "Your stomach churns... That stew did **not** sit well.")
                elif effect == "heal":
                    player.heal(TAVERN_HEAL_AMOUNT // 2)  # Half the healing of sleeping
                    typewriter_print(
                        "Weirdly, you feel energized! Maybe that stew wasn't so bad after all.")
                else:
                    typewriter_print(
                        "You wait... but nothing happens. Just gas.")

                player.display_status()
                time.sleep(2)
                clear_screen()

            elif choice == '3':
                typewriter_print("You wisely decide to leave the tavern.")
                time.sleep(1)
                clear_screen()
                go_to_town()
                break

            else:
                typewriter_print("Invalid choice. Please pick 1, 2, or 3.")
                time.sleep(1)
                clear_screen()

        except ValueError:
            typewriter_print(
                "Oops! That wasn't a valid input. Please enter a number.")
            time.sleep(1)
            clear_screen()


register_tavern_function(tavern)
