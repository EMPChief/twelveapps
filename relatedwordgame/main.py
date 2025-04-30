import time
import random

print("🎯 Related Word Game 🎯")

# Dictionary of main words and their related terms
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


points = 0

while True:
    try:
        # Pick a random topic
        random_word = random.choice(list(related_words.keys()))

        # Start the timer
        start_seconds = time.time()

        # Ask the user for a related word
        guess_word = input(
            f"\nGuess a related word for '{random_word.title()}' (or type 'exit' to quit): "
        ).strip().lower()

        # Exit condition
        if guess_word == "exit":
            print("\nThanks for playing! Goodbye!")
            break

        # Check the user's guess
        normalized_related = [word.lower()
                              for word in related_words[random_word]]
        if guess_word in normalized_related:
            finished_seconds = time.time()
            time_taken = finished_seconds - start_seconds

            print(f"✅ Correct! '{guess_word}' is related to '{random_word}'.")
            print(f"⏱️ You took {time_taken:.2f} seconds.")

            # Scoring based on response time
            if time_taken < 2:
                points += 5
                print("🔥 Great job! You earned 5 points.")
            elif time_taken < 3:
                points += 4
                print("👍 Good job! You earned 4 points.")
            elif time_taken < 4:
                points += 3
                print("🙂 Nice try! You earned 3 points.")
            elif time_taken < 5:
                points += 2
                print("😐 Not bad! You earned 2 points.")
            elif time_taken < 10:
                points += 1
                print("😅 Good effort! You earned 1 point.")
            else:
                print("🕓 Better luck next time! You earned 0 points.")

        else:
            print(
                f"❌ Sorry, '{guess_word}' is not related to '{random_word}'.")

        print(f"🏆 Total points: {points}")

    except KeyboardInterrupt:
        print("\n\nThanks for playing! Goodbye!")
        break
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")
        break

    # Ask to play again
    restart = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if restart.startswith("n"):
        print("\nThanks for playing! Goodbye!")
        print(f"🎯 Your total points: {points}")
        break
    elif restart != "yes":
        print("\nInvalid input. Exiting the game.")
        print(f"🎯 Your total points: {points}")
        break
