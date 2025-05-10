print("🧮 Inventory Management System")

inventory_data = {
    "Ice Storage": {"Ice": 42, "Water": 63},
    "Fire Storage": {"Fire": 12, "Lava": 5},
    "Earth Storage": {"Earth": 100, "Rock": 50},
    "Air Storage": {"Air": 200, "Wind": 150},
}

def storage_exists(storage_name: str) -> bool:
    """Return True if a storage unit with the given name exists."""
    return any(storage_name.lower() == key.lower() for key in inventory_data)


def get_storage_key(storage_name: str) -> str:
    """Return the canonical storage key matching the given name (case-insensitive)."""
    for key in inventory_data:
        if storage_name.lower() == key.lower():
            return key
    raise KeyError(f"❌ Storage '{storage_name}' not found")


def list_storage_items(storage_name: str) -> None:
    """Print all items and their quantities in the specified storage unit."""
    try:
        canonical_key = get_storage_key(storage_name)
        print(f"📦 Items in {canonical_key}:")
        for item_name, quantity in inventory_data[canonical_key].items():
            print(f"  • {item_name}: {quantity}")
    except KeyError as error:
        print(error)


def list_all_inventory() -> None:
    """Print the full inventory of all storage units."""
    print("\n📚 Full Inventory:")
    for storage_name, contents in inventory_data.items():
        print(f"  {storage_name}:")
        for item_name, quantity in contents.items():
            print(f"    • {item_name}: {quantity}")
    print()


def add_item_to_storage(storage_name: str, item_name: str, quantity: int) -> None:
    """Add or overwrite an item with the given quantity in the specified storage."""
    if storage_exists(storage_name):
        canonical_key = get_storage_key(storage_name)
        inventory_data[canonical_key][item_name] = quantity
        print(f"✅ Added/Updated {quantity} x {item_name} in {canonical_key}.")
    else:
        print(f"❌ Storage '{storage_name}' does not exist.")


def remove_item_from_storage(storage_name: str, item_name: str) -> None:
    """Remove an item from the specified storage unit."""
    try:
        canonical_key = get_storage_key(storage_name)
        if item_name in inventory_data[canonical_key]:
            del inventory_data[canonical_key][item_name]
            print(f"🗑️ Removed {item_name} from {canonical_key}.")
        else:
            print(f"❌ Item '{item_name}' not found in {canonical_key}.")
    except KeyError as error:
        print(error)


def update_item_quantity(storage_name: str, item_name: str, new_quantity: int) -> None:
    """Update the quantity of an existing item in the specified storage."""
    try:
        canonical_key = get_storage_key(storage_name)
        if item_name in inventory_data[canonical_key]:
            inventory_data[canonical_key][item_name] = new_quantity
            print(f"✏️ Set {item_name} quantity to {new_quantity} in {canonical_key}.")
        else:
            print(f"❌ Item '{item_name}' not found in {canonical_key}.")
    except KeyError as error:
        print(error)


def delete_storage(storage_name: str) -> None:
    """Remove an entire storage unit from the inventory."""
    try:
        canonical_key = get_storage_key(storage_name)
        del inventory_data[canonical_key]
        print(f"🗑️ Deleted storage unit: {canonical_key}.")
    except KeyError as error:
        print(error)


def create_storage(storage_name: str) -> None:
    """Create a new storage unit with no items."""
    if storage_exists(storage_name):
        print(f"❗ Storage '{storage_name}' already exists.")
    else:
        inventory_data[storage_name] = {}
        print(f"🆕 Created new storage unit: {storage_name}.")


def list_storage_names() -> None:
    """Print the names of all available storage units."""
    print("\n📦 Available Storages:")
    for storage_name in inventory_data:
        print(f"  • {storage_name}")
    print()


def main_menu() -> None:
    while True:
        print("\n📁 Inventory Management Menu:")
        print(" 1️⃣  List Storage Units")
        print(" 2️⃣  Show Full Inventory")
        print(" 3️⃣  View Storage Contents")
        print(" 4️⃣  Add or Update Item")
        print(" 5️⃣  Change Item Quantity")
        print(" 6️⃣  Remove Item")
        print(" 7️⃣  Create Storage Unit")
        print(" 8️⃣  Delete Storage Unit")
        print(" 9️⃣  Exit")

        user_choice = input("👉 Select an option (1-9): ").strip()

        if user_choice == '1':
            list_storage_names()
        elif user_choice == '2':
            list_all_inventory()
        elif user_choice == '3':
            storage_name = input("📦 Enter storage name: ").strip()
            list_storage_items(storage_name)
        elif user_choice == '4':
            storage_name = input("📦 Storage name: ").strip()
            item_name = input("📝 Item name: ").strip()
            quantity = int(input("🔢 Quantity: ").strip())
            add_item_to_storage(storage_name, item_name, quantity)
        elif user_choice == '5':
            storage_name = input("📦 Storage name: ").strip()
            item_name = input("✏️ Item to update: ").strip()
            new_quantity = int(input("🔢 New quantity: ").strip())
            update_item_quantity(storage_name, item_name, new_quantity)
        elif user_choice == '6':
            storage_name = input("📦 Storage name: ").strip()
            item_name = input("🗑️ Item to remove: ").strip()
            remove_item_from_storage(storage_name, item_name)
        elif user_choice == '7':
            storage_name = input("🆕 New storage name: ").strip()
            create_storage(storage_name)
        elif user_choice == '8':
            storage_name = input("🗑️ Storage name to delete: ").strip()
            delete_storage(storage_name)
        elif user_choice == '9':
            print("👋 Goodbye!")
            break
        else:
            print("❗ Invalid choice. Please select 1-9.")

if __name__ == "__main__":
    main_menu()