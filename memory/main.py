import random
import time
import os

class MemoryGame:
    """
    A class representing the Memory Game. The game generates a random sequence of 
    numbers, displays it briefly for the player to memorize, and then asks them to 
    input the sequence. Points are awarded for correct sequences.
    """
    
    def __init__(self):
        """
        Initializes the MemoryGame instance, setting the initial score to 0. 🎮
        """
        self.points = 0

    def clear_screen(self):
        """
        Clears the terminal screen based on the operating system.
        'cls' for Windows and 'clear' for other systems. 🧹
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def generate_sequence(self, length=10):
        """
        Generates a random sequence of numbers between 1 and 4, inclusive.
        
        Args:
            length (int): The length of the sequence to generate. Default is 10. 🔢

        Returns:
            list: A list of random integers representing the sequence. 
        """
        return [random.randint(1, 4) for _ in range(length)]

    def display_sequence(self, sequence):
        """
        Displays the generated sequence on the screen for the player to memorize. 👀
        
        Args:
            sequence (list): The sequence of numbers to display. 🧠
        """
        print("Sequence: ", end="")
        for num in sequence:
            print(num, end=" ")
        print()  # Prints a newline

    def get_user_input(self):
        """
        Prompts the user to input the sequence they memorized. ⌨️
        
        Returns:
            list: A list of integers representing the sequence entered by the user. 
        """
        user_input = input("Enter your sequence: 🧠💭 ")
        return [int(num) for num in user_input.split()]

    def check_sequence(self, sequence, user_sequence):
        """
        Compares the player's input sequence with the correct sequence.
        Updates the score based on whether the sequence is correct or not. ✔️❌
        
        Args:
            sequence (list): The correct sequence of numbers.
            user_sequence (list): The sequence entered by the player.
        """
        if user_sequence == sequence:
            self.points += 1
            print("Correct! ✅🎉")
        else:
            print("Incorrect! ❌💀")
        print(f"Your score is: {self.points} 🏆")

    def play_game(self):
        """
        Starts and runs the memory game. The game continues until interrupted. ⏳
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
                print("Blinked, did ye? It's gone now! 🕳️🧊")
                time.sleep(10)
                self.clear_screen()
                user_sequence = self.get_user_input()
                self.check_sequence(sequence, user_sequence)
                time.sleep(2)
        except KeyboardInterrupt:
            print("\nGoodbye! ⚓👋")

def main():
    """
    The main function that starts the MemoryGame and runs the game loop. 🎮
    """
    print("Memory Sequence Order Game (Press Ctrl+C to exit) ⚓🎲")
    game = MemoryGame()
    game.play_game()

if __name__ == "__main__":
    main()
