import random

print("🧮 A Very Simple Calculator — But With Attitude.")

addition_quotes = [
    "🔫 You add like you're stacking chips at the poker table.",
    "💸 That addition looks cleaner than a money-laundering operation.",
    "🕴️ Addition? That’s how we grow the empire."
]

subtraction_quotes = [
    "🔪 Nice subtraction. Someone just got 'cut out' of the business.",
    "🧾 That’s how you subtract problems... or witnesses.",
    "💼 Money in, problems out. Clean subtraction."
]

multiplication_quotes = [
    "💥 You multiply like we expand territories.",
    "🧠 Smart move. You know how to double the profits.",
    "💣 Multiply like you're making more soldiers for the cause."
]

division_quotes = [
    "⚖️ You divided cleaner than a territory split in Brooklyn.",
    "🍝 Careful... divide too much and someone ends up in the river.",
    "🪓 Divide and conquer, just like the old families did."
]

while True:
    try:
        operator = input(
            "Enter the operator (+, -, *, /, add, subtract, multiply, divide): ").strip().lower()
        if operator not in ('+', '-', '*', '/', 'add', 'subtract', 'multiply', 'divide'):
            print("❌ Invalid operator. Try again.")
            continue

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if operator in ('+', 'add'):
            result = num1 + num2
            print(f"The result of {num1} + {num2} is: {result}")
            print(random.choice(addition_quotes))
        elif operator in ('-', 'subtract'):
            result = num1 - num2
            print(f"The result of {num1} - {num2} is: {result}")
            print(random.choice(subtraction_quotes))
        elif operator in ('*', 'multiply'):
            result = num1 * num2
            print(f"The result of {num1} * {num2} is: {result}")
            print(random.choice(multiplication_quotes))
        elif operator in ('/', 'divide'):
            if num2 == 0:
                print("🚫 Error: Division by zero? Even the Don wouldn’t allow that.")
            else:
                result = num1 / num2
                print(f"The result of {num1} / {num2} is: {result}")
                print(random.choice(division_quotes))
    except ValueError:
        print("⚠️ Invalid input. We deal in numbers, not riddles.")
    except KeyboardInterrupt:
        print("\n🕶️ You walk away silently. Respect.")
        break
    except Exception as e:
        print(f"😬 Something went sideways: {e}")

    restart = input("🔁 Wanna do some more math deals? (yes/no): ").lower()
    if restart.startswith('n'):
        print("👋 Take care, and remember: numbers don't lie, but people do.")
        break
    elif restart != 'yes':
        print("❌ Not a clear answer... but we know how to handle confusion.")
        break
