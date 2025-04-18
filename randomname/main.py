import random
from itertools import product

print("🎲 Random Name Generator 🎲")

name_first = ["John", "Jane", "Alex", "Emily",
              "Chris", "Katie", "Michael", "Sarah"]
name_last = ["Smith", "Johnson", "Williams",
             "Jones", "Brown", "Davis", "Miller", "Wilson"]
adjectives = ["Brave", "Clever", "Swift",
              "Wise", "Bold", "Gentle", "Fierce", "Kind"]
before_adjectives = ["Mighty", "Fearless", "Cunning",
                     "Noble", "Valiant", "Daring", "Gallant", "Heroic"]

all_combinations = list(
    product(before_adjectives, adjectives, name_first, name_last))
random.shuffle(all_combinations)

number_of_names = int(
    input("How many random names do you want to generate?: "))

number_of_names = min(number_of_names, len(all_combinations))
if number_of_names <= 0:
    print("Please enter a positive number.")
    exit()
if number_of_names > len(all_combinations):
    print(
        f"Only {len(all_combinations)} names available. Generating all of them.")
    number_of_names = len(all_combinations)
print(f"Generating {number_of_names} random names...")
for i in range(number_of_names):
    funny_adjectives, adjective, first_name, last_name = all_combinations[i]
    random_name = f"{funny_adjectives} {adjective} {first_name} {last_name}"
    print(f"Generated Name: {random_name}")
