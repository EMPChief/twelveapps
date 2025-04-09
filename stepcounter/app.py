import random

print("💀 Step Counter 💀")
print("Welcome to the step counter that whispers: You're doing great. But your knees disagree.")

# Dark motivational quotes
dark_quotes = [
    "“Every step brings you closer to the inevitable… but at least you're active.” ⚰️",
    "“Keep going! Your body hasn't failed you… yet.” 🧠💥",
    "“They say movement is life. Until your joints give out.” 🦴",
    "“You're doing better than yesterday. But so is your future back pain.” 🔮",
    "“Too many steps can lead to overuse injuries. Or enlightenment. Mostly injuries.” 🏥"
]

# Sarcastic rewards
rewards = [
    "🏆 You've earned 0.0004 self-worth points! Spend them wisely.",
    "🥇 Congrats! That totally filled the void. (It didn’t.)",
    "🎖️ Achievement unlocked: ‘Not Entirely Useless Human’.",
    "💼 Reward: Delayed existential dread by 10 minutes.",
    "🎁 You win: A temporary distraction from life's meaninglessness."
]

# Fake badges
badges = [
    "🏅 Badge Unlocked: Walked Away From Responsibilities",
    "🛑 Badge Unlocked: Avoided Life Choices For 5,000 Steps",
    "👣 Badge Unlocked: Stepped On Hopes And Dreams",
    "🥾 Badge Unlocked: Outwalked Anxiety (briefly)",
    "🎭 Badge Unlocked: Pretended Walking Was A Solution"
]

# Body parts
body_parts = [
    "🦵 Your knees are filing a formal complaint.",
    "🦶 Your feet are planning a walkout. Literally.",
    "🫁 Your lungs would like to unsubscribe.",
    "🧠 Your brain says: 'Why are we like this?'",
    "🦴 Your joints are drafting their resignation letter."
]

steps = int(input("💀 Enter your step goal, because pretending you’re going somewhere is fun: "))
check_steps = int(input("💀 Enter how many steps you've taken. Overachieving may result in joint pain: "))

if check_steps >= steps:
    print(f"\n🎉 Whoa, you actually reached your goal of {steps} steps. Take a bow. Slowly. 💀")
    print(random.choice(rewards))
    print(random.choice(badges))
    print(random.choice(dark_quotes))
    if check_steps > steps * 2:
        print("⚠️ But seriously… that’s a lot of steps. One of your body parts wants to have a word.")
        print(random.choice(body_parts))
else:
    print(f"\n💔 You’ve walked {check_steps} steps out of your {steps}-step goal. You tried. Kind of.")
    remaining_steps = steps - check_steps
    print(f"🚶 You're just {remaining_steps} steps away from glory… or shin splints.")
    print(random.choice(dark_quotes))
    if check_steps > steps * 1.5:
        print("🔧 Also, you're technically under your goal, but your body still wants a break.")
        print(random.choice(body_parts))
