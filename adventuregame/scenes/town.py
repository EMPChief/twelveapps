"""Town scene implementation."""
from utils.printing import typewriter_print, clear_screen
from router import go_to_shop, register_town_function, go_to_tavern, go_to_spaceship
from player import player
import time


def town():
    """The town scene where the player can shop, eat, or regret everything."""
    while True:
        player.display_status()
        typewriter_print(
            "You stroll into a small town. It's... charmingly suspicious.")
        typewriter_print("1. Shop   - Buy stuff you probably can't afford.")
        typewriter_print(
            "2. Tavern - Overpriced rest and stew that might fight back.")
        typewriter_print("3. Ship   - Return to your trusty spaceship.")
        typewriter_print(
            "4. Leave  - Run back to your spaceship like the brave soul you are.")
        typewriter_print("5. Quit   - Leave the game and cry in a corner.")

        choice = input("What would you like to do? (1-5): ")

        if choice == '1':
            typewriter_print(
                "Marching into the shop like you're not terrified. Bold.")
            time.sleep(1)
            clear_screen()
            go_to_shop()
            break
        elif choice == '2':
            typewriter_print(
                "You head to the tavern. Bring your stomach and your will.")
            time.sleep(1)
            clear_screen()
            go_to_tavern()
            break
        elif choice == '3':
            typewriter_print("Heading back to your ship. Home sweet home.")
            time.sleep(1)
            clear_screen()
            go_to_spaceship()
            break
        elif choice == '4':
            typewriter_print("You flee the town. Heroic.")
            time.sleep(1)
            clear_screen()
            break
        elif choice == '5':
            typewriter_print(
                "You quit the game. The universe is a little less bright.")
            time.sleep(1)
            clear_screen()
            exit()
        else:
            typewriter_print("Invalid option. Did you even read the list?")
            time.sleep(1)
            clear_screen()


register_town_function(town)
