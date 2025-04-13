import random

print("🤯 Word Scrambler 🤯")
print("Welcome to the word scrambler that'll turn your words into gibberish! 😂")

while True:
    word = input("Enter a word you want to scramble (or 'done' to finish): ")
    if word.lower() == 'done':
        print("Goodbye! 👋 May your words be forever unscrambled.")
        break
    if not word.isalpha():
        print("Error: Please enter a valid word. No numbers or special characters, please. 🙅‍♂️")
        continue
    scrambled_word = ''.join(random.sample(word, len(word)))
    print(f"Scrambled word: {scrambled_word} 🤯")
    another = input(
        "Do you want to scramble another word? (yes/no): ").strip().lower()
    if another != 'yes':
        print("Goodbye! 👋 May your words always make sense.")
        break
