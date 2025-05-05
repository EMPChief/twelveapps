import random
import time
import os

class MemoryGame:
    """
    A class representing the Memory Game where the user has to memorize and
    input a sequence of numbers. The goal is to correctly input the sequence to
    earn points. If the sequence is incorrect, the user is punished by the ghost ship.
    """
    
    def __init__(self):
        """
        Initializes the MemoryGame instance, setting the initial score to 0.
        """
        self.points = 0

    def clear_screen(self):
        """
        Clears the terminal screen based on the operating system.
        On Windows, it uses 'cls', on other systems, it uses 'clear'.
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def generate_sequence(self, length=10):
        """
        Generates a random sequence of numbers between 1 and 4 of a specified length.
        
        Args:
            length (int): The length of the sequence to generate. Default is 10.
        
        Returns:
            list: A list of random integers representing the sequence.
        """
        return [random.randint(1, 4) for _ in range(length)]

    def display_sequence(self, sequence):
        """
        Displays the generated sequence on the screen for the user to memorize.
        
        Args:
            sequence (list): The sequence of numbers to display.
        """
        print("⚓🧠 Sequence of Doom: ", end="")
        for num in sequence:
            print(f"{num}️⃣", end=" ")
        print("\n☠️👁️‍🗨️ Memorize it well, ye soggy barnacle... or walk the plank! 🏴‍☠️🦑")

    def get_user_input(self):
        """
        Prompts the user to input the sequence they memorized.
        
        Returns:
            list: A list of integers representing the user's input sequence.
        """
        user_input = input("\n🧠💭 Enter yer cursed sequence (space-separated): ")
        return [int(num) for num in user_input.split()]

    def check_sequence(self, sequence, user_sequence):
        """
        Compares the user's input sequence with the correct sequence and updates the score.
        
        Args:
            sequence (list): The correct sequence.
            user_sequence (list): The sequence entered by the user.
        """
        if user_sequence == sequence:
            self.points += 1
            print("\n✅🏴‍☠️ Aye! Yer brain still works — for now...")
            print("🎉 Yer ghost crew cheers in the background... faintly. ☠️👻")
        else:
            print("\n❌💀 WRONG! Ye’ve brought shame upon the ship!")
            print(f"🪦 The correct sequence was: {' '.join(map(str, sequence))} ⚓")
            print("🗡️ May Davy Jones take pity on yer soul. Or not.")
        print(f"🪙💰 Yer cursed score be: {self.points} 🍻")

    def play_game(self):
        """
        Starts and runs the memory game. The game continues until the user interrupts
        it with a keyboard interrupt (Ctrl+C).
        """
        try:
            while True:
                self.clear_screen()
                sequence = self.generate_sequence(random.randint(3, 10))
                self.display_sequence(sequence)
                if len(sequence) == 5:
                    time.sleep(3)
                elif len(sequence) == 8:
                    time.sleep(5)
                else:
                    time.sleep(10)
                self.clear_screen()
                print("💨👀 Blinked, did ye? It's gone now! 🕳️🧊")
                user_sequence = self.get_user_input()
                self.check_sequence(sequence, user_sequence)
                print("\n⏳ Next round be comin'... if ye still draw breath 🧟‍♂️")
                time.sleep(3)
        except KeyboardInterrupt:
            print("\n⚰️🖤 Farewell, ye coward. May the sea forget yer name. 🌊💀")
        except Exception as e:
            print(f"❌💀 Uh-oh, ye've messed with the wrong ghost ship! {e}")
            print("🪦 The spirits are laughin' at yer foolishness... Better luck in the afterlife, matey. ☠️🦑")

def main():
    """
    The main function that starts the MemoryGame and runs the game loop.
    """
    print("🏴‍☠️🧟‍♂️ Welcome to the Memory Sequence of the Damned!")
    print("🎲 Survive by memory or perish like the others... Press Ctrl+C to abandon ship. 🪦🚪\n")
    game = MemoryGame()
    game.play_game()

if __name__ == "__main__":
    main()
