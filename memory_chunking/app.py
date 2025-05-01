import random
import time
import string
import os


class MemoryChunkingGame:
    # Initialize chunk size and list of chunks
    def __init__(self):
        self.chunk_size = 3
        self.chunks = []

        # Define different themes with dark humor and mafia humor
        self.themes = {
            'mafia': {
                'intro': "🎲 Welcome to Don Vito’s Memory Test (Ctrl+C to chicken out)",
                'capisce': "🕶️ Memorize this number, capisce?",
                'get_input': "🔎 Spill the digits you remember before the boss gets angry: ",
                'correct': "💵 Correct! You might just earn yourself some respect.",
                'incorrect': "💀 Wrong! The number was: {0}. Don’t disappoint the family again.",
                'progress': "👑 You’re making some real progress, you’re looking like a real wise guy.",
                'inner_circle': "🎩 Ooh, you’re starting to look like you belong in the inner circle.",
                'don_watching': "💼 The Don might just be watching you now, stay sharp!",
                'close_boss': "🚨 You're close to crossing into boss territory... don’t mess it up!",
                'next_chunk': "📈 Next number’s got {0} digits. Don’t screw it up.",
                'exit': "👋 You walked away... hope the Don doesn't find out.",
                'error': "⚠️ Something went wrong, and it wasn’t a simple mistake. The Don's gonna be mad. Error: {0}"
            },
            'dark_humor': {
                'intro': "🎲 Welcome to the Dark Humor Memory Challenge (Ctrl+C to bail out)",
                'capisce': "🕶️ Memorize this number, if you can.",
                'get_input': "🔎 Type the digits you remember, or just give up.",
                'correct': "💵 Wow, you actually got it right. Unbelievable.",
                'incorrect': "💀 Wrong! You fail. The number was: {0}. Too bad!",
                'progress': "👑 Oh, you're getting better... Or maybe you're just lucky.",
                'inner_circle': "🎩 You're starting to do okay... I guess.",
                'don_watching': "💼 Your progress is under scrutiny. Don't screw it up!",
                'close_boss': "🚨 You're on the edge. One more slip and you're done.",
                'next_chunk': "📈 Get ready, next number's got {0} digits. Hope you remember...",
                'exit': "👋 You quit. Weak. Hope you can sleep tonight.",
                'error': "⚠️ Whoops, something went wrong... but who cares, really? Error: {0}"
            },
            'olympic_god': {
                'intro': "🏅 Welcome to the Olympian Memory Trials (Ctrl+C to bow out)",
                'capisce': "🏆 Memorize this number, mortal.",
                'get_input': "🔮 Enter the number you remember, or face the wrath of the gods.",
                'correct': "🌟 Correct! You have earned the favor of the gods.",
                'incorrect': "⚡ Wrong! The number was: {0}. You have angered the gods.",
                'progress': "⚔️ Your strength increases, mere mortal.",
                'inner_circle': "🛡️ You’re gaining divine favor, soon you may be immortal.",
                'don_watching': "🗡️ The gods are watching. Fail and feel their wrath.",
                'close_boss': "🔥 You’re about to face Zeus himself. Don’t mess it up.",
                'next_chunk': "📜 Prepare yourself, the next number has {0} digits.",
                'exit': "🌪️ You fled the trial. No god will remember you.",
                'error': "🌑 Something went wrong, and now the gods are displeased. Error: {0}"
            },
            'space_odyssey': {
                'intro': "🚀 Welcome to the Space Odyssey Memory Game (Ctrl+C to jump to hyperspace)",
                'capisce': "🛸 Memorize this alien code.",
                'get_input': "🛸 Enter the code before the ship's AI kicks you out.",
                'correct': "💫 Correct! You’ve just passed the space test.",
                'incorrect': "💥 Wrong! The code was: {0}. You’ve been ejected into space.",
                'progress': "🌌 Your neural networks are growing, astronaut.",
                'inner_circle': "🌠 You’re gaining access to higher space command.",
                'don_watching': "🌍 The AI is watching. One wrong move, and you're lost in space.",
                'close_boss': "🪐 You’re about to face the Galactic Council. Good luck.",
                'next_chunk': "🚀 The next code has {0} digits. Can you remember it?",
                'exit': "🛸 You’ve abandoned the mission. No one will remember you.",
                'error': "🌑 The AI failed. Something went wrong in the system. Error: {0}"
            },
            'pirate': {
                'intro': "🏴‍☠️ Welcome to the Pirate Memory Test (Ctrl+C to abandon ship)",
                'capisce': "⚓ Memorize this number, ye scallywag!",
                'get_input': "💀 Enter the number before the Kraken gets ye!",
                'correct': "💰 Correct! Yer startin’ to earn some gold.",
                'incorrect': "☠️ Wrong! The number was: {0}. Walk the plank!",
                'progress': "⚔️ Yer gettin’ better, ye might just become a captain one day.",
                'inner_circle': "🏴‍☠️ Ye be on yer way to the captain’s quarters, matey.",
                'don_watching': "💣 The crew’s watchin’. Don’t make a fool of yerself!",
                'close_boss': "🏴‍☠️ Ye be close to become a true pirate lord. Arrr!",
                'next_chunk': "📜 The next number has {0} digits. Remember it, or ye be sorry.",
                'exit': "⚓ Ye deserted the ship! Hope ye don't mind walking the plank.",
                'error': "⚔️ Something went wrong, and ye'll face the consequences, pirate. Error: {0}"
            }
        }

        # Randomly choose a theme from the available themes
        self.current_theme = random.choice(list(self.themes.keys()))
        print(f"🎮 You are playing under the '{self.current_theme}' theme!")

    # Generate one random chunk of numbers with the current chunk size
    def generate_chunks(self):
        chunk = ''.join(random.choices(string.digits, k=self.chunk_size))
        self.chunks = [chunk]  # Store the chunk in a list
        return self.chunks

    # Display the chunk to the user with spaces between digits
    def display_chunks(self):
        print(self.themes[self.current_theme]['capisce'])
        for chunk in self.chunks:
            spaced_chunk = ' '.join(chunk)
            print(f"📟 {spaced_chunk}")
        time.sleep(self.chunk_size)

    # Clear the console screen
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # Get the user's guess
    def get_user_input(self):
        print(self.themes[self.current_theme]['get_input'])
        return input().strip()

    # Main game loop
    def play_game(self):
        print(self.themes[self.current_theme]['intro'])
        try:
            while True:
                # Clear the screen, generate and display new chunks
                self.clear_screen()
                self.generate_chunks()
                self.display_chunks()
                self.clear_screen()

                # Get user input and check if it's correct
                user_input = self.get_user_input()

                if user_input == self.chunks[0]:
                    # Correct input message
                    print(self.themes[self.current_theme]['correct'])
                    self.chunk_size += 1 
                else:
                    # Incorrect input message
                    print(self.themes[self.current_theme]
                          ['incorrect'].format(self.chunks[0]))
                    # Decrease chunk size (minimum size is 3)
                    self.chunk_size = max(3, self.chunk_size - 1)

                # Progress-based messages
                if self.chunk_size > 5:
                    print(self.themes[self.current_theme]['progress'])
                elif self.chunk_size > 7:
                    print(self.themes[self.current_theme]['inner_circle'])
                elif self.chunk_size > 10:
                    print(self.themes[self.current_theme]['don_watching'])
                elif self.chunk_size > 12:
                    print(self.themes[self.current_theme]['close_boss'])

                # Message for the next chunk of numbers
                print(self.themes[self.current_theme]
                      ['next_chunk'].format(self.chunk_size))
                time.sleep(2)

        except KeyboardInterrupt:
            print(self.themes[self.current_theme]['exit'])
        except Exception as e:
            print(self.themes[self.current_theme]['error'].format(e))


if __name__ == "__main__":
    # Instantiate the game and start playing
    game = MemoryChunkingGame()
    game.play_game()
