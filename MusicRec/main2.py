import random

print("🎶 Welcome to the Ultimate Music Recommendation Station! 🎶\n")

music_genres = {
    "rock": [
        "🎸 Queen - Bohemian Rhapsody",
        "🎸 Led Zeppelin - Stairway to Heaven",
        "🎸 AC/DC - Back In Black",
        "🎸 Nirvana - Smells Like Teen Spirit",
        "🎸 The Rolling Stones - Paint It Black",
        "🎸 Guns N' Roses - Sweet Child O' Mine",
        "🎸 Pink Floyd - Comfortably Numb",
        "🎸 Foo Fighters - Everlong",
        "🎸 The Beatles - Come Together",
        "🎸 Linkin Park - Numb"
    ],
    "pop": [
        "🎤 Taylor Swift - Blank Space",
        "🎤 Dua Lipa - Don't Start Now",
        "🎤 Billie Eilish - Bad Guy",
        "🎤 Ed Sheeran - Shape of You",
        "🎤 Katy Perry - Firework",
        "🎤 Ariana Grande - Into You",
        "🎤 The Weeknd - Blinding Lights",
        "🎤 Rihanna - Umbrella",
        "🎤 Justin Bieber - Sorry",
        "🎤 Bruno Mars - Uptown Funk"
    ],
    "jazz": [
        "🎷 Miles Davis - So What",
        "🎷 John Coltrane - Giant Steps",
        "🎷 Dave Brubeck - Take Five",
        "🎷 Herbie Hancock - Chameleon",
        "🎷 Charles Mingus - Goodbye Pork Pie Hat",
        "🎷 Ella Fitzgerald - Dream a Little Dream of Me",
        "🎷 Louis Armstrong - What a Wonderful World",
        "🎷 Duke Ellington - In a Sentimental Mood",
        "🎷 Thelonious Monk - Round Midnight",
        "🎷 Chet Baker - My Funny Valentine"
    ],
    "classical": [
        "🎻 Beethoven - Symphony No. 9",
        "🎻 Bach - Cello Suite No. 1",
        "🎻 Mozart - Eine kleine Nachtmusik",
        "🎻 Tchaikovsky - Swan Lake",
        "🎻 Chopin - Nocturne Op. 9 No. 2",
        "🎻 Vivaldi - Four Seasons",
        "🎻 Brahms - Hungarian Dance No. 5",
        "🎻 Debussy - Clair de Lune",
        "🎻 Handel - Messiah",
        "🎻 Stravinsky - The Firebird"
    ],
    "hip-hop": [
        "🎧 Kendrick Lamar - HUMBLE.",
        "🎧 J. Cole - Middle Child",
        "🎧 Drake - God's Plan",
        "🎧 Nas - N.Y. State of Mind",
        "🎧 The Notorious B.I.G. - Juicy",
        "🎧 Tupac - Changes",
        "🎧 Jay-Z - 99 Problems",
        "🎧 Eminem - Lose Yourself",
        "🎧 Megan Thee Stallion - Savage",
        "🎧 Run DMC - It's Tricky"
    ],
    "country": [
        "🤠 Johnny Cash - Ring of Fire",
        "🤠 Dolly Parton - Jolene",
        "🤠 Luke Combs - Beautiful Crazy",
        "🤠 Carrie Underwood - Before He Cheats",
        "🤠 Blake Shelton - God's Country",
        "🤠 Kenny Chesney - American Kids",
        "🤠 Miranda Lambert - The House That Built Me",
        "🤠 Chris Stapleton - Tennessee Whiskey",
        "🤠 Garth Brooks - Friends in Low Places",
        "🤠 Shania Twain - Man! I Feel Like A Woman!"
    ],
    "electronic": [
        "🎛 Daft Punk - One More Time",
        "🎛 Calvin Harris - Summer",
        "🎛 Avicii - Levels",
        "🎛 Zedd - Clarity",
        "🎛 Martin Garrix - Animals",
        "🎛 Kygo - Firestone",
        "🎛 Deadmau5 - Strobe",
        "🎛 The Chainsmokers - Don't Let Me Down",
        "🎛 Skrillex - Bangarang",
        "🎛 Marshmello - Alone"
    ],
    "reggae": [
        "🌴 Bob Marley - No Woman, No Cry",
        "🌴 Toots & The Maytals - Pressure Drop",
        "🌴 Peter Tosh - Legalize It",
        "🌴 Jimmy Cliff - The Harder They Come",
        "🌴 Steel Pulse - Your House",
        "🌴 Ziggy Marley - Love Is My Religion",
        "🌴 Protoje - Who Knows",
        "🌴 Chronixx - Here Comes Trouble",
        "🌴 Dennis Brown - Money in My Pocket",
        "🌴 Buju Banton - Champion"
    ],
    "metal": [
        "🤘 Metallica - Enter Sandman",
        "🤘 Iron Maiden - The Trooper",
        "🤘 Black Sabbath - Paranoid",
        "🤘 Slipknot - Duality",
        "🤘 System of a Down - Chop Suey!",
        "🤘 Pantera - Walk",
        "🤘 Megadeth - Symphony of Destruction",
        "🤘 Judas Priest - Breaking the Law",
        "🤘 Tool - Schism",
        "🤘 Lamb of God - Laid to Rest"
    ],
    "r&b": [
        "🎶 Alicia Keys - If I Ain't Got You",
        "🎶 Usher - U Got It Bad",
        "🎶 Beyoncé - Irreplaceable",
        "🎶 SZA - Good Days",
        "🎶 The Weeknd - Earned It",
        "🎶 H.E.R. - Best Part",
        "🎶 Brandy - Full Moon",
        "🎶 Toni Braxton - Un-Break My Heart",
        "🎶 Mary J. Blige - Family Affair",
        "🎶 Miguel - Adorn"
    ]
}


chosen_genre = input(
    "🎧 What genre of music do you want to vibe to today?\n(rock, pop, jazz, classical, hip-hop, country, electronic, reggae, metal, r&b)\n👉 ").strip().lower()

if chosen_genre in music_genres:
    song = random.choice(music_genres[chosen_genre])
    print(f"\n🔥 Your {chosen_genre.capitalize()} jam of the day: {song} 🔥")
else:
    print("😢 Sorry, I don't have recommendations for that genre. Please try one from the list above.")

print("\nThanks for tuning in! 🎵 Keep the good vibes going! ✨")
