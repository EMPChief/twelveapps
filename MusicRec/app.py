import json
import random
import os

path = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(path, "dark_rec.json"), "r", encoding="utf-8") as file:
    music_genres = json.load(file)

genre_emojis = {
    "rock": "🪨", "pop": "🫠", "jazz": "🌀", "classical": "🕰️",
    "hip-hop": "💀", "country": "🪦", "electronic": "⚡",
    "reggae": "💨", "metal": "☠️", "r&b": "🖤"
}

print("\n☠️ Welcome to the Music Recommendation Machine: Doom Edition ☠️")
print("Pick a genre. Numb the noise. Pretend everything’s fine.\n")

print("📼 Genres to accompany your descent:")
for genre in music_genres:
    emoji = genre_emojis.get(genre, "🎶")
    print(f"  {emoji} {genre.title()}")

chosen_genre = input("\n🕳️ Which genre will you use to soundtrack your spiral today?\n👉 ").strip().lower()

if chosen_genre in music_genres:
    song = random.choice(music_genres[chosen_genre])
    print(f"\n🩸 Here's your {genre_emojis.get(chosen_genre, '')} *{chosen_genre.title()}* track for the void:")
    print(f"   🎶 {song} 🎶")
    print("Crank it up. Drown out the existential dread. It's either this or screaming into the abyss. 🤷\n")
else:
    print("\n👻 That genre isn’t here. Just like your will to go on.")
    print("Try again… or don’t. The silence is loud enough.\n")
