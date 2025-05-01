import random
import time
import string
import os


class MemoryChunkingGame:
    def __init__(self):
        self.chunk_size = 3
        self.chunks = []

    def generate_chunks(self):
        """Generate one random chunk of numbers with current chunk_size"""
        chunk = ''.join(random.choices(string.digits, k=self.chunk_size))
        self.chunks = [chunk]
        return self.chunks

    def display_chunks(self):
        """Display the chunk to the user with spaces between digits"""
        print("Memorize this number:")
        for chunk in self.chunks:
            spaced_chunk = ' '.join(chunk)
            print(spaced_chunk)
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
        """Clear the console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_user_input(self):
        """Get the user's guess"""
        return input("Enter the number you remember: ").strip()

    def play_game(self):
        """Main game loop"""
        print("Memory Number Chunking Game (Press Ctrl+C to exit)")
        try:
            while True:
                self.clear_screen()
                self.generate_chunks()
                self.display_chunks()
                self.clear_screen()
                user_input = self.get_user_input()

                if user_input == self.chunks[0]:
                    print("Correct!")
                    self.chunk_size += 1
                else:
                    print(
                        f"Incorrect! The correct number was: {self.chunks[0]}")
                    self.chunk_size = max(3, self.chunk_size - 1)

                print(f"Next number will have {self.chunk_size} digits.")
                time.sleep(2)
        except KeyboardInterrupt:
            print("\nThanks for playing! Exiting...")


if __name__ == "__main__":
    game = MemoryChunkingGame()
    game.play_game()
