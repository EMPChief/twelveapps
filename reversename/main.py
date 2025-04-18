print("🎉 Reversing your name! 🎉")

while True:
    name = input("Enter your name: ")

    # Print the name normally
    for i in range(len(name)):
        print(name[i], end="")
    print("\n")

    # Print the name in reverse
    print("Reversed name:")
    reversed_name = ""
    for i in range(len(name) - 1, -1, -1):
        reversed_name += name[i]
    print(reversed_name.title())

    print("Your name is now reversed! 🎉")
    another = input(
        "Do you want to reverse another name? (yes/no): ").strip().lower()
    if another != 'yes':
        print("Goodbye! 👋")
        break
