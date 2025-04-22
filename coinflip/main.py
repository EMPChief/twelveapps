import random
import time
import sys

print("===🎲 Welcome to the Wacky Coin Flip Challenge! 🎲===")
print("🤔 Can you beat the odds? Guess heads or tails!")

total_guesses = 0
correct_guesses = 0

while True:
    guess = input(
        "🔮 Enter your guess (heads/tails) or 'exit' to flee: ").lower()

    if guess == 'exit':
        break
    if guess not in ['heads', 'tails']:
        print("❌ Oops! That's not a valid guess. Try 'heads' or 'tails'!")
        continue

    print("🪄 The coin is spinning", end="")
    for _ in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.5)
    print()

    time.sleep(1.5)
    result = random.choice(['heads', 'tails'])
    print(f"🎉 The coin landed on: {result} 🪙")
    if guess == result:
        print("🎊 Congratulations! You guessed right! 🎉")
        correct_guesses += 1
    else:
        print("😬 Better luck next time! Keep trying! 🔄")

    total_guesses += 1

    restart = input("🔄 Do you want to play again? (yes/no): ").lower()
    if restart == 'no':
        break
    elif restart != 'yes':
        print("❌ Invalid input. Exiting the game.")
        break


print("\n=== 🧾 Game Summary ===")
print(f"📊 Total guesses: {total_guesses}")
print(f"✅ Correct guesses: {correct_guesses}")
if total_guesses > 0:
    accuracy = (correct_guesses / total_guesses) * 100
    print(f"📈 Accuracy: {accuracy:.2f}%")
print("👋 Thanks for playing! See you next time!")
