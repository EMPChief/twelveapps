print("🎉 Reversing your name! 🎉")

while True:
    name = input("Enter your name: ")
    if not name:
        print("You must enter a valid name. It may be the only thing that can save you.")
        continue
    

    # Print the name normally
    for i in range(len(name)):
        print(name[i], end="")
    print("\n")

    # Print the name in reverse
    print("Reversed name:")
    print(name[::-1].title())

    print("Your name is now reversed! 🎉")
    another = input(
        "Do you want to reverse another name? (yes/no): ").strip().lower()
    if another != 'yes':
        print("Goodbye! 👋")
        break
