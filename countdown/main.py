import time

print("=== ⏳ Welcome to the Countdown Timer! ⏳ ===")

while True:
    try:
        countdown = int(input("⏳ Enter the countdown time in seconds: "))
        if countdown <= 0:
            print("⚠️ Please enter a positive number. Try again!")
            continue
        print(f"🚀 Starting countdown from {countdown} seconds...")

        for i in range(countdown, 0, -1):
            print(f"⏰ {i} seconds remaining...")
            time.sleep(1)

        print("🎉 Time's up! 🎊 Well done!")

    except ValueError:
        print("⚠️ Invalid input. Please enter a valid number! ⛔")
        continue
    except KeyboardInterrupt:
        print("\n⛔ Countdown interrupted. Exiting... 👋")
        break

    restart = input(
        "🔄 Do you want to start another countdown? (yes/no): ").lower()
    if restart.startswith('n'):
        print("👋 Goodbye! Thanks for playing. 🎉")
        break
    elif restart != 'yes':
        print("❌ Invalid input. Exiting... ⛔")
        break
