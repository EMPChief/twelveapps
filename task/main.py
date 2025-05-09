print("📝✨ Welcome to Your To-Do List Manager ✨📝")
todo_list = []


def add_task(task):
    todo_list.append(task)
    print(f"➕✅ Task '{task}' has been added to your list!")


def display_tasks():
    if not todo_list:
        print("📭 Your to-do list is currently empty. Time to get productive!")
    else:
        print("\n📋 Here’s what’s on your to-do list:")
        for i, task in enumerate(todo_list, start=1):
            print(f"  {i}. 🗂️ {task}")
        print("🔚 That’s everything for now!")


def remove_task(task_number):
    try:
        task_number = int(task_number) - 1
        if 0 <= task_number < len(todo_list):
            removed_task = todo_list.pop(task_number)
            print(f"🗑️❎ Removed task: '{removed_task}'")
        else:
            print("🚫 Invalid task number. Please try again.")
    except ValueError:
        print("🚫 Please enter a valid number.")
    except IndexError:
        print("🚫 Task number out of range.")


def edit_task(task_number, new_task):
    try:
        task_number = int(task_number) - 1
        if 0 <= task_number < len(todo_list):
            old_task = todo_list[task_number]
            todo_list[task_number] = new_task
            print(
                f"📝🔄 Updated task {task_number + 1}: '{old_task}' ➡️ '{new_task}'")
        else:
            print("🚫 Invalid task number. Please try again.")
    except ValueError:
        print("🚫 Please enter a valid number.")
    except IndexError:
        print("🚫 Task number out of range.")


def clear_tasks():
    todo_list.clear()
    print("🧹🗑️ All tasks cleared! A fresh start awaits.")


def main():
    while True:
        print("\n📌 Menu:")
        print("  1️⃣ Add Task")
        print("  2️⃣ Display Tasks")
        print("  3️⃣ Remove Task")
        print("  4️⃣ Edit Task")
        print("  5️⃣ Clear All Tasks")
        print("  6️⃣ Exit")

        choice = input("💡 Choose an option (1-6): ")

        if choice == '1':
            task = input("🖊️ Enter the task: ")
            add_task(task)
        elif choice == '2':
            display_tasks()
        elif choice == '3':
            task_number = input("❓ Enter the task number to remove: ")
            remove_task(task_number)
        elif choice == '4':
            task_number = input("✏️ Enter the task number to edit: ")
            new_task = input("🆕 Enter the new task: ")
            edit_task(task_number, new_task)
        elif choice == '5':
            clear_tasks()
        elif choice == '6':
            print("👋✨ Goodbye! Stay organized and crush your goals! 💪📈")
            break
        else:
            print("🚫 Invalid choice. Please select a number from 1 to 6.")


if __name__ == "__main__":
    main()
