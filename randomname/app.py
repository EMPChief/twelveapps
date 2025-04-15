import random
from itertools import product

print("🕯️ Cursed Name Generator 🕯️")

name_first = ["Ash", "Raven", "Lucien", "Lilith", "Dorian", "Morgue", "Salem", "Nyx"]
name_last = ["Graves", "Hollow", "Dusk", "Thorne", "Vex", "Nocturne", "Bane", "Mire"]
adjectives = ["Fallen", "Broken", "Twisted", "Forgotten", "Pale", "Withered", "Nameless", "Doomed"]

all_combinations = list(product(adjectives, name_first, name_last))
random.shuffle(all_combinations)

try:
    number_of_names = int(input("How many cursed names do you dare summon?: "))
except ValueError:
    print("🪦 Invalid input. Generating one name to haunt you anyway.")
    number_of_names = 1

number_of_names = min(number_of_names, len(all_combinations))

for i in range(number_of_names):
    adjective, first_name, last_name = all_combinations[i]
    cursed_name = f"{adjective} {first_name} {last_name}"
    print(f"💀 Summoned: {cursed_name}")
