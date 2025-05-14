from utils.printing import typewriter_print, clear_screen
from router import go_to_town, register_tavern_function
from player import player, health_gold_name, player_heal, player_damage, poison_damage
import time
import random


def tavern():
    """The tavern scene where players can enjoy questionable hospitality and regret their choices."""
    typewriter_print(
        "You stumble into the tavern. Ah yes, nothing like the warm embrace of stale beer and desperation.")
    typewriter_print("1. Rest   - Pretend sleeping here is remotely safe.")
    typewriter_print(
        "2. Eat    - Sample the local stew. It's... legendary. For all the wrong reasons.")
    typewriter_print("3. Leave  - Run before your life choices get worse.")

    while True:
        choice = input("What would you like to do? (1/2/3): ")

        if choice == '1':
            typewriter_print(
                "You collapse onto something vaguely resembling a bed. Comfy-ish.")
            time.sleep(1)
            clear_screen()
            player_heal(20)
            health_gold_name()

            typewriter_print(
                "Miraculously, you wake up with fewer bruises. Health restored!")
            time.sleep(1)
            clear_screen()
            go_to_town()
            break

        elif choice == '2':
            typewriter_print(
                "You bravely (or foolishly) dig into the stew. It’s... a culinary mystery.")
            effect = random.choice(["poison", "damage", "heal", "nothing"])
            time.sleep(1)
            clear_screen()

            if effect == "poison":
                survived = poison_damage(5, 3)
                if survived:
                    typewriter_print(
                        "Surprise! The stew was spiked. You live—somehow.")
            elif effect == "damage":
                player_damage(5)
                typewriter_print(
                    "The stew hits back. Your insides protest violently.")
            elif effect == "heal":
                player_heal(10)
                typewriter_print(
                    "Shockingly, you feel great. Maybe it *wasn't* made of swamp water.")
            else:
                typewriter_print(
                    "Nothing happens. Just your dignity slowly slipping away.")

            health_gold_name()
            time.sleep(2)
            clear_screen()

        elif choice == '3':
            typewriter_print(
                "You leave the tavern, your sanity barely intact. Smart move.")
            time.sleep(1)
            clear_screen()
            go_to_town()
            break

        else:
            typewriter_print("It's not rocket science. Pick 1, 2, or 3.")


register_tavern_function(tavern)
