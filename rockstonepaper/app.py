import random
import sys


class OlympianGame:
    """A darkly humorous Rock-Paper-Scissors game of the Gods, featuring extra chaos."""

    def __init__(self):
        self.total_rounds = 0
        self.player_score = 0
        self.opponent_score = 0
        self.choices = ["rock", "paper", "scissors", "trident",
                        "lightning", "shield", "wine", "underworld"]
        self.emoji_choices = {
            "rock": "🪨",
            "paper": "🧻",
            "scissors": "✂️",
            "trident": "🔱",
            "lightning": "⚡",
            "shield": "🛡️",
            "wine": "🍷",
            "underworld": "💀"
        }
        self.wins_against = {
            "rock": ["scissors", "wine"],
            "scissors": ["paper", "shield"],
            "paper": ["rock", "lightning"],
            "trident": ["rock", "underworld"],
            "lightning": ["trident", "scissors"],
            "shield": ["lightning", "trident"],
            "wine": ["shield", "paper"],
            "underworld": ["wine", "scissors"]
        }

    def _clear_screen(self):
        if sys.platform.startswith("win"):
            _ = sys.stdout.write('\033[2J\033[H')
        else:
            _ = sys.stdout.write('\033c')

    def play_round(self, player1_choice, player2_choice):
        print(
            f"\n👤 Mortal chose: {player1_choice.capitalize()} {self.emoji_choices[player1_choice]}")
        print(
            f"⚡ God chose: {player2_choice.capitalize()} {self.emoji_choices[player2_choice]}")

        if player1_choice == player2_choice:
            print("⚖️ A tie! The Fates yawn.")
        elif player2_choice in self.wins_against.get(player1_choice, []):
            print("✅ Mortal triumphs! Olympus trembles.")
            self.player_score += 1
        elif player1_choice in self.wins_against.get(player2_choice, []):
            print("❌ The Gods laugh. Mortal loses this round.")
            self.opponent_score += 1
        else:
            print("☠️ The universe implodes from confusion. No points awarded.")

    def player_vs_computer(self):
        try:
            self.total_rounds = int(
                input("🏛️ How many trials shall the mortal endure? "))
        except ValueError:
            print("❌ Zeus demands a number, not your mortal ramblings.\n")
            return

        for round_number in range(1, self.total_rounds + 1):
            print(f"\n🔁 Trial {round_number}")
            player_choice = input(
                "👉 Choose your divine weapon: ").lower().strip()

            if player_choice not in self.choices:
                print("❌ That item is lost to myth. Choose again.")
                continue

            computer_choice = random.choice(self.choices)
            self.play_round(player_choice, computer_choice)

        self._show_result()

    def player_vs_player(self):
        try:
            self.total_rounds = int(
                input("🏛️ How many divine duels will be fought? "))
        except ValueError:
            print("❌ Apollo can't interpret gibberish.\n")
            return

        for round_number in range(1, self.total_rounds + 1):
            print(f"\n🔁 Duel {round_number}")
            player1_choice = input(
                "⚔️ Challenger 1, declare your weapon: ").lower().strip()
            self._clear_screen()
            player2_choice = input(
                "⚔️ Challenger 2, your counter: ").lower().strip()

            if player1_choice not in self.choices or player2_choice not in self.choices:
                print("❌ Hades denies invalid offerings. Try again.")
                continue

            self.play_round(player1_choice, player2_choice)

        self._show_result()

    def _show_result(self):
        print("\n🏁 Judgment Day has arrived.")
        print(f"👤 Mortal Score: {self.player_score}")
        print(f"⚡ Olympian Score: {self.opponent_score}")

        if self.player_score > self.opponent_score:
            print("🏆 The mortal ascends! Zeus reluctantly nods.")
        elif self.player_score < self.opponent_score:
            print("🔥 Banished to Tartarus. Better luck next reincarnation.")
        else:
            print("⚖️ Even the Gods can't decide. It's a draw.")


if __name__ == "__main__":
    game = OlympianGame()
    while True:
        mode = input(
            "Choose your battle mode (1 = Mortal vs God, 2 = God vs God): ").strip()
        if mode == "1":
            game.player_vs_computer()
        elif mode == "2":
            game.player_vs_player()
        else:
            print("❌ Hermes is confused. Pick a real number.")
