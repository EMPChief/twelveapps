print("📚 Letter Grade Evaluator: Whole Class Edition 💀")

students = []

while True:
    name = input("Enter student name (or 'done' to finish): 🧑‍🎓 ")
    if name.lower() == 'done':
        break

    grade_input = input(f"Enter {name}'s grade (0–100): ")
    try:
        grade = float(grade_input)
        if 0 <= grade <= 100:
            students.append((name, grade))
            print(
                f"✅ {name}'s grade has been added. There's still hope... or not. 🕳️")
        else:
            print("🚫 Invalid grade. Should be between 0 and 100. Like expectations. 📉")
    except ValueError:
        print("❌ That's not a number. Much like your future if this keeps up. 💀")


def get_letter_grade(score):
    if score >= 90:
        return 'A', "🎓 Future CEO or villain mastermind."
    elif score >= 80:
        return 'B', "📈 Doing well. You’ll peak at middle management."
    elif score >= 70:
        return 'C', "😐 Mediocrity is comforting, isn't it?"
    elif score >= 60:
        return 'D', "🫤 Barely passing, like your will to keep going."
    else:
        return 'F', "💀 Epic fail. But hey, now you have character."


print("\n📋 Final Report Card – Class of Doom 📋\n")
total_score = 0

for name, grade in students:
    letter, comment = get_letter_grade(grade)
    print(f"{name}: {grade:.2f} ➡️ {letter} — {comment}")
    total_score += grade

if students:
    class_average = total_score / len(students)
    class_letter, class_comment = get_letter_grade(class_average)
    print("\n🏫 Class Summary 💀")
    print(
        f"Class average: {class_average:.2f} ➡️ {class_letter} — {class_comment}")
else:
    print("🤷 No students. No grades. Just silence and the echo of lost potential.")

print("\nGoodbye! 👋 May your next exam be slightly less soul-crushing. 📚🕯️")
