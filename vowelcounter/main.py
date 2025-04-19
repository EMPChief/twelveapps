print("🔤 Vowel Counter 🔍")

input_string = input("🎤 Enter a string to count its vowels: ")

vowels = "aeiou"
vowel_count = 0

for char in input_string:
    if char.lower() in vowels:
        vowel_count += 1

vowel_method = sum(1 for char in input_string if char.lower() in vowels)

print(f"🔤 The string you entered is: {input_string} 🎤")
print(f"🎉 The number of vowels in your string is: {vowel_count} 🎈")
print("👏 Thank you for using the Vowel Counter! Have a great day! 🌟")
print(f"Vowel method 2: {vowel_method}")