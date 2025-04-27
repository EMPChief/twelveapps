import random

print("=== 🎲 Welcome to the Unscramble the Word Game! Where laughter is just a coping mechanism. 🎲 ===")

words = [
    # Programming
    "python", "debug", "crash", "segfault",
    # Dark Humor Themes
    "regret", "taxes", "insomnia", "divorce", "therapy", "hangover",
    # Life's Little Joys
    "pizza", "coffee", "sarcasm", "doomscroll",
    # Careers
    "intern", "burnout", "deadline", "rejection",
    # Miscellaneous
    "funeral", "zombie", "existence", "mortgage", "overdraft", "capitalism"
]

while True:
    random_word = random.choice(words)
    shuffled = list(random_word)
    while True:
        random.shuffle(shuffled)
        shuffled_word = ''.join(shuffled)
        if shuffled_word != random_word:
            break

    print("\n🔀 Unscramble the letters to form a word.")
    print(f"Shuffled word: {shuffled_word}")
    user_guess = input("Your guess (as futile as it may be): ").lower()

    if user_guess == random_word:
        print("🎉 Nailed it! Too bad validation is fleeting. 🎉")
    else:
        print(
            f"❌ Nope. The correct word was: {random_word}. Just like life, you don’t get a second chance.")

    play_again = input(
        "\nPlay again and numb the pain some more? (y/n): ").lower()
    if play_again != 'y':
        print("👋 Thanks for playing. Time to stare into the abyss again. Bye.")
        break
