import random
import time

print("=== ⏳ Welcome to the Countdown Timer... Your Final Countdown. ⏳ ===")


random_quotes = [
    "⏰ Time waits for no one... but it sure likes to make you wait.",
    "⏰ Every second you waste is another chance for regret.",
    "⏰ You’re running out of time, but you’ll never outrun your past.",
    "⏰ Tick tock... you can feel it, can’t you? The inevitability.",
    "⏰ Time’s a thief, and it’s stealing your chances.",
    "⏰ We all have an expiration date. Yours is just a little closer.",
    "⏰ You’re closer to your doom with each passing second.",
    "⏰ The clock’s your enemy. It never stops. It never cares.",
    "⏰ The more you waste, the less you have left. Sounds familiar?",
    "⏰ You can hear the clock, can’t you? It’s laughing at you.",
    "⏰ Every second that ticks by is one you’ll never get back. Welcome to the end.",
    "⏰ Remember: Time's a cruel mistress. She’s got no mercy for you.",
    "⏰ Not even time can save you now.",
    "⏰ Keep watching the clock. It’s the only thing that knows when you’ll fail.",
    "⏰ The only thing certain is that you’re closer to your end... one second at a time.",
    "⏰ The clock doesn’t lie. It’s telling you that you’re out of time.",
    "⏰ The more time you waste, the less time you have to redeem yourself.",
    "⏰ Time's like a bullet... it’ll find you eventually, whether you’re ready or not.",
    "⏰ Enjoy the countdown. It’s the only thing that’s counting down to something.",
    "⏰ The end is closer than you think. The clock knows."
    "⏰ Time is a relentless beast, and it’s hungry for your mistakes.",
]

while True:
    try:
        countdown = int(
            input("⏳ Enter the countdown time in seconds. Hurry, you’re already late. "))
        if countdown <= 0:
            print(
                "⚠️ C’mon, give me something real. Time’s a luxury you don’t have. Try again.")
            continue
        print(f"🚀 Starting countdown from {countdown} seconds...")

        for i in range(countdown, 0, -1):
            if i == 10:
                print(
                    "⏰ 10 seconds remaining... You have 10 seconds to change your destiny.")
            elif i == 5:
                print(
                    "⏰ 5 seconds remaining... The clock is ticking, but you can't outrun your fate.")
            elif i == 3:
                print("⏰ 3 seconds remaining... Feels like the end is near, doesn’t it?")
            elif i == 1:
                print(
                    "⏰ 1 second remaining... Make it count. Or don’t. It’s all the same.")
            else:
                print(
                    f"⏰ {i} seconds remaining... {random.choice(random_quotes)}")
            time.sleep(1)

        print("🎉 Time's up! 🎊 You made it... for now. But this ain't over.")

    except ValueError:
        print(
            "⚠️ Invalid input. Was that a cry for help? Maybe you need more than a timer. ⛔")
        continue
    except KeyboardInterrupt:
        print("\n⛔ Countdown interrupted. Exiting... 👋 You were always meant to fail.")
        break

    restart = input(
        "🔄 Do you want to start another countdown? Or are you running from your fate? (yes/no): ").lower()
    if restart.startswith('n'):
        print("👋 Goodbye. I don’t think you’ll find peace. 🎉")
        break
    elif restart != 'yes':
        print("❌ Invalid input. It doesn’t matter. We all end up in the same place. ⛔")
        break
