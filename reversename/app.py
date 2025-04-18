print("🪞 Welcome to the Name Reversal Ritual 🪞")
print("Speak your name... so we may twist it backwards into the void.")

name = input("👁️ Enter your name (it may never be the same): ")

# Echo their name for the last time
print("\n 🔊 Your name, as it was once spoken:")
for i in range(len(name)):
    print(name[i], end="")
print("\n")

# Reverse it... becouse nothing every goes forward
print("🔄 Reversing your name into the abyss...")
reversed_name = ""
for i in range(len(name) - 1, -1, -1):
    reversed_name += name[i]
print(f"👻 {reversed_name.title()}")

print("🪦 Your name is now forever twisted in the void! 🪦")