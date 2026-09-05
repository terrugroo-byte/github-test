#!/usr/bin/env python3
"""A tiny command-line to-do list, backed by a local JSON file."""
import json
import sys
from pathlib import Path

STORE_PATH = Path(__file__).parent / "todo.json"


def load_tasks():
    if not STORE_PATH.exists():
        return []
    return json.loads(STORE_PATH.read_text())


def save_tasks(tasks):
    STORE_PATH.write_text(json.dumps(tasks, indent=2))


def add_task(tasks, text):
    tasks.append({"text": text, "done": False})
    save_tasks(tasks)
    print(f"Added: {text}")


def list_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for i, task in enumerate(tasks):
        mark = "x" if task["done"] else " "
        print(f"[{mark}] {i}: {task['text']}")


def complete_task(tasks, index):
    tasks[index]["done"] = True
    save_tasks(tasks)
    print(f"Completed: {tasks[index]['text']}")


def remove_task(tasks, index):
    removed = tasks.pop(index)
    save_tasks(tasks)
    print(f"Removed: {removed['text']}")


def clear_tasks(tasks):
    count = len(tasks)
    tasks.clear()
    save_tasks(tasks)
    print(f"Cleared {count} task(s)")


def count_remaining(tasks):
    remaining = sum(1 for task in tasks if not task["done"])
    print(f"{remaining} task(s) remaining")
    return remaining


def parse_index(raw, tasks):
    try:
        index = int(raw)
    except ValueError:
        print(f"Error: '{raw}' is not a valid task number")
        return None
    if not 0 <= index < len(tasks):
        print(f"Error: no task at index {index}")
        return None
    return index


def main(argv):
    tasks = load_tasks()
    if not argv:
        list_tasks(tasks)
        return 0

    command, *rest = argv
    if command == "add":
        add_task(tasks, " ".join(rest))
    elif command == "list":
        list_tasks(tasks)
    elif command == "done":
        index = parse_index(rest[0], tasks)
        if index is None:
            return 1
        complete_task(tasks, index)
    elif command == "rm":
        index = parse_index(rest[0], tasks)
        if index is None:
            return 1
        remove_task(tasks, index)
    elif command == "clear":
        clear_tasks(tasks)
    elif command == "count":
        count_remaining(tasks)
    else:
        print(f"Unknown command: {command}")
        print("Usage: todo.py [add <text> | list | done <index> | rm <index> | clear | count]")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
