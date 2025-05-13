import time
import sys
import os

def clear_screen():
    """Clears the console screen."""
    if sys.platform.startswith('win'):
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def typewriter_print(text, delay=0.05):
    """Prints text one letter at a time with a delay."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()