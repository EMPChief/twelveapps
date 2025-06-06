import json
import os

path = os.path.dirname(os.path.abspath(__file__))

print("=== 🎨 Welcome to the Color Mixer, where even your creativity might be as messed up as your life choices. 🎨 ===")


def load_colors():
    try:
        with open(os.path.join(path, "color_mix.json"), "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("❌ Error: color_mix.json file not found. But hey, at least you can't blame this failure on your parents.")
        exit(1)
    except json.JSONDecodeError:
        print("❌ Error: color_mix.json file is corrupted, much like your sense of hope. Try again.")
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
            print("❌ Invalid color combination. Maybe you should stop trying to force things that don’t work. Try again.")
            continue

        print(
            f"🎨 The mixed color is: {mix}. It's not going to fix your problems, but it's something to look at.")
    except Exception as e:
        print(
            f"❌ An unexpected error occurred: {e}. Just like life. But hey, at least you're not alone in your suffering.")
    finally:
        restart = input(
            "\n🔄 Do you want to mix more colors, or just wallow in your misery? (yes/no): ").lower()
        if restart.startswith('n'):
            print("👋 Thanks for using the Color Mixer! Goodbye, and good luck with your inevitable descent into despair.")
            break
