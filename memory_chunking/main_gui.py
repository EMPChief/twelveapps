import tkinter as tk
import random
import string


class MemoryChunkingGame:
    def __init__(self, root):
        self.root = root
        self.chunk_size = 3
        self.chunks = []

        self.root.title("Memory Number Chunking Game")
        self.root.geometry("400x350")

        # Instruction
        self.instructions_label = tk.Label(
            self.root, text="Memorize the number", font=("Helvetica", 16))
        self.instructions_label.pack(pady=20)

        # Chunk display
        self.chunk_label = tk.Label(self.root, text="", font=("Arial", 24))
        self.chunk_label.pack(pady=20)

        # Entry prompt
        self.input_label = tk.Label(
            self.root, text="Enter the number you remember:", font=("Arial", 12))
        self.input_label.pack()

        # Entry field
        self.user_input = tk.Entry(
            self.root, font=("Arial", 14), state=tk.DISABLED)
        self.user_input.pack(pady=10)

        # Submit button
        self.submit_button = tk.Button(self.root, text="Submit", font=("Arial", 12),
                                       command=self.check_user_input, state=tk.DISABLED)
        self.submit_button.pack(pady=5)

        # Result label
        self.result_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        # Bind Enter key to submit
        self.root.bind('<Return>', self.handle_enter_key)

        # Start the game
        self.next_chunk()

    def generate_chunk(self):
        """Generate a new number chunk"""
        chunk = ''.join(random.choices(string.digits, k=self.chunk_size))
        self.chunks = [chunk]

    def display_chunk(self):
        """Show spaced chunk, then hide after a delay"""
        spaced_chunk = ' '.join(self.chunks[0])
        self.chunk_label.config(text=spaced_chunk)
        self.user_input.delete(0, tk.END)
        self.user_input.config(state=tk.DISABLED)
        self.result_label.config(text="")
        self.submit_button.config(state=tk.DISABLED)
        if self.chunk_size < 4:
            delay = 1500
        elif self.chunk_size < 5:
            delay = 2000
        elif self.chunk_size < 8:
            delay = 3000
        elif self.chunk_size < 12:
            delay = 5000
        else:
            delay = 7000

        self.root.after(delay, self.hide_chunk)

    def hide_chunk(self):
        """Hide the chunk and enable input"""
        self.chunk_label.config(text="")
        self.result_label.config(text="")
        self.user_input.config(state=tk.NORMAL)
        self.user_input.delete(0, tk.END)
        self.user_input.focus()
        self.submit_button.config(state=tk.NORMAL)

    def check_user_input(self):
        """Check user answer and show result"""
        entered = self.user_input.get().strip().replace(" ", "")
        correct = self.chunks[0]
        if entered == correct:
            self.result_label.config(text="✅ Correct!", fg="green")
            self.chunk_size += 1
        else:
            self.result_label.config(
                text=f"❌ Incorrect! The correct number was: {correct}", fg="red")
            self.chunk_size = max(3, self.chunk_size - 1)

        self.submit_button.config(state=tk.DISABLED)
        self.user_input.config(state=tk.DISABLED)
        self.root.after(3000, self.next_chunk)

    def handle_enter_key(self, event):
        """Handle Enter key for submission"""
        if self.user_input['state'] == tk.NORMAL:
            self.check_user_input()

    def next_chunk(self):
        """Prepare and show the next chunk"""
        self.generate_chunk()
        self.display_chunk()


if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryChunkingGame(root)
    root.mainloop()
