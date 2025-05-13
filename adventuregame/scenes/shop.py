from utils.printing import typewriter_print
from router import go_to_town, register_shop_function
from player import player

def shop():
    shop_items = {
        "1": {"name": "Health Potion", "inventory": 71, "price": 10},
        "2": {"name": "Gold Bar", "inventory": 82, "price": 100},
        "3": {"name": "Space Suit", "inventory": 92, "price": 50},
        "4": {"name": "Fuel", "inventory": 107, "price": 5},
    }
    typewriter_print("Welcome to the space shop!")
    typewriter_print("Yes, the prices are ridiculous. No, we don't take coupons.")
    for key, item in shop_items.items():
        typewriter_print(f"{key}. {item['name']} (Price: {item['price']}, In stock: {item['inventory']})")
    choice = input("Enter the number of the item you want to buy (or 'q' to quit): ")
    if choice in shop_items:
        item = shop_items[choice]
        if player["gold"] >= item["price"]:
            player["gold"] -= item["price"]
            player["inventory"].append(item["name"])
            item["inventory"] -= 1
            typewriter_print(f"You bought a {item['name']}! Big spender, huh?")
        else:
            typewriter_print("Aww... not enough gold. Maybe sell a kidney?")
    elif choice.lower() == 'q':
        typewriter_print("Fine, leave. The shopkeeper didn't like you anyway.")
        go_to_town()
        return
    else:
        typewriter_print("Bold strategy. Picked an option that doesn't exist.")
        shop()


register_shop_function(shop)