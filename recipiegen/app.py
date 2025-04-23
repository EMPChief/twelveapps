import random
import time

flavors = [
    "Citrus", "Creamy", "Earthy", "Fruity", "Garlic", "Herb",
    "Lemon", "Nutty", "Peppery", "Savory", "Smoky", "Spicy",
    "Sweet", "Tangy", "Umami", "Zesty"
]

methods = [
    "Bake", "Boil", "Grill", "Pan-fry", "Roast", "Sauté",
    "Simmer", "Stew", "Stir-fry"
]

proteins = [
    "Beef", "Chicken", "Fish", "Lamb", "Pork", "Sausage",
    "Shrimp", "Tofu", "Tuna", "Veggie"
]

vegetables = [
    "Asparagus", "Bell Pepper", "Broccoli", "Carrot", "Cauliflower",
    "Garlic", "Mushroom", "Onion", "Spinach", "Zucchini"
]

carbs = [
    "Barley", "Bread", "Corn", "Couscous", "Noodles",
    "Pasta", "Polenta", "Potato", "Quinoa", "Rice"
]

dark_words = [
    "Cursed", "Forgotten", "Hollow", "Wretched", "Bloodied", "Silent",
    "Forsaken", "Mourning", "Twisted", "Veiled", "Chained", "Crimson",
    "Rotten", "Haunted", "Buried", "Shattered"
]

print("=== 🩸 Welcome to 'Last Meal Roulette' 🩸 ===")
print("🎭 The judges are hungry. You're the contestant. And the prize?")
print("⏳ A few more minutes of borrowed time.")

while True:
    random_flavor = random.choice(flavors)
    random_method = random.choice(methods)
    random_protein = random.choice(proteins)
    random_vegetable = random.choice(vegetables)
    random_carb = random.choice(carbs)
    dark_1 = random.choice(dark_words)
    dark_2 = random.choice(dark_words)

    print("\n📜 The menu written in crimson ink:")
    print(f"🧪 Flavor:     {random_flavor}")
    print(f"🧨 Method:     {random_method}")
    print(f"🧟 Protein:    {dark_1} {random_protein}")
    print(f"🌑 Vegetable:  {random_vegetable}")
    print(f"🕸️ Carbs:      {dark_2} {random_carb}")
    print(
        f"🍽️ Dish Name:  '{dark_1} {random_protein}' over '{dark_2} {random_carb}' with a {random_flavor} twist")
    print("🔪 Cook fast. The voices don’t like to wait...")

    restart_input = input(
        "\n🔁 Dare to roll the culinary dice again? (yes/no/leave): ").lower()

    if restart_input.startswith('n'):
        print("\n🎬 The curtain falls. Your apron is stained. Not with sauce.")
        time.sleep(1)
        print("🩸 As you leave the kitchen, something whispers... 'See you at dinner.'")
        time.sleep(1)
        print("🔕 But no one else heard it. Not this time.")
        break
    elif restart_input.startswith('l'):
        print("\n🖤 You attempt to leave... but the door doesn’t open. No exit.")
        time.sleep(1)
        print("🪶 The walls whisper, 'You cannot leave... not yet.'")
        time.sleep(1)
    elif restart_input.startswith('y'):
        if random.random() > 0.7:
            print("\n🔮 You hear a faint voice say, 'This meal... will be your last.'")
            time.sleep(1)
        print("\n🔁 The roulette spins once more...")
    else:
        print("❌ Invalid response. It seems the game has no place for uncertainty.")
        time.sleep(1)
        print("🕳️ The darkness swallows your hesitation.")
        break

print("\n🕯️ Last Meal Roulette has ended. For you, at least.")
