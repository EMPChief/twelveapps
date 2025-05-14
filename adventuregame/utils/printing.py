import time
import sys
import os


def clear_screen():
    """Clears the console screen."""
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')


def typewriter_print(text, delay=0.05, force_typewriter=True):
    """Prints text one letter at a time with a delay unless dev mode is on."""
    dev_mode = True

    if dev_mode and not force_typewriter:
        print(text)
        return

    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
