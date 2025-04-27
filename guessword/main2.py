import random

print("=== 🎲 Welcome to the Unscramble the Word Game! 🎲 ===")
words = [
    # Programming
    "python", "java", "javascript", "ruby", "html", "css",
    # Animals
    "elephant", "giraffe", "penguin", "kangaroo",
    # Food
    "pizza", "sushi", "banana", "chocolate",
    # Sports
    "soccer", "tennis", "cricket",
    # Technology
    "robot", "internet", "smartphone",
    # Geography
    "desert", "island", "mountain",
    # Miscellaneous
    "puzzle", "guitar", "rocket"
]

while True:
    random_word = random.choice(words)
    shuffled = list(random_word)
    while True:
        random.shuffle(shuffled)
        shuffled_word = ''.join(shuffled)
        if shuffled_word != random_word:
            break

    print("\n🔀 Unscramble the letters to form a word:")
    print("Shuffled word: ", shuffled_word)
    user_guess = input("Your guess: ").lower()

    if user_guess == random_word:
        print("🎉 Correct! You unscrambled the word! 🎉")
    else:
        print(f"❌ Nope! The correct word was: {random_word}")

    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again != 'y':
        print("👋 Thanks for playing!")
        break
