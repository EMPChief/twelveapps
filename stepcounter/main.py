print("🏃 Step Counter 🎯")

steps = int(input("🎯 Enter your step goal: "))

check_steps = int(input("📊 Enter the number of steps you have taken: "))
if check_steps >= steps:
    print(
        f"🎉 Congratulations! You've smashed your step goal of {steps} steps! 🌟")
else:
    print(
        f"💪 Keep going! You've taken {check_steps} steps out of your goal of {steps} steps.")
    remaining_steps = steps - check_steps
    print(
        f"🚶‍♂️🚶‍♀️ You're just {remaining_steps} steps away from reaching your goal. Keep it up! 🌟")
