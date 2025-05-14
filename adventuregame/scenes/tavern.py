from utils.printing import typewriter_print, clear_screen
from router import go_to_town, register_tavern_function
from player import player, health_gold_name, player_heal, player_damage, poison_damage
import time
import random


def tavern():
    """The tavern scene where player can rest and eat some funny suspicious stew."""
    typewriter_print(
        "You enter the tavern. It's... cozy? Or is that just the smell?")
    typewriter_print("1. Rest   - Get some sleep and heal.")
    typewriter_print(
        "2. Eat    - Try the suspicious stew. (Warning: may cause side effects.)")
    typewriter_print("3. Leave  - Get out while you can.")

    while True:
        choice = input("What would you like to do? (1/2/3): ")

        if choice == '1':
            typewriter_print("You take a nap. Sweet dreams!")
            time.sleep(1)
            clear_screen()
            player_heal(20)
            health_gold_name()

            typewriter_print("You feel refreshed! Health restored.")
            time.sleep(1)
            clear_screen()
            go_to_town()
            break

        elif choice == '2':
            typewriter_print(
                "You eat the suspicious stew. It tastes... interesting.")
            effect = random.choice(["poison", "damage", "heal", "nothing"])
            time.sleep(1)
            clear_screen()

            if effect == "poison":
                survived = poison_damage(5, 3)
                if survived:
                    typewriter_print(
                        "That stew was laced with something! You barely survived.")
            elif effect == "damage":
                player_damage(5)
                typewriter_print(
                    "Your stomach churns... That stew did **not** sit well.")
            elif effect == "heal":
                player_heal(10)
                typewriter_print(
                    "Weirdly, you feel energized! Maybe that stew wasn’t so bad after all.")
            else:
                typewriter_print("You wait... but nothing happens. Just gas.")

            health_gold_name()
            time.sleep(2)
            clear_screen()

        elif choice == '3':
            typewriter_print("You wisely decide to leave the tavern.")
            time.sleep(1)
            clear_screen()
            go_to_town()
            break

        else:
            typewriter_print("Please choose 1, 2, or 3.")


register_tavern_function(tavern)
