import json
import random
import os

path = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(path, "music_recommendations.json"), "r", encoding="utf-8") as file:
    music_genres = json.load(file)

genre_emojis = {
    "rock": "🎸", "pop": "🎤", "jazz": "🎷", "classical": "🎻",
    "hip-hop": "🎧", "country": "🤠", "electronic": "🎛️",
    "reggae": "🌴", "metal": "🤘", "r&b": "💜"
}

print("\n🎶 Welcome to the Music Recommendation Machine 🎶")
print("✨ Pick your vibe and get a song you'll love!\n")

print("🎵 Available Genres:")
for genre in music_genres:
    emoji = genre_emojis.get(genre, "🎶")
    print(f"  {emoji} {genre.title()}")

chosen_genre = input("\n🎧 What genre do you want to vibe to today?\n👉 ").strip().lower()

if chosen_genre in music_genres:
    song = random.choice(music_genres[chosen_genre])
    print(f"\n🔥 Your {genre_emojis.get(chosen_genre, '')} *{chosen_genre.title()}* jam of the day:")
    print(f"   🎵 {song} 🎵\n")
else:
    print("\n😢 Sorry, I don't have recommendations for that genre.")
    print("📝 Please choose from the listed genres next time!\n")
