from utils.printing import typewriter_print, clear_screen
from router import go_to_shop, register_town_function
import time
def town():
    typewriter_print("You stroll into a small town. It's... charmingly suspicious.")
    typewriter_print("1. Shop - Buy items and supplies.")
    typewriter_print("2. Tavern - Overpriced rest and suspicious stew.")
    typewriter_print("3. Leave Town - Run back to your spaceship.")
    choice = input("What would you like to do? (1/2/3): ")
    if choice == '1':
        typewriter_print("Your walking to the shop looking real scared huh?")
        time.sleep(1)
        clear_screen()
        go_to_shop()
    elif choice == '2':
        # add tavern scene if it exists
        typewriter_print("The tavern is under construction.")
    elif choice == '3':
        typewriter_print("You head back to the spaceship.")
    else:
        typewriter_print("Invalid option. Not even trying, huh?")
        town()

register_town_function(town)