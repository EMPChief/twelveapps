print("🎉 Text Formatter 🎉")
print("Welcome to the text formatter that won't fix your life, but hey, it's something.")

while True:
    text = input("Enter the text you want to format: ")
    if not text:
        print("Error: Please enter a valid text. Or just scream into the void, that works too.")
        continue

    print("Choose the formatting style, because why not make your meaningless words look fancy:")
    print("1. Uppercase 🔊 (LIKE YOU'RE SHOUTING INTO THE ABYSS)")
    print("2. Lowercase 🗣️ (like your will to live)")
    print("3. Title Case 👑 (because every tragedy deserves a title)")
    print("4. Sentence Case 📝 (for when you want to sound *just* sane enough)")

    try:
        choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        print(
            "Error: Please enter a number. Math might not save you, but it's still a rule.")
        continue

    if choice < 1 or choice > 4:
        print("Error: That's not a valid option. But then again, neither is life.")
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
        print("Goodbye! 👋 May your text be better formatted than your decisions.")
        break
