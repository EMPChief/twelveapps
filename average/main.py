print("📊 Grade Average Calculator: Happy Edition 🌟")

grades = []

while True:
    grade = input("Enter a grade (or 'done' to finish): 📚 ")
    if grade.lower() == 'done':
        break
    try:
        grade = float(grade)
        if 0 <= grade <= 100:
            grades.append(grade)
            print("✅ Great job! You're doing awesome — keep it going! 🎉")
        else:
            print("🚫 Oops! Please enter a number between 0 and 100. You’ve got this! 💪")
    except ValueError:
        print("❌ That doesn’t seem right. Try entering a number or type 'done' when you're finished. 🌼")

if grades:
    average = sum(grades) / len(grades)
    print(f"\n🎓 Your average grade is: {average:.2f} 🎊")
    if average >= 90:
        print("🏆 Incredible! You’re shining like a star! Keep reaching for the top! 🌠")
    elif average >= 75:
        print("🌟 Great work! You're on the right track — keep that momentum going! 🚀")
    elif average >= 60:
        print("😊 You passed! Every step forward counts — let’s keep improving! 🧠✨")
    else:
        print("🌱 Don’t worry — progress takes time. You’ve already taken the first step, and that’s amazing! 💖")
else:
    print("\n🤷‍♂️ No grades entered. No worries — every journey starts somewhere! 🌈")


print(f"Here is your grade list: {grades} 📜")
print("Goodbye! 👋 Keep smiling, keep learning, and believe in yourself! 💫🎉")

