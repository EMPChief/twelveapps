import random
import time
import string
import os


class MemoryChunkingGame:
    def __init__(self):
        # Initialize the chunk size and an empty list for chunks
        self.chunk_size = 3
        self.chunks = []

    def generate_chunks(self):
        """Generate one random chunk of numbers based on the current chunk_size"""
        # Generate a random string of digits of length 'chunk_size'
        chunk = ''.join(random.choices(string.digits, k=self.chunk_size))
        # Store the generated chunk in the chunks list
        self.chunks = [chunk]
        return self.chunks

    def display_chunks(self):
        """Display the generated chunk to the user with spaces between digits"""
        print("Memorize this number:")
        for chunk in self.chunks:
            # Add spaces between the digits of the chunk
            spaced_chunk = ' '.join(chunk)
            print(spaced_chunk)

        # Adjust the time to memorize based on the chunk size
        if self.chunk_size < 5:
            time.sleep(5)
        elif self.chunk_size < 7:
            time.sleep(8)
        elif self.chunk_size < 10:
            time.sleep(10)
        elif self.chunk_size < 12:
            time.sleep(12)
        elif self.chunk_size < 15:
            time.sleep(13)
        elif self.chunk_size < 20:
            time.sleep(14)
        else:
            time.sleep(15)

    def clear_screen(self):
        """Clear the console screen for a clean display"""
        # Clear the console screen depending on the operating system
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_user_input(self):
        """Prompt the user to input the number they remember"""
        return input("Enter the number you remember: ").strip()

    def play_game(self):
        """Main game loop to start and play the memory chunking game"""
        print("Memory Number Chunking Game (Press Ctrl+C to exit)")
        try:
            while True:
                # Clear screen before showing the new chunk
                self.clear_screen()
                # Generate a new chunk
                self.generate_chunks()
                # Display the chunk to the user
                self.display_chunks()
                # Clear screen after display
                self.clear_screen()
                # Get the user's guess
                user_input = self.get_user_input()

                # Check if the user's guess matches the chunk
                if user_input == self.chunks[0]:
                    print("Correct!")
                    # Increase the chunk size if the guess is correct
                    self.chunk_size += 1
                else:
                    print(
                        f"Incorrect! The correct number was: {self.chunks[0]}")
                    # Decrease the chunk size if the guess is incorrect, but not below 3
                    self.chunk_size = max(3, self.chunk_size - 1)

                print(f"Next number will have {self.chunk_size} digits.")
                time.sleep(2)
        except KeyboardInterrupt:
            print("\nThanks for playing! Exiting...")


if __name__ == "__main__":
    # Create an instance of the game and start playing
    game = MemoryChunkingGame()
    game.play_game()
