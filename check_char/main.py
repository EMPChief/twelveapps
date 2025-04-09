print("🔍 Character Type Checker 🔍")

input_string = input("Enter a character: ")

if input_string.isalpha():
    print(f"🔤 {input_string} is an alphabet. 🎉")
elif input_string.isdigit():
    print(f"🔢 {input_string} is a digit. 🎉")
elif input_string.isalnum():
    print(f"🔠 {input_string} is an alphanumeric character. 🎉")
elif input_string.isspace():
    print(f"⬜ {input_string} is a whitespace character. 🎉")
else:
    print(f"✨ {input_string} is a special character. 🎉")
