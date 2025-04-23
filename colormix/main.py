import json
import os

path = os.path.dirname(os.path.abspath(__file__))

print("=== 🎨 Welcome to the Color Mixer 🎨 ===")


def load_colors():
    try:
        with open(os.path.join(path, "color_mix.json"), "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("❌ Error: color_mix.json file not found.")
        exit(1)
    except json.JSONDecodeError:
        print("❌ Error: color_mix.json file is not valid JSON.")
        exit(1)


colors = load_colors()

while True:
    try:
        color1 = input("\n🎨 Enter the first color: ").lower().strip()
        color2 = input("🎨 Enter the second color: ").lower().strip()

        key1 = f"{color1},{color2}"
        key2 = f"{color2},{color1}"

        if key1 in colors:
            mix = colors[key1]
        elif key2 in colors:
            mix = colors[key2]
        else:
            print("❌ Invalid color combination. Please try again.")
            continue

        print(f"🎨 The mixed color is: {mix}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
    finally:
        restart = input(
            "\n🔄 Do you want to mix more colors? (yes/no): ").lower()
        if restart.startswith('n'):
            print("👋 Thanks for using the Color Mixer! Goodbye!")
            break
