import random
import time
import sys

print("=== 🪙 Welcome to the Coin Flip Execution Chamber 🪙 ===")
print("One flip. Two outcomes. Neither will save you.")

total_guesses = 0
correct_guesses = 0

while True:
    guess = input(
        "\n🧠 Heads or tails? Or type 'exit' to reject the ritual: ").lower()

    if guess == 'exit':
        print("🚪 You walk away... but the coin still spins in your dreams.")
        break
    if guess not in ['heads', 'tails']:
        print("❌ Invalid choice. But mistakes are what brought you here.")
        continue

    print("🔪 The coin is cast — destiny shudders", end="")
    for _ in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.4)
    print()

    time.sleep(1.2)
    result = random.choice(['heads', 'tails'])
    print(f"📉 The coin speaks: {result.upper()}")

    if guess == result:
        print("🫀 You live. For now. But the whispering doesn't stop.")
        correct_guesses += 1
    else:
        print("🔕 Wrong again. Another name etched in the silence.")

    total_guesses += 1

    restart = input("\n🔁 Again? (yes/no): ").lower()
    if restart == 'no':
        print("🕯️ Very well. The chamber remembers.")
        break
    elif not restart.startswith('y'):
        print("💤 Mumbled nonsense. Lights flicker. You’re gone.")
        break

print("\n=== ⚰️ Final Report ===")
print(f"📊 Rituals performed: {total_guesses}")
print(f"✅ Offerings accepted: {correct_guesses}")
if total_guesses > 0:
    accuracy = (correct_guesses / total_guesses) * 100
    print(f"📈 Survival chance: {accuracy:.2f}%. Still not enough.")
print("🪦 You leave. But something followed you home.")
