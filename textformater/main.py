print("🎉 Text Formatter 🎉")

while True:
    text = input("Enter the text you want to format: ")
    if not text:
        print("Error: Please enter a valid text.")
        continue
    print("Choose the formatting style:")
    print("1. Uppercase 🔊")
    print("2. Lowercase 🗣️")
    print("3. Title Case 👑")
    print("4. Sentence Case 📝")

    try:
        choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Error: Please enter a number.")
        continue

    if choice < 1 or choice > 4:
        print("Error: Please enter a number between 1 and 4.")
        continue

    formated_text = {
        1: text.upper(),
        2: text.lower(),
        3: text.title(),
        4: text.capitalize(),
    }[choice]

    print(f"Formatted text: {formated_text}")
    another = input(
        "Do you want to format another text? (yes/no): ").strip().lower()
    if another != 'yes':
        print("Goodbye! 👋")
        break
