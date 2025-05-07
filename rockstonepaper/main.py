import random
import sys


class RockScissorsPaper:
    def __init__(self):
        """Initialize game settings and scores."""
        self.total_rounds = 0
        self.player_score = 0
        self.opponent_score = 0
        self.choices = ["rock", "paper", "scissors"]
        self.emoji_choices = {"rock": "🪨", "paper": "🧻", "scissors": "✂️"}
        self.wins_against = {
            "rock": "scissors",
            "scissors": "paper",
            "paper": "rock"
        }

    def _clear_screen(self):
        """Clear the terminal screen."""
        if sys.platform.startswith("win"):
            _ = sys.stdout.write('\033[2J\033[H')
        else:
            _ = sys.stdout.write('\033c')

    def play_round(self, player1_choice, player2_choice):
        """Play a single round and update scores."""
        print(
            f"\n🧑 Player chose: {player1_choice.capitalize()} {self.emoji_choices[player1_choice]}")
        print(
            f"🎮 Opponent chose: {player2_choice.capitalize()} {self.emoji_choices[player2_choice]}")

        if player1_choice == player2_choice:
            print("⚖️ It's a tie!")
        elif self.wins_against[player1_choice] == player2_choice:
            print("✅ Player wins this round!")
            self.player_score += 1
        else:
            print("❌ Opponent wins this round.")
            self.opponent_score += 1

    def player_vs_computer(self):
        """Play multiple rounds against the computer."""
        try:
            self.total_rounds = int(
                input("🎮 How many rounds do you want to play? "))
        except ValueError:
            print("❌ Please enter a valid number.\n")
            return

        for round_number in range(1, self.total_rounds + 1):
            print(f"\n🔁 Round {round_number}")
            player_choice = input(
                "👉 Enter your choice (rock, paper, scissors): ").lower().strip()

            if player_choice not in self.choices:
                print("❌ Invalid choice. Try again.")
                continue

            computer_choice = random.choice(self.choices)
            self.play_round(player_choice, computer_choice)

        self._show_result()

    def player_vs_player(self):
        """Play multiple rounds between two players."""
        try:
            self.total_rounds = int(
                input("🎮 How many rounds do you want to play? "))
        except ValueError:
            print("❌ Please enter a valid number.\n")
            return

        for round_number in range(1, self.total_rounds + 1):
            print(f"\n🔁 Round {round_number}")
            player1_choice = input(
                "🧑 Player 1, enter your choice: ").lower().strip()

            self._clear_screen()
            player2_choice = input(
                "🧑 Player 2, enter your choice: ").lower().strip()

            if player1_choice not in self.choices or player2_choice not in self.choices:
                print("❌ Invalid choice by one or both players. Try again.")
                continue

            self.play_round(player1_choice, player2_choice)

        self._show_result()

    def _show_result(self):
        """Display final result of the game."""
        print("\n🏁 Game Over!")
        print(f"🧑 Player Score: {self.player_score}")
        print(f"🎮 Opponent Score: {self.opponent_score}")
        if self.player_score > self.opponent_score:
            print("🎉 Player wins the game!")
        elif self.player_score < self.opponent_score:
            print("😢 Opponent wins the game.")
        else:
            print("⚖️ The game is a draw!")


if __name__ == "__main__":
    game = RockScissorsPaper()
    while True:
        mode = input(
            "Choose game mode: '1' for Player vs Computer, '2' for Player vs Player: ").strip()
        if mode == "1":
            game.player_vs_computer()
        elif mode == "2":
            game.player_vs_player()
        else:
            print("❌ Invalid mode. Try again.\n")
