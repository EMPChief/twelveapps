print("📑💀 Welcome to the Afterlife Task Manager — Hell’s Favorite Productivity Tool 💀📑")
todo_list = []


def add_task(task):
    todo_list.append(task)
    print(f"☠️🗃️ Task '{task}' has been added to your eternal workload. Denial is no longer an option.")


def display_tasks():
    if not todo_list:
        print("⚰️ Your list is emptier than a soul on a Monday. Add something before the demons get bored.")
    else:
        print("\n📋 Current Tasks Assigned by the Afterlife Administration:")
        for i, task in enumerate(todo_list, start=1):
            print(f"  {i}. 🗂️ {task}")
        print("📌 End of list. Remember, even death doesn’t excuse missed deadlines.")


def remove_task(task_number):
    try:
        task_number = int(task_number) - 1
        if 0 <= task_number < len(todo_list):
            removed_task = todo_list.pop(task_number)
            print(f"🪦 Task '{removed_task}' has been sent to the underworld’s recycling bin.")
        else:
            print("🚫 That task number is as fake as most resumes. Try again.")
    except ValueError:
        print("🚫 That’s not a number. Are you even trying, mortal?")
    except IndexError:
        print("🚫 You’re reaching into the void. That task doesn’t exist.")


def edit_task(task_number, new_task):
    try:
        task_number = int(task_number) - 1
        if 0 <= task_number < len(todo_list):
            old_task = todo_list[task_number]
            todo_list[task_number] = new_task
            print(f"🔄 Task updated: '{old_task}' has been reincarnated as '{new_task}'.")
        else:
            print("🚫 That task number never existed. Just like your free will.")
    except ValueError:
        print("🚫 Numbers only, unless you want to summon something.")
    except IndexError:
        print("🚫 Out of range. Not even the Fates can find that one.")


def clear_tasks():
    todo_list.clear()
    print("🧹 All tasks purged. Your sins are not forgiven, but your list is.")


def main():
    while True:
        print("\n🗃️ Soul Admin Menu:")
        print("  1️⃣ Add Task to Eternal Queue")
        print("  2️⃣ Review Assigned Purgatory Tasks")
        print("  3️⃣ Delete a Task from Memory (temporarily)")
        print("  4️⃣ Rewrite History (Edit a Task)")
        print("  5️⃣ Obliterate All Evidence (Clear List)")
        print("  6️⃣ Exit the Afterlife Desk")

        choice = input("🔮 Choose your torment (1-6): ")

        if choice == '1':
            task = input("📜 What shall be added to your eternal to-do scroll?: ")
            add_task(task)
        elif choice == '2':
            display_tasks()
        elif choice == '3':
            task_number = input("⛔ Which task do you wish to cast into the abyss?: ")
            remove_task(task_number)
        elif choice == '4':
            task_number = input("🪬 Which task shall be reborn?: ")
            new_task = input("✨ Enter its cursed new form: ")
            edit_task(task_number, new_task)
        elif choice == '5':
            clear_tasks()
        elif choice == '6':
            print("👻 Farewell, admin of the damned. May your inbox stay empty (but we know it won’t).")
            break
        else:
            print("📛 That option isn’t real. Much like retirement in this department.")


if __name__ == "__main__":
    main()
