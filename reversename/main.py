print("🎉 Reversing your name! 🎉")

name = input("Enter your name: ")

# Print the name normally
for i in range(len(name)):
    print(name[i], end="")
print("\n")

print("Reversed name:")
reversed_name = ""
for i in range(len(name) - 1, -1, -1):
    reversed_name += name[i]
print(reversed_name.title())
