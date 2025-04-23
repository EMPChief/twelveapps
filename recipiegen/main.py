# Flavor - Method - Protein - Vegetable - Carbs
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

print("=== 🍽️ Welcome to the Recipe Generator! 🍽️ ===")

while True:
    random_flavor = random.choice(flavors)
    random_method = random.choice(methods)
    random_protein = random.choice(proteins)
    random_vegetable = random.choice(vegetables)
    random_carb = random.choice(carbs)

    print("\n=== 🥘 Your Random Recipe Idea: ===")
    print(f"🌶️ Flavor:    {random_flavor}")
    print(f"🔥 Method:    {random_method}")
    print(f"🍗 Protein:   {random_protein}")
    print(f"🥦 Vegetable: {random_vegetable}")
    print(f"🍞 Carbs:     {random_carb}")

    restart = input(
        "\n🔄 Do you want to generate another recipe? (yes/no): ").lower()
    if restart.startswith('n'):
        break

print("👋 Thanks for using the Recipe Generator! Happy cooking! 🍳")
