print("📊 Grade Average Calculator: Grim Edition 💀")

grades = []

while True:
    grade = input("Enter a grade (or 'done' to finish): 📚 ")
    if grade.lower() == 'done':
        break
    try:
        grade = float(grade)
        if 0 <= grade <= 100:
            grades.append(grade)
            print("✅ Grade added! One step closer to questioning your life choices. 🎈")
        else:
            print("🚫 Error: Invalid grade. Please enter a number between 0 and 100. Preferably not 42—unless you're into irony. 🤡")
    except ValueError:
        print("❌ Error: Invalid input. Numbers only, or 'done' if you've given up on success. 🧐")

if grades:
    average = sum(grades) / len(grades)
    print(f"🎓 Your average grade is: {average:.2f} 🎊")
    if average >= 90:
        print("🏆 Wow, look at you! You might actually have a future! For now. ☀️")
    elif average >= 75:
        print("👍 Not bad! Just enough to avoid total shame at family dinners. 🍽️")
    elif average >= 60:
        print("😬 Passing… technically. But don’t get too comfy—mediocrity is a slippery slope. 🪦")
    else:
        print(
            "💀 Yikes. Start Googling 'careers with no qualifications and lots of tears'. 🕳️")

    print(
        f"📜 Here's your grade list: {grades} — probably lower than you'd admit on a first date. 💔")
else:
    print("🤷‍♂️ No grades entered. That’s one way to avoid disappointment, I guess. ✨")

print("Goodbye! 👋 Don’t let the crushing weight of expectations hit you on the way out. 🎓💀")
