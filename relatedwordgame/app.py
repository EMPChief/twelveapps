import time
import random

print("🎯 Welcome to the Mafia-Themed Word Game 🎯")

# Mafia-themed words
related_words = {
    "car": ["vehicle", "automobile", "engine", "tires", "drive", "garage", "steering", "road"],
    "dog": ["pet", "bark", "canine", "tail", "walk", "leash", "fetch", "loyal"],
    "computer": ["keyboard", "mouse", "monitor", "software", "hardware", "CPU", "internet", "code"],
    "book": ["pages", "author", "reading", "chapter", "library", "fiction", "nonfiction", "cover"],
    "music": ["song", "melody", "notes", "rhythm", "band", "instrument", "lyrics", "beat"],
    "movie": ["film", "actor", "director", "cinema", "screenplay", "scenes", "ticket", "trailer"],
    "travel": ["trip", "journey", "flight", "passport", "hotel", "explore", "adventure", "destination"],
    "sports": ["game", "team", "athlete", "coach", "score", "competition", "trophy", "practice"],
    "food": ["meal", "snack", "recipe", "flavor", "kitchen", "cook", "taste", "dinner"],
    "phone": ["call", "text", "contact", "ring", "smartphone", "apps", "screen", "battery"],
    "school": ["teacher", "student", "homework", "classroom", "subject", "exam", "desk", "lesson"],
    "nature": ["tree", "river", "mountain", "wildlife", "forest", "sky", "flowers", "rocks"],
    "science": ["experiment", "lab", "microscope", "research", "biology", "chemistry", "physics", "data"],
    "history": ["past", "event", "war", "timeline", "civilization", "king", "revolution", "ancient"],
    "art": ["painting", "drawing", "gallery", "sculpture", "canvas", "artist", "brush", "color"],
    "fashion": ["style", "clothing", "runway", "model", "trend", "designer", "fabric", "outfit"],
    "coffee": ["caffeine", "mug", "brew", "espresso", "bean", "latte", "café", "roast"],
    "city": ["urban", "building", "traffic", "crowd", "downtown", "skyscraper", "street", "metro"],
    "internet": ["website", "browser", "online", "email", "search", "social", "network", "streaming"],
    "beach": ["sand", "waves", "ocean", "sun", "swim", "shells", "surf", "relax"],
    "shiny space": ["stars", "planets", "galaxy", "universe", "cosmos", "black hole", "nebula", "asteroid"]
}

# Mafia quotes for each outcome
mafia_quotes = [
    "❌ Wrong guess, you got more chance of surviving a drive-by in the Bronx.",
    "❌ You think you’re a wise guy? That guess was more of a joke than our accountant.",
    "❌ You made a mistake that no one walks away from. Not in this business.",
    "❌ You’re as wrong as a rat in the family’s pasta pot.",
    "❌ Guess again, or we'll throw you in the trunk for a while.",
    "❌ You think this is a game? That guess? It’s a death sentence, kid.",
    "❌ What you just said is worse than what we did to Johnny Two-Times last week.",
    "❌ You’re playing with fire here, pal. This guess won’t save you from the fallout.",
    "❌ You’ve got the brains of a broken jukebox, kid.",
    "❌ You’re not even close, but I’ll give you credit for not running your mouth like a rookie."
]

points = 0

while True:
    try:
        # Pick a random topic from the mafia-themed list
        random_word = random.choice(list(related_words.keys()))

        # Start the timer
        start_seconds = time.time()

        # Mafia-style prompt
        guess_word = input(
            f"\nAlright, wise guy... guess a related word for '{random_word.title()}' (or type 'exit' to quit): "
        ).strip().lower()

        # Exit condition
        if guess_word == "exit":
            print("\nYou ain't got the guts to keep going? Alright, I see how it is. Goodbye!")
            break

        # Check the user's guess
        normalized_related = [word.lower() for word in related_words[random_word]]
        if guess_word in normalized_related:
            finished_seconds = time.time()
            time_taken = finished_seconds - start_seconds

            print(f"✅ Correct! '{guess_word}' is related to '{random_word}'.")
            print(f"⏱️ You took {time_taken:.2f} seconds.")

            # Mafia-style scoring based on response time
            if time_taken < 2:
                points += 5
                print("🔥 That’s how a real made man handles business! You earned 5 points.")
            elif time_taken < 3:
                points += 4
                print("👍 Not bad, not bad at all. You earned 4 points.")
            elif time_taken < 4:
                points += 3
                print("🙂 You’re getting the hang of it, but it ain’t perfect. 3 points.")
            elif time_taken < 5:
                points += 2
                print("😐 I’m not impressed, but here’s 2 points. Don’t waste my time.")
            elif time_taken < 10:
                points += 1
                print("😅 You’re barely getting by. 1 point, but don’t make me regret it.")
            else:
                print("🕓 You’ve just cost yourself a seat at the table. 0 points, kid.")

        else:
            print(f"❌ Wrong guess, you got more chance of surviving a drive-by in the Bronx.")

        print(f"🏆 Total points: {points} — Don’t make me count any more than this.")

    except KeyboardInterrupt:
        print("\nOh, you wanna quit? That’s fine. We don’t take kindly to quitters... 👋")
        break
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")
        break

    # Mafia-style prompt to play again
    restart = input("\nSo, you think you’ve had enough? You want another round? (yes/no): ").strip().lower()
    if restart.startswith("n"):
        print("\nAlright, alright... that’s it. Go take a seat somewhere. Goodbye.")
        print(f"🎯 Your total points: {points}")
        break
    elif restart != "yes":
        print("\nYou can’t even answer a simple question? Fine, we’re done here.")
        print(f"🎯 Your total points: {points}")
        break
