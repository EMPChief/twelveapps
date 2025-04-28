import random
import time

print("=== 🎲 Welcome to the Guessing Number Game! 🎲 ===")

while True:
    get_random = random.randint(1, 100)
    attempts = 0
    print("🕵️‍♂️ Try to guess the number I'm thinking of between 1 and 100!")
    print("You have 10 attempts to guess the number. Good luck! 🍀")

    start_time = time.time()

    for attempt in range(10):
        try:
            guess_number = int(input(f"Attempt {attempt + 1}: Enter your guess: "))
        except ValueError:
            print("⚠️ Invalid input! Please enter a number.")
            continue
        
        attempts += 1
        if guess_number < get_random:
            print("📉 Too low! Try again.")
        elif guess_number > get_random:
            print("📈 Too high! Try again.")
        else:
            end_time = time.time()
            total_time = end_time - start_time
            print(f"🎉 Congratulations! You've guessed the number {get_random} in {attempts} attempts! 🎊")
            print(f"⏱️ It took you {total_time:.2f} seconds.")
            break
    else:
        end_time = time.time()
        total_time = end_time - start_time
        print(f"❌ Sorry, you've used all 10 attempts! The number was {get_random}.")
        print(f"⏱️ Total time spent guessing: {total_time:.2f} seconds.")

    restart = input("🔄 Do you want to play again? (yes/no): ").lower()
    if restart.startswith('n'):
        print("👋 Thanks for playing! Goodbye!")
        break
    elif restart != 'yes':
        print("❌ Invalid input. Exiting the game.")
        break
