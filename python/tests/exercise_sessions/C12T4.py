import sys

def load_tasks():
    tasks = []
    try:
        with open("todo.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    tasks.append(line)
    except FileNotFoundError:
        pass
    return tasks


def save_tasks(tasks):
    with open("todo.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")


def main():
    if len(sys.argv) < 2:
        print("No tasks.")
        return

    command = sys.argv[1]
    tasks = load_tasks()

    if command == "add":
        if len(sys.argv) < 3:
            print("No tasks.")
            return

        task = sys.argv[2]
        tasks.append(task)
        save_tasks(tasks)
        print("Task added.")
        return

    if command == "list":
        if not tasks:
            print("No tasks.")
            return

        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")
        return

    if command == "delete":
        if len(sys.argv) < 3:
            print("No tasks.")
            return

        try:
            index = int(sys.argv[2]) - 1
        except ValueError:
            print("No tasks.")
            return

        if not (0 <= index < len(tasks)):
            print("No tasks.")
            return

        tasks.pop(index)
        save_tasks(tasks)
        print("Task deleted.")
        return


if __name__ == "__main__":
    main()