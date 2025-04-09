print("🕵️‍♂️ Character Type Checker: Judgment Day 🕵️‍♂️")

input_string = input(
    "Enter a character to be judged mercilessly by a machine: ")

if input_string.isalpha():
    print(
        f"📚 '{input_string}' is an alphabet letter. Congratulations, it's literate. 🧠")
elif input_string.isdigit():
    print(f"🔪 '{input_string}' is a digit. Just a number in the system… like you. 🧾")
elif input_string.isalnum():
    print(f"🧬 '{input_string}' is alphanumeric. A hybrid. A glitch in the matrix. 🧟")
elif input_string.isspace():
    print(f"🌫️ You entered whitespace. Like your future if you keep doing this. ☁️")
else:
    print(f"☢️ '{input_string}' is a special character. Just like you… unstable and slightly concerning. 🧨")
