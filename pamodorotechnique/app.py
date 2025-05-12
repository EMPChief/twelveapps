import os
import time
import simpleaudio as sa

def clear_console_screen():
    """Clear the console screen, because the crushing void of existence deserves to be hidden."""
    os.system('cls' if os.name == 'nt' else 'clear')

def play_ding_sound_two_times():
    """Play the soothing, soul-crushing ding sound twice, as you cling to the remnants of your humanity."""
    try:
        wave_object = sa.WaveObject.from_wave_file("pamodorotechnique/dingy.wav")
        for _ in range(2):
            play_object = wave_object.play()
            play_object.wait_done()
    except Exception as error:
        print(f"🔇 Could not play sound: {error}. Even technology abandons us.")

def print_time_remaining(timer_label, minutes_left, seconds_left):
    """Print the remaining time on the timer in a poetic reminder of your diminishing existence."""
    print(f"{timer_label} - Time Remaining: {minutes_left:02d}:{seconds_left:02d}", end='\r')

def countdown_timer(duration_in_minutes, timer_label):
    """Countdown timer, a reminder of how little time you have left in this miserable world."""
    total_seconds = duration_in_minutes * 60
    while total_seconds > 0:
        minutes_left, seconds_left = divmod(total_seconds, 60)
        print_time_remaining(timer_label, minutes_left, seconds_left)
        time.sleep(1)
        total_seconds -= 1
    print(f"{timer_label} - Time's up!{' ' * 20}")
    play_ding_sound_two_times()

def perform_cycle(cycle_number, total_cycles, work_duration_in_minutes, short_break_duration_in_minutes,
                  long_break_duration_in_minutes):
    """Perform a single Pomodoro cycle including work and breaks."""
    print(f"\n🔁 Cycle {cycle_number + 1} of {total_cycles}... It's too late to turn back now.")
    print(f"🧠 Focus time! Work for {work_duration_in_minutes} minutes... there's no escape.")
    countdown_timer(work_duration_in_minutes, "Work")

    cycle_counter = 0
    if cycle_counter == 4 and cycle_number != total_cycles - 1:
        print(f"🌴 Long break! Relax for {long_break_duration_in_minutes} minutes... the calm before the storm.")
        countdown_timer(long_break_duration_in_minutes, "Long Break")
        cycle_counter = 0
    elif cycle_number != total_cycles - 1:
        print(f"☕ Short break! Rest for {short_break_duration_in_minutes} minutes... enjoy it while it lasts.")
        countdown_timer(short_break_duration_in_minutes, "Short Break")

def get_custom_settings():
    """Prompt the user to input custom settings for the Pomodoro Timer."""
    custom_work_duration = int(input("Enter work duration in minutes (default 25): ") or 25)
    custom_short_break_duration = int(input("Enter short break duration in minutes (default 5): ") or 5)
    custom_long_break_duration = int(input("Enter long break duration in minutes (default 15): ") or 15)
    custom_total_cycles = int(input("Enter number of cycles (default 4): ") or 4)
    return custom_work_duration, custom_short_break_duration, custom_long_break_duration, custom_total_cycles

def handle_default_settings(number_of_cycles):
    """Handle the default Pomodoro Timer settings."""
    print("Default Pomodoro settings applied. The countdown to despair begins.")
    print(f"Work for 25 minutes, take a short break for 5 minutes, and a long break for 15 minutes after every 4 cycles.")
    print(f"Total cycles to run: {number_of_cycles}\n")
    run_pomodoro_timer(work_duration_in_minutes=25, short_break_duration_in_minutes=5,
                       long_break_duration_in_minutes=15, total_cycles=number_of_cycles)

def run_pomodoro_timer(work_duration_in_minutes=25, short_break_duration_in_minutes=5,
                       long_break_duration_in_minutes=15, total_cycles=4):
    """
    Pomodoro Timer. A brutal cycle of work and agony. You won't escape.
    :param work_duration_in_minutes: Duration of work (default 25 minutes of pure suffering)
    :param short_break_duration_in_minutes: Duration of short break (default 5 minutes to momentarily forget you're alive)
    :param long_break_duration_in_minutes: Duration of long break (default 15 minutes of false hope)
    :param total_cycles: Number of cycles before your soul is crushed (default 4)
    """
    cycle_counter = 0
    for cycle_number in range(total_cycles):
        perform_cycle(cycle_number, total_cycles, work_duration_in_minutes, short_break_duration_in_minutes,
                      long_break_duration_in_minutes)

    print("\n✅ All cycles completed. You've survived... for now. But at what cost?")

def main():
    """Main function to run the Pomodoro Timer."""
    while True:
        try:
            use_default_settings = input(
                "Do you want to use the default Pomodoro settings? (yes/no): ").strip().lower()
            if use_default_settings.startswith('y'):
                number_of_cycles = int(input("How many cycles do you want to run? (default 4): ") or 4)
                handle_default_settings(number_of_cycles)
            else:
                custom_work_duration, custom_short_break_duration, custom_long_break_duration, custom_total_cycles = get_custom_settings()
                print(f"\nCustom settings applied... but why bother?")
                print(f"- Work: {custom_work_duration} min")
                print(f"- Short Break: {custom_short_break_duration} min")
                print(f"- Long Break: {custom_long_break_duration} min (after every 4 cycles)")
                print(f"- Total Cycles: {custom_total_cycles}\n")
                run_pomodoro_timer(custom_work_duration, custom_short_break_duration,
                                   custom_long_break_duration, custom_total_cycles)
        except ValueError:
            print("❌ Invalid input. You’re still clinging to hope, but reality is relentless.")
        except KeyboardInterrupt:
            print("\n⏹️ Exiting Pomodoro Timer. You've escaped this time... but not for long.")
            break
        except Exception as error:
            print(f"⚠️ An error occurred: {error}. Everything is broken, including your spirit.")
            break
        finally:
            restart_prompt = input(
                "\n🔄 Do you want to start again? (yes/no): ").strip().lower()
            if restart_prompt.startswith('n'):
                print("👋 Goodbye! Enjoy the crushing weight of existence.")
                break
            elif restart_prompt != 'yes':
                print("⚠️ Invalid input. Exiting Pomodoro Timer. The end is inevitable.")
                break


if __name__ == "__main__":
    print("🔔 Welcome to the Pomodoro Technique Timer. Embrace the grind. 🔔")
    time.sleep(1)
    clear_console_screen()
    main()
