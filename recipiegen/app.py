import random

flavors = [
    "Citrus", "Creamy", "Earthy", "Fruity", "Garlic", "Herb",
    "Lemon", "Nutty", "Peppery", "Savory", "Smoky", "Spicy",
    "Sweet", "Tangy", "Umami", "Zesty"
]

methods = [
    "Bake", "Boil", "Grill", "Pan-fry", "Roast", "Sauté",
    "Saute", "Simmer", "Stew", "Stir-fry"
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

print("=== 🩸 Welcome to 'Last Meal Roulette' 🩸 ===")
print("🎭 The judges are hungry. You're the contestant. And the prize?")
print("⏳ A few more minutes of borrowed time.")

while True:
    random_flavor = random.choice(flavors)
    random_method = random.choice(methods)
    random_protein = random.choice(proteins)
    random_vegetable = random.choice(vegetables)
    random_carb = random.choice(carbs)

    print("\n📜 The menu written in crimson ink:")
    print(f"🧪 Flavor:    {random_flavor}")
    print(f"🧨 Method:    {random_method}")
    print(f"🧟 Protein:   {random_protein}")
    print(f"🌑 Vegetable: {random_vegetable}")
    print(f"🕸️ Carbs:     {random_carb}")
    print("🍽️ Cook fast. The voices don’t like to wait.")

    restart = input(
        "\n🔁 Dare to roll the culinary dice again? (yes/no): ").lower()
    if restart.startswith('n'):
        print("🎬 The curtain falls. Your apron is stained. Not with sauce.")
        break

print("🕯️ They liked your dish. They’ll let you wake up tomorrow.")
