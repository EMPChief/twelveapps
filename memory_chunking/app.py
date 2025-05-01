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
        print("🕶️ Memorize this number, capisce?")
        for chunk in self.chunks:
            spaced_chunk = ' '.join(chunk)
            print(f"📟 {spaced_chunk}")
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
        return input("🔎 Spill the digits you remember before the boss gets angry: ").strip()

    def play_game(self):
        """Main game loop"""
        print("🎲 Welcome to Don Vito’s Memory Test (Ctrl+C to chicken out)")
        try:
            while True:
                self.clear_screen()
                self.generate_chunks()
                self.display_chunks()
                self.clear_screen()
                user_input = self.get_user_input()

                if user_input == self.chunks[0]:
                    print("💵 Correct! You might just earn yourself some respect.")
                    self.chunk_size += 1
                else:
                    print(
                        f"💀 Wrong! The number was: {self.chunks[0]}. Don’t disappoint the family again.")
                    self.chunk_size = max(3, self.chunk_size - 1)

                if self.chunk_size > 5:
                    print(
                        "👑 You’re making some real progress, you’re looking like a real wise guy.")
                elif self.chunk_size > 7:
                    print(
                        "🎩 Ooh, you’re starting to look like you belong in the inner circle.")
                elif self.chunk_size > 10:
                    print("💼 The Don might just be watching you now, stay sharp!")
                elif self.chunk_size > 12:
                    print(
                        "🚨 You're close to crossing into boss territory... don’t mess it up!")

                print(
                    f"📈 Next number’s got {self.chunk_size} digits. Don’t screw it up.")
                time.sleep(2)

        except KeyboardInterrupt:
            print("\n👋 You walked away... hope the Don doesn't find out.")
        except Exception as e:
            print(
                f"⚠️ Something went wrong, and it wasn’t a simple mistake. The Don's gonna be mad. Error: {e}")


if __name__ == "__main__":
    game = MemoryChunkingGame()
    game.play_game()
