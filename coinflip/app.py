import random
import time
import sys

print("=== 🪙 Welcome to the Coin Flip Execution Chamber 🪙 ===")
print("Two sides. One flip. One soul. Let's begin.")

total_guesses = 0
correct_guesses = 0

while True:
    guess = input(
        "\n🧠 Heads or tails? Or type 'exit' to avoid your fate: ").lower()

    if guess == 'exit':
        print("🚪 You leave. But some doors never truly close.")
        break
    if guess not in ['heads', 'tails']:
        print("❌ Invalid input. Just like your birth, apparently.")
        continue

    print("🔪 Tossing the coin... someone's fate is sealed", end="")
    for _ in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.4)
    print()

    time.sleep(1)
    result = random.choice(['heads', 'tails'])
    print(f"📉 The verdict: {result.upper()}")

    if guess == result:
        print("🫀 You guessed right. One more breath before the darkness.")
        correct_guesses += 1
    else:
        print("🔕 Wrong. A silent bell tolls. Nobody hears it. Not even you.")

    total_guesses += 1

    restart = input("\n🔁 Play again? (yes/no): ").lower()
    if restart == 'no':
        print("🕯️ So be it. Lights out.")
        break
    elif restart != 'yes':
        print("💤 Incoherent last words. Game over.")
        break

print("\n=== ⚰️ Autopsy Report ===")
print(f"📊 Guesses made: {total_guesses}")
print(f"✅ Guesses correct: {correct_guesses}")
if total_guesses > 0:
    accuracy = (correct_guesses / total_guesses) * 100
    print(f"📈 Accuracy: {accuracy:.2f}%. Enough to fool Death once, maybe.")
print("🪦 Game complete. Cold, quiet, and forgotten. Like the rest.")
