from player import player, set_player_name
from utils import clear_screen, typewriter_print
import time

# Import these after defining player
from router import go_to_town
import scenes.town
import scenes.shop
import scenes.tavern


def main():
    typewriter_print("Welcome to the Space Adventure Game!")
    typewriter_print(
        "You are an astronaut on a mission to explore a distant planet.")
    typewriter_print(
        "Your goal is to collect samples and return safely to your spaceship.")
    typewriter_print("You will face various challenges along the way.")
    typewriter_print("Good luck!")
    time.sleep(2)
    clear_screen()

    player_name = input("Enter your name: ")
    time.sleep(1)
    clear_screen()
    set_player_name(player_name)
    while True:
        go_to_town()


if __name__ == "__main__":
    main()
