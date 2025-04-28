import random
import time

print("=== 🎲 Welcome to the Guessing Number Game! Don't disappoint the boss. 🎲 ===")

while True:
    get_random = random.randint(1, 100)
    attempts = 0
    print("\n🕵️‍♂️ I'm thinking of a number between 1 and 100. Guess it right, or... let's just say you might need a new pair of shoes. Concrete ones.")
    print("You got 10 attempts before you end up on a 'permanent vacation'. Good luck, kid. 🍀")

    start_time = time.time()

    for attempt in range(10):
        try:
            guess_number = int(input(f"Attempt {attempt + 1}: Take a guess, before someone gets nervous: "))
        except ValueError:
            print("❌ That ain't even a number, genius. You trying to insult the Don?")
            continue

        attempts += 1

        if guess_number < get_random:
            print("📉 Too low! Like your chances of walkin' outta here if you keep guessin' like that.")
        elif guess_number > get_random:
            print("📈 Too high! You aiming for the moon, kid? Aim lower, unless you want to be *planted* somewhere.")
        else:
            end_time = time.time()
            total_time = end_time - start_time
            print(f"\n🎉 You got it! {get_random}! The boss is pleased... for now. 🎊")
            print(f"⏱️ You wasted {total_time:.2f} seconds, but at least you're still breathing.")
            break
    else:
        end_time = time.time()
        total_time = end_time - start_time
        print(f"\n❌ You blew it. The number was {get_random}.")
        print(f"Word of advice? Start sleeping with one eye open.")
        print(f"⏱️ Time wasted before the 'cleanup crew' arrives: {total_time:.2f} seconds.")

    restart = input("\n🔄 Wanna try your luck again, tough guy? (yes/no): ").lower()
    if restart.startswith('n'):
        print("👋 Wise move. Thanks for playin'. Stay safe out there, capisce?")
        break
    elif restart != 'yes':
        print("❌ Can't follow simple orders, huh? Someone's gonna hear about this.")
        break
