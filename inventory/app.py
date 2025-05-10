print("🌌🔫 Welcome to the Interstellar Inventory Management System 🔫🌌")

# 🚨 Cargo hold data structure 🚨
inventory_data = {
    "Cryo Bay Alpha": {"Frozen Xenon": 42, "Liquid Helium": 63},
    "Thermal Reactor Vault": {"Plasma": 12, "Stellar Ash": 5},
    "Regolith Hold": {"Moon Dust": 100, "Asteroid Fragments": 50},
    "Atmosphere Tank": {"Compressed Air": 200, "Cosmic Wind": 150},
}

def storage_exists(storage_name: str) -> bool:
    """Return True if a cargo bay isn’t lost in space (exists)."""
    return any(storage_name.lower() == bay.lower() for bay in inventory_data)


def get_cargo_bay_key(storage_name: str) -> str:
    """Case-insensitive match; or send you screaming into the void."""
    for bay in inventory_data:
        if storage_name.lower() == bay.lower():
            return bay
    raise KeyError(f"💀 ERROR: Cargo bay '{storage_name}' vanished into subspace! 💀")


def list_cargo_bay_contents(storage_name: str) -> None:
    """Print items and quantities or laugh as you realize you're stranded."""
    try:
        bay_key = get_cargo_bay_key(storage_name)
        print(f"🔍 Scanning {bay_key} for survivors… oops, I mean cargo:")
        if not inventory_data[bay_key]:
            print("   🌑 Nothing here—just like your hopes.")
        for item_name, quantity in inventory_data[bay_key].items():
            print(f"   • {item_name}: {quantity} units (may implode anytime)")
    except KeyError as error:
        print(error)


def list_all_cargo() -> None:
    """Show full interstellar inventory. Plot twist: crew already used most of it."""
    print("\n🛰️ Full Inventory Across Doomed Fleets 🛰️")
    for bay, contents in inventory_data.items():
        print(f"   {bay}:")
        if not contents:
            print("     🌌 Empty—as is your destiny.")
        for item_name, quantity in contents.items():
            print(f"     • {item_name}: {quantity}")
    print()


def add_item_to_cargo_bay(storage_name: str, item_name: str, quantity: int) -> None:
    """Load new horrors or supplies—one wrong move and you all die."""
    if storage_exists(storage_name):
        bay_key = get_cargo_bay_key(storage_name)
        inventory_data[bay_key][item_name] = quantity
        print(f"⚙️ Loaded {quantity} units of {item_name} into {bay_key}. Hope it doesn’t kill us.")
    else:
        print(f"🌪️ Can't load onto '{storage_name}'—that bay drifted off to oblivion.")


def remove_item_from_cargo_bay(storage_name: str, item_name: str) -> None:
    """Jettison cargo and watch it burn in the void."""
    try:
        bay_key = get_cargo_bay_key(storage_name)
        if item_name in inventory_data[bay_key]:
            del inventory_data[bay_key][item_name]
            print(f"🔥 Jettisoned {item_name} from {bay_key}. At least it's lonely down there.")
        else:
            print(f"☢️ You can’t jettison '{item_name}'—it decided to haunt this bay forever.")
    except KeyError as error:
        print(error)


def update_item_quantity_in_cargo_bay(storage_name: str, item_name: str, new_quantity: int) -> None:
    """Adjust cargo counts—like changing the odds of your survival."""
    try:
        bay_key = get_cargo_bay_key(storage_name)
        if item_name in inventory_data[bay_key]:
            inventory_data[bay_key][item_name] = new_quantity
            print(f"✏️ Updated {item_name} count to {new_quantity} in {bay_key}. Cool, now we're doomed by math.")
        else:
            print(f"☣️ '{item_name}' not found—you really ARE alone out here.")
    except KeyError as error:
        print(error)


def delete_cargo_bay(storage_name: str) -> None:
    """Disassemble a bay; maybe nobody was inside… maybe they were."""
    try:
        bay_key = get_cargo_bay_key(storage_name)
        del inventory_data[bay_key]
        print(f"💥 Disassembled {bay_key}. If there were survivors, they’re gone now.")
    except KeyError as error:
        print(error)


def create_cargo_bay(storage_name: str) -> None:
    """Create a new bay—congratulations, more space to die in."""
    if storage_exists(storage_name):
        print(f"⚠️ '{storage_name}' already exists. Space isn’t the only thing that’s dead here.")
    else:
        inventory_data[storage_name] = {}
        print(f"✨ Created brand-new cargo bay '{storage_name}'. Enjoy your solitude.")


def list_cargo_bay_names() -> None:
    """List all bays—so you know where you’ll meet your end."""
    print("\n📦 Available Cargo Bays (Your Final Stops):")
    for bay in inventory_data:
        print(f"   • {bay}")
    print()


def main_menu() -> None:
    while True:
        print("\n🚀🌑 Interstellar Inventory Command Deck 🌑🚀")
        print(" 1️⃣  List Cargo Bays")
        print(" 2️⃣  Show Full Inventory")
        print(" 3️⃣  Scan Cargo Bay Contents")
        print(" 4️⃣  Load or Update Cargo")
        print(" 5️⃣  Adjust Cargo Quantity")
        print(" 6️⃣  Jettison Cargo Item")
        print(" 7️⃣  Create Cargo Bay")
        print(" 8️⃣  Disassemble Cargo Bay")
        print(" 9️⃣  Initiate Self-Destruct & Exit 💥🖤")

        command = input("👨‍🚀 Enter command (1-9), if you dare: ").strip()

        if command == '1':
            list_cargo_bay_names()
        elif command == '2':
            list_all_cargo()
        elif command == '3':
            bay = input("📡 Target cargo bay: ").strip()
            list_cargo_bay_contents(bay)
        elif command == '4':
            bay = input("📦 Cargo bay: ").strip()
            item = input("📝 Cargo item: ").strip()
            qty = int(input("🔢 Units: ").strip())
            add_item_to_cargo_bay(bay, item, qty)
        elif command == '5':
            bay = input("📦 Cargo bay: ").strip()
            item = input("✏️ Item to adjust: ").strip()
            qty = int(input("🔢 New unit count: ").strip())
            update_item_quantity_in_cargo_bay(bay, item, qty)
        elif command == '6':
            bay = input("📦 Cargo bay: ").strip()
            item = input("🚮 Item to jettison: ").strip()
            remove_item_from_cargo_bay(bay, item)
        elif command == '7':
            bay = input("🆕 New cargo bay name: ").strip()
            create_cargo_bay(bay)
        elif command == '8':
            bay = input("🗑️ Bay to disassemble: ").strip()
            delete_cargo_bay(bay)
        elif command == '9':
            print("💥 Self-destruct engaged. May the vacuum take you gently. Goodbye.🖤")
            break
        else:
            print("❌ Invalid command. The void mocks your incompetence.")

if __name__ == "__main__":
    main_menu()
