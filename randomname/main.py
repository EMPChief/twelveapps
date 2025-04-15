import random
from itertools import product

print("🎲 Random Name Generator 🎲")

name_first = ["John", "Jane", "Alex", "Emily", "Chris", "Katie", "Michael", "Sarah"]
name_last = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson"]
adjectives = ["Brave", "Clever", "Swift", "Wise", "Bold", "Gentle", "Fierce", "Kind"]


all_combinations = list(product(adjectives, name_first, name_last))
random.shuffle(all_combinations)

number_of_names = int(input("How many random names do you want to generate?: "))

number_of_names = min(number_of_names, len(all_combinations))

for i in range(number_of_names):
    adjective, first_name, last_name = all_combinations[i]
    random_name = f"{adjective} {first_name} {last_name}"
    print(f"Generated Name: {random_name}")
