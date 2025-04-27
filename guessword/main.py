import random

print("=== 🎲 Welcome to the Guess the Word Game! 🎲 ===")
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
    guessed_letters = []
    attempts = 6
    word_display = "_" * len(random_word)
    print("\n=== 🕵️‍♂️ Let's start guessing! ===")
    print(f"Word to guess: {word_display}")
    print(f"Attempts left: {attempts}")
    print("Guessed letters: ", end="")
    print(", ".join(guessed_letters) if guessed_letters else "None")
    print("")

    while attempts > 0:
        guess = input("Enter a letter: ").lower()
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        guessed_letters.append(guess)
        if guess in random_word:
            for i in range(len(random_word)):
                if random_word[i] == guess:
                    word_display = word_display[:i] + \
                        guess + word_display[i + 1:]
            print(f"Word to guess: {word_display}")
            print(f"Attempts left: {attempts}")
            print("Guessed letters: ", end="")
            print(", ".join(guessed_letters))
            print("")
            if word_display == random_word:
                print(
                    f"🎉 Congratulations! You've guessed the word: {random_word} 🎉")
                break
        else:
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}")
            print("Guessed letters: ", end="")
            print(", ".join(guessed_letters))
            print("")
    if attempts == 0:
        print(
            f"💔 Sorry, you've run out of attempts. The word was: {random_word} 💔")
