import os
import time

print("Welcome to the Pomodoro Technique Timer!")
print("This is a simple timer to help you manage your work and break intervals.")

def clear_screen():
    """Clear the console screen for a clean display."""
    os.system('cls' if os.name == 'nt' else 'clear')

def countdown(minutes, label):
    """Display a countdown timer for the given number of minutes."""
    total_seconds = minutes * 60
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        print(f"{label} - Time Remaining: {mins:02d}:{secs:02d}", end='\r')
        time.sleep(1)
        total_seconds -= 1
    print(f"{label} - Time's up!{' ' * 20}")

def pomodoro_timer(work_duration=25, break_duration=5, long_break_duration=15, cycles=4):
    """
    Pomodoro Timer function to manage work and break intervals.
    :param work_duration: Duration of work in minutes (default 25)
    :param break_duration: Duration of short break in minutes (default 5)
    :param long_break_duration: Duration of long break in minutes (default 15)
    :param cycles: Number of work sessions before finishing (default 4)
    """
    cycle_counter = 0
    for i in range(cycles):
        print(f"\n🔁 Cycle {i + 1} of {cycles}")
        print(f"🧠 Focus time! Work for {work_duration} minutes.")
        countdown(work_duration, "Work")

        cycle_counter += 1
        if cycle_counter == 4 and i != cycles - 1:
            print(f"🌴 Long break! Relax for {long_break_duration} minutes.")
            countdown(long_break_duration, "Long Break")
            cycle_counter = 0
        elif i != cycles - 1:
            print(f"☕ Short break! Rest for {break_duration} minutes.")
            countdown(break_duration, "Short Break")

    print("\n✅ All cycles completed. Great job staying focused!")

def main():
    while True:
        try:
            use_default = input("Do you want to use the default Pomodoro settings? (yes/no): ").strip().lower()
            if use_default.startswith('y'):
                how_many_cycles = int(input("How many cycles do you want to run? (default 4): ") or 4)
                print("Default Pomodoro settings applied.")
                print(f"Work for 25 minutes, take a short break for 5 minutes, and a long break for 15 minutes after every 4 cycles.")
                print(f"Total cycles to run: {how_many_cycles}\n")
                pomodoro_timer(work_duration=25, break_duration=5, long_break_duration=15, cycles=how_many_cycles)
            else:
                work_duration = int(input("Enter work duration in minutes (default 25): ") or 25)
                break_duration = int(input("Enter short break duration in minutes (default 5): ") or 5)
                long_break_duration = int(input("Enter long break duration in minutes (default 15): ") or 15)
                cycles = int(input("Enter number of cycles (default 4): ") or 4)
                print(f"\nCustom settings applied:")
                print(f"- Work: {work_duration} min")
                print(f"- Short Break: {break_duration} min")
                print(f"- Long Break: {long_break_duration} min (after every 4 cycles)")
                print(f"- Total Cycles: {cycles}\n")
                pomodoro_timer(work_duration, break_duration, long_break_duration, cycles)
        except ValueError:
            print("❌ Invalid input. Please enter a number.")
        except KeyboardInterrupt:
            print("\n⏹️ Exiting Pomodoro Timer. Stay productive!")
            break
        except Exception as e:
            print(f"⚠️ An error occurred: {e}")
            break
        finally:
            restart = input("\n🔄 Do you want to start again? (yes/no): ").strip().lower()
            if restart.startswith('n'):
                print("👋 Goodbye! Stay productive!")
                break
            elif restart != 'yes':
                print("⚠️ Invalid input. Exiting Pomodoro Timer.")
                break

if __name__ == "__main__":
    time.sleep(1)
    clear_screen()
    main()
